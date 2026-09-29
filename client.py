"""Unified Diff Generator & Code Patch Synthesizer.
100% Python Standard Library.
"""

import difflib

class CodePatchSynthesizer:
    """Unified diff synthesis and patch generation utility."""
    @staticmethod
    def generate_unified_diff(original, modified, filename="file.py"):
        orig_lines = original.splitlines(keepends=True)
        mod_lines = modified.splitlines(keepends=True)
        diff = difflib.unified_diff(orig_lines, mod_lines, fromfile=f"a/{filename}", tofile=f"b/{filename}")
        return "".join(diff)
