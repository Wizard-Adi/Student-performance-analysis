Student Performance Analysis System
📌 Objective
This project aims to analyze the relationship between student habits—specifically study hours and attendance—and their final marks. By applying data preprocessing, cleaning, and feature engineering, the system extracts meaningful patterns to identify what truly drives academic success and where performance drops off.
📌 Dataset Description
StudyHours: The number of hours a student spends studying per day.
Attendance: The student's attendance percentage in classes.
Marks: The academic scores achieved by the student.
📌 Steps Performed
Data Loading: Imported the dataset using pandas and inspected the structure using .head(), .shape, and .info().
Data Cleaning: Handled missing values by filling Marks with the mean and StudyHours with the median. Removed outliers where StudyHours exceeded 15 or Marks exceeded 100.
Feature Engineering: Created a Performance category (Excellent, Good, Needs Improvement) and an EffortScore (StudyHours × Attendance) to better quantify student engagement.
Data Analysis: Performed correlation analysis and grouping to compare how different levels of study and attendance impact the final average marks.
📌 Key Insights (MANDATORY)
Study time doesn't change marks much: The correlation is -0.04 (nearly zero), meaning more hours didn't automatically result in higher marks.
Too much study might be bad: Students studying over 10 hours had the lowest average marks (44.7), likely due to burnout or fatigue.
The "Best" study range: The highest average marks (69.6) were found in the 6–10 hour range, suggesting this is the most effective study duration.
Attendance has a small impact: Average marks remained stable at approximately 69 across all attendance levels, showing it wasn't the primary driver of scores.
High passing rate: The majority of the dataset (1,086 students) scored above 50 marks, indicating generally solid performance across the board.