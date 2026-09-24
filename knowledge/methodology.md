# Methodology, Recon & Reporting

Distilled from aw-junaid/bug-bounty methodologies/cheatsheets and hack-skills recon/api-sec routers.

## Recon pipeline

1. **Asset discovery**
   - Subdomains: subfinder, assetfinder, amass, crt.sh, DNS brute (ffuf -w wordlist).
   - Probing: httpx (status, tech detect, titles), dnsx.
   - Takeover check: nuclei subdomain-takeover templates / can-i-take-over-xyz.
2. **Content discovery**
   - URLs: katana, gau, waybackurls, hakrawler; merge + dedupe.
   - Directories/files: ffuf/gobuster with seclists/common + backup extensions (`.bak`, `.old`, `~`).
   - APIs: kiterunner, ApiHunter, OpenAPI/Swagger/GQL introspection, JS file endpoint extraction (LinkFinder/knockpy).
3. **Secrets & exposure**
   - GitHub/gitlab secret scanning (trufflehog, gitleaks), `.git`/`.env`/`.DS_Store`, backup files, npm/pip package leaks, dependency confusion checks.
4. **Tech fingerprint**: Wappalyzer/httpx tech, framework-specific defaults (Flask debug, Spring actuators, Jenkins, Tomcat manager).
5. **Auth surface mapping**: login, SSO/SAML/OIDC providers, password reset flows, 2FA enrollment, API keys in JS.

## Prioritization (impact first)

```
RCE / SQLi (data dump) > Auth bypass / ATO > SSRF (cloud metadata) >
IDOR (PII/mass data) > Stored XSS (admin) > Business logic (money) >
Race limits > CSRF/CORS/open redirect > Info disclosure > Low-impact XSS
```

## API testing notes

- Discover: OpenAPI (`/swagger.json`, `/openapi.yaml`), GraphQL `/graphql` introspection, mobile backend certs.
- Test: BOLA (swap object IDs across roles), BFLA (function-level: admin endpoint with user token), mass assignment (send `role`, `is_admin`, `user_id`), rate limits (bomb one endpoint), pagination abuse (`limit=-1` or huge), JWT/API-key hygiene in transit + logs.
- GraphQL: introspection off? batching, depth/complexity DoS, IDOR on global IDs, mutation authz.

## Report template

```markdown
# Title: [Vuln type] in [endpoint/feature] leading to [impact]

## Summary
One paragraph: what, where, impact.

## Severity
[CVSS or program rubric] — justification.

## Affected endpoint(s)
- METHOD https://host/path (param names)

## Steps to reproduce
1. ...
2. ...

## Proof of concept
Request/response (redact secrets). Screenshots if UI.

## Impact
Who/what is affected; data or action demonstrated (minimal).

## Remediation
Server-side check, authz fix, rate limit, etc.

## References
OWASP/CWE/writeup links.
```

## Cheatsheet command anchors

- ffuf dir: `ffuf -u https://t/FUZZ -w seclists/Discovery/Web-Content/common.txt -mc 200,301,403,500`
- ffuf vhosts: `ffuf -u https://t -H "Host: FUZZ.t" -w subdomains.txt`
- nuclei: `nuclei -u https://t -severity critical,high -rl 100`
- httpx: `cat subs.txt | httpx -sc -title -tech-detect`
- sqlmap: `sqlmap -u 'https://t/?id=1' --batch --level 3 --risk 2`
- dalfox: `dalfox url 'https://t/?q=x' --pipe`
- cookie auth replay: copy low-priv session → Burp Autorize / Suite Auth Replay.

## Wordlists (in aw-junaid/bug-bounty resources)

- `custom-subdomains.txt` — curated subdomains for asset discovery.
- `directories-small.txt` — compact directory fuzz list.
- `xss-payloads.txt` — XSS collection for filter bypass.

## Safety

Only test assets in program scope. Respect rate limits and ROE. Stop on destructive findings and report privately.
