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
    employer = df['EMPLOYERNAME'].values
    salary_range = df['SALARYRANGE($)'].values
    country = df['LOCATION'].values
    employment_status = df["EMPLOYMENTSTATUS"].values
    total_employees = df['ALLCOUNT'].values
    total_male = df['ALLMENCOUNT'].values
    total_women = df['ALLWOMENCOUNT'].values
    total_aboriginal = df['ABORIGALLCOUNT'].values
    total_aboriginal_men = df['ABORIGMENCOUNT'].values
    total_aboriginal_women = df['ABORIGWOMENCOUNT'].values
    total_disabled = df['PWDALLCOUNT'].values
    total_disabled_women = df['PWDMENCOUNT'].values
    total_disabled_women = df['PWDWOMENCOUNT'].values
    total_vis_min = df['VISMINALLCOUNT'].values
    total_vis_min_men = df['VISMINMENCOUNT'].values
    total_vis_min_women = df['VISMINWOMENCOUNT'].values

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

                        # Set up data for distribution over time
                        male_overTime = np.append(male_overTime, ft_male)
                        women_overTime = np.append(women_overTime, ft_women)
                        aboriginal_overTime = np.append(aboriginal_overTime, ft_aboriginal)
                        vis_min_overTime = np.append(vis_min_overTime, ft_vis_min)                        
                        disabled_overTime = np.append(disabled_overTime, ft_disabled)
    year_overTime = np.append(year_overTime, int(i))

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
