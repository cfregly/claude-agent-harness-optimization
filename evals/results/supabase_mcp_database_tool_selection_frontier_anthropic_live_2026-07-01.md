# supabase mcp database tool-selection matrix

Live: yes
Passed: yes
Planned: 24
Passed cases: 24
Failed cases: 0
Errors: 0
Skipped: 0
Score: 1.000

## Matrix Summary

- total: 24
- passed_cases: 24
- failed_cases: 0
- errors: 0
- skipped: 0
- score: 1.0

## Results

| Provider | Model | Harness | Tool Variant | Instruction Variant | Case | Status | Chosen |
|---|---|---|---|---|---|---|---|
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | list public tables | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | inspect table columns | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | list applied migrations | passed | list_migrations |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | list installed extensions | passed | list_extensions |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | run read only report query | passed | execute_sql |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | ddl create table uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | ddl alter table uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | ddl create index uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | rls policy uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | unknown relation error inspects schema | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | table inventory concise skips verbose | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | schema metadata before select star | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | list public tables | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | inspect table columns | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | list applied migrations | passed | list_migrations |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | list installed extensions | passed | list_extensions |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | run read only report query | passed | execute_sql |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | ddl create table uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | ddl alter table uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | ddl create index uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | rls policy uses migration | passed | apply_migration |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | unknown relation error inspects schema | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | table inventory concise skips verbose | passed | list_tables |
| anthropic | claude-opus-4-8 | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | schema metadata before select star | passed | list_tables |

## Cell Summary

| Provider | Harness | Tool Variant | Instruction Variant | Passed | Failed | Errors | Skipped | Score |
|---|---|---|---|---:|---:|---:|---:|---:|
| anthropic | prompt_json | terse_supabase_database_mcp | supabase_database_host_rules | 12 | 0 | 0 | 0 | 1.000 |
| anthropic | prompt_json | tuned_supabase_database_boundaries | supabase_database_host_rules | 12 | 0 | 0 | 0 | 1.000 |
