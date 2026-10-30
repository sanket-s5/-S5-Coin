# Upstream Bitcoin Core Policy

- Do not pin an upstream release based on guesswork. Review the current maintained release and security advisories at the time of implementation.
- Record the exact upstream tag and commit hash before creating the fork.
- Preserve `COPYING` and all copyright notices; review license obligations before distribution.
- Maintain a clean record of S5 patches and periodically merge upstream security fixes.
- Never silently modify consensus rules. Every change requires a written specification, test vectors, review, and a clearly documented activation plan.
- The current S5 repository is a documentation scaffold. No upstream source has been copied or modified yet.
