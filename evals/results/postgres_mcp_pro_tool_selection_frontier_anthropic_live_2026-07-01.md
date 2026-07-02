# postgres mcp pro tool-selection matrix

Live: yes
Passed: yes
Planned: 18
Passed cases: 18
Failed cases: 0
Errors: 0
Skipped: 0
Score: 1.000

## Matrix Summary

- total: 18
- passed_cases: 18
- failed_cases: 0
- errors: 0
- skipped: 0
- score: 1.0

## Results

| Provider | Model | Harness | Tool Variant | Instruction Variant | Case | Status | Chosen |
|---|---|---|---|---|---|---|---|
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | discover schemas | passed | list_schemas |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | list schema objects | passed | list_objects |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | inspect table structure | passed | get_object_details |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | run ready read query | passed | execute_sql |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | get query plan | passed | explain_query |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | rank slow workload queries | passed | get_top_queries |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | workload index tuning | passed | analyze_workload_indexes |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | specific query index tuning | passed | analyze_query_indexes |
| anthropic | claude-opus-4-8 | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | database health check | passed | analyze_db_health |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | discover schemas | passed | list_schemas |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | list schema objects | passed | list_objects |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | inspect table structure | passed | get_object_details |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | run ready read query | passed | execute_sql |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | get query plan | passed | explain_query |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | rank slow workload queries | passed | get_top_queries |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | workload index tuning | passed | analyze_workload_indexes |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | specific query index tuning | passed | analyze_query_indexes |
| anthropic | claude-opus-4-8 | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | database health check | passed | analyze_db_health |

## Cell Summary

| Provider | Harness | Tool Variant | Instruction Variant | Passed | Failed | Errors | Skipped | Score |
|---|---|---|---|---:|---:|---:|---:|---:|
| anthropic | prompt_json | stock_postgres_mcp_pro | postgres_host_rules | 9 | 0 | 0 | 0 | 1.000 |
| anthropic | prompt_json | tuned_postgres_mcp_pro_boundaries | postgres_host_rules | 9 | 0 | 0 | 0 | 1.000 |
