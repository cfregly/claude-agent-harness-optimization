#!/usr/bin/env python3
"""Ensure every public CLI subcommand is exercised by CI."""

from __future__ import annotations

import ast
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
HELP_COMMANDS_RE = re.compile(r"\{([^}]+)\}")
CLI_COMMAND_RE = re.compile(r"python -m claude_agent_harness_opt\s+([a-z0-9][a-z0-9-]*)")


def main() -> int:
    failures = check_cli_coverage()
    if failures:
        print("\n".join(sorted(failures)))
        return 1
    print("CLI coverage check passed")
    return 0


def check_cli_coverage(root: Path = ROOT, cli_commands: set[str] | None = None) -> list[str]:
    commands = cli_commands or _load_cli_commands(root)
    ci_path = root / ".github" / "workflows" / "ci.yml"
    if not ci_path.exists():
        return [".github/workflows/ci.yml: missing"]

    ci_text = ci_path.read_text(encoding="utf-8")
    ci_commands = set(CLI_COMMAND_RE.findall(ci_text))
    unit_commands = _unit_test_commands(root)
    failures = [
        f".github/workflows/ci.yml: missing direct CLI smoke for {command}"
        for command in sorted(commands - ci_commands)
    ]
    failures.extend(
        f".github/workflows/ci.yml: unknown CLI command {command}"
        for command in sorted(ci_commands - commands)
    )
    failures.extend(
        f"tests/test_cli.py: missing direct CLI unit smoke for {command}"
        for command in sorted(commands - unit_commands)
    )
    failures.extend(
        f"tests/test_cli.py: unknown CLI command {command}"
        for command in sorted(unit_commands - commands)
    )
    return failures


def _load_cli_commands(root: Path = ROOT) -> set[str]:
    result = subprocess.run(
        [sys.executable, "-m", "claude_agent_harness_opt", "--help"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    match = HELP_COMMANDS_RE.search(result.stdout)
    if not match:
        raise RuntimeError("could not parse CLI command list from --help")
    return {command.strip() for command in match.group(1).split(",") if command.strip()}


def _unit_test_commands(root: Path = ROOT) -> set[str]:
    path = root / "tests" / "test_cli.py"
    if not path.exists():
        return set()
    text = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return set()
    commands: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and _is_run_cli_call(node):
            if node.args and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                commands.add(node.args[0].value)
        if isinstance(node, ast.Assign):
            if any(isinstance(target, ast.Name) and target.id == "cases" for target in node.targets):
                commands.update(_commands_from_cases_literal(node.value))
    return commands


def _is_run_cli_call(node: ast.Call) -> bool:
    func = node.func
    if isinstance(func, ast.Name):
        return func.id == "run_cli"
    if isinstance(func, ast.Attribute):
        return func.attr == "run_cli"
    return False


def _commands_from_cases_literal(node: ast.AST) -> set[str]:
    if not isinstance(node, (ast.List, ast.Tuple)):
        return set()
    commands: set[str] = set()
    for item in node.elts:
        if not isinstance(item, (ast.List, ast.Tuple)) or not item.elts:
            continue
        first = item.elts[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str):
            commands.add(first.value)
    return commands


if __name__ == "__main__":
    raise SystemExit(main())
