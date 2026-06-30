import unittest

from claude_agent_harness_opt.matrix_coverage import (
    audit_matrix_coverage_suite,
    audit_matrix_coverage_data,
    render_matrix_coverage_suite_markdown,
    render_matrix_coverage_markdown,
)


class MatrixCoverageTests(unittest.TestCase):
    def test_audit_reports_missing_positive_negative_and_argument_coverage(self):
        audit = audit_matrix_coverage_data(
            {
                "cases": [
                    {
                        "check_family": "boundary",
                        "expected_args_contains": {"path": ".json"},
                        "expected_tools": ["read_file"],
                        "forbidden_tools": ["search_files"],
                        "name": "read known file",
                        "task": "Read package.json.",
                    },
                    {
                        "expected_tools": ["search_files"],
                        "forbidden_tools": [],
                        "name": "search broad tree",
                        "task": "Find config files.",
                    },
                ],
                "profiles": [{"harnesses": ["prompt_json"], "provider": "trace_fixture"}],
                "tool_variants": [
                    {
                        "name": "test_tools",
                        "tools": [
                            {
                                "name": "read_file",
                                "purpose": "Read one file.",
                                "quality_checks": ["Require a path."],
                            },
                            {
                                "input_schema": {
                                    "properties": {"pattern": "Search pattern"},
                                    "required": ["pattern"],
                                    "type": "object",
                                },
                                "name": "search_files",
                                "purpose": "Search files.",
                            },
                            {"name": "write_file", "purpose": "Write files."},
                        ],
                    }
                ],
            }
        )

        self.assertFalse(audit["passed"])
        self.assertEqual(["write_file"], audit["uncovered"]["never_expected"])
        self.assertEqual(
            ["read_file", "write_file"],
            audit["uncovered"]["never_forbidden"],
        )
        self.assertEqual(
            ["search_files"],
            audit["uncovered"]["expected_without_argument_check"],
        )
        self.assertEqual(
            ["search_files", "write_file"],
            audit["uncovered"]["missing_quality_checks"],
        )
        self.assertEqual(["search broad tree"], audit["uncovered"]["cases_without_check_family"])
        self.assertEqual(["search broad tree"], audit["uncovered"]["cases_without_forbidden"])

    def test_render_matrix_coverage_markdown_includes_summary_and_table(self):
        audit = audit_matrix_coverage_data(
            {
                "cases": [
                    {
                        "check_family": "boundary",
                        "expected_tools": ["lookup"],
                        "forbidden_tools": ["NO_TOOL"],
                        "name": "lookup case",
                        "task": "Lookup a value.",
                    }
                ],
                "name": "sample matrix",
                "profiles": [{"harnesses": ["prompt_json"], "provider": "trace_fixture"}],
                "tool_variants": [
                    {
                        "name": "sample",
                        "tools": [
                            {
                                "name": "lookup",
                                "purpose": "Lookup values.",
                                "quality_checks": ["Use exact ids."],
                            }
                        ],
                    }
                ],
            }
        )

        output = render_matrix_coverage_markdown(audit)

        self.assertIn("# Matrix Coverage: sample matrix", output)
        self.assertIn("Expected tool coverage: 1.000", output)
        self.assertIn("| lookup | 1 | 0 | 0 | yes |", output)

    def test_suite_audit_summarizes_multiple_matrices(self):
        suite = audit_matrix_coverage_suite(
            [
                "evals/model_matrix/zymtrace_mcp_tool_selection.json",
                "evals/model_matrix/clickhouse_mcp_tool_selection.json",
            ]
        )

        self.assertEqual(2, suite["summary"]["matrix_count"])
        self.assertEqual(2, suite["summary"]["passed_matrices"])
        self.assertEqual(0, suite["summary"]["failed_matrices"])
        self.assertTrue(suite["passed"])

    def test_render_suite_markdown_lists_remaining_gaps(self):
        suite = {
            "audits": [
                audit_matrix_coverage_data(
                    {
                "cases": [
                    {
                        "check_family": "boundary",
                        "expected_tools": ["lookup"],
                        "forbidden_tools": ["fallback"],
                        "name": "lookup case",
                        "task": "Lookup a value.",
                    },
                    {
                        "check_family": "boundary",
                        "expected_tools": ["fallback"],
                        "forbidden_tools": ["lookup"],
                        "name": "fallback case",
                        "task": "Use fallback.",
                    }
                ],
                "name": "passing matrix",
                "profiles": [{"harnesses": ["prompt_json"], "provider": "trace_fixture"}],
                "tool_variants": [
                            {
                                "name": "sample",
                                "tools": [
                                    {
                                        "name": "lookup",
                                        "purpose": "Lookup values.",
                                        "quality_checks": ["Use exact ids."],
                                    },
                                    {
                                        "name": "fallback",
                                        "purpose": "Fallback safely.",
                                        "quality_checks": ["Use only for fallback."],
                                    }
                                ],
                            }
                        ],
                    }
                ),
                audit_matrix_coverage_data(
                    {
                        "cases": [
                            {
                                "expected_tools": ["search"],
                                "forbidden_tools": [],
                                "name": "search case",
                                "task": "Search.",
                            }
                        ],
                        "name": "failing matrix",
                        "profiles": [{"harnesses": ["prompt_json"], "provider": "trace_fixture"}],
                        "tool_variants": [
                            {
                                "name": "sample",
                                "tools": [
                                    {"name": "search", "purpose": "Search."},
                                ],
                            }
                        ],
                    }
                ),
            ],
            "passed": False,
            "summary": {
                "failed_matrices": 1,
                "matrix_count": 2,
                "passed_matrices": 1,
                "total_argument_cases": 0,
                "total_boundary_pairs": 2,
                "total_cases": 3,
                "total_tools": 3,
            },
        }

        output = render_matrix_coverage_suite_markdown(suite)

        self.assertIn("# Matrix Coverage Suite", output)
        self.assertIn("| passing matrix | yes |", output)
        self.assertIn("### failing matrix", output)
        self.assertIn("Cases without forbidden tools: search case", output)


if __name__ == "__main__":
    unittest.main()
