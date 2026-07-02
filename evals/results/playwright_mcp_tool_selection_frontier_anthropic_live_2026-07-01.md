# playwright mcp tool-selection matrix

Live: yes
Passed: no
Planned: 26
Passed cases: 24
Failed cases: 2
Errors: 0
Skipped: 0
Score: 0.923

## Matrix Summary

- total: 26
- passed_cases: 24
- failed_cases: 2
- errors: 0
- skipped: 0
- score: 0.923

## Results

| Provider | Model | Harness | Tool Variant | Instruction Variant | Case | Status | Chosen |
|---|---|---|---|---|---|---|---|
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | navigate to url | passed | browser_navigate |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | inspect page for actionable refs | failed | browser_snapshot |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | capture full page visual proof | passed | browser_take_screenshot |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | click known target | passed | browser_click |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | type search and submit | passed | browser_type |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | fill multi field form | passed | browser_fill_form |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | select dropdown option | passed | browser_select_option |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | wait for success text | passed | browser_wait_for |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | evaluate local storage | passed | browser_evaluate |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | press escape key | passed | browser_press_key |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | list api network requests | passed | browser_network_requests |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | inspect numbered network request | passed | browser_network_request |
| anthropic | claude-opus-4-8 | prompt_json | stock_playwright_mcp | playwright_host_rules | get console errors | passed | browser_console_messages |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | navigate to url | passed | browser_navigate |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | inspect page for actionable refs | failed | browser_snapshot |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | capture full page visual proof | passed | browser_take_screenshot |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | click known target | passed | browser_click |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | type search and submit | passed | browser_type |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | fill multi field form | passed | browser_fill_form |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | select dropdown option | passed | browser_select_option |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | wait for success text | passed | browser_wait_for |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | evaluate local storage | passed | browser_evaluate |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | press escape key | passed | browser_press_key |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | list api network requests | passed | browser_network_requests |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | inspect numbered network request | passed | browser_network_request |
| anthropic | claude-opus-4-8 | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | get console errors | passed | browser_console_messages |

## Cell Summary

| Provider | Harness | Tool Variant | Instruction Variant | Passed | Failed | Errors | Skipped | Score |
|---|---|---|---|---:|---:|---:|---:|---:|
| anthropic | prompt_json | stock_playwright_mcp | playwright_host_rules | 12 | 1 | 0 | 0 | 0.923 |
| anthropic | prompt_json | tuned_playwright_mcp_boundaries | playwright_host_rules | 12 | 1 | 0 | 0 | 0.923 |
