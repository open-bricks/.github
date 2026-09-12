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

- **Zero-Egress & Local-First:** All desktop utilities, document tools, MCP servers, and data storage workflows are engineered to run 100% locally with zero unconsented telemetry, analytics, or cloud data egress.
- **Unprivileged User Mode (Non-Elevation):** Tools operate within standard user privileges and do not require elevated administrator or root privileges for normal desktop operation.
- **Integrity & Source Preservation:** Local transformations, file actions, and data indexers preserve original input data by default and operate non-destructively.
