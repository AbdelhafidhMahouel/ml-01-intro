"""student_risk_abdel.py - custom Phase 5 project.

Author: Abdelhafidh Mahouel
Date: 2026-06

Classify student performance risk using a supervised machine learning model.

Run from the root project folder:
uv run python -m mlstudio.student_risk_abdel
"""

from typing import Final

from datafun_toolkit.logger import get_logger, log_header
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

LOG = get_logger("P5", level="INFO")
log_header(LOG, "P5")

FEATURE_COLS: Final[list[str]] = [
    "hours_studied",
    "practice_quizzes",
    "attendance_pct",
    "sleep_hours",
    "prior_score",
]

TARGET_COL: Final[str] = "risk_status"


def main() -> None:
    """Run the custom classification workflow."""
    LOG.info("Creating custom student risk dataset")

    df = pd.DataFrame(
        [
            [2.0, 1, 72, 6.0, 58, "At Risk"],
            [3.5, 2, 80, 6.5, 61, "At Risk"],
            [4.0, 3, 85, 7.0, 64, "On Track"],
            [5.0, 3, 88, 7.5, 66, "On Track"],
            [6.0, 4, 90, 7.0, 70, "On Track"],
            [7.0, 5, 95, 8.0, 78, "On Track"],
            [1.5, 1, 60, 5.5, 50, "At Risk"],
            [8.0, 5, 97, 7.5, 82, "On Track"],
            [2.5, 1, 70, 6.0, 55, "At Risk"],
            [6.5, 4, 92, 7.0, 72, "On Track"],
        ],
        columns=FEATURE_COLS + [TARGET_COL],
    )

    LOG.info(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

    x = df[FEATURE_COLS]
    y = df[TARGET_COL]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.30,
        random_state=42,
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)
    LOG.info(f"Accuracy: {accuracy:.2f}")
    LOG.info("Classification report:")
    LOG.info(f"\n{classification_report(y_test, y_pred)}")

    new_student = pd.DataFrame(
        [
            {
                "hours_studied": 3.0,
                "practice_quizzes": 2,
                "attendance_pct": 76,
                "sleep_hours": 6.0,
                "prior_score": 59,
            }
        ]
    )

    prediction = model.predict(new_student)[0]

    LOG.info(f"New student case:\n{new_student}")
    LOG.info(f"Predicted risk status: {prediction}")
    LOG.info("========================")
    LOG.info("Phase 5 custom project executed successfully!")
    LOG.info("========================")


if __name__ == "__main__":
    main()
