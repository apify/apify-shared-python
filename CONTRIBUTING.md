# Development

## Environment

For local development, it is required to have Python 3.8 installed.

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

To install this package and its development dependencies, run `make install-dev`

## Formatting

We use `autopep8` and `isort` to automatically format the code to a common format. To run the formatting, just run `make format`.

## Linting, type-checking and unit testing

We use `flake8` for linting, `mypy` for type checking and `pytest` for unit testing. To run these tools, just run `make check-code`.

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

- Make sure that in the [pyproject.toml](https://github.com/apify/apify-sdk-python/blob/master/pyproject.toml) a project version is set to the latest non-published version.
- Describe your changes to the [CHANGELOG.md](https://github.com/apify/apify-sdk-python/blob/master/CHANGELOG.md) in the section with the latest non-published version.

### Production release checklist

Production release happens after the GitHub release is created. Before you do that check the following:

- Make sure that the beta release with the latest commit is successfully deployed.
- Make sure that all the changes that happened from the last production release are described in the [CHANGELOG.md](https://github.com/apify/apify-sdk-python/blob/master/CHANGELOG.md).
- When drafting a new GitHub release:
    - Create a new tag in the format of `v1.2.3` targeting the master branch.
    - Fill in the release title in the format of `1.2.3`.
    - Copy the changes from the [CHANGELOG.md](https://github.com/apify/apify-sdk-python/blob/master/CHANGELOG.md) and paste them into the release description.
    - Check the "Set as the latest release" option.
