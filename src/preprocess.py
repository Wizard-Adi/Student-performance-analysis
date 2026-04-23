import pandas as pd

def preprocessing():
    path = "C:/Users/adity/OneDrive/Desktop/student_performance_analysis/data/student_dataset_p2.csv"
    df = pd.read_csv(path)

    # task 3.1
    print("First 15 rows :\n", df.head(15))
    #print("\nLast 10 rows :\n", df.tail(10))
    print("\ndataset shape :\n", df.shape)
    print("\nColumns\n", df.columns)

    #task 3.2
    print("\nMIssing values\n",df.isnull().sum())

    df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

    df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].median())

    df.loc[df["StudyHours"] > 15, "StudyHours"] = df["StudyHours"].median()

    df.loc[df["Marks"] > 100, "Marks"] = df["Marks"].median()

    #task 3.3
    df.loc[df["Marks"] >= 80, "Performance"] = "Excellent"

    df.loc[(df["Marks"] >= 60) & (df["Marks"] <= 79), "Performance"] = "Good"

    df.loc[df["Marks"] < 60, "Performance"] = "Needs Improvement"

    df["EffortScore"] = df["StudyHours"] * df["Attendance"]

    df.to_csv(path, index=False)
    print("\nFile updated successfully\n")