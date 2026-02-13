import pandas as pd

data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

it_employees = df[df["Department"] == "IT"]
print("IT Department Employees:")
print(it_employees)
print("-" * 30)

avg_salary = df.groupby("Department")["Salary"].mean()
print("Average Salary per Department:")
print(avg_salary)
print("-" * 30)

df["Salary_Adjusted"] = df["Salary"] * 1.1

print("Final DataFrame with Adjusted Salaries:")
print(df)