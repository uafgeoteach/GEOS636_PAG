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