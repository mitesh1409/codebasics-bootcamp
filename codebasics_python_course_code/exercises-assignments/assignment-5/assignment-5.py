import numpy as np

# Employee Details: Employee ID, Department, Number of Years with AtliQ
employee_details = np.array([
    [101, 'Sales', 3],  
    [102, 'HR', 5],    
    [103, 'IT', 2],        
    [104, 'Sales', 8],    
    [105, 'IT', 6],      
    [106, 'HR', 4],           
    [107, 'IT', 7],    
    [108, 'Sales', 1], 
    [109, 'HR', 3]          
])

# Survey Results: Employee ID, Happiness Score (1-10)
survey_results = np.array([
    [101, 8],
    [102, 10],
    [103, 9],
    [104, 6],
    [105, 7],
    [106, 8],
    [107, 9],
    [108, 5],
    [109, 7]
])

# Task 1: Merge Arrays
# Scenario: To streamline analysis, combine the employee details with their survey results.
# Action: Use np.hstack to horizontally stack the two arrays.

employee_with_survey_results = np.hstack((employee_details, survey_results))
print(employee_with_survey_results)

# Task 2: Print Scores
# Scenario: HR wants a quick view of all happiness scores to gauge overall employee sentiment.
# Action: Display all happiness scores from the merged array.

print(employee_with_survey_results[:, 4])

happiness_scores = employee_with_survey_results[:, 4].astype(int)
print(happiness_scores)

# Task 3: Sort Scores
# Scenario: HR needs to identify the range of happiness scores to plan specific interventions.
# Action: Sort and print the happiness scores in ascending order.

# Way #1
# Calling sort on the array modifies the original array.
# happiness_scores.sort()
# print(happiness_scores)

# Way #2
# We may need to keep original copy as it is.
# So for that we can use np.sort(), it will keep original copy 
# as it is and returns a new sorted array.
sorted_happiness_scores = np.sort(happiness_scores)
print('Sorted Happiness Scores: ', sorted_happiness_scores)
print('Original Happiness Scores: ', happiness_scores)

# Task 4: Employee Details
# Scenario: For a meeting, HR needs a list of employees' IDs and departments without other details.
# Action: Iterate through the array and print each employee's ID and department.

for employee in employee_details:
    print(f'Employee ID: {employee[0]} Department: {employee[1]}')

# Task 5: Happiness Scores
# Scenario: HR wants to review individual happiness scores to follow up with specific departments or employees.
# Action: Print the happiness score alongside each employee ID from the merged array.

for employee in employee_with_survey_results:
    print(f'Employee ID: {employee[0]}, Happiness Score: {employee[4]}')

# Task 6: Convert Scores
# Scenario: For statistical analysis, the HR team needs the happiness scores in a consistent format.
# Action: Convert the happiness scores to float type using astype(float).

happiness_scores = employee_with_survey_results[:, 4].astype(float)
print(happiness_scores)

# Task 7: Average Score
# Scenario: To measure the effectiveness of current policies, HR needs the average happiness score.
# Action: Calculate and print the average happiness score of all employees.

# Way #1
average_happiness_score = sum(happiness_scores) / len(happiness_scores)
print(average_happiness_score)

# Way #2
print(np.average(happiness_scores))

# Task 8: Unique Departments
# Scenario: HR is reviewing which departments are represented in the survey to ensure all are included in future plans.
# Action: Use np.unique to find and print all unique departments from the employee details.

all_departments = employee_details[:, 1]
unique_departments = np.unique(all_departments)
print('All departments: ', all_departments)
print('Unique departments: ', unique_departments)

# Task 9: HR Happiness
# Scenario: HR is conducting a self-assessment to understand how their own department perceives company policies.
# Action: Calculate and print the average happiness score within the HR department.

# Way #1, this is step by step and readable
filter_hr_deparment = employee_with_survey_results[:, 1] == 'HR'
hr_employees = employee_with_survey_results[filter_hr_deparment]
hr_employees_happiness_scores = hr_employees[:, 4].astype(float)
np.average(hr_employees_happiness_scores)

# Way #2, single line, hard to understand
np.average(employee_with_survey_results[
    employee_with_survey_results[:, 1] == 'HR'
][:, 4].astype(float))
