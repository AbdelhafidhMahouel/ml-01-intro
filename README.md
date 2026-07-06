# ml-01-intro

[![Workflow Guide](https://img.shields.io/badge/Pro--Guide-pro--analytics--02-green)](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](./pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project: characterizing machine learning.

## Project Description

This project focuses on learning to find good data problems in a dataset,
and learning when machine learning (ML) might be helpful.

We learn to characterize:

- supervised (when we pick a target to predict)
- unsupervised (no target, just exploring, e.g. clustering)

In this project, we pick a dataset and a target.

If the target is:

- a discrete category column, we know it is a classification problem
- a continuous numeric column, we know it is a regression problem.

Some numbers are actually categories, for example a rating of 1, 2, 3.
May be better characterized as a category / discrete variable.

## Example Notebook + Your Notebook

Keep the example notebook as it is.
Either copy it or use it to build a new notebook that ends in _yourname.
See [docs/your-files.md] for more.

Links:

- [ml_01_case.ipynb](notebooks/ml_01_case.ipynb)

## Working Files

You'll work with these areas:

- **data/raw** - raw data for exploration (only if you add a dataset)
- **docs/** - project narrative and documentation
- **src/mlstudio/** - the app is an example; run only (no need to modify)
- **notebooks/** - interactive analysis
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions (pro-analytics-02)

Follow the
[step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/)
to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Change Authorship**
3. Phase 3. **Read & Understand**
4. Phase 4. **Modify**
5. Phase 5. **Apply** <mark>(optional for Module 1)</mark>

**Completing Phases 1-4 is the goal for Module 1.**
Phase 5 is optional in Module 1.
If your environment is working well and you still have some time, you might try it.

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project,
with the example notebook executed and committed,
and running the example module will print out:

```shell
========================
Executed successfully!
========================
```

A new file `project.log` will appear in the root project folder.

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/AbdelhafidhMahouel/ml-01-intro

cd ml-01-intro
code .
```

### In a VS Code terminal

These are listed for convenience.
For best results, follow the detailed instructions in
[pro-analytics-02 guide](https://denisecase.github.io/pro-analytics-02/).

```shell
uv self update
uv python pin 3.14
uv lock --upgrade
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
uvx pre-commit autoupdate

# git add all files and auto fix them as much as possible while working
git add -A
uvx pre-commit run --all-files
# repeat if changes were made
uvx pre-commit run --all-files

# run the example module to verify the environment (.venv/)
uv run python -m mlstudio.app_case

# run common chores: format, lint, run checks and tests...
uv run ruff format .
uv run ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress after every major change (customize the commit message)
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
- You do not need to add to or modify `tests/`. They are provided for example only.
- Many files are silent helpers. Explore as you like, but nothing is required.
- You do NOT need to understand everything; understanding builds naturally over time.

## Troubleshooting >>>

If you see something like this in your terminal: `>>>` or `...`
You accidentally started Python interactive mode.
It happens.
Press `Ctrl+c` (both keys together) or `Ctrl+Z` then `Enter` on Windows.

## Example Output (Can Remove this Section after You Verify)

```shell
| INFO | ML | Summarize workflow........
| INFO | ML | ========================
| INFO | ML | SUMMARY
| INFO | ML | ========================
| INFO | ML | Dataset: hours_scores_case
| INFO | ML | Original rows: 10
| INFO | ML | Clean rows: 10
| INFO | ML | Features: ['hours_studied', 'practice_quizzes', 'attendance_pct', 'sleep_hours', 'prior_score']
| INFO | ML | Target: score
| INFO | ML | ----- in a script, call plt.show() once at the end to display all charts -----
| INFO | ML | ----- in a script, CLOSE the chart windows with the close button to CONTINUE -----
| INFO | ML | Workflow complete
| INFO | ML | IMPORTANT: This script creates chart windows.
| INFO | ML | Close chart windows and terminate this process with CTRL+c as needed.
| INFO | ML | ========================
| INFO | ML | Executed successfully!
| INFO | ML | ========================
```

## Findings and Visuals

Take screenshots of your charts and provide them here with a discussion.
In Markdown, display a figure by using:
an exclamation mark immediately followed by square brackets containing a useful caption
immediately followed by parentheses containing the relative path to your figure.
Note: When you start typing the path with a dot (.) for "here, in this directory",
the IDE may help complete the path.

In your custom project, follow this example, but

- your figures and narrative should reflect your work,
- this `README.md` should include your commands, process, and visuals, and
- `docs/index.md` should include your narrative.

Remove unnecessary instructional comments in your custom files.

These are from the example app used to test the .venv/.
If possible, replace these to present interesting results from your custom project.

## Phase 4 Technical Modification

For my technical modification, I created a copy of the original regression
application and named it `app_abdel.py`. I added a new
**Actual Scores vs Predicted Scores** visualization to improve the evaluation
of the regression model.

The original project reported model performance metrics in the project log,
but I wanted to provide a visual comparison between the actual test scores and
the model predictions.

To support the new visualization, I modified the training workflow to return
the test target values and predicted values. I then created a new plotting
function that displays the actual scores against the predicted scores with a
reference line for comparison.

The modified application successfully produced three charts instead of the
two charts created by the original example. The new visualization shows that
the predicted scores are very close to the actual scores for the test cases.

### Run My Modified Project

```shell
uv run python -m mlstudio.app_abdel
```

### Actual Scores vs Predicted Scores

The new chart provides a visual comparison between the actual test scores and
the scores predicted by the Linear Regression model. Points close to the
reference line indicate that the model prediction is close to the actual value.

![Actual Scores vs Predicted Scores](./docs/images/actual-vs-predicted-scores.png)

## Phase 5: Student Performance Risk Classification

For my custom machine learning project, I changed the problem from regression
to classification. The provided example predicts a numeric student score,
while my project classifies students as either **At Risk** or **On Track**.

I used five features: hours studied, number of practice quizzes, attendance
percentage, sleep hours, and prior score. The target variable is `risk_status`.

I trained a Decision Tree Classifier and evaluated the model using accuracy,
precision, recall, and F1-score. The model achieved 1.00 accuracy on the small
test set. However, the dataset contains only 10 records, so this result should
be interpreted as a demonstration of the classification workflow rather than
evidence of production-level model performance.

The model also predicted a new student case with 3 hours of study, 2 practice
quizzes, 76% attendance, 6 hours of sleep, and a prior score of 59 as
**At Risk**.

### Run the Custom Project

```shell
uv run python -m mlstudio.student_risk_abdel
```

### Custom Project Result

The Decision Tree Classifier successfully completed the classification
workflow. The model achieved an accuracy of 1.00 on the small test set and
predicted the new student case as **At Risk**.

Because the dataset contains only 10 student records, this result is presented
as a demonstration of supervised classification rather than a production-ready
student risk prediction system.

![Student Risk Classification Result](./docs/images/student-risk-classification.png)

## Project Documentation

Additional project instructions, terms, and notes:

[docs/index.md](docs/index.md)

## Citation

[CITATION.cff](./CITATION.cff)

## License

[MIT](./LICENSE)
