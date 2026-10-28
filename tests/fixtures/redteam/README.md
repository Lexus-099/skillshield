# Red-team corpus

Realistic malicious skills, and safe skills that look suspicious, used by `tests/test_redteam.py`.

- `malicious/` holds one skill per attack technique. Each must be flagged at the severity listed in `EXPECTED` in the test file.
- `benign/` holds safe skills that use similar words. Each must have no findings.

Samples SkillShield does not catch yet are listed in `KNOWN_GAPS` (or `KNOWN_FALSE_POSITIVES`) and are expected to fail. Each has a GitHub issue. To fix one, change the rules until its test passes, then remove it from the list.

**Every sample is defanged.** URLs use the reserved domain `example.com`, account numbers are zeros, and nothing here runs. New samples must follow the same rules (see "Test samples must be safe" in CONTRIBUTING.md).

Two files contain characters you cannot see in most editors:

- `04-zero-width-split.md` has zero-width spaces (U+200B) inside words.
- `05-homoglyph.md` uses the Cyrillic letter о (U+043E) in place of the Latin o.
