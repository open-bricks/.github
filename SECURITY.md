# Security Policy / Sicherheitsrichtlinie

## Reporting a Vulnerability / Sicherheitslücke melden

If you discover a security vulnerability or security concern within any repository in the `open-bricks` organization or linked open-bricks family repositories, please report it responsibly:

1. **Do NOT open a public issue** or disclose vulnerability details publicly before a fix is available.
2. Use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories) on the affected repository to create a private draft advisory.
3. Or contact the maintainers directly via email:
   - `security@open-bricks.org`
   - `security@ellmos.ai`
   - `lukas@open-bricks.org`
   - `support@lukasgeiger.com`

Project-specific SECURITY policies govern the repositories they cover. For a report about a product repository, consult that repository's current policy for its response commitments.

---

## Response Timeline / Reaktionszeit

- **Acknowledgment:** Within 48 hours (best effort, guaranteed within 7 days)
- **Initial Assessment & Triage:** Within 7 to 14 days
- **Fix & Disclosure Coordination:** Best effort, typically within 30 days depending on severity

---

## Supported Versions / Unterstützte Versionen

| Repository / Tool | Supported Release | Security Updates |
|---|---|---|
| Umbrella repository (`open-bricks/.github`) | Latest commit on `main` | :white_check_mark: Supported |
| Active ecosystem repositories (across `file-bricks`, `doc-bricks`, `dev-bricks`, `ellmos-ai`, `research-line`, `biotec-line`, `assistassets-ai`, `entertain-and-more`, `um-bruch`) | Latest commit or latest stable tag on `main`/`master` | :white_check_mark: Supported |
| Explicitly archived repositories (e.g. `fable-5-hunter`, `recludos-legacy`, `rfep-framework`) | None | :x: End of Life / Read-Only |

---

## Security Invariants / Sicherheitsinvarianten

- **Network, telemetry, and data behavior:** These properties vary by repository and are described in its current documentation and SECURITY policy; no blanket zero-egress guarantee applies to every linked project.
- **Privilege requirements:** Requirements depend on the repository and workflow. The Zombie-Killer-Tray tray launcher can request UAC elevation for termination workflows; see its project documentation.
- **Data integrity and source preservation:** These properties are repository-specific; consult the affected project's documentation rather than treating them as ecosystem-wide guarantees.
