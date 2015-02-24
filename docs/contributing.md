# Contributing
All contributions are much welcome and greatly appreciated! Expect to be credited for you effort.

This document is adapted from the cookiecutter [CONTRIBUTING.rst][cookie-contrib].


## General
Generally try to limit the scope of any Pull Request to an atomic update if possible. This way, it's much easier to assess and review your changes.

You should expect a considerably faster turn around if you submit two or more PRs instead of baking them all into one major PR.


## Issue tracker
confing uses the [GitHub issue tracker][issues].


## Types of Contributions
There are many ways you can help out and improve this repository.

### Report Bugs
Report bugs at [fahhem/confing/issues][issues].

Consider including the following data in your bug report:

- Your operating system name and version
- Any details about your local setup that might be helpful in troubleshooting
- If you can, provide detailed steps to reproduce the bug
- If you don't have steps to reproduce the bug, just note your observations in as much detail as you can. Questions to start a discussion about the issue are welcome.

### Fix Bugs
Look through the [GitHub issues][issues] for bugs. Anything tagged with "bug" is open to whoever wants to implement it. A good idea is also to review the comment thread to see if the issue is already referenced in any open pull requests.

### Implement Features
Look through the [GitHub issues][issues] for features. Anything tagged with "feature" is open to whoever wants to implement it.

### Write Documentation
confing could always use more documentation, whether as part of the official confing docs, in inline docstrings, or even on the web in blog posts, articles, and such.

If you have written your own tutorial or review of the software, please consider adding a referral link to the repository.

### Submit Feedback
The best way to send feedback is to [open a new issue][issues].

If you are requesting a feature:

- Explain in detail how it would work
- Keep the scope as narrow as possible, to make it easier to implement (atomic)


## Get Started!
Ready to contribute? Here's how to set up `confing` for local development.

> Over time my ambition is to provide a reproducable and automated setup through Vagrant.

1. Fork the [fahhem/confing][repo] repo on GitHub

2. Clone your fork locally:

  ```bash
  $ git clone git@github.com:<your github username>/confing.git
  ```

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

  ```bash
  $ mkvirtualenv confing
  $ cd confing/
  $ pip install -r requirements/development.txt
  $ pip install --editable .
  ```

4. Create a branch for local development:

  ```bash
  $ git checkout -b name-of-your-bugfix-or-feature
  ```

5. Make you changes locally

6. When you're done making changes, check that your changes pass flake8 and the tests, including testing other Python versions with tox:

  ```bash
  $ flake8 confing tests
  $ invoke test
  $ tox
  ```

7. Commit your changes and push your branch to GitHub:

  ```bash
  $ git add .
  $ git commit -m "Detailed description of your changes."
  $ git push origin name-of-your-bugfix-or-feature
  ```

8. Check that the test coverage hasn't dropped:

	```bash
	$ invoke coverage
	```

9. Submit a pull request through the GitHub website. I would encourage you to submit your pull request early in the process. This makes it easier to maintain an overview of current development and opens up for continous discussion.


## Pull Request Guidelines
Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests if applicable.

2. If the pull request adds functionality, the docs should be updated. Additionally, add the feature to the list in README.md.

3. The pull request should work for Python 3.4. Check the [Travis page][travis] and make sure that the tests pass for all supported Python versions.


## Coding conventions
Please stay up-to-date on confing coding standards by reading current code in the repository


## Tips
To run a particular test:

```bash
$ pytest tests.test_find.TestFind.test_find_template
```

To run a subset of tests:

```bash
$ pytest tests.test_find
```


[cookie-contrib]: https://github.com/audreyr/cookiecutter/blob/master/CONTRIBUTING.rst
[issues]: https://github.com/fahhem/confing/issues
[repo]: https://github.com/fahhem/confing
[travis]: https://travis-ci.org/fahhem/confing/pull_requests
