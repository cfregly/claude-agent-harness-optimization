# Demo recipe for the checked-in public GIF.
# Regenerate from the repo root with:
# python scripts/render_demo_gif.py --out demo.gif --mp4-out demo.mp4
Output demo.gif
Output demo.mp4

Set Width 1200
Set Height 720

Run "python -m claude_agent_harness_opt matrix-coverage evals/model_matrix/zymtrace_mcp_tool_selection.json --strict --markdown"
Run "python scripts/optimize_mcp.py zymtrace --markdown --max-cases 2 --providers anthropic --harnesses prompt_json --variants stock_zymtrace_mcp,tuned_zymtrace_mcp_boundaries --instruction-variants zymtrace_host_and_skill_rules --out /tmp/zymtrace-demo-optimization.md"
Run "python -m claude_agent_harness_opt upstream-pr-packet evals/results/zymtrace_mcp_matrix_live_2026-06-30.json --matrix evals/model_matrix/zymtrace_mcp_tool_selection.json --target-name 'Zymtrace MCP' --target-repo https://docs.zymtrace.com/category/model-context-protocol-mcp/ --baseline-variant stock_zymtrace_mcp --candidate-variant tuned_zymtrace_mcp_boundaries --change-summary 'Clarify default-project, metrics-discovery, resource-first, and bounded hot-trace routing.' --evidence-url https://github.com/cfregly/claude-agent-harness-opt/tree/main/evals/pr_packets/zymtrace_mcp_tool_tuning_2026-06-30 --markdown"
Run "python scripts/check_finding_packets.py"
Run "python scripts/check_public_links.py"
Run "python -c 'print(\"Zymtrace bundle: https://github.com/cfregly/claude-agent-harness-opt/tree/main/evals/pr_packets/zymtrace_mcp_tool_tuning_2026-06-30\")'"
