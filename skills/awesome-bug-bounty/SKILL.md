---
name: awesome-bug-bounty
description: Use when doing bug bounty hunting, vulnerability research, writing or analyzing security reports, picking payloads/bypasses, testing business logic flaws, IDOR/authorization testing, API security testing, recon methodology, or looking up writeups/programs — e.g. "find XSS payload", "business logic checklist", "IDOR testing", "HackerOne top reports", "SSRF bypass", "bug bounty methodology". Merges knowledge from curated repos; falls back to source repos for deep research.
license: MIT
---

# Awesome Bug Bounty

Distilled knowledge base for bug bounty hunting and authorized security research, merged from curated writeup indexes, payload libraries, methodology repos, business-logic playbooks, and tool repos. **Use this skill first; only fetch source repos (Fallback table below) when deeper detail is needed.**

## Operating rules

1. Prefer the distilled knowledge below. Read extended detail in the `knowledge/*.md` files of this repo:
   - `knowledge/vuln-types.md` — per-vuln hunt focus + example patterns
   - `knowledge/payloads.md` — payload/bypass cheat sheet by context
   - `knowledge/business-logic.md` — business logic + race condition playbooks
   - `knowledge/methodology.md` — recon/API methodology, report template, wordlists
   - `knowledge/tools.md` — AutorizePro, BurpAPISecuritySuite, bizlogic usage notes
2. For writeup links, full payload lists, or tool internals: fall back to source repos via the registered opencode references (`@awesome-bb-writeups`, `@bug-bounty-reference`, `@payloads-all-the-things`, `@hack-skills`, `@bizlogic`, `@aw-junaid-bug-bounty`, `@hackerone-reports`, `@autorizepro`, `@burp-api-security-suite`) or the GitHub URLs in the Fallback table.
3. **Authorized testing only.** Stay inside program scope and rules of engagement.
4. Evidence standard for reports: clear impact, minimal repro steps, screenshot/PoC request-response, severity justification (CVSS or program rubric), fix guidance.

## Engage flow (impact-first)

1. **Scope** — confirm in-scope domains/apps, excluded actions, rate limits.
2. **Recon / attack-surface map** — subdomains, endpoints, APIs, tech stack, auth surfaces, JS/API specs (OpenAPI/Swagger), historical endpoints (Wayback).
3. **Route by surface** — pick highest-impact path first (auth bypass > ATO > RCE > SSRF/IDOR > XSS > info leaks).
4. **Deep playbooks** — read matching `knowledge/*.md` section; escalate to fallback repos only if uncovered.
5. **Report** — impact-first writeup per template in `knowledge/methodology.md`.

## Category routers (symptom → knowledge → fallback)

| Symptom / surface | Knowledge | Primary fallback |
|---|---|---|
| Reflected/stored/DOM/blind XSS, CSP bypass | `knowledge/vuln-types.md` | Awesome-Bugbounty-Writeups, PayloadsAllTheThings |
| SQLi, NoSQLi, injection into interpreter | `knowledge/vuln-types.md`, `knowledge/payloads.md` | PayloadsAllTheThings |
| SSRF, cloud metadata, DNS rebinding | `knowledge/vuln-types.md` | PayloadsAllTheThings, hackerone-reports (TOPSSRF) |
| IDOR / BOLA / broken object authz | `knowledge/vuln-types.md`, `knowledge/tools.md` | AutorizePro, BurpAPISecuritySuite, bug-bounty-reference |
| Auth bypass, 2FA/MFA, OAuth/JWT/SAML, ATO | `knowledge/vuln-types.md` | bug-bounty-reference, hack-skills (auth-sec) |
| Business logic (pricing, coupons, workflow, stock, limits) | `knowledge/business-logic.md` | hack-skills business-logic-vulnerabilities, bizlogic |
| Race conditions / TOCTOU | `knowledge/business-logic.md` | PayloadsAllTheThings, hackerone-reports (TOPRACECONDITION) |
| CSRF, CORS, clickjacking, open redirect | `knowledge/vuln-types.md` | Awesome-Bugbounty-Writeups |
| RCE, deserialization, SSTI, template injection | `knowledge/vuln-types.md`, `knowledge/payloads.md` | PayloadsAllTheThings |
| File upload, LFI/RFI, path traversal | `knowledge/vuln-types.md`, `knowledge/payloads.md` | PayloadsAllTheThings |
| API recon, GraphQL, REST, mass assignment | `knowledge/methodology.md`, `knowledge/tools.md` | BurpAPISecuritySuite, hack-skills (api-sec) |
| Subdomain takeover, cache deception, smuggling | `knowledge/vuln-types.md` | PayloadsAllTheThings, bug-bounty-reference |
| Payload / WAF bypass by context | `knowledge/payloads.md` | PayloadsAllTheThings |
| Recon, wordlists, cheatsheets, report templates | `knowledge/methodology.md` | aw-junaid/bug-bounty |
| Top disclosed reports / program-specific patterns | `knowledge/vuln-types.md` (index) | hackerone-reports (`docs/tops_*`) |
| Tooling: authz testing, API fuzzing, biz-logic scan | `knowledge/tools.md` | AutorizePro, BurpAPISecuritySuite, bizlogic |

## Vuln-type quick index

Full detail in `knowledge/vuln-types.md`. Covered classes:

XSS (reflected/stored/DOM/blind/XSSI) · SQLi · NoSQLi · SSRF · XXE · IDOR/BOLA · CSRF · CORS · Auth bypass/ATO · 2FA/MFA bypass · OAuth/JWT/SAML flaws · Race condition · Business logic · RCE/deserialization/SSTI · Command injection · File upload/LFI/RFI · Path traversal · Open redirect · Clickjacking · Subdomain takeover · Web cache deception/poisoning · HTTP request smuggling · CRLF/header injection · Host header attacks · Prototype pollution · GraphQL abuse · Mass assignment · API key leaks · Info disclosure/secrets · DoS · Email/header injection · Supply chain/dependency confusion · WebSocket hijacking · 401/403 bypass · SAML/SSO abuse

## Fallback repositories

| Reference alias | Repository | Role |
|---|---|---|
| `@awesome-bb-writeups` | [devanshbatham/Awesome-Bugbounty-Writeups](https://github.com/devanshbatham/Awesome-Bugbounty-Writeups) | Writeups indexed by bug type (XSS, CSRF, LFI, IDOR, SSRF, RCE, race, 2FA, CORS…) |
| `@bug-bounty-reference` | [ngalongc/bug-bounty-reference](https://github.com/ngalongc/bug-bounty-reference) | Writeups categorized by bug nature (XSSI, OAuth/token theft, money stealing, business logic…) |
| `@payloads-all-the-things` | [swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) | 64+ vuln categories: payloads, bypasses, methodology |
| `@hack-skills` | [yaklang/hack-skills](https://github.com/yaklang/hack-skills) | 100+ agent skills across 14 domains; master/category routers (recon, api-sec, auth-sec…) |
| `@bizlogic` | [ekomsSavior/bizlogic](https://github.com/ekomsSavior/bizlogic) | Business-logic heuristic scanner (9 checks) + optional safe exploitation |
| `@aw-junaid-bug-bounty` | [aw-junaid/bug-bounty](https://github.com/aw-junaid/bug-bounty) | Methodologies, cheatsheets, wordlists, tools, report templates |
| `@hackerone-reports` | [reddelexc/hackerone-reports](https://github.com/reddelexc/hackerone-reports) | Top disclosed HackerOne reports by bug type + by program (`docs/tops_*`) |
| `@autorizepro` | [WuliRuler/AutorizePro](https://github.com/WuliRuler/AutorizePro) | Burp authz-enforcement tester with optional AI false-positive reduction |
| `@burp-api-security-suite` | [Teycir/BurpAPISecuritySuite](https://github.com/Teycir/BurpAPISecuritySuite) | Burp API suite: recon, 15 attack types, BOLA/IDOR, Nuclei/Katana/FFUF integration |

Deep research on a topic: fetch the corresponding reference path (e.g. `@payloads-all-the-things` → `SQL Injection/README.md`) rather than guessing payloads.
