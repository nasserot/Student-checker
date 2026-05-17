from grading import is_valid_score, classify_score 
from report_writer import build_report, save_report

try:
    student_name = input("Enter student name: ").strip()
    if student_name == "":
        print("Student name cannot be empty.")
    else:
        # حلقة تكرار للتحقق من صحة الدرجة وإعادة السؤال في حال الخطأ
        while True:
            score = float(input("Enter student score from 0 to 100: "))
            if is_valid_score(score):
                break  # الخروج من الحلقة إذا كانت الدرجة صحيحة
            print("Invalid score. Score must be between 0 and 100. Please try again.")

        year = int(input("Enter Graduation year(after 2023) : "))
        
        if year < 2023:
            print("the Graduation year It Must be 2023 or later")
        else:
            status = classify_score(score)
            report = build_report(student_name, score, status, year)
            filename = save_report(student_name, report)

            print(report)
            print(f"Report saved to: {filename}")
     
except ValueError:
    print("Invalid input. Score and Year must be numbers.")