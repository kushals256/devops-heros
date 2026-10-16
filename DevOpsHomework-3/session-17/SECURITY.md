# Security controls — Session 17

| Control | Tool | Gate |
|---|---|---|
| Unit tests | pytest | Fail job if tests fail |
| SAST | Bandit | Fail on medium+ findings (`-ll`) |
| SCA | pip-audit | Fail on known vulnerable packages |
| Secret scan | grep for `AKIA…` / aws_secret patterns | Fail if matches found |
| Container scan | Trivy HIGH/CRITICAL | Fail with `--exit-code 1` |
| Deploy | Only after push succeeds | `needs: push` |

Never commit `.env`, access keys, or production Secrets to Git.
