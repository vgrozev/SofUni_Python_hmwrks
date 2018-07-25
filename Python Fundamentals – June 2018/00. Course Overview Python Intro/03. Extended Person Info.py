name = input()
age = int(input())
town = input()
salary = float(input())

age_range = None
salary_range = None

if age < 18:
    age_range = 'teen'
elif age < 70:
    age_range = 'adult'
else:
    age_range = 'elder'

if salary < 500:
    salary_range = 'low'
elif salary < 2000:
    salary_range = 'medium'
else:
    salary_range = 'high'


print("Name: {0}".format(name))
print("Age: {0}".format(age))
print("Town: {0}".format(town))
print("Salary: ${0:.2f}".format(salary))
print("Age range: {0}".format(age_range))
print("Salary range: {0}".format(salary_range))
