import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt

def analysing():
    location = "C:/Users/adity/OneDrive/Desktop/student_performance_analysis/data/student_dataset_p2.csv"

    df = pd.read_csv(location)

    #task 3.4
    high_Scores = df[df["Marks"] > 50]
    print("\ntop 5 scorers :\n", df.nlargest(5, "Marks"))
    print("\nStudents with marks more than 50 :", high_Scores)

    #correlation studyHours vs marks
    correlation = df["StudyHours"].corr(df["Marks"])
    print(f"Correlation Coefficient StudyHours vs Marks: {correlation:.2f}")

    # plt.figure(figsize=(10,6))
    # sns.regplot(x="StudyHours", y="Marks", data=df, line_kws={'color':'red'})
    # plt.title("analysis: studyHours vs Marks")
    # plt.show()

    attendanceCorr = df["Attendance"].corr(df["Marks"])
    print(f"\nCorrelation coefficient Attendance vs Marks: {attendanceCorr:.2f}")