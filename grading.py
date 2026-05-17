def is_valid_score(score):
    return score >= 0 and score <= 100

def classify_score(score):
    if score >= 85:
        return "Excellent! You should try advanced exercises."
    elif score >= 70:
        return "Good job! You should review small mistakes and practice more."
    elif score >= 50:
        return "Passed, but you need more practice."
    else:
        return "Failed. You need support and should review the basics."