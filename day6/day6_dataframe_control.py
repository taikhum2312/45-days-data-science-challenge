import pandas as pd
data={
    "employee": [chr(i) for i in range(ord('A'), ord('F')+1)],
    "department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
    "salary": [50000, 60000, 55000, 45000, 62000, 58000],
    "experience": [5, 7, 6, 4, 8, 6]
}
df=pd.DataFrame(data)
print(df)
print(type(df))
print(type(df['salary']))


#filtering

employee_with_high_salary=df[df["salary"]>55000]
employee_in_IT=df[df["department"]=="IT"]
employee_in_IT_with_high_salary=df[(df["department"]=="IT") & (df["salary"]>55000)]
employee_with_experience_3_to_6_years=df[df["experience"].between(3,6)]
print("Employees with salary greater than 55000:")
print(employee_with_high_salary)
print("\nEmployees in IT department:")
print(employee_in_IT)
print("\nEmployees in IT department with salary greater than 55000:")
print(employee_in_IT_with_high_salary)
print("\nEmployees with experience between 3 to 6 years:")
print(employee_with_experience_3_to_6_years)



#create nwe coulumns
df["senior"]=df["experience"]>=5
df["high_paid"]=df["salary"]>55000
df["category"]=df["senior"] & df["high_paid"]

print("\nDataFrame with new columns:")
print(df)


#grouping control
group_salary= df.groupby("department")["salary"].mean().round(0)
group_count=df.groupby("department")["employee"].count()
group_experience=df.groupby("department")["experience"].mean().round(1)
print(group_salary)
print(group_count)
print(group_experience)



"""
INSIGHTS:

1. IT department has the highest average salary, likely due to having multiple high-salary employees.

2. Sales has only one employee, so its average salary equals that individual's salary.

3. HR has fewer employees than IT but maintains a relatively high average salary, suggesting experienced staff.
"""
