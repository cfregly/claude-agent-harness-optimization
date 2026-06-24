from pathlib import Path
import subprocess
import sys
import unittest

from claude_agent_prompting.adapters import claude_messages_to_trace, load_json


ROOT = Path(__file__).resolve().parents[1]


class AdapterTests(unittest.TestCase):
    def test_claude_messages_normalize_to_trace(self):
        payload = load_json(ROOT / "evals" / "examples" / "claude_messages.json")
        trace = claude_messages_to_trace(payload)
        self.assertEqual("claude_messages_trace", trace["name"])
        self.assertEqual("reasoning", trace["steps"][0]["type"])
        self.assertEqual("tool_call", trace["steps"][1]["type"])
        self.assertEqual("tool_result", trace["steps"][2]["type"])
        self.assertEqual("final", trace["steps"][-1]["type"])

    def test_cli_normalize_claude(self):
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "claude_agent_prompting",
                "normalize-claude",
                "evals/examples/claude_messages.json",
            ],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn('"type": "tool_call"', result.stdout)


if __name__ == "__main__":
    unittest.main()
