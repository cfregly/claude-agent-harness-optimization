# openwork ui mcp tool-selection matrix

Live: yes
Passed: yes
Planned: 14
Passed cases: 14
Failed cases: 0
Errors: 0
Skipped: 0
Score: 1.000

## Matrix Summary

- total: 14
- passed_cases: 14
- failed_cases: 0
- errors: 0
- skipped: 0
- score: 1.0

## Results

| Provider | Model | Harness | Tool Variant | Instruction Variant | Case | Status | Chosen |
|---|---|---|---|---|---|---|---|
| anthropic | claude-opus-4-8 | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | bridge check uses status | passed | ui_status |
| anthropic | claude-opus-4-8 | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | unknown current screen uses snapshot | passed | ui_snapshot |
| anthropic | claude-opus-4-8 | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | action discovery uses list actions | passed | ui_list_actions |
| anthropic | claude-opus-4-8 | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | known action id executes action | passed | ui_execute_action |
| anthropic | claude-opus-4-8 | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | unknown action id lists actions first | passed | ui_list_actions |
| anthropic | claude-opus-4-8 | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | coordinate click avoids semantic bridge | passed | NO_TOOL |
| anthropic | claude-opus-4-8 | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | app maybe closed checks status before action | passed | ui_status |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | bridge check uses status | passed | ui_status |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | unknown current screen uses snapshot | passed | ui_snapshot |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | action discovery uses list actions | passed | ui_list_actions |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | known action id executes action | passed | ui_execute_action |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | unknown action id lists actions first | passed | ui_list_actions |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | coordinate click avoids semantic bridge | passed | NO_TOOL |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | app maybe closed checks status before action | passed | ui_status |

## Cell Summary

| Provider | Harness | Tool Variant | Instruction Variant | Passed | Failed | Errors | Skipped | Score |
|---|---|---|---|---:|---:|---:|---:|---:|
| anthropic | prompt_json | docs_openwork_ui_mcp | openwork_ui_host_rules | 7 | 0 | 0 | 0 | 1.000 |
| anthropic | prompt_json | source_tuned_openwork_ui_mcp | openwork_ui_host_rules | 7 | 0 | 0 | 0 | 1.000 |
