# Bank API

This is a standalone exercise to practice writing tests and engaging in Test Driven Development (TDD). Clone this repository and then open the resulting `DevOps-Course-Bank-API` folder in VSCode. Open it as the project folder - don't open a parent folder and then browse down to the repository folder, otherwise subsequent instructions here will not work.

Read through this file to get the project running and then follow the instructions in [exercise_instructions.md](./exercise_instructions.md).

## Setup

This project requires Python 3.8 (or higher) and uses pip to handle dependencies. If you are familiar with using virtual environments to manage dependencies, use your usual workflow to create and activate a virtual environment before proceeding.

Run the following command (run from the project root) to install project dependencies:

`pip install -r requirements.txt`

To launch the API, run the following:

```bash
cd bank_api
python -m flask run
```

The API should be live with swagger docs visible at http://localhost:5000/.

## Tests

You can run both unit and integration tests suites using pytest. Run this from the root directory:

`python -m pytest`

Or you can run them from VSCode:

Click the conical flask icon on the activity bar on the left edge of VSCode. Click the refresh icon at the top of the panel to rediscover tests. Click the play icon at the top to run all tests. Click the play icon next to a file or test name to run that file or test individually.
* Intellisense annotations for running/debugging each test should also appear above the test functions in the code.
* If test discovery fails, check that "poetry install" ran successfully and that the Python interpreter is selected correctly. See the "setup" section above for details.

You can now go back to the [exercise instructions](./exercise_instructions.md).
