"""Coverage audits for model-matrix tool-selection cases."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .model_matrix import load_matrix


SPECIAL_TOOLS = {"NO_TOOL"}


def audit_matrix_coverage(path: str | Path) -> dict[str, Any]:
    matrix_path = Path(path)
    matrix = load_matrix(matrix_path)
    audit = audit_matrix_coverage_data(matrix, matrix_path=str(matrix_path))
    return audit


def audit_matrix_coverage_data(
    matrix: dict[str, Any],
    *,
    matrix_path: str = "",
) -> dict[str, Any]:
    variants = matrix.get("tool_variants", [])
    tools = _tool_names(variants)
    cases = matrix.get("cases", [])
    expected_cases = {tool: [] for tool in tools}
    forbidden_cases = {tool: [] for tool in tools}
    arg_cases = {tool: [] for tool in tools}
    boundary_pairs: dict[tuple[str, str], list[str]] = {}
    case_rows = []
    check_families: dict[str, list[str]] = {}
    unknown_expected: set[str] = set()
    unknown_forbidden: set[str] = set()

    for case in cases:
        name = str(case.get("name", ""))
        expected = [str(tool) for tool in case.get("expected_tools", [])]
        forbidden = [str(tool) for tool in case.get("forbidden_tools", [])]
        arg_checks = case.get("expected_args_contains") or {}
        check_family = str(case.get("check_family", "")).strip()
        if check_family:
            check_families.setdefault(check_family, []).append(name)
        for tool in expected:
            if tool in expected_cases:
                expected_cases[tool].append(name)
            elif tool not in SPECIAL_TOOLS:
                unknown_expected.add(tool)
            if arg_checks and tool in arg_cases:
                arg_cases[tool].append(name)
        for tool in forbidden:
            if tool in forbidden_cases:
                forbidden_cases[tool].append(name)
            elif tool not in SPECIAL_TOOLS:
                unknown_forbidden.add(tool)
        for expected_tool in expected:
            for forbidden_tool in forbidden:
                boundary_pairs.setdefault((expected_tool, forbidden_tool), []).append(name)
        case_rows.append(
            {
                "allow_no_tool": bool(case.get("allow_no_tool", False)),
                "argument_checks": sorted(arg_checks),
                "check_family": check_family,
                "expected_tools": expected,
                "forbidden_tools": forbidden,
                "name": name,
                "task": str(case.get("task", "")),
            }
        )

    tools_detail = []
    for tool in tools:
        tool_def = _first_tool_def(variants, tool)
        missing_quality_checks = not bool(tool_def.get("quality_checks"))
        tools_detail.append(
            {
                "argument_cases": arg_cases[tool],
                "expected_cases": expected_cases[tool],
                "forbidden_cases": forbidden_cases[tool],
                "has_quality_checks": not missing_quality_checks,
                "name": tool,
            }
        )

    operational_tools = [tool for tool in tools if tool not in SPECIAL_TOOLS]
    never_expected = [tool for tool in operational_tools if not expected_cases[tool]]
    never_forbidden = [tool for tool in operational_tools if not forbidden_cases[tool]]
    expected_without_argument_check = [
        tool
        for tool in operational_tools
        if expected_cases[tool] and not arg_cases[tool] and _tool_accepts_arguments(variants, tool)
    ]
    missing_quality_checks = [
        item["name"]
        for item in tools_detail
        if not item["has_quality_checks"]
    ]
    cases_without_forbidden = [
        row["name"]
        for row in case_rows
        if row["expected_tools"] and not row["forbidden_tools"]
    ]
    cases_without_check_family = [
        row["name"]
        for row in case_rows
        if not row["check_family"]
    ]
    warnings = []
    if never_expected:
        warnings.append("some catalog tools are never expected by a case")
    if never_forbidden:
        warnings.append("some catalog tools are never tested as confusable negatives")
    if expected_without_argument_check:
        warnings.append("some expected tools never have argument checks")
    if missing_quality_checks:
        warnings.append("some tuned tools have no quality checks")
    if cases_without_forbidden:
        warnings.append("some cases do not name forbidden confusable tools")
    if cases_without_check_family:
        warnings.append("some cases do not name a check_family")

    return {
        "boundary_pairs": [
            {
                "cases": names,
                "expected_tool": expected_tool,
                "forbidden_tool": forbidden_tool,
            }
            for (expected_tool, forbidden_tool), names in sorted(boundary_pairs.items())
        ],
        "cases": case_rows,
        "check_families": {
            family: names
            for family, names in sorted(check_families.items())
        },
        "matrix": matrix.get("name", ""),
        "matrix_path": matrix_path,
        "passed": not bool(warnings),
        "source": matrix.get("source", {}),
        "summary": {
            "argument_case_count": sum(1 for row in case_rows if row["argument_checks"]),
            "boundary_pair_count": len(boundary_pairs),
            "case_count": len(cases),
            "case_count_with_check_family": len(cases) - len(cases_without_check_family),
            "forbidden_tool_coverage": _ratio(
                len(operational_tools) - len(never_forbidden),
                len(operational_tools),
            ),
            "no_tool_case_count": sum(1 for row in case_rows if row["allow_no_tool"]),
            "tool_count": len(operational_tools),
            "tool_expected_coverage": _ratio(
                len(operational_tools) - len(never_expected),
                len(operational_tools),
            ),
            "tool_variant_count": len(variants),
        },
        "tool_variants": [
            {
                "name": str(variant.get("name", "")),
                "tool_count": len(variant.get("tools", [])),
            }
            for variant in variants
        ],
        "tools": tools_detail,
        "uncovered": {
            "cases_without_check_family": cases_without_check_family,
            "cases_without_forbidden": cases_without_forbidden,
            "expected_without_argument_check": expected_without_argument_check,
            "missing_quality_checks": missing_quality_checks,
            "never_expected": never_expected,
            "never_forbidden": never_forbidden,
            "unknown_expected_tools": sorted(unknown_expected),
            "unknown_forbidden_tools": sorted(unknown_forbidden),
        },
        "warnings": warnings,
    }


def render_matrix_coverage_markdown(audit: dict[str, Any]) -> str:
    summary = audit["summary"]
    uncovered = audit["uncovered"]
    lines = [
        f"# Matrix Coverage: {audit['matrix']}",
        "",
        f"Passed: {'yes' if audit['passed'] else 'no'}",
        f"Tools: {summary['tool_count']}",
        f"Cases: {summary['case_count']}",
        f"Expected tool coverage: {summary['tool_expected_coverage']:.3f}",
        f"Forbidden tool coverage: {summary['forbidden_tool_coverage']:.3f}",
        f"Cases with argument checks: {summary['argument_case_count']}",
        f"Boundary pairs: {summary['boundary_pair_count']}",
        f"Cases with check_family: {summary['case_count_with_check_family']}",
        "",
        "## Gaps",
        "",
    ]
    for label, key in (
        ("Never expected", "never_expected"),
        ("Never forbidden", "never_forbidden"),
        ("Expected without argument checks", "expected_without_argument_check"),
        ("Missing quality checks", "missing_quality_checks"),
        ("Cases without forbidden tools", "cases_without_forbidden"),
        ("Cases without check_family", "cases_without_check_family"),
        ("Unknown expected tools", "unknown_expected_tools"),
        ("Unknown forbidden tools", "unknown_forbidden_tools"),
    ):
        values = uncovered.get(key, [])
        rendered = ", ".join(values) if values else "none"
        lines.append(f"- {label}: {rendered}")

    lines.extend(
        [
            "",
            "## Tool Coverage",
            "",
            "| Tool | Expected Cases | Forbidden Cases | Argument Cases | Quality Checks |",
            "|---|---:|---:|---:|---|",
        ]
    )
    for tool in audit["tools"]:
        lines.append(
            "| {name} | {expected} | {forbidden} | {args} | {checks} |".format(
                args=len(tool["argument_cases"]),
                checks="yes" if tool["has_quality_checks"] else "no",
                expected=len(tool["expected_cases"]),
                forbidden=len(tool["forbidden_cases"]),
                name=tool["name"],
            )
        )

    if audit["check_families"]:
        lines.extend(
            [
                "",
                "## Check Families",
                "",
                "| Family | Cases |",
                "|---|---:|",
            ]
        )
        for family, names in audit["check_families"].items():
            lines.append(f"| {family} | {len(names)} |")

    return "\n".join(lines) + "\n"


def matrix_coverage_json(audit: dict[str, Any]) -> str:
    return json.dumps(audit, indent=2, sort_keys=True)


def _tool_names(variants: list[dict[str, Any]]) -> list[str]:
    names: list[str] = []
    seen = set()
    for variant in variants:
        for tool in variant.get("tools", []):
            name = str(tool.get("name", ""))
            if name and name not in seen:
                seen.add(name)
                names.append(name)
    return names


def _first_tool_def(variants: list[dict[str, Any]], name: str) -> dict[str, Any]:
    for variant in reversed(variants):
        for tool in variant.get("tools", []):
            if tool.get("name") == name:
                return tool
    return {}


def _tool_accepts_arguments(variants: list[dict[str, Any]], name: str) -> bool:
    schema = _first_tool_def(variants, name).get("input_schema", {})
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    return bool(properties or required)


def _ratio(numerator: int, denominator: int) -> float:
    if not denominator:
        return 1.0
    return round(numerator / denominator, 3)
