Show HN: Agent skill that routes bug-bounty work by impact, not scanner noise

https://github.com/YangTech-gh/Awesome-Bug-Bounty

I merged curated bug-bounty writeup indexes, payload libraries, business-logic playbooks, and tool matrices into one Agent Skills package (SKILL.md + knowledge/ files). It installs anywhere the open standard works:

npx skills@latest add YangTech-gh/Awesome-Bug-Bounty@awesome-bug-bounty

What it does:
- One-question operating profile (stealth / no API keys vs full) persisted per engagement
- Scope → deduped recon workspace → route by highest-impact surface → playbook → report
- 36 vuln classes, payload/WAF-bypass cheat sheet, race/business-logic playbooks
- Tool matrix (Burp vs Caido vs ZAP, AI hunters, MCP stack) + copy-paste install guide
- Falls back to 12 source repos only when the distilled knowledge isn't enough

Authorized testing only — the skill refuses to suggest going out of scope.

Curious what other hunters think: is distilling writeups into agent context useful, or does it rot too fast to trust?
