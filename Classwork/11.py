basicSalary = float(input("What is the salary\n"))

if basicSalary <= 10000:
    grossSalary = basicSalary + 0.2 * basicSalary + 0.8 * basicSalary
    print(grossSalary)
elif basicSalary <= 20000:
    grossSalary = basicSalary + 0.25 * basicSalary + 0.9 * basicSalary
    print(grossSalary)
else:
    grossSalary = basicSalary + 0.3 * basicSalary + 0.95 * basicSalary
    print(grossSalary)
