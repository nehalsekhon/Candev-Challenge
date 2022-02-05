import pandas as pd
import collections
import matplotlib.pyplot as plt
import os
from natsort import os_sorted

sectorcode = int(input("Enter sector code: "))

coloum = []
files = []
for folder in os.listdir("Dataset"):
    for file in os.listdir("Dataset/" + folder):
        if file == "Form1.csv":
            files.append(os.path.join("Dataset/" + folder + "/", file))
            files = os_sorted(files)

years =[]
employees = []

for file in files:
    data = pd.read_csv(file, encoding = "ISO-8859-1")
    id = {}
    count=0
    year = 0

    NAICSID = data["NAICSID"].values
    NAICSCLASSTITLE = data["NAICSCLASSTITLE"].values
    EMPLOYER = data["EMPLOYERNAME"].values
    YEAR = data["CALENDARYEAR"].values
    PEAKEMPLOYEECOUNT = data["PEAKEMPLOYEECOUNT"].values

    for i in range(0, len(EMPLOYER)):
        year =YEAR[i]
        if NAICSID[i] == sectorcode:
            if str(PEAKEMPLOYEECOUNT[i]) != 'nan':
                count = count + PEAKEMPLOYEECOUNT[i]
    years.append(year)
    employees.append(count)
print(years)
print(employees)
fig, ax = plt.subplots()
ax.bar(years, employees, width=1, edgecolor="white", linewidth=0.7)
plt.savefig("j.png")