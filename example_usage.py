from client import CodePatchSynthesizer

before = "def add(x, y):\n    return x + y\n"
after = "def add(x, y):\n    # Ensure numbers\n    return float(x) + float(y)\n"

diff = CodePatchSynthesizer.generate_unified_diff(before, after)
print("Synthesized Git Patch:\n" + diff)
