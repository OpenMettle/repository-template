# Development

The starter requires Python 3.10 or later for repository checks. Add language-specific setup, pinned dependencies and meaningful tests when implementation is introduced.

## Baseline check

```sh
python3 scripts/check_repository.py
```

## Component tests

No component implementation or functional test suite exists yet. Document actual test commands, fixtures and required services here as they are added. CI must not silently skip a required test suite.

## Local configuration

Use sanitized examples. Keep local overrides in ignored files and obtain credentials through the component's documented secret-management mechanism. Do not assume a developer has a particular hostname, disk layout, domain or cluster.

## Performance and quality

For optimization work, record the configuration, workload, repeat count and results. Evaluate representative task quality alongside speed and memory use. Keep a known-good configuration and a rollback path.
