Title options (pick one):
1. Open-source agent skill for bug bounty: recon → impact routing → playbooks → report
2. I distilled bug-bounty writeups into an installable agent skill — feedback?
3. Agent skill: scope-first bug bounty workflow that defaults to stealth

Body:

Hey all — I open-sourced an Agent Skills package that turns Claude Code / OpenCode / Codex into a scope-aware bug-bounty assistant.

Repo: https://github.com/YangTech-gh/Awesome-Bug-Bounty
Install: `npx skills@latest add YangTech-gh/Awesome-Bug-Bounty@awesome-bug-bounty`

It's not a scanner. It's context + workflow:

- Operating profile gate: stealth (no cloud keys, offline tools) vs full, written to `profile.yaml` per engagement
- Non-duplicated path: one scope manifest → one asset inventory → tools read shared surfaces
- Impact-first routing (auth bypass > ATO > RCE > SSRF/IDOR > XSS > leaks)
- Distilled playbooks for 36 vuln classes, payloads, business logic/races
- Fallback to 12 source repos only when local knowledge is thin

Authorized testing only — built to keep you inside ROE.

What I want feedback on:
1. Would you trust agent-distilled writeup knowledge, or do you always go to primary sources?
2. What's missing for API/MCP surface testing?
3. Stealth defaults — too aggressive or right?

Not affiliated with any program. No auto-scanning against third parties.
