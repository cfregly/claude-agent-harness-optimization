# zymtrace mcp tool-selection matrix

Live: yes
Passed: no
Planned: 136
Passed cases: 118
Failed cases: 18
Errors: 0
Skipped: 0
Score: 0.868

## Matrix Summary

- total: 136
- passed_cases: 118
- failed_cases: 18
- errors: 0
- skipped: 0
- score: 0.868

## Results

| Provider | Model | Harness | Tool Variant | Instruction Variant | Case | Status | Chosen |
|---|---|---|---|---|---|---|---|
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | relative time needs date helper | passed | get_date_time |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | unknown project id uses search | passed | projects_search |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | cpu hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | hot containers use entities | passed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | first trace discovery is meta only | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | high level flamegraph | passed | flamegraph |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | discover metrics before query | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | known metric query | passed | project_metrics_query |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | generated optimization advice | passed | recommendations |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | raw events are explicit | passed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | discover common filter fields | passed | projects_events_aggregate_top_field_values |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top pods endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | default project metrics discovery skips search | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | default project raw sample skips search | passed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | cpu rank first containerized apps | passed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | gpu inference workflow starts with metrics | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | gpu call tree uses hot traces | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | selected trace drilldown is bounded | failed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | full trace error recovers to discovery | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | hot trace discovery is bounded | failed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | resource fallback hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project json flamegraph stays project scoped | passed | project_flamegraph_json |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project event aggregate counts | passed | projects_events_aggregate |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | host metadata aggregation | passed | projects_events_aggregate_host_metadata |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top architectures endpoint | passed | projects_stats_aggregate_top_architectures |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top clusters endpoint | passed | projects_stats_aggregate_top_clusters |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top containers endpoint | passed | projects_stats_aggregate_top_containers |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top deployments endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top hosts endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top executables endpoint | passed | projects_stats_aggregate_top_main_exes |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top namespaces endpoint | passed | projects_stats_aggregate_top_namespaces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top scripts endpoint | passed | projects_stats_aggregate_top_script_names |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top threads endpoint | passed | projects_stats_aggregate_top_thread_names |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | project top user tags endpoint | passed | projects_stats_aggregate_top_user_tags |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | relative time needs date helper | passed | get_date_time |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | unknown project id uses search | passed | projects_search |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | cpu hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | hot containers use entities | passed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | first trace discovery is meta only | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | high level flamegraph | passed | flamegraph |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | discover metrics before query | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | known metric query | passed | project_metrics_query |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | generated optimization advice | passed | recommendations |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | raw events are explicit | passed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | discover common filter fields | passed | projects_events_aggregate_top_field_values |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top pods endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | default project metrics discovery skips search | failed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | default project raw sample skips search | failed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | cpu rank first containerized apps | passed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | gpu inference workflow starts with metrics | failed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | gpu call tree uses hot traces | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | selected trace drilldown is bounded | failed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | full trace error recovers to discovery | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | hot trace discovery is bounded | failed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | resource fallback hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project json flamegraph stays project scoped | failed | project_flamegraph_json |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project event aggregate counts | passed | projects_events_aggregate |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | host metadata aggregation | passed | projects_events_aggregate_host_metadata |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top architectures endpoint | passed | projects_stats_aggregate_top_architectures |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top clusters endpoint | passed | projects_stats_aggregate_top_clusters |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top containers endpoint | passed | projects_stats_aggregate_top_containers |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top deployments endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top hosts endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top executables endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top namespaces endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top scripts endpoint | failed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top threads endpoint | passed | projects_stats_aggregate_top_thread_names |
| anthropic | claude-opus-4-8 | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | project top user tags endpoint | passed | projects_stats_aggregate_top_user_tags |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | relative time needs date helper | passed | get_date_time |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | unknown project id uses search | passed | projects_search |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | cpu hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | hot containers use entities | passed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | first trace discovery is meta only | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | high level flamegraph | passed | flamegraph |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | discover metrics before query | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | known metric query | passed | project_metrics_query |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | generated optimization advice | passed | recommendations |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | raw events are explicit | passed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | discover common filter fields | passed | projects_events_aggregate_top_field_values |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top pods endpoint | passed | projects_stats_aggregate_top_pods |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | default project metrics discovery skips search | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | default project raw sample skips search | passed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | cpu rank first containerized apps | passed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | gpu inference workflow starts with metrics | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | gpu call tree uses hot traces | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | selected trace drilldown is bounded | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | full trace error recovers to discovery | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | hot trace discovery is bounded | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | resource fallback hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project json flamegraph stays project scoped | passed | project_flamegraph_json |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project event aggregate counts | passed | projects_events_aggregate |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | host metadata aggregation | passed | projects_events_aggregate_host_metadata |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top architectures endpoint | passed | projects_stats_aggregate_top_architectures |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top clusters endpoint | passed | projects_stats_aggregate_top_clusters |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top containers endpoint | passed | projects_stats_aggregate_top_containers |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top deployments endpoint | passed | projects_stats_aggregate_top_deployments |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top hosts endpoint | passed | projects_stats_aggregate_top_hosts |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top executables endpoint | passed | projects_stats_aggregate_top_main_exes |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top namespaces endpoint | passed | projects_stats_aggregate_top_namespaces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top scripts endpoint | passed | projects_stats_aggregate_top_script_names |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top threads endpoint | passed | projects_stats_aggregate_top_thread_names |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | project top user tags endpoint | passed | projects_stats_aggregate_top_user_tags |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | relative time needs date helper | passed | get_date_time |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | unknown project id uses search | passed | projects_search |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | cpu hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | hot containers use entities | failed | projects_stats_aggregate_top_containers |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | first trace discovery is meta only | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | high level flamegraph | passed | flamegraph |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | discover metrics before query | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | known metric query | passed | project_metrics_query |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | generated optimization advice | passed | recommendations |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | raw events are explicit | passed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | discover common filter fields | passed | projects_events_aggregate_top_field_values |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top pods endpoint | passed | projects_stats_aggregate_top_pods |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | default project metrics discovery skips search | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | default project raw sample skips search | passed | project_events_raw |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | cpu rank first containerized apps | passed | topentities |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | gpu inference workflow starts with metrics | passed | project_metrics_activity_aggr |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | gpu call tree uses hot traces | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | selected trace drilldown is bounded | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | full trace error recovers to discovery | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | hot trace discovery is bounded | passed | hot_traces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | resource fallback hot functions | passed | topfunctions |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project json flamegraph stays project scoped | passed | project_flamegraph_json |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project event aggregate counts | passed | projects_events_aggregate |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | host metadata aggregation | passed | projects_events_aggregate_host_metadata |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top architectures endpoint | passed | projects_stats_aggregate_top_architectures |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top clusters endpoint | passed | projects_stats_aggregate_top_clusters |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top containers endpoint | passed | projects_stats_aggregate_top_containers |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top deployments endpoint | passed | projects_stats_aggregate_top_deployments |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top hosts endpoint | passed | projects_stats_aggregate_top_hosts |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top executables endpoint | passed | projects_stats_aggregate_top_main_exes |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top namespaces endpoint | passed | projects_stats_aggregate_top_namespaces |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top scripts endpoint | passed | projects_stats_aggregate_top_script_names |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top threads endpoint | passed | projects_stats_aggregate_top_thread_names |
| anthropic | claude-opus-4-8 | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | project top user tags endpoint | passed | projects_stats_aggregate_top_user_tags |

## Cell Summary

| Provider | Harness | Tool Variant | Instruction Variant | Passed | Failed | Errors | Skipped | Score |
|---|---|---|---|---:|---:|---:|---:|---:|
| anthropic | prompt_json | stock_zymtrace_mcp | zymtrace_host_and_skill_rules | 22 | 12 | 0 | 0 | 0.647 |
| anthropic | prompt_json | stock_zymtrace_mcp | zymtrace_host_rules | 29 | 5 | 0 | 0 | 0.853 |
| anthropic | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_and_skill_rules | 33 | 1 | 0 | 0 | 0.971 |
| anthropic | prompt_json | tuned_zymtrace_mcp_boundaries | zymtrace_host_rules | 34 | 0 | 0 | 0 | 1.000 |
