I open-sourced an agent skill for bug bounty hunting.

One install command puts a scope-aware workflow into Claude Code, OpenCode, Codex, Cursor, and 70+ other agents:

npx skills@latest add YangTech-gh/Awesome-Bug-Bounty@awesome-bug-bounty

What it packages:
→ Recon methodology with a non-duplicated engagement path (one workspace per program)
→ Impact-first routing so agents chase auth bypass / ATO / RCE before low-hive XSS
→ Playbooks for 36 vulnerability classes, payload cheat sheets, business-logic + race condition checklists
→ Tool selection matrix and copy-paste install guides
→ A "stealth" default that keeps cloud API keys out unless you opt in

Built for authorized testing only — the skill is written to keep agents inside program scope and rules of engagement.

Repo: https://github.com/YangTech-gh/Awesome-Bug-Bounty
skills.sh: https://skills.sh/yangtech-gh/awesome-bug-bounty/awesome-bug-bounty

Curious whether other security folks find agent-maintained knowledge bases useful in real engagements, or if primary sources always win.
