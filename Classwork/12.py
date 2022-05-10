marks = 0
for x in range(5):
    y = int(input(f"What are your marks Subject {x + 1}\n"))
    marks = (marks + y)
marks = marks / 5
if marks < 30:
    print("E")
elif marks < 50 and marks >= 30:
    print("D")
elif marks < 70 and marks >= 50:
    print("C")
elif marks < 80 and marks >= 70:
    print("B")
elif marks < 100 and marks >= 80:
    print("A")
