"""Adapters that normalize provider transcripts into trace-review events."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> Any:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def claude_messages_to_trace(payload: dict[str, Any] | list[dict[str, Any]]) -> dict[str, Any]:
    """Normalize Claude-style Messages API content blocks into trace steps."""

    if isinstance(payload, list):
        messages = payload
        name = "claude_trace"
        task = ""
        rubric = {}
    else:
        messages = payload.get("messages", [])
        name = payload.get("name", "claude_trace")
        task = payload.get("task", "")
        rubric = payload.get("rubric", {})

    steps: list[dict[str, Any]] = []
    for message in messages:
        role = message.get("role")
        content = _content_blocks(message.get("content", []))
        for index, block in enumerate(content):
            block_type = block.get("type")
            if role == "assistant":
                if block_type == "thinking":
                    steps.append(
                        {
                            "source": "claude_thinking",
                            "summary": block.get("thinking", ""),
                            "signature_present": bool(block.get("signature")),
                            "type": "reasoning",
                        }
                    )
                elif block_type == "redacted_thinking":
                    steps.append(
                        {
                            "opaque": True,
                            "source": "claude_redacted_thinking",
                            "summary": "",
                            "type": "reasoning",
                        }
                    )
                elif block_type == "tool_use":
                    steps.append(
                        {
                            "args": block.get("input", {}),
                            "id": block.get("id"),
                            "name": block.get("name"),
                            "type": "tool_call",
                        }
                    )
                elif block_type == "text":
                    step_type = "reasoning" if _has_later_tool_use(content, index) else "final"
                    key = "summary" if step_type == "reasoning" else "text"
                    steps.append(
                        {
                            key: block.get("text", ""),
                            "source": "assistant_text" if step_type == "reasoning" else "assistant_final_text",
                            "type": step_type,
                        }
                    )
            elif role == "user" and block_type == "tool_result":
                steps.append(
                    {
                        "ok": not bool(block.get("is_error", False)),
                        "output": _stringify_tool_result(block.get("content", "")),
                        "tool_call_id": block.get("tool_use_id"),
                        "type": "tool_result",
                    }
                )

    return {
        "name": name,
        "rubric": rubric,
        "steps": steps,
        "task": task,
    }


def _content_blocks(content: Any) -> list[dict[str, Any]]:
    if isinstance(content, str):
        return [{"text": content, "type": "text"}]
    if isinstance(content, list):
        return [block for block in content if isinstance(block, dict)]
    return []


def _has_later_tool_use(content: list[dict[str, Any]], index: int) -> bool:
    return any(block.get("type") == "tool_use" for block in content[index + 1 :])


def _stringify_tool_result(content: Any) -> str:
    if isinstance(content, str):
        return content
    return json.dumps(content, sort_keys=True)
