def build_report(student_name, score, status , year):
    report = f"""Student Performance Report

Student Name: {student_name}
Score: {score}
Status: {status}
year_of_graduation: {year}
------------------------------------------------------------------------------------------------------
|   For universities                                                                                 |
|   who struggle to restrict applications to recent graduates and filter out older cohorts           |
|    we built a graduation year validation feature                                                   |
|    so that they can automatically validate and accept students based on a custom year they define  | 
------------------------------------------------------------------------------------------------------
"""
    return report

def save_report(student_name, report):
    filename = f"{student_name.lower().replace(' ', '_')}_report.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report)
    return filename