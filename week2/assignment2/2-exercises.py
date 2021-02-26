import re
import pandas as pd
import io

filename = 'Salaries.csv'
salaries = pd.read_csv(filename)

print('Exercise 1')
print(salaries.columns.tolist())
print('\n')

print('Exercise 2')
buffer = io.StringIO()
salaries.info(verbose=False, buf=buffer, memory_usage=False, null_counts=True)
print(list(buffer.getvalue().split('\n'))[1].split(' ')[1])
print('\n')

print('Exercise 3')
valid_base_pay = salaries[pd.to_numeric(salaries['BasePay'], errors='coerce').notna()]
print(valid_base_pay['BasePay'].head(1000).mean())
print('\n')

print('Exercise 4')
valid_total_pay_benefits = salaries[pd.to_numeric(salaries['TotalPayBenefits'], errors='coerce').notna()]
print(valid_total_pay_benefits['TotalPayBenefits'].head(1000).max())
print('\n')

print('Exercise 5')
person = salaries[salaries['EmployeeName'] == 'JOSEPH DRISCOLL']
print(person['JobTitle'].iloc[0])
print('\n')

print('Exercise 6')
print(person['TotalPayBenefits'].iloc[0])
print('\n')

print('Exercise 7')
max_total_pay_benefits = valid_total_pay_benefits['TotalPayBenefits'].max()
person = salaries.query(f'TotalPayBenefits == {max_total_pay_benefits}')
print(person['EmployeeName'].iloc[0])
print('\n')

print('Exercise 8')
min_total_pay_benefits = valid_total_pay_benefits['TotalPayBenefits'].min()
person = valid_total_pay_benefits.query(f'TotalPayBenefits == {min_total_pay_benefits}')
print(person['EmployeeName'].iloc[0], min_total_pay_benefits)
print('Their pay is negative')
print('\n')

print('Exercise 9')
valid_total_pay = salaries[pd.to_numeric(salaries['TotalPay'], errors='coerce').notna()]
mean_total_pay = valid_total_pay.query(f'2010 < Year < 2015')['TotalPay'].mean()
print(mean_total_pay)
print('\n')

print('Exercise 10')
num_unique_job_titles = salaries[salaries['JobTitle'] != 'Not Provided']['JobTitle'].nunique(dropna=True)
print(num_unique_job_titles)
print('\n')

print('Exercise 11')
unique_job_titles = salaries.groupby(by=['JobTitle'], dropna=True)['JobTitle'].count()
print(unique_job_titles.sort_values(ascending=False).head(7))
print('\n')

print('Exercise 12')
job_titles = salaries[salaries['JobTitle'] != 'Not Provided']
job_titles_2013 = job_titles[job_titles['Year'] == 2013]
job_titles_2013 = job_titles_2013.groupby(by=['JobTitle'], dropna=True)['JobTitle'].count().reset_index(name='count')
job_titles_2013 = job_titles_2013[job_titles_2013['count'] == 1]['JobTitle'].count()
print(job_titles_2013)
print('\n')

print('Exercise 13')
job_titles = salaries[salaries['JobTitle'] != 'Not Provided']['JobTitle'].to_list()
count = 0
for job in job_titles:
    if re.match(r'[\W\w]*chief[\W\w]*', job.lower()) != None:
        count += 1
print(count)
print('\n')

print('Exercise 14')
# Used the average salary for each unique job title
job_title_lengths = []
job_titles = salaries[salaries['JobTitle'] != 'Not Provided']
job_titles = job_titles.groupby(by=['JobTitle'], dropna=True)['TotalPay'].mean().reset_index(name='mean')
pay = job_titles[job_titles['JobTitle'] != 'Not Provided']['mean'].to_list()

for job in job_titles['JobTitle'].to_list():
    job_title_lengths.append(len(job))

df = pd.DataFrame(list(zip(job_title_lengths, pay)), columns=['JobTitle Length', 'Average Salary'])
print("There is no clear correlation between job title length and average salary\n")
print("Correlation Matrix:")
correlation = df.corr(method='pearson')
print(correlation)

print("\nTop 50 JobTitle Length vs Salary:")
print(df.sort_values(by=['JobTitle Length'], ascending=False).head(50))
print('\n')