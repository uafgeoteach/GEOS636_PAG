#!/usr/bin/env python

def letter_grade(percent):
    if   percent > 90:
        return "A"
    elif percent > 80:
        return "B"
    elif percent > 70:
        return "C"
    elif percent > 60:
        return "D"
    else:
        return "F"

def gpa(letter_grades, credits):
    grades={'A': 4.00, 'B': 3.00, 'C':2.00, 'D':1.00, 'F':0.00}

    total_points = 0

    for i in range(len(letter_grades)):
        total_points += grades[ letter_grades[i] ] * credits[i]

    return float(total_points)/float(sum(credits))

if __name__ == "__main__":
    print letter_grade(85)
    print gpa(['B','A','C','A','B'], [4, 3, 3, 4, 2]) 