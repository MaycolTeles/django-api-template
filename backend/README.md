# Backend / API Template

The template includes the following:

* [Features](#features)
* [Packages and dependencies](#packages-and-dependencies)
* [Setup](#setup)
* [Reminders](#reminders)


## Features

### Custom User model: <a name="features"></a>
This template includes a custom User model that extends the AbstractBaseUser class. You can use this model to store user information in your project.

The user model is located in `account.models.user` module and is ready to be used in your project. You can use this model to store user information and authenticate users in your project.

### Base Mixin classes:
This template includes a few base mixin classes that can be used to add common functionality to your Models,  Views, Admin and Test classes. You can check the modules under `core.mixins` for more details on these classes and how to use them.

### Makefile:
This template includes a `Makefile` that can be used to run common commands for the project. You can use the `make` command to run the commands listed in the `Makefile` and manage your project more easily. The `Makefile` includes commands to run the Django development server, run tests, create migrations, apply migrations, and more. All the available commands are listed in the `Makefile` and you can add more commands as needed.

### Management Commands / Async Tasks:
This template includes an example of a management command and a `celery` async task that can be executed in the background. You can use these commands to perform long-running tasks, schedule tasks to run at specific times, or run tasks in parallel. The management command is located in the `account.management.commands` module and the Celery task is located in the `account.tasks` module. You can use these examples as a starting point and build more commands and tasks on top of them.

## Packages and dependencies: <a name="packages-and-dependencies"></a>

### Poetry (Environment and dependencies):
This template uses `poetry` to manage dependencies and virtual environments. You can use the `poetry` commands to manage your project dependencies and create a virtual environment for your project. All the dependencies are listed in the `pyproject.toml` file and they're split into `main`, `dev` and `prod` dependencies.

### Ruff (Linter and formatter):
This template uses `ruff` to lint and format the code. You can use the `ruff` commands to check the code quality and style, and to format the code according to the project standards. All the configurations needed for `ruff` are under `pyproject.toml` file and you can customize it to fit your project requirements. You can run the linter using the `make lint` command and the formatter using the `make format` command.

### Pre-commit hooks:
This template includes a `.pre-commit-config.yaml` configuration file that can be used to run pre-commit hooks before committing changes to the repository. You can use this configuration file to run linting, formatting, and other checks before committing changes to the repository. The file includes a few common hooks that can be used to check the code quality and style, along with a few custom hooks using ruff. You can add more hooks as needed and customize the configuration to fit your project requirements.

### Tests
This template uses `pytest` as the test runner, mainly because it's capability of generating test and coverage reports, run tests in parallel, and many other features. It already includes a few example tests that can be used to test the project. You should use them as a starting point and build more tests on top of them. The tests can be run using the `make test` command for a simple test run, or `make coverage` to generate a test and coverage reports.

### Environment variables:
This template uses the `python-decouple` package to manage environment variables. In order to run the project, create a `.env` file in the `backend` directory from the `.env.example` template and assign the required values to the variables.

## Setup <a name="setup"></a>
In order to set up the project, follow these steps:

1. Create a `.env` file in the `backend` directory from the `.env.example` template and assign the required values to the variables.

2. (Optional) Update the `pyproject.toml` file with your project name, version, description, and author.

3. Run the script `./scripts/setup.sh` to install the dependencies and set up the project.
    ```bash
    ./scripts/setup.sh
    ```

    or using the Makefile:
    ```bash
    make setup
    ```

4. Run the container using the command documented in the [main README](../README.md) file.

## Reminders <a name="reminders"></a>
* Don't forget to create `backend/.env` file

* Don't forget to update `pyproject.toml` with your project name, version, description, and author.
