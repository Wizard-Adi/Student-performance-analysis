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

    # group based analysis
    df.loc[df["Attendance"] >= 90, "AttendanceCategory"] = "Excellent"

    df.loc[(df["Attendance"] >= 75) & (df["Attendance"] <= 89), "AttendanceCategory"] = "Good"

    df.loc[(df["Attendance"] >= 50) & (df["Attendance"] <= 74), "AttendanceCategory"] = "Satisfactory"

    df.loc[df["Attendance"] < 50, "AttendanceCategory"] = "Poor"

    df.to_csv(location, index=False)
    print("\nFile updated successfully\n")

    # Group by attendance and calculate the mean of the marks column
    avg_marks_by_attendance = df.groupby('AttendanceCategory')['Marks'].mean()

    print("\nAverage marks based on different Attendance levels : ",avg_marks_by_attendance)

    #group by study category then mean()
    # 1. Create attendance groups (bins)
    bins = [-1, 5, 10, 15]
    labels = ['Low (0-5)', 'Medium (6-10)', 'High (>10)']
    df["StudyHoursGroup"] = pd.cut(df["StudyHours"], bins=bins, labels=labels)

    # 2. Find average marks for these new groups
    result = df.groupby("StudyHoursGroup", observed=False)["Marks"].mean()
    print("\nAverage marks based on different Study Hours : ",result)
