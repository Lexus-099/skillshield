## What does this PR do?

<!-- One to three sentences: what was wrong, and what you changed. -->

## Related issue

<!-- Fixes #123. New rules, scoring changes, new options and new dependencies need an issue first. Bug fixes, false-positive fixes, tests and docs do not. -->

## Type of change

- [ ] Bug fix
- [ ] False-positive or missed-detection fix in an existing rule
- [ ] New detection rule
- [ ] New feature
- [ ] Documentation
- [ ] Refactor (no behaviour change)

## How I checked it

<!-- The commands you ran and what they showed. Say which new test fails without your change. -->

## Checklist

- [ ] I have read [CONTRIBUTING.md](https://github.com/obielin/skillshield/blob/main/CONTRIBUTING.md)
- [ ] If this is a new rule or feature, it has an agreed issue
- [ ] I added a test that fails without this change
- [ ] `pytest`, `ruff check src tests` and `black --check src tests` pass locally
- [ ] Test samples are defanged: no working payloads, live malicious URLs or real secrets
- [ ] For a new rule: two true positives, one true negative and one near-miss test, plus a reference
- [ ] I added a line under `[Unreleased]` in CHANGELOG.md
- [ ] No new runtime dependencies or network calls
