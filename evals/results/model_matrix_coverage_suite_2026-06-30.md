# Matrix Coverage Suite

Passed: no
Matrices: 18
Passed matrices: 2
Failed matrices: 16
Total tools: 152
Total cases: 192
Total argument cases: 141
Total boundary pairs: 766

## Matrix Summary

| Matrix | Passed | Tools | Cases | Expected | Forbidden | Arg Cases | Check Families | Boundary Pairs |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| agent audit skill workflow-selection matrix | no | 7 | 7 | 1.000 | 1.000 | 7 | 0 | 42 |
| clickhouse mcp tool-selection matrix | no | 3 | 10 | 1.000 | 1.000 | 7 | 3 | 6 |
| codex harness trace adapter matrix | yes | 2 | 2 | 1.000 | 1.000 | 2 | 2 | 2 |
| coding file-tool selection matrix | no | 4 | 7 | 1.000 | 1.000 | 7 | 0 | 12 |
| context7 mcp tool-selection matrix | no | 2 | 9 | 1.000 | 1.000 | 9 | 3 | 2 |
| filesystem mcp tool-selection matrix | no | 11 | 11 | 1.000 | 1.000 | 10 | 0 | 110 |
| firecrawl mcp tool-selection matrix | no | 12 | 15 | 1.000 | 0.833 | 14 | 3 | 34 |
| github mcp tool-selection matrix | no | 12 | 16 | 1.000 | 1.000 | 15 | 4 | 132 |
| trace-adapter harness matrix | no | 1 | 2 | 1.000 | 0.000 | 2 | 0 | 3 |
| humwork mcp tool-selection matrix | no | 5 | 7 | 1.000 | 1.000 | 0 | 0 | 20 |
| insforge mcp tool-selection matrix | no | 18 | 16 | 0.833 | 0.778 | 0 | 0 | 36 |
| openwork ui mcp tool-selection matrix | no | 4 | 7 | 1.000 | 1.000 | 1 | 0 | 12 |
| playwright mcp tool-selection matrix | no | 13 | 13 | 1.000 | 1.000 | 11 | 0 | 156 |
| postgres mcp pro tool-selection matrix | no | 9 | 9 | 1.000 | 1.000 | 5 | 0 | 24 |
| screenpipe mcp tool-selection matrix | no | 11 | 7 | 0.636 | 0.727 | 0 | 0 | 20 |
| slack mcp tool-selection matrix | no | 8 | 8 | 1.000 | 1.000 | 6 | 0 | 56 |
| supabase mcp database tool-selection matrix | no | 5 | 12 | 1.000 | 1.000 | 12 | 3 | 14 |
| zymtrace mcp tool-selection matrix | yes | 25 | 34 | 1.000 | 1.000 | 33 | 34 | 85 |

## Remaining Gaps

### agent audit skill workflow-selection matrix
- Cases without check_family: raw ide events need normalization, single normalized trace review, trace regression suite, full agent audit bundle, tool descriptions causing bad selection, new model skill tuning, repeated matrix failures need hill climb

### clickhouse mcp tool-selection matrix
- Cases without check_family: unknown connection lists databases, known database table pattern uses metadata, schema question uses table metadata, aggregate count uses select, top rows sample uses select, insert is refused in read only catalog, drop table is refused in read only catalog

### coding file-tool selection matrix
- Cases without check_family: find python files, find function definition, read known file, find todos, list markdown docs, investigate trace review flow, map model matrix implementation

### context7 mcp tool-selection matrix
- Cases without check_family: generic library needs resolution, well known framework still resolves, exact id bypasses resolution, versioned exact id bypasses resolution, package name with topic resolves first, previously resolved id queries directly

### filesystem mcp tool-selection matrix
- Cases without check_family: read one known file, read several known files, create new file with full content, targeted line edit, create nested directory, list immediate directory children, recursive tree view, recursive filename search, get file metadata, move file to archive, list accessible roots

### firecrawl mcp tool-selection matrix
- Never forbidden: firecrawl_interact, firecrawl_monitor_create
- Expected without argument checks: firecrawl_agent
- Cases without check_family: single known page structured fields, several known pages, batch status, discover matching urls on known site, unknown source web search, comprehensive section crawl, crawl status, multi page structured extraction, complex autonomous research, agent status, interactive page operation, create pricing monitor

### github mcp tool-selection matrix
- Cases without check_family: read known repository file, find code symbol with unknown path, search issues by phrase, read specific issue, comment on existing issue, create new issue, list open pull requests by base branch, search pull requests by author and phrase, read changed files for specific pull request, create draft pull request, get failed job log content, get workflow run metadata

### trace-adapter harness matrix
- Never forbidden: Task
- Cases without check_family: investigate trace review flow, map model matrix implementation
- Unknown forbidden tools: Glob, Grep, Read

### humwork mcp tool-selection matrix
- Expected without argument checks: consult_expert, send_chat_message, get_chat_messages, close_chat, rate_chat
- Cases without check_family: blocked production incident consults expert, active expert session sends focused follow-up, check expert reply reads messages, resolved consultation closes chat, closed consultation gets rating, basic docs answer avoids expert spend, secrets request avoids external chat

### insforge mcp tool-selection matrix
- Never expected: delete-bucket, create-function, delete-function
- Never forbidden: fetch-sdk-docs, get-anon-key, get-container-logs, bulk-upsert
- Expected without argument checks: fetch-docs, fetch-sdk-docs, get-anon-key, get-container-logs, get-table-schema, run-raw-sql, download-template, bulk-upsert, create-bucket, get-function, update-function, create-deployment, start-deployment
- Missing quality checks: fetch-sdk-docs, get-container-logs, get-table-schema, get-backend-metadata, bulk-upsert, create-bucket, list-buckets, delete-bucket, create-function, get-function, update-function, delete-function, start-deployment
- Cases without check_family: new project setup reads instructions, new app bootstrap uses template, backend inventory uses metadata, known table details use schema, explicit sql uses raw sql, csv import uses bulk upsert, storage inventory lists buckets, create storage bucket uses create bucket, read function uses get function, update function uses update function, function logs use container logs, sdk docs use sdk docs, client token uses anon key, absolute source deploy uses create deployment, prepared remote upload starts deployment, relative deploy path avoids tool

### openwork ui mcp tool-selection matrix
- Cases without check_family: bridge check uses status, unknown current screen uses snapshot, action discovery uses list actions, known action id executes action, unknown action id lists actions first, coordinate click avoids semantic bridge, app maybe closed checks status before action

### playwright mcp tool-selection matrix
- Expected without argument checks: browser_snapshot, browser_fill_form
- Cases without check_family: navigate to url, inspect page for actionable refs, capture full page visual proof, click known target, type search and submit, fill multi field form, select dropdown option, wait for success text, evaluate local storage, press escape key, list api network requests, inspect numbered network request, get console errors

### postgres mcp pro tool-selection matrix
- Expected without argument checks: get_top_queries, analyze_workload_indexes
- Cases without check_family: discover schemas, list schema objects, inspect table structure, run ready read query, get query plan, rank slow workload queries, workload index tuning, specific query index tuning, database health check

### screenpipe mcp tool-selection matrix
- Never expected: export-video, list-meetings, get-frame-elements, run-pipe
- Never forbidden: export-video, list-meetings, frame-context
- Expected without argument checks: search-content, activity-summary, search-elements, frame-context, keyword-search, create-pipe, pipe-logs
- Missing quality checks: export-video
- Cases without check_family: broad morning recap starts summary, exact keyword uses keyword search, speaker transcript uses content search, ui button lookup uses elements, known frame detail uses frame context, create recurring automation uses pipe, verify pipe output uses logs

### slack mcp tool-selection matrix
- Expected without argument checks: slack_list_channels, slack_get_users
- Cases without check_family: list channels to find id, post top level channel message, reply in existing thread, read recent channel messages, read thread replies, add reaction to message, list users to find id, get known user profile

### supabase mcp database tool-selection matrix
- Cases without check_family: list public tables, inspect table columns, list applied migrations, list installed extensions, run read only report query, ddl create table uses migration, ddl alter table uses migration, ddl create index uses migration, rls policy uses migration
