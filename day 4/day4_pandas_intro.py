# Create DataFrame from Dictionary
import pandas as pd
import random
# Create a DataFrame with random data of 50 employees with coulmns "EmployeeID", "Name", "Department", "Salary" and create it as a function that takes the number of employees as an argument and returns the DataFrame.
def create_employee_data(num_employees=int(input("Enter the number of employees you want to create: "))):
    employee_ids = [f"E{str(i).zfill(3)}" for i in range(1, num_employees + 1)]
    names = [f"Employee_{i}" for i in range(1, num_employees + 1)]
    departments = [random.choice(["HR", "Finance", "IT", "Marketing", "Sales"])for _ in range(num_employees)]
    salaries = [random.randint(30000, 100000) for _ in range(num_employees)]
    Ages = [random.randint(22, 60) for i in range(num_employees)]
    work_experience = [random.randint(1, 40) for i in range(num_employees)]

    data = {
        "EmployeeID": employee_ids,
        "Name": names,
        "Department": departments,
        "Salary": salaries,
        "Age": Ages,
        "Work_Experience": work_experience,
    }

    df = pd.DataFrame(data)
    return df

# Example usage
employee_df = create_employee_data()
# print(employee_df)









# filtering data
high_salary_employees = employee_df[employee_df["Salary"] > 80000]
employee_in_IT = employee_df[employee_df["Department"] == "IT"]
employee_age_and_sal = employee_df[
(employee_df["Age"] > 30) & (employee_df["Salary"] > 60000)]
employee_experience = employee_df[employee_df["Work_Experience"] >10]
print("people with salary > 80000", high_salary_employees)
print()
print(" employee who works in IT",employee_in_IT)
print()
print("Employees age < 30 AND salary > 60000",employee_age_and_sal)
print()
print("Employees with experience > 10 years",employee_experience)
print()
employee_df.to_csv("employee_data.csv", index=False)

average_salary = employee_df["Salary"].mean()
average_salary_by_department = employee_df.groupby("Department")["Salary"].mean()
highest_paid_employee = employee_df.loc[employee_df["Salary"].idxmax()]
department_with_most_employees = employee_df["Department"].value_counts().idxmax()
print("Average Salary:", average_salary)
print()  
print("Average Salary by Department:", average_salary_by_department)
print()
print("Highest Paid Employee:", highest_paid_employee)
print()
print("Department with Most Employees:", department_with_most_employees)
print()


salary_desending = employee_df.sort_values(by="Salary", ascending=False)
experience_desending = employee_df.sort_values(by="Work_Experience", ascending=False)
print("Employees sorted by Salary (Descending):", salary_desending)
print()
print("Employees sorted by Work Experience (Descending):", experience_desending)
print()
