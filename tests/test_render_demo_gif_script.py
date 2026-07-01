from pathlib import Path
import subprocess
import sys
import unittest

from scripts import render_demo_gif


ROOT = Path(__file__).resolve().parents[1]


class RenderDemoGifScriptTests(unittest.TestCase):
    def test_help_smoke(self):
        result = subprocess.run(
            [sys.executable, "scripts/render_demo_gif.py", "--help"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("--out", result.stdout)
        self.assertIn("--mp4-out", result.stdout)

    def test_kept_output_lines_summarizes_middle(self):
        lines = render_demo_gif._kept_output_lines("\n".join(f"line {index}" for index in range(10)), 5)

        self.assertEqual("line 0", lines[0])
        self.assertIn("lines omitted", lines[2])
        self.assertEqual("line 9", lines[-1])


if __name__ == "__main__":
    unittest.main()
