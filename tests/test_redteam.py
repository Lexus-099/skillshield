"""
Red-team corpus: realistic malicious skills, and safe skills that look suspicious.

Each malicious sample must be flagged at its expected severity or above, judged
by its worst finding. Each safe sample must have no findings.

Samples SkillShield does not handle yet are marked xfail(strict=True). When a
change makes one pass, pytest reports it as an unexpected pass and fails, so
remove that sample from KNOWN_GAPS or KNOWN_FALSE_POSITIVES in the same PR.
Each entry names the GitHub issue that tracks it.

All samples are defanged: they use example.com and dummy account numbers, and
contain nothing that runs. See tests/fixtures/redteam/README.md.
"""

from pathlib import Path

import pytest

from skillshield import SkillScanner
from skillshield.rules import Severity

CORPUS = Path(__file__).parent / "fixtures" / "redteam"
ORDER = [Severity.INFO, Severity.LOW, Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL]

# The lowest severity each malicious sample must be flagged at.
EXPECTED = {
    "01-plain-injection": Severity.CRITICAL,
    "02-paraphrased-injection": Severity.CRITICAL,
    "03-hidden-html-comment": Severity.CRITICAL,
    "04-zero-width-split": Severity.CRITICAL,
    "05-homoglyph": Severity.CRITICAL,
    "06-base64-payload": Severity.CRITICAL,
    "07-curl-pipe-shell": Severity.CRITICAL,
    "08-natural-exfil": Severity.CRITICAL,
    "09-markdown-image-exfil": Severity.HIGH,
    "10-python-exfil": Severity.CRITICAL,
    "11-impersonation": Severity.HIGH,
    "12-rug-pull": Severity.CRITICAL,
    "13-tool-poisoning": Severity.HIGH,
    "14-delayed-trigger": Severity.HIGH,
}

# Malicious samples not yet flagged at their expected severity: sample -> what is missing.
KNOWN_GAPS = {
    "02-paraphrased-injection": "reworded instruction override",
    "04-zero-width-split": "text is not normalised before matching (zero-width characters)",
    "05-homoglyph": "text is not normalised before matching (lookalike letters)",
    "06-base64-payload": "base64 is flagged but its decoded content is not scanned",
    "07-curl-pipe-shell": "piping a downloaded script into a shell",
    "08-natural-exfil": "plain-English instruction to send secret files to a URL",
    "09-markdown-image-exfil": "data leaked through a markdown image URL",
    "10-python-exfil": "code that posts environment variables to a URL",
    "11-impersonation": "persona that denies being an AI",
    "12-rug-pull": "instruction to replace the skill with remote content",
    "13-tool-poisoning": "hidden side action the user is told nothing about",
    "14-delayed-trigger": "dormant instruction that fires on a trigger word",
}

# Safe samples that are wrongly flagged: sample -> why it is safe.
KNOWN_FALSE_POSITIVES = {
    "b1-security-docs": "documentation that quotes an attack phrase as an example",
}


def _worst(findings) -> Severity | None:
    return max((f.severity for f in findings), key=ORDER.index, default=None)


def _samples(kind, known):
    params = []
    for path in sorted((CORPUS / kind).glob("*.md")):
        marks = []
        if path.stem in known:
            marks.append(pytest.mark.xfail(reason=known[path.stem], strict=True))
        params.append(pytest.param(path, id=path.stem, marks=marks))
    return params


def test_every_malicious_sample_has_an_expected_severity():
    stems = {p.stem for p in (CORPUS / "malicious").glob("*.md")}
    assert stems == set(EXPECTED)
    assert set(KNOWN_GAPS) <= stems


@pytest.mark.parametrize("path", _samples("malicious", KNOWN_GAPS))
def test_malicious_sample_is_flagged(path):
    result = SkillScanner().scan_file(path)
    worst = _worst(result.findings)
    expected = EXPECTED[path.stem]
    assert worst is not None, f"{path.stem}: no findings"
    assert ORDER.index(worst) >= ORDER.index(
        expected
    ), f"{path.stem}: worst finding is {worst.value}, expected {expected.value} or above"


@pytest.mark.parametrize("path", _samples("benign", KNOWN_FALSE_POSITIVES))
def test_safe_sample_is_not_flagged(path):
    result = SkillScanner().scan_file(path)
    assert result.findings == [], f"{path.stem}: {[f.rule_id for f in result.findings]}"
