# Security policy

## Reporting a vulnerability

**Do not open a public issue for a vulnerability in SkillShield.**

Report it privately through GitHub: go to the [Security tab](https://github.com/obielin/skillshield/security), select **Report a vulnerability**, and include:

1. what the vulnerability is;
2. the steps or file that reproduce it;
3. the impact;
4. a suggested fix, if you have one.

You will get a reply within 7 days. We will agree a fix and a disclosure date with you before anything is made public.

## What counts as a vulnerability

A vulnerability is a flaw in SkillShield itself, for example:

- a crafted skill file that makes SkillShield run code, read or write files outside the scan, or make a network request;
- a crafted file that makes a scan hang or use unbounded memory, such as a regular expression with catastrophic backtracking;
- a crafted file or path that makes `skillshield scan` exit 0 (pass) when it should fail, other than by evading a rule's pattern;
- a flaw in the SARIF or JSON output that could inject content into a tool that reads it.

## What is not a vulnerability

**A skill that SkillShield fails to flag is a detection gap, not a vulnerability.** Pattern-based scanners can always be evaded by rewording, and improving coverage in the open is how the rules get better. Report it with the **Detection gap** issue form, using a defanged sample.

The one exception: if the missed skill is part of an active campaign that is not yet public, report it privately as above, so the details are not published before the skill is taken down.

Also out of scope:

- vulnerabilities in Python itself or in the development tools (report those upstream);
- attacks that need someone to already control the machine running the scan.

## Supported versions

Security fixes are made for the latest release. Please upgrade before reporting.

## Disclosure

We follow coordinated disclosure. Once a fix is released, the reporter is credited in [CHANGELOG.md](CHANGELOG.md) and the GitHub advisory, unless they prefer to stay anonymous.
