import unittest

from claude_agent_harness_opt.matrix_coverage import (
    audit_matrix_coverage_data,
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


if __name__ == "__main__":
    unittest.main()
