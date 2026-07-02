# insforge mcp tool-selection matrix

Live: yes
Passed: no
Planned: 38
Passed cases: 34
Failed cases: 4
Errors: 0
Skipped: 0
Score: 0.895

## Matrix Summary

- total: 38
- passed_cases: 34
- failed_cases: 4
- errors: 0
- skipped: 0
- score: 0.895

## Results

| Provider | Model | Harness | Tool Variant | Instruction Variant | Case | Status | Chosen |
|---|---|---|---|---|---|---|---|
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | new project setup reads instructions | passed | fetch-docs |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | new app bootstrap uses template | passed | download-template |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | backend inventory uses metadata | passed | get-backend-metadata |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | known table details use schema | passed | get-table-schema |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | explicit sql uses raw sql | passed | run-raw-sql |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | csv import uses bulk upsert | passed | bulk-upsert |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | storage inventory lists buckets | passed | list-buckets |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | create storage bucket uses create bucket | passed | create-bucket |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | read function uses get function | passed | get-function |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | update function uses update function | passed | update-function |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | function logs use container logs | failed | get-container-logs |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | sdk docs use sdk docs | passed | fetch-sdk-docs |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | client token uses anon key | failed | get-anon-key |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | absolute source deploy uses create deployment | passed | create-deployment |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | prepared remote upload starts deployment | passed | start-deployment |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | relative deploy path avoids tool | failed | create-deployment |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | delete storage bucket uses delete bucket | passed | delete-bucket |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | create function uses create function | passed | create-function |
| anthropic | claude-opus-4-8 | prompt_json | readme_insforge_mcp | insforge_host_rules | delete function uses delete function | passed | delete-function |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | new project setup reads instructions | passed | fetch-docs |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | new app bootstrap uses template | passed | download-template |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | backend inventory uses metadata | passed | get-backend-metadata |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | known table details use schema | passed | get-table-schema |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | explicit sql uses raw sql | passed | run-raw-sql |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | csv import uses bulk upsert | passed | bulk-upsert |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | storage inventory lists buckets | passed | list-buckets |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | create storage bucket uses create bucket | passed | create-bucket |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | read function uses get function | passed | get-function |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | update function uses update function | passed | update-function |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | function logs use container logs | passed | get-container-logs |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | sdk docs use sdk docs | passed | fetch-sdk-docs |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | client token uses anon key | failed | get-anon-key |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | absolute source deploy uses create deployment | passed | create-deployment |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | prepared remote upload starts deployment | passed | start-deployment |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | relative deploy path avoids tool | passed | NO_TOOL |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | delete storage bucket uses delete bucket | passed | delete-bucket |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | create function uses create function | passed | create-function |
| anthropic | claude-opus-4-8 | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | delete function uses delete function | passed | delete-function |

## Cell Summary

| Provider | Harness | Tool Variant | Instruction Variant | Passed | Failed | Errors | Skipped | Score |
|---|---|---|---|---:|---:|---:|---:|---:|
| anthropic | prompt_json | readme_insforge_mcp | insforge_host_rules | 16 | 3 | 0 | 0 | 0.842 |
| anthropic | prompt_json | source_tuned_insforge_mcp | insforge_host_rules | 18 | 1 | 0 | 0 | 0.947 |
