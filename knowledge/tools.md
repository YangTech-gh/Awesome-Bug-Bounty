# Tooling Notes

## AutorizePro (WuliRuler/AutorizePro)

Burp extension for **authorization enforcement** testing with optional AI triage.

- **Setup**: Burp → Extender → Python env → Jython standalone JAR → Add extension `AutorizePro.py` (no non-ASCII in path).
- **Use**:
  1. Configuration tab → paste low-privilege (2nd account) auth headers into "Insert injected header here".
  2. Optional: uncheck "Check unauthenticated" to skip cookieless tests.
  3. Optional AI: default API or custom OpenAI-compatible endpoint (e.g. Ollama `http://localhost:11434/v1/chat/completions`) + "Enable AI".
  4. Toggle AutorizePro on; browse target with high-priv session.
- **Statuses**: `Bypassed!` (authz fail — red), `Enforced!` (ok — green), `Is enforced???` (configure enforcement detector rules).
- **Filters**: Interception Filters (blacklist/whitelist/regex/Burp scope) — **always scope to target** to avoid cookie leakage and AI cost.
- **Safety**: AI only runs on status-equal JSON responses (length 50–6000); export HTML/CSV reports; logs show AI reasoning per request.

## BurpAPISecuritySuite (Teycir/BurpAPISecuritySuite)

All-in-one Burp suite for **API recon, fuzzing, and AI-assisted triage** (15 attack types, 108+ payloads).

- **Install**: Burp → Extensions → Add → Python → `BurpAPISecuritySuite.py` (Community or Pro + Jython).
- **Workflow**: capture traffic (Recon auto-capture) → review normalized endpoints → optional Passive Discovery (differentials, token lineage, parity drift, abuse chains) → Export AI Bundle → LLM triage.
- **Key tabs**:
  - **Recon**: smart endpoint grouping, noise filter, Export AI Bundle, Refresh Invariants.
  - **Auth Replay**: guest/user/admin header profiles → replay + severity ranking (BOLA triage).
  - **Fuzzer**: 15 attack types (BOLA, IDOR, SQLi, XSS, SSTI, JWT, GraphQL, race, business logic, WAF bypass…) → Intruder/Turbo/cURL/JSON export.
  - **Discovery**: Version Scanner (v1/v2/dev/legacy), Param Miner (admin/debug params), Wayback, Katana, HTTPX, FFUF, Kiterunner, ApiHunter.
  - **Verify**: SQLMap verify, Dalfox verify for candidates.
  - **Sensitive Data**: regex packs for secrets/PII/credentials/infra exposure.
- **Integrations**: Nuclei (with GraphQL templates), subfinder/dnsx, export to Intruder positions, Postman, Insomnia.

## bizlogic (ekomsSavior/bizlogic)

Heuristic **business-logic scanner** (Python, no heavy deps: `requests` + `beautifulsoup4`).

```bash
git clone https://github.com/ekomsSavior/bizlogic && cd bizlogic
pip install requests beautifulsoup4
python bizlogic_scanner.py
# prompts: base URL, rate (default 0.5s), max pages (default 50)
```

- Phases: discovery (crawl, robots/sitemaps/OpenAPI) → auth detection → 9 heuristic checks → optional controlled exploitation (max 5 attempts/finding, 1.0s rate, non-destructive).
- Outputs: `reports/scan_[domain]_[timestamp]/` with text, JSON, HTML, Nuclei templates.
- Detection categories: ownership/transfer, alternate-channel authz, user-controlled keys, weak recovery, wrong ownership, unlimited allocation, premature release, single-action flaws, client-side workflow.

## Complementary stack (from PayloadsAllTheThings / aw-junaid)

| Phase | Tools |
|---|---|
| Subdomains | subfinder, amass, assetfinder, crt.sh |
| Probe | httpx, dnsx |
| Crawl/URLs | katana, gau, waybackurls, hakrawler |
| Content fuzz | ffuf, gobuster, feroxbuster |
| API routes | kiterunner, ApiHunter, LinkFinder |
| Vuln scan | nuclei (custom templates) |
| SQLi/XSS verify | sqlmap, dalfox |
| Race | Turbo Intruder, Burp Suite concurrent tab |
| Authz | AutorizePro, BurpAPISecuritySuite Auth Replay |
| Secrets | trufflehog, gitleaks, git-dumper |
| Logic | bizlogic + manual state-machine mapping |
