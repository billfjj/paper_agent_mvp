import pandas as pd


def check_classification_table(df: pd.DataFrame) -> list[str]:
    findings: list[str] = []
    required = {"Precision", "Recall", "F1"}
    if required.issubset(df.columns):
        for idx, row in df.iterrows():
            p = float(row["Precision"])
            r = float(row["Recall"])
            expected = 0.0 if p + r == 0 else 2 * p * r / (p + r)
            actual = float(row["F1"])
            if abs(expected - actual) > 0.01:
                findings.append(f"Row {idx}: F1={actual:.4f}, expected about {expected:.4f}.")
    if not findings:
        findings.append("No obvious Precision/Recall/F1 inconsistency was found.")
    return findings
