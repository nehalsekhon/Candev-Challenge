from calendar import LocaleHTMLCalendar
import pandas as pd
import collections
import matplotlib.pyplot as plt
import os
from natsort import os_sorted


def filepathextraction(formname):
    ''' 
        gets all the file paths and returns them
    '''
    form =[]

    # all path directories for the forms
    for folder in os.listdir("Dataset"):
        for file in os.listdir("Dataset/" + folder):
            if file == formname +".csv":
                form.append(os.path.join("Dataset/" + folder + "/", file))
                form = os_sorted(form)
    return form

# get peak employee for company
def peakcompanyemployee(company):

    form1 = filepathextraction("Form1")
    f = open("src/employeecount.txt", "w")
    f.write(company + "\n")
    year = []
    permfulltime = []
    permparttime = []
    tempcount = []

    for file in form1:
        data = pd.read_csv(file, encoding = "ISO-8859-1")

        NAICSID = data["NAICSID"].fillna(0).values
        EMPLOYER = data["EMPLOYERNAME"].fillna(0).values
        GEOGRAPHY = data["GEOGRAPHY"].fillna(0).values
        YEAR = data["CALENDARYEAR"].fillna(0).values
        PERMFULLTIMECOUNT = data["PERMFULLTIMECOUNT"].fillna(0).values
        PERMPARTTIMECOUNT = data["PERMPARTTIMECOUNT"].fillna(0).values
        TEMPCOUNT = data["TEMPCOUNT"].fillna(0).values
        CANADACOUNT = data["CANADACOUNT"].fillna(0).values

        f.write("year " + str(YEAR[1]) + "\n")
        year.append(YEAR[1])

        for i in range(0, len(EMPLOYER)):
            if (EMPLOYER[i] == company and GEOGRAPHY[i] == "National" and NAICSID[i] == 0):
                f.write("total " + str(CANADACOUNT[i]) + "\n")
                f.write("permfulltime " + str(PERMFULLTIMECOUNT[i]) + "\n")
                permfulltime.append(PERMPARTTIMECOUNT[i])
                f.write("permparttime " + str(PERMPARTTIMECOUNT[i]) + "\n")
                permparttime.append(PERMPARTTIMECOUNT[i])
                f.write("tempcount " + str(TEMPCOUNT[i]) + "\n")
                tempcount.append(TEMPCOUNT[i])
                break
        if len(permfulltime) != len(year):
            permfulltime.append(0)
            permparttime.append(0)
            tempcount.append(0)

        f.write("\n")
    f.close()
     
    fig, ax = plt.subplots() 
    ax.bar(year, permfulltime, label="Permanant Full Time Employees", width=0.35)
    ax.bar(year, permparttime, label="Permanant Part Time Employees", bottom=permfulltime, width=0.35)   
    ax.bar(year, tempcount, label="Temporary Employees", bottom=permparttime, width=0.35)    

    ax.set_ylabel('Total Employees')
    ax.set_xlabel('Year')
    ax.set_title(company +" Total Employees")
    ax.legend(bbox_to_anchor = (1.05, 0.6))   
    plt.tight_layout()
    plt.savefig("src/companyemployeecounte.png")

# def jobtypes(company):
#     types = ["Senior Managers", "Middle and Other Managers", "Professionals", "Semi-Professionals and Technicians", "Supervisors",
#      "Supervisors: Crafts and Trades", "Administrative and Senior Clerical Personnel", "Skilled Crafts and Trades Workers",
#       "Clerical Personnel", "Intermediate Sales and Service Personnel", "Semi-Skilled Manual Workers", "Other Manual Workers"]

#     form6 = filepathextraction("Form6")
#     f = open("src/positiondiversity.txt", "w")
#     f.write(company + "\n")

#     for file in form6:
#         data = pd.read_csv(file, encoding = "ISO-8859-1")

#         employer = data['EMPLOYERNAME'].fillna(0).values
#         year = data["CALENDARYEAR"].fillna(0).values
#         geography = data["GEOGRAPHY"].fillna(0).values
#         country = data['LOCATION'].fillna(0).values
#         employment_status = data["EMPLOYMENTSTATUS"].fillna(0).values
#         occupation = data["OCCGROUP"].fillna(0).values
#         total_male = data['ALLMENCOUNT'].fillna(0).values
#         total_women = data['ALLWOMENCOUNT'].fillna(0).values
#         total_aboriginal_men = data['ABORIGMENCOUNT'].fillna(0).values
#         total_aboriginal_woman = data['ABORIGWOMENCOUNT'].fillna(0).values
#         total_disabled_men = data['PWDMENCOUNT'].fillna(0).values
#         total_disabled_woman = data['PWDWOMENCOUNT'].fillna(0).values
#         total_vis_min_man = data['VISMINMENCOUNT'].fillna(0).values
#         total_vis_min_woman = data['VISMINWOMENCOUNT'].fillna(0).values

#         for i in range(0, len(employer)):
#             if (employer[i] == company and geography[i] == "National" and occupation[i] == "Overall"):
#                 f.write("totalmen " + str(total_male[i]) + "\n")
#                 f.write("permfulltime " + str(PERMFULLTIMECOUNT[i]) + "\n")
#                 f.write("permparttime " + str(PERMPARTTIMECOUNT[i]) + "\n")
#                 f.write("tempcount " + str(TEMPCOUNT[i]) + "\n")
#                 break
#         # if len(permfulltime) != len(year):
#         #     permfulltime.append(0)
#         #     permparttime.append(0)
#         #     tempcount.append(0)

        
