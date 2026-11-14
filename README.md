# OpenMettle component starter

Use this repository as a template for a new OpenMettle component. It supplies repository conventions and CI; it does not contain a running AI service.

## Customize your new repository

1. Replace this title and introduction with the component's purpose and current status.
2. Describe supported environments, prerequisites and how the component connects to the platform.
3. Add working installation and usage instructions as implementation becomes available.
4. Add meaningful tests and extend CI for the language and behavior of this component.
5. Fill in the documentation templates and maintain upstream provenance for imported code.
6. Review the license: the starter is MIT; imported material may have different requirements.

## Check the repository

Requires Python 3.10 or later. No Python packages are needed for the baseline checker.

```sh
python3 scripts/check_repository.py
```

The checker covers basic file hygiene, some common credential patterns and pinned workflow actions. It is not an application test suite or a comprehensive secret scanner. CI runs the same checker on pushes and pull requests.

## Configuration

`config/site.example.yaml` demonstrates the separation of site values from source. Its keys are illustrative until this component defines a real configuration schema. Copy it to the ignored `config/site.local.yaml` only after adapting it for the implementation. The example does not configure a firewall, ingress controller or authentication service.

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Development](docs/DEVELOPMENT.md)
- [Operations](docs/OPERATIONS.md)
- [Upstream provenance](UPSTREAM.md)

Contribution, support and security guidance are supplied by [OpenMettle's shared defaults](https://github.com/OpenMettle/.github). Review repository settings after creation: private vulnerability reporting, Actions permissions and branch rules are not all copied by GitHub's template mechanism.
