# Safety and Authorization

1. **Only test systems you own or have written permission to test.**
2. Run agents in a sandbox: no external network, least privilege, whitelisted tools, argument validation, step and time limits.
3. The model never runs arbitrary commands. Ordinary software decides which tools exist and which arguments are valid.
4. Keep exploit-generating capability narrow and local. Think before publishing models or traces that automate attacks.
5. Check dataset licenses before commercial use.
6. Check the terms of any stronger model whose outputs you train on (Stage 6).
7. Never commit secrets, tokens or real credentials. Use `.env` (ignored) and cloud secret stores.
8. Disclose real vulnerabilities you find responsibly to maintainers.
