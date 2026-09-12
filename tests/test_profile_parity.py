"""Tests for open-bricks profile parity, timestamps, and ecosystem consistency."""

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILE_EN = REPO_ROOT / "profile" / "README.md"
PROFILE_DE = REPO_ROOT / "profile" / "README_de.md"
ROOT_README = REPO_ROOT / "README.md"
LLMS_TXT = REPO_ROOT / "llms.txt"


def test_files_exist_and_non_empty():
    for f in [PROFILE_EN, PROFILE_DE, ROOT_README, LLMS_TXT]:
        assert f.exists(), f"File {f.name} does not exist"
        assert f.stat().st_size > 200, f"File {f.name} is too small"


def test_timestamp_parity():
    en_content = PROFILE_EN.read_text(encoding="utf-8")
    de_content = PROFILE_DE.read_text(encoding="utf-8")
    root_content = ROOT_README.read_text(encoding="utf-8")
    llms_content = LLMS_TXT.read_text(encoding="utf-8")

    assert "<!-- last-checked: 2026-09-12 -->" in en_content
    assert "<!-- last-checked: 2026-09-12 -->" in de_content
    assert "Last verified: 2026-09-12" in root_content
    assert "## Last-checked: 2026-09-12" in llms_content


def test_repository_counts():
    en_content = PROFILE_EN.read_text(encoding="utf-8")
    de_content = PROFILE_DE.read_text(encoding="utf-8")
    root_content = ROOT_README.read_text(encoding="utf-8")
    llms_content = LLMS_TXT.read_text(encoding="utf-8")

    # Badges
    assert "Public_Repositories-130_Active-success" in en_content
    assert "Oeffentliche_Repositories-130_Aktiv-success" in de_content

    # Summary text
    assert "130 active public repositories" in en_content
    assert "130 aktive öffentliche Repositories" in de_content
    assert "130 active public repositories in total" in root_content
    assert "130 active public repositories total" in llms_content


def test_all_partner_organizations_present():
    expected_orgs = [
        "file-bricks",
        "doc-bricks",
        "dev-bricks",
        "ellmos-ai",
        "research-line",
        "biotec-line",
        "assistassets-ai",
        "entertain-and-more",
        "um-bruch",
    ]
    for path in [PROFILE_EN, PROFILE_DE, ROOT_README, LLMS_TXT]:
        content = path.read_text(encoding="utf-8")
        for org in expected_orgs:
            assert f"https://github.com/{org}" in content or f"github.com/{org}" in content, (
                f"Missing {org} in {path.name}"
            )


def test_no_forbidden_local_paths():
    forbidden = [
        r"C:\Users",
        "C:/Users",
        r"C:\_Local_DEV",
        "C:/_Local_DEV",
        "OneDrive",
    ]
    for path in [PROFILE_EN, PROFILE_DE, ROOT_README, LLMS_TXT]:
        content = path.read_text(encoding="utf-8")
        for pattern in forbidden:
            assert pattern not in content, f"Forbidden local path '{pattern}' found in {path.name}"


def test_fenced_code_blocks_and_mermaid():
    for path in [PROFILE_EN, PROFILE_DE]:
        content = path.read_text(encoding="utf-8")
        # Check backticks count parity
        backticks = content.count("```")
        assert backticks % 2 == 0, f"Odd number of backticks in {path.name}"
        assert "flowchart TD" in content, f"Missing flowchart TD in {path.name}"


def test_security_policy_parity():
    sec_path = REPO_ROOT / "SECURITY.md"
    assert sec_path.is_file(), "SECURITY.md does not exist"
    sec_content = sec_path.read_text(encoding="utf-8")
    assert "48 hours" in sec_content, "Missing 48 hours SLA in SECURITY.md"
    assert "security@open-bricks.org" in sec_content, "Missing primary security contact"
    assert "Zero-Egress" in sec_content, "Missing Zero-Egress invariant in SECURITY.md"
