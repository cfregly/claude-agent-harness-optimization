# slack mcp tool-selection matrix

Live: yes
Passed: yes
Planned: 16
Passed cases: 16
Failed cases: 0
Errors: 0
Skipped: 0
Score: 1.000

## Matrix Summary

- total: 16
- passed_cases: 16
- failed_cases: 0
- errors: 0
- skipped: 0
- score: 1.0

## Results

| Provider | Model | Harness | Tool Variant | Instruction Variant | Case | Status | Chosen |
|---|---|---|---|---|---|---|---|
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | list channels to find id | passed | slack_list_channels |
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | post top level channel message | passed | slack_post_message |
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | reply in existing thread | passed | slack_reply_to_thread |
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | read recent channel messages | passed | slack_get_channel_history |
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | read thread replies | passed | slack_get_thread_replies |
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | add reaction to message | passed | slack_add_reaction |
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | list users to find id | passed | slack_get_users |
| anthropic | claude-opus-4-8 | prompt_json | stock_slack_mcp | slack_host_rules | get known user profile | passed | slack_get_user_profile |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | list channels to find id | passed | slack_list_channels |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | post top level channel message | passed | slack_post_message |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | reply in existing thread | passed | slack_reply_to_thread |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | read recent channel messages | passed | slack_get_channel_history |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | read thread replies | passed | slack_get_thread_replies |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | add reaction to message | passed | slack_add_reaction |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | list users to find id | passed | slack_get_users |
| anthropic | claude-opus-4-8 | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | get known user profile | passed | slack_get_user_profile |

## Cell Summary

| Provider | Harness | Tool Variant | Instruction Variant | Passed | Failed | Errors | Skipped | Score |
|---|---|---|---|---:|---:|---:|---:|---:|
| anthropic | prompt_json | stock_slack_mcp | slack_host_rules | 8 | 0 | 0 | 0 | 1.000 |
| anthropic | prompt_json | tuned_slack_mcp_boundaries | slack_host_rules | 8 | 0 | 0 | 0 | 1.000 |
