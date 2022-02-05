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
