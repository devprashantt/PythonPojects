student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades={} 
for student in student_scores:
    score=student_scores[student]
    if score>90:
        student_grades[student]="outstanding"
    elif score>80:
        student_grades[student]="excellent"
    elif score>70:       
        student_grades[student]="very good"
    elif score>60:    
        student_grades[student]="good"
    else:
        student_grades[student]="poor"
print(student_grades)

        
    
  

 



    