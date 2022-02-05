import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib

employer_selection = input("Enter company name: ")
year_min = int(input("Input minimum year: "))
year_max = int(input("Input maximum year: "))

for i in range(year_min, year_max):
    df = pd.read_csv('Dataset/' + str(i) + '/Form3.csv', encoding = "ISO-8859-1")
    employer = df['EMPLOYERNAME'].fillna(0).values
    salary_range = df['SALARYRANGE($)'].fillna(0).values
    country = df['LOCATION'].fillna(0).values
    employment_status = df["EMPLOYMENTSTATUS"].fillna(0).values
    total_employees = df['ALLCOUNT'].fillna(0).values
    total_male = df['ALLMENCOUNT'].fillna(0).values
    total_women = df['ALLWOMENCOUNT'].fillna(0).values
    total_aboriginal = df['ABORIGALLCOUNT'].fillna(0).values
    total_aboriginal_men = df['ABORIGMENCOUNT'].fillna(0).values
    total_aboriginal_women = df['ABORIGWOMENCOUNT'].fillna(0).values
    total_disabled = df['PWDALLCOUNT'].fillna(0).values
    total_disabled_women = df['PWDMENCOUNT'].fillna(0).values
    total_disabled_women = df['PWDWOMENCOUNT'].fillna(0).values
    total_vis_min = df['VISMINALLCOUNT'].fillna(0).values
    total_vis_min_men = df['VISMINMENCOUNT'].fillna(0).values
    total_vis_min_women = df['VISMINWOMENCOUNT'].fillna(0).values

    #----- Code for Pie Graph of Employment Equity Group Distribution in a Year-----#
    for j in range (0, len(employer)-1):
        if employer[j] == employer_selection:
            if salary_range[j] == "Overall":
                if country[j] == "Canada":
                    if employment_status[j] == "Full-Time":
                        ft_employees = total_employees[j]
                        ft_male = total_male[j]
                        ft_women = total_women[j]
                        ft_aboriginal = total_aboriginal[j]
                        ft_disabled = total_disabled[j]
                        ft_vis_min = total_vis_min[j]
                        data = [ft_women, ft_aboriginal, ft_disabled, ft_vis_min]
                        minority_categories = ['women', 'aboriginal', 'person with disability', 'visible minority']
                        fig = plt.figure(figsize =(10, 7))
                        plt.pie(data, labels = minority_categories)
                        plt.savefig('Minority_Distributions_' + employer_selection + str(i) + '.png')

#----- Code for number of employment equity group employees over time -----# NEED FIXES
#                         # Set up data for distribution over time
#                         male_overTime = np.append(male_overTime, ft_male)
#                         women_overTime = np.append(women_overTime, ft_women)
#                         aboriginal_overTime = np.append(aboriginal_overTime, ft_aboriginal)
#                         vis_min_overTime = np.append(vis_min_overTime, ft_vis_min)                        
#                         disabled_overTime = np.append(disabled_overTime, ft_disabled)
#     year_overTime = np.append(year_overTime, int(i))

    # # Plot minority groups over time graph
    # def Delta(x):
    #   return len(x)*np.sum(x**2)-np.sum(x)**2
    # def A(x,y):
    #   return (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/Delta(x)
    # def B(x,y):
    #   return (len(x)*np.sum(x*y)-np.sum(x)*np.sum(y))/Delta(x)
    # delta_year = year_max - year_min
    # newx = np.linspace(year_min, year_max, delta_year + 1)
    # # plt.scatter(year_overTime, male_overTime, color='black', label='Linear Model')
    # plt.xlim(year_min-1, year_max+1)
    # plt.scatter(year_overTime, male_overTime, color='black', label='Linear Model')
    # # plt.plot(year_overTime, women_overTime, color='blue', label='Linear Model')
    # # plt.plot(year_overTime, aboriginal_overTime, color='red', label='Linear Model')
    # # plt.plot(year_overTime, vis_min_overTime, color='orange', label='Linear Model')
    # # plt.plot(year_overTime, disabled_overTime, year_overTime, color='yellow', label='Linear Model')
    # # plt.plot(newx, A(women_overTime, year_overTime) + B(women_overTime, year_overTime)*newx, color='blue', label='Linear Model')
    # # plt.plot(newx, A(aboriginal_overTime, year_overTime) + B(aboriginal_overTime, year_overTime)*newx, color='red', label='Linear Model')
    # # plt.plot(newx, A(vis_min_overTime, year_overTime) + B(vis_min_overTime, year_overTime)*newx, color='orange', label='Linear Model')
    # # plt.plot(newx, A(disabled_overTime, year_overTime) + B(disabled_overTime, year_overTime)*newx, color='yellow', label='Linear Model')
    # plt.xlabel('Year')
    # plt.ylabel('Number of Employees in Groups')
    # plt.title(employer_selection + 'Employees in Minority Groups Over Time')
    # # plt.legend(loc=0)
    # plt.savefig('employee_groups_over_time_' + employer_selection)
    

#----- Code for Bar Graph: "Percentage of Employees in Employment Equity Groups by Salary" -----#
    minority_ratio = []
    for j in range (0, len(employer)-1):
        if employer[j] == employer_selection:
            if country[j] == "Canada":
                if employment_status[j] == "Full-Time":
                    if salary_range[j] == "Under $15,000":
                        u15K_employees = total_employees[j]
                        u15K_male = total_male[j]
                        u15K_women = total_women[j]
                        u15K_aboriginal = total_aboriginal[j]
                        u15K_disabled = total_disabled[j]
                        u15K_vis_min = total_vis_min[j]
                        u15K_aboriginal_women = total_aboriginal_women[j]
                        u15K_disabled_women = total_disabled_women[j]
                        u15K_vis_min_women = total_vis_min_women[j]
                        u15Kminority_ratio = (u15K_women + u15K_aboriginal + u15K_disabled + u15K_vis_min - u15K_aboriginal_women - u15K_disabled_women - u15K_vis_min_women)/u15K_employees
                        minority_ratio.append(u15Kminority_ratio)
                    if salary_range[j] == "$ 15,000 - $19,999":
                        p15K_employees = total_employees[j]
                        p15K_male = total_male[j]
                        p15K_women = total_women[j]
                        p15K_aboriginal = total_aboriginal[j]
                        p15K_disabled = total_disabled[j]
                        p15K_vis_min = total_vis_min[j]
                        p15K_aboriginal_women = total_aboriginal_women[j]
                        p15K_disabled_women = total_disabled_women[j]
                        p15K_vis_min_women = total_vis_min_women[j]
                        p15Kminority_ratio = (p15K_women + p15K_aboriginal + p15K_disabled + p15K_vis_min - p15K_aboriginal_women - p15K_disabled_women - p15K_vis_min_women)/p15K_employees                
                        minority_ratio.append(p15Kminority_ratio)
                    elif salary_range[j] == "$ 20,000 - $24,999":
                        p20K_employees = total_employees[j]
                        p20K_male = total_male[j]
                        p20K_women = total_women[j]
                        p20K_aboriginal = total_aboriginal[j]
                        p20K_disabled = total_disabled[j]
                        p20K_vis_min = total_vis_min[j]
                        p20K_aboriginal_women = total_aboriginal_women[j]
                        p20K_disabled_women = total_disabled_women[j]
                        p20K_vis_min_women = total_vis_min_women[j]
                        p20Kminority_ratio= (p20K_women + p20K_aboriginal + p20K_disabled + p20K_vis_min - p20K_aboriginal_women - p20K_disabled_women - p20K_vis_min_women)/p20K_employees
                        minority_ratio.append(p20Kminority_ratio)
                    elif salary_range[j] == "$ 25,000 - $29,999":
                        p25K_employees = total_employees[j]
                        p25K_male = total_male[j]
                        p25K_women = total_women[j]
                        p25K_aboriginal = total_aboriginal[j]
                        p25K_disabled = total_disabled[j]
                        p25K_vis_min = total_vis_min[j]
                        p25K_aboriginal_women = total_aboriginal_women[j]
                        p25K_disabled_women = total_disabled_women[j]
                        p25K_vis_min_women = total_vis_min_women[j]
                        p25Kminority_ratio = (p25K_women + p25K_aboriginal + p25K_disabled + p25K_vis_min - p25K_aboriginal_women - p25K_disabled_women - p25K_vis_min_women)/p25K_employees
                        minority_ratio.append(p25Kminority_ratio)
                    elif salary_range[j] == "$ 30,000 - $34,999":
                        p30K_employees = total_employees[j]
                        p30K_male = total_male[j]
                        p30K_women = total_women[j]
                        p30K_aboriginal = total_aboriginal[j]
                        p30K_disabled = total_disabled[j]
                        p30K_vis_min = total_vis_min[j]
                        p30K_aboriginal_women = total_aboriginal_women[j]
                        p30K_disabled_women = total_disabled_women[j]
                        p30K_vis_min_women = total_vis_min_women[j]
                        p30Kminority_ratio = (p30K_women + p30K_aboriginal + p30K_disabled + p30K_vis_min - p30K_aboriginal_women - p30K_disabled_women - p30K_vis_min_women)/p30K_employees
                        minority_ratio.append(p30Kminority_ratio)
                    elif salary_range[j] == "$ 35,000 - $37,499":
                        p35K_employees = total_employees[j]
                        p35K_male = total_male[j]
                        p35K_women = total_women[j]
                        p35K_aboriginal = total_aboriginal[j]
                        p35K_disabled = total_disabled[j]
                        p35K_vis_min = total_vis_min[j]
                        p35K_aboriginal_women = total_aboriginal_women[j]
                        p35K_disabled_women = total_disabled_women[j]
                        p35K_vis_min_women = total_vis_min_women[j]
                        p35Kminority_ratio = (p35K_women + p35K_aboriginal + p35K_disabled + p35K_vis_min - p35K_aboriginal_women - p35K_disabled_women - p35K_vis_min_women)/p35K_employees
                        minority_ratio.append(p35Kminority_ratio)
                    elif salary_range[j] == "$ 37,500 - $39,999":
                        p37K_employees = total_employees[j]
                        p37K_male = total_male[j]
                        p37K_women = total_women[j]
                        p37K_aboriginal = total_aboriginal[j]
                        p37K_disabled = total_disabled[j]
                        p37K_vis_min = total_vis_min[j]
                        p37K_aboriginal_women = total_aboriginal_women[j]
                        p37K_disabled_women = total_disabled_women[j]
                        p37K_vis_min_women = total_vis_min_women[j]
                        p37Kminority_ratio = (p37K_women + p37K_aboriginal + p37K_disabled + p37K_vis_min - p37K_aboriginal_women - p37K_disabled_women - p37K_vis_min_women)/p37K_employees
                        minority_ratio.append(p37Kminority_ratio)
                    elif salary_range[j] == "$ 40,000 - $44,999":
                        p40K_employees = total_employees[j]
                        p40K_male = total_male[j]
                        p40K_women = total_women[j]
                        p40K_aboriginal = total_aboriginal[j]
                        p40K_disabled = total_disabled[j]
                        p40K_vis_min = total_vis_min[j]
                        p40K_aboriginal_women = total_aboriginal_women[j]
                        p40K_disabled_women = total_disabled_women[j]
                        p40K_vis_min_women = total_vis_min_women[j]
                        p40Kminority_ratio = (p40K_women + p40K_aboriginal + p40K_disabled + p40K_vis_min - p40K_aboriginal_women - p40K_disabled_women - p40K_vis_min_women)/p40K_employees
                        minority_ratio.append(p40Kminority_ratio)
                    elif salary_range[j] == "$ 45,000 - $49,999":
                        p45K_employees = total_employees[j]
                        p45K_male = total_male[j]
                        p45K_women = total_women[j]
                        p45K_aboriginal = total_aboriginal[j]
                        p45K_disabled = total_disabled[j]
                        p45K_vis_min = total_vis_min[j]
                        p45K_aboriginal_women = total_aboriginal_women[j]
                        p45K_disabled_women = total_disabled_women[j]
                        p45K_vis_min_women = total_vis_min_women[j]
                        p45Kminority_ratio = (p45K_women + p45K_aboriginal + p45K_disabled + p45K_vis_min - p45K_aboriginal_women - p45K_disabled_women - p45K_vis_min_women)/p45K_employees
                        minority_ratio.append(p45Kminority_ratio)
                    elif salary_range[j] == "$ 50,000 - $59,999":
                        p50K_employees = total_employees[j]
                        p50K_male = total_male[j]
                        p50K_women = total_women[j]
                        p50K_aboriginal = total_aboriginal[j]
                        p50K_disabled = total_disabled[j]
                        p50K_vis_min = total_vis_min[j]
                        p50K_aboriginal_women = total_aboriginal_women[j]
                        p50K_disabled_women = total_disabled_women[j]
                        p50K_vis_min_women = total_vis_min_women[j]
                        p50Kminority_ratio = (p50K_women + p50K_aboriginal + p50K_disabled + p50K_vis_min - p50K_aboriginal_women - p50K_disabled_women - p50K_vis_min_women)/p50K_employees
                        minority_ratio.append(p50Kminority_ratio)
                    elif salary_range[j] == "$ 60,000 - $69,999":
                        p60K_employees = total_employees[j]
                        p60K_male = total_male[j]
                        p60K_women = total_women[j]
                        p60K_aboriginal = total_aboriginal[j]
                        p60K_disabled = total_disabled[j]
                        p60K_vis_min = total_vis_min[j]
                        p60K_aboriginal_women = total_aboriginal_women[j]
                        p60K_disabled_women = total_disabled_women[j]
                        p60K_vis_min_women = total_vis_min_women[j]
                        p60Kminority_ratio = (p60K_women + p60K_aboriginal + p60K_disabled + p60K_vis_min - p60K_aboriginal_women - p60K_disabled_women - p60K_vis_min_women)/p60K_employees
                        minority_ratio.append(p60Kminority_ratio)
                    elif salary_range[j] == "$ 70,000 - $84,999":
                        p70K_employees = total_employees[j]
                        p70K_male = total_male[j]
                        p70K_women = total_women[j]
                        p70K_aboriginal = total_aboriginal[j]
                        p70K_disabled = total_disabled[j]
                        p70K_vis_min = total_vis_min[j]
                        p70K_aboriginal_women = total_aboriginal_women[j]
                        p70K_disabled_women = total_disabled_women[j]
                        p70K_vis_min_women = total_vis_min_women[j]
                        p70Kminority_ratio = (p70K_women + p70K_aboriginal + p70K_disabled + p70K_vis_min - p70K_aboriginal_women - p70K_disabled_women - p70K_vis_min_women)/p70K_employees
                        minority_ratio.append(p70Kminority_ratio)
                    elif salary_range[j] == "$ 85,000 - $99,999":
                        p85K_employees = total_employees[j]
                        p85K_male = total_male[j]
                        p85K_women = total_women[j]
                        p85K_aboriginal = total_aboriginal[j]
                        p85K_disabled = total_disabled[j]
                        p85K_vis_min = total_vis_min[j]
                        p85K_aboriginal_women = total_aboriginal_women[j]
                        p85K_disabled_women = total_disabled_women[j]
                        p85K_vis_min_women = total_vis_min_women[j]
                        p85Kminority_ratio = (p85K_women + p85K_aboriginal + p85K_disabled + p85K_vis_min - p85K_aboriginal_women - p85K_disabled_women - p85K_vis_min_women)/p85K_employees
                        minority_ratio.append(p85Kminority_ratio)
                    elif salary_range[j] == "$100,000 and over":
                        p100K_employees = total_employees[j]
                        p100K_male = total_male[j]
                        p100K_women = total_women[j]
                        p100K_aboriginal = total_aboriginal[j]
                        p100K_disabled = total_disabled[j]
                        p100K_vis_min = total_vis_min[j]
                        p100K_aboriginal_women = total_aboriginal_women[j]
                        p100K_disabled_women = total_disabled_women[j]
                        p100K_vis_min_women = total_vis_min_women[j]
                        p100Kminority_ratio = (p100K_women + p100K_aboriginal + p100K_disabled + p100K_vis_min - p100K_aboriginal_women - p100K_disabled_women - p100K_vis_min_women)/p100K_employees
                        minority_ratio.append(p100Kminority_ratio)
                    else: 
                        pass
                    
salary = ['Under $15K', '$15K - $20K', '$20K - $25K', '$25K - $30K', '$30K - $35K', '$35K - $37.5K', '$37.5K - $40K', '$40K - $45K', '$45K - $50K', '$50K - $60K', '$60K - $70K', '$70K - $85K', '$85K - $100K', 'Over $100K']
fig3 = plt.bar(salary, minority_ratio)
plt.title(str(i) + ' ' + employer_selection + ' ' + 'Percentage of Employees\nin Employment Equity Groups by Salary', fontsize=10)
plt.xlabel('Income', fontsize=8)
plt.ylabel('Percentage of Employees in Employment Equity Groups', fontsize=8)
plt.xticks(rotation=45)
plt.xticks(fontsize=8)
plt.tight_layout()
plt.savefig('minority_ratio_salary' + employer_selection)
