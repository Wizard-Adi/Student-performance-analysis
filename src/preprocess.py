import pandas as pd

def preprocessing():
    df = pd.read_csv("student_dataset_p2.csv")

    print("\nMIssing values\n",df.isnull().sum())

    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

    df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].median())

    df.loc[df["StudyHours"] > 15, "StudyHours"] = df["StudyHours"].median()