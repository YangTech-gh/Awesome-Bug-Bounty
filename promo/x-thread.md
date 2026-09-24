🧵 1/ Bug bounty knowledge, packaged as an agent skill.

Recon → route by impact → playbook → report. Installs into Claude Code, OpenCode, Codex, Cursor + 70 other agents with one command:

npx skills@latest add YangTech-gh/Awesome-Bug-Bounty@awesome-bug-bounty

2/ What's inside
• 36 vuln classes with hunt focus (XSS → smuggling → GraphQL)
• Payload/WAF-bypass cheat sheet by context
• Business logic + race playbooks (payment matrix, 9 heuristic checks)
• Recon methodology, deduped engagement path, report template
• Tool matrix + install commands for the whole stack

3/ Design choices that matter for agents:
• Stealth-first default: no cloud API keys unless you opt in
• One workspace per program — tools fan out over shared files, no duplicate scanning
• Findings deduped by METHOD+host+path+param+class before writeup
• Source repos as fallback only when distilled knowledge isn't enough

4/ Install (any skills-compatible agent):

npx skills@latest add YangTech-gh/Awesome-Bug-Bounty@awesome-bug-bounty

Claude Code plugin path:
/plugin marketplace add YangTech-gh/Awesome-Bug-Bounty

Repo: https://github.com/YangTech-gh/Awesome-Bug-Bounty
Listed: https://skills.sh/yangtech-gh/awesome-bug-bounty/awesome-bug-bounty

5/ Authorized testing only. Stay in scope.

Feedback welcome — especially from hunters who've tried agent-assisted recon. What would you cut from the knowledge base?
