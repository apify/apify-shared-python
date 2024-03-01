# Development

## Environment

For local development, it is required to have Python 3.8 (or a later version) installed.

It is recommended to set up a virtual environment while developing this package to isolate your development environment,
however, due to the many varied ways Python can be installed and virtual environments can be set up,
this is left up to the developers to do themselves.

One recommended way is with the built-in `venv` module:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

To improve on the experience, you can use [pyenv](https://github.com/pyenv/pyenv) to have an environment with a pinned Python version,
and [direnv](https://github.com/direnv/direnv) to automatically activate/deactivate the environment when you enter/exit the project folder.

## Dependencies

To install this package and its development dependencies, run `make install-dev`.

## Code checking

To run all our code checking tools together, just run `make check-code`.

### Linting

We use [ruff](https://docs.astral.sh/ruff/) for linting to to analyze the code for potential issues and enforce
uniformed code style. See the `pyproject.toml` for its configuration. To run the linting, just run `make lint`.

### Formatting

We use [ruff](https://docs.astral.sh/ruff/) for automated code formatting. It formats the code to follow uniformed
code style and addresses auto-fixable linting issues. See the `pyproject.toml` for its configuration. To run
the formatting, just run `make format`.

### Type checking

We use [mypy](https://mypy.readthedocs.io/en/stable/) for type checking. See the `mypy.ini` for its configuration.
To run the type checking, just run `make type-check`.

### Unit tests

We use [pytest](https://docs.pytest.org/) as a testing framework with many plugins. See the `pyproject.toml` for
both its configuration and the list of installed plugins. To run unit tests execute `make unit-tests`. To run unit
tests with HTML coverage report execute `make unit-tests-cov`.

## Release process

Publishing new versions to [PyPI](https://pypi.org/project/apify-shared) happens automatically through GitHub Actions.

On each commit to the `master` branch, a new beta release is published, taking the version number from `pyproject.toml`
and automatically incrementing the beta version suffix by 1 from the last beta release published to PyPI.

A stable version is published when a new release is created using GitHub Releases, again taking the version number from `pyproject.toml`.
The built package assets are automatically uploaded to the GitHub release.

If there is already a stable version with the same version number as in `pyproject.toml` published to PyPI, the publish process fails,
so don't forget to update the version number before releasing a new version.
The release process also fails when the released version is not described in `CHANGELOG.md`,
so don't forget to describe the changes in the new version there.

### Beta release checklist

Beta release happens automatically after you merge a pull request or add a direct commit to the master branch. Before you do that check the following:

- Make sure that in the [pyproject.toml](./pyproject.toml) a project version is set to the latest non-published version.
- Describe your changes to the [CHANGELOG.md](./CHANGELOG.md) in the section with the latest non-published version.

### Production release checklist

Production release happens after the GitHub release is created. Before you do that check the following:

- Make sure [here](https://pypi.org/project/apify-shared/#history) that the beta release with the latest commit is successfully deployed.
- Make sure that all changes that happened from the last production release are described in [CHANGELOG.md](./CHANGELOG.md) (it's okay to skip DX related changes, repo setup etc).
- When drafting a new GitHub release:
    - Create a new tag in the format of `v1.2.3` targeting the master branch.
    - Fill in the release title in the format of `1.2.3`.
    - Copy the changes from the [CHANGELOG.md](./CHANGELOG.md) and paste them into the release description. Make sure that all changes are properly categorized using headlines (`Added`, `Fixed` or `Internal changes`).
    - Check the "Set as the latest release" option.

Currently, there is no explicit approval process, so when you are done with the checklist, proceed with the release.

Once released, manually bump the version in `pyproject.toml` ([commit example](https://github.com/apify/apify-shared-python/commit/24a269bcf046df7202a8652ee788ffe9a461e58b)).

## Maintanance

### Removing Support for an outdated Python version

- Todo: Fill in once Python 3.8 is deprecated.

### Adding support for a new Python version

1) Firstly, ensure that the package (
    [apify-sdk-python](https://github.com/apify/apify-sdk-python),
    [apify-client-python](https://github.com/apify/apify-client-python),
    [apify-shared-python](https://github.com/apify/apify-shared-python)
) is compatible with the new Python version. Both in our code base and
the dependencies we use. Then, release a new version of the package.
    - For inspiration, see the PR
    [apify/apify-sdk-python#121](https://github.com/apify/apify-sdk-python/pull/121),
    where support for Python 3.12 was added to the Apify Python SDK.

2) Next, build and publish the new versions of Python base Docker images.
    - For inspiration, see the PR
    [apify/apify-actor-docker#112](https://github.com/apify/apify-actor-docker/pull/112),
    where support for Python 3.12 was added.
    - Apify base Docker images are built using GitHub Actions, accessible at
    [apify/apify-actor-docker/actions](https://github.com/apify/apify-actor-docker/actions).

3) Integrate the new Python version into the CI/CD workflows
of existing Python projects (
    [apify-sdk-python](https://github.com/apify/apify-sdk-python),
    [apify-client-python](https://github.com/apify/apify-client-python),
    [apify-shared-python](https://github.com/apify/apify-shared-python),
    [actor-templates](https://github.com/apify/actor-templates)
).
    - For inspiration, see the PR
    [apify/apify-sdk-python#124](https://github.com/apify/apify-sdk-python/pull/124),
    where support for Python 3.12 was added to the CI/CD of the Apify Python SDK.
