# Awesome Bug Bounty

A merged bug-bounty knowledge base packaged as an **opencode skill**, distilled from curated writeup indexes, payload libraries, methodology repos, business-logic playbooks, and Burp tooling — with the **source repos registered as fallback references** for deep research.

> Authorized testing only. Stay in program scope and rules of engagement.

## Install (opencode)

The skill lives at `skills/awesome-bug-bounty/SKILL.md`. It is registered globally via `~/.config/opencode/opencode.jsonc`:

- `skills.paths` → this repo's `skills/`
- `references` → all source repos as `@` aliases for fallback research

Restart opencode after config changes. Skill triggers on: bug bounty, writeups, payloads, IDOR, business logic, SSRF, recon methodology, HackerOne reports, API security, etc.

## Structure

```
Awesome-Bug-Bounty/
├── README.md                          ← this file (programs/repos reference)
├── skills/awesome-bug-bounty/SKILL.md ← the skill (distilled knowledge + routers)
└── knowledge/
    ├── vuln-types.md                  ← per-vuln hunt focus + patterns
    ├── payloads.md                    ← payload/bypass cheat sheet
    ├── business-logic.md              ← logic + race playbooks (9 checks, matrices)
    ├── methodology.md                 ← recon pipeline, report template, commands
    └── tools.md                       ← AutorizePro, BurpAPISecuritySuite, bizlogic
```

## Knowledge sources (analysis summary)

| Repo | What was merged |
|---|---|
| [devanshbatham/Awesome-Bugbounty-Writeups](https://github.com/devanshbatham/Awesome-Bugbounty-Writeups) | Writeup index by bug type (XSS, CSRF, LFI, IDOR, SSRF, RCE, race, 2FA, CORS, subdomain takeover, DoS, Android) |
| [ngalongc/bug-bounty-reference](https://github.com/ngalongc/bug-bounty-reference) | Writeups by bug nature incl. XSSI, token theft, OAuth, money stealing, business logic, email, header injection |
| [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 64+ vuln categories: payloads, WAF bypasses, methodology → condensed cheat sheet |
| [yaklang/hack-skills (business-logic-vulnerabilities)](https://github.com/yaklang/hack-skills/tree/main/skills/business-logic-vulnerabilities) | Business-logic methodology, checklist, scenarios (payment matrix, state machines, races) |
| [ekomsSavior/bizlogic](https://github.com/ekomsSavior/bizlogic) | 9 heuristic logic checks + safe exploitation workflow |
| [aw-junaid/bug-bounty](https://github.com/aw-junaid/bug-bounty) | Full web/API methodology, cheatsheets, wordlists, report templates, tool automation |
| [reddelexc/hackerone-reports](https://github.com/reddelexc/hackerone-reports) | Top disclosed reports by bug type + by program (index pointers) |
| [WuliRuler/AutorizePro](https://github.com/WuliRuler/AutorizePro) | Authz-enforcement testing workflow (headers, AI triage, filters) |
| [Teycir/BurpAPISecuritySuite](https://github.com/Teycir/BurpAPISecuritySuite) | API recon/fuzzing suite: 15 attack types, BOLA, multi-role auth replay |

## Programs & platforms reference

### Platforms

| Platform | Notes |
|---|---|
| [HackerOne](https://www.hackerone.com) | Largest marketplace; disclosed report archive via `reddelexc/hackerone-reports` (`docs/tops_by_bug_type`, `docs/tops_by_program`) |
| [Bugcrowd](https://www.bugcrowd.com) | Crowdsourced + private programs |
| [Intigriti](https://www.intigriti.com) | EU-heavy platform, monthly XSS challenges |
| [YesWeHack](https://www.yeswehack.com) | EU VDP/BB platform |
| [Google VRP](https://bughunters.google.com) | Android, Google, Abuse; high payouts |
| [Microsoft MSRC](https://www.microsoft.com/msrc) | Azure/Windows/Office; AAA style |
| [Apple Security](https://security.apple.com) | iOS/macOS/web services |
| [Internet Bug Bounty (IBB)](https://www.internetbugbounty.org) | Internet-critical OSS (curl, Python, OpenSSL…) |

### Programs frequently referenced in top-report datasets

Shopify · GitLab · HackerOne · Uber · Twitter/X/xAI · Node.js · U.S. DoD · Slack · Coinbase · Verizon Media · Automattic · ownCloud/Nextcloud · Vimeo · Pornhub · Rockstar · TikTok · Brave · Yahoo · Starbucks · WordPress · Curl · Rocket.Chat · Acronis — full lists under hackerone-reports `docs/tops_by_program/`.

### Program-selection tips

- Prefer **signal-rich, payout-clear** programs with documented scopes (public or VDP → paid).
- Study **program-specific top reports** before hunting: patterns repeat per codebase.
- Track **acquisition/subdomain sprawl** for takeover & legacy-endpoint hunting.

## Fallback research routing (opencode references)

| Alias | Use when you need… |
|---|---|
| `@awesome-bb-writeups` | Real-world writeup links for a specific bug type |
| `@bug-bounty-reference` | Categorized historical writeups (OAuth, money, XSSI…) |
| `@payloads-all-the-things` | Full payload lists / bypass matrices per category |
| `@hack-skills` | Deep skill playbooks (auth, recon, API, priv-esc…) |
| `@bizlogic` | Logic-scanner source + check definitions |
| `@aw-junaid-bug-bounty` | Methodologies, cheatsheets, wordlists, templates |
| `@hackerone-reports` | Top disclosed reports by type/program |
| `@autorizepro` | AutorizePro source/config details |
| `@burp-api-security-suite` | Suite tabs, export formats, integration flags |

## License

MIT. Source repos retain their own licenses; knowledge is distilled for educational/authorized-testing use.
