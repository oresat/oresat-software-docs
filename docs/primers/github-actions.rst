Github Actions
==============

What is Github Actions?
-----------------------
GitHub Actions is a tool provided by GitHub, the platform where you store and manage your code.
This tool helps you automate tasks related to your code, such as automatically testing it,
checking its quality, and even deploying it to a server. It's like having a helpful robot
that can perform these tasks for you whenever you make changes to your code.

By using GitHub Actions, you can:

#. **Save time**: Instead of doing repetitive tasks manually, like running tests or deploying your
   code, you can let GitHub Actions do it for you automatically.

#. **Improve code quality**: By automatically running tests and other checks on your code, you can
   catch errors and issues before they become bigger problems.

#. **Simplify collaboration**: When working with a team, GitHub Actions can help ensure that
   everyone's code meets the same standards by running the same checks and tests for each person's changes.

#. **Streamline deployments**: You can set up GitHub Actions to automatically deploy your code to
   a server or a cloud provider whenever you make changes, making the deployment process faster
   and smoother.

To use GitHub Actions, you create a workflow file in your repository, which is written in YAML, a
simple and human-readable language. This file tells GitHub Actions what tasks to perform and
when to perform them, such as when new code is pushed or a pull request is created.

Example WorkFlow
----------------

Below is an example workflow for a Python-based project that will check the formatting of code,
lint the code, and then run unit tests on all PRs and pushes to the mater branch.

.. code-block:: yaml

   name: tests

   on:
     push:
       branches:
         - master
     pull_request:
       branches:
         - master

   jobs:
     tests:
       runs-on: ubuntu-latest

       steps:
       - name: Clone this repository
         uses: actions/checkout@v2

       - name: Set up Python 3.9
         uses: actions/setup-python@v2
         with:
           python-version: "3.9"

       - name: Install dependencies
         run: |
           python -m pip install --upgrade pip
           pip install -r requirements.txt

       - name: Check format with Black
         run: black --check --diff .

       - name: Check format with isort
         run: isort --check --diff .

       - name: Lint with Pylama
         run: pylama

       - name: Test with Python's unittest
         run: python -m unittest
