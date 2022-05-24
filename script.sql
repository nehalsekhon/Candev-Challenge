------------- Automate Excel to SQL -------------

------------- Create the tables -------------
DROP TABLE FORM1
DROP TABLE FORM2
DROP TABLE FORM3
DROP TABLE FORM4
DROP TABLE FORM5
DROP TABLE FORM6

CREATE TABLE FORM1
(EMPLOYERNAME NVARCHAR(200),
CALENDARYEAR INT,
GEOGRAPHY NVARCHAR(200),
LOCATION NVARCHAR(200),
NAICSID INT,
NAICSCLASSTITLE NVARCHAR(200),
PEAKEMPLOYEECOUNT INT,
PERMFULLTIMECOUNT INT,
PERMPARTTIMECOUNT INT,
TEMPCOUNT INT,
CANADACOUNT INT
)

CREATE TABLE FORM2
(EMPLOYERNAME NVARCHAR(200),
CALENDARYEAR INT,
EMPLOYMENTSTATUS NVARCHAR(200),
GEOGRAPHY NVARCHAR(200),
LOCATION NVARCHAR(200),
NAICSID INT,
NAICSCLASSTITLE NVARCHAR(200),
OCCGROUP NVARCHAR(200),
QUARTERID INT,
ALLCOUNT INT,
ALLMENCOUNT INT,
ALLWOMENCOUNT INT,
ABORIGALLCOUNT INT,
ABORIGMENCOUNT INT,
ABORIGWOMENCOUNT INT,
PWDALLCOUNT INT,
PWDMENCOUNT INT,
PWDWOMENCOUNT INT,
VISMINALLCOUNT INT,
VISMINMENCOUNT INT,
VISMINWOMENCOUNT INT,
SALARYRANGEBOTTOM NVARCHAR(200),
SALARYRANGETOP NVARCHAR(200)
)

CREATE TABLE FORM3
(EMPLOYERNAME NVARCHAR(200),
CALENDARYEAR INT,
EMPLOYMENTSTATUS NVARCHAR(200),
GEOGRAPHY NVARCHAR(200),
LOCATION NVARCHAR(200),
NAICSID INT,
NAICSCLASSTITLE NVARCHAR(200),
SALARYRANGE NVARCHAR(200),
ALLCOUNT INT,
ALLMENCOUNT INT,
ALLWOMENCOUNT INT,
ABORIGALLCOUNT INT,
ABORIGMENCOUNT INT,
ABORIGWOMENCOUNT INT,
PWDALLCOUNT INT,
PWDMENCOUNT INT,
PWDWOMENCOUNT INT,
VISMINALLCOUNT INT,
VISMINMENCOUNT INT,
VISMINWOMENCOUNT INT
)

CREATE TABLE FORM4
(EMPLOYERNAME NVARCHAR(200),
CALENDARYEAR INT,
GEOGRAPHY NVARCHAR(200),
LOCATION NVARCHAR(200),
NAICSID INT,
NAICSCLASSTITLE NVARCHAR(200),
OCCGROUP NVARCHAR(200),
EMPLOYMENTSTATUS NVARCHAR(200),
ALLCOUNT INT,
ALLMENCOUNT INT,
ALLWOMENCOUNT INT,
ABORIGALLCOUNT INT,
ABORIGMENCOUNT INT,
ABORIGWOMENCOUNT INT,
PWDALLCOUNT INT,
PWDMENCOUNT INT,
PWDWOMENCOUNT INT,
VISMINALLCOUNT INT,
VISMINMENCOUNT INT,
VISMINWOMENCOUNT INT
)

CREATE TABLE FORM5
(EMPLOYERNAME NVARCHAR(200),
CALENDARYEAR INT,
GEOGRAPHY NVARCHAR(200),
LOCATION NVARCHAR(200),
NAICSID INT,
NAICSCLASSTITLE NVARCHAR(200),
OCCGROUP NVARCHAR(200),
EMPLOYMENTSTATUS NVARCHAR(200),
TOTALPROMOTIONS INT,
TOTALMENPROMOTIONS INT,
TOTALWOMENPROMOTIONS INT,
TOTALABORIGALLPROMOTIONS INT,
TOTALABORIGMENPROMOTIONS INT,
TOTALABORIGWOMENPROMOTIONS INT,
TOTALPWDALLPROMOTIONS INT,
TOTALPWDMENPROMOTIONS INT,
TOTALPWDWOMENPROMOTIONS INT,
TOTALVISMINALLPROMOTIONS INT,
TOTALVISMINMENPROMOTIONS INT,
TOTALVISMINWOMENPROMOTIONS INT,
ALLCOUNT INT,
ALLMENCOUNT INT,
ALLWOMENCOUNT INT,
ABORIGALLCOUNT INT,
ABORIGMENCOUNT INT,
ABORIGWOMENCOUNT INT,
PWDALLCOUNT INT,
PWDMENCOUNT INT,
PWDWOMENCOUNT INT,
VISMINALLCOUNT INT,
VISMINMENCOUNT INT,
VISMINWOMENCOUNT INT
)

CREATE TABLE FORM6
(EMPLOYERNAME NVARCHAR(200),
CALENDARYEAR INT,
GEOGRAPHY NVARCHAR(200),
LOCATION NVARCHAR(200),
NAICSID INT,
NAICSCLASSTITLE NVARCHAR(200),
OCCGROUP NVARCHAR(200),
EMPLOYMENTSTATUS NVARCHAR(200),
ALLCOUNT INT,
ALLMENCOUNT INT,
ALLWOMENCOUNT INT,
ABORIGALLCOUNT INT,
ABORIGMENCOUNT INT,
ABORIGWOMENCOUNT INT,
PWDALLCOUNT INT,
PWDMENCOUNT INT,
PWDWOMENCOUNT INT,
VISMINALLCOUNT INT,
VISMINMENCOUNT INT,
VISMINWOMENCOUNT INT,
)

------------- Import Excel Data -------------
BULK INSERT FORM1
FROM 'C:\Users\nehal\Downloads\CANDEV\Form1_2019.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM1
FROM 'C:\Users\nehal\Downloads\CANDEV\Form1_2018.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM1
FROM 'C:\Users\nehal\Downloads\CANDEV\Form1_2017.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM1
FROM 'C:\Users\nehal\Downloads\CANDEV\Form1_2016.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM1
FROM 'C:\Users\nehal\Downloads\CANDEV\Form1_2015.csv'
WITH (FORMAT='CSV')



BULK INSERT FORM2
FROM 'C:\Users\nehal\Downloads\CANDEV\Form2_2019.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM2
FROM 'C:\Users\nehal\Downloads\CANDEV\Form2_2018.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM2
FROM 'C:\Users\nehal\Downloads\CANDEV\Form2_2017.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM2
FROM 'C:\Users\nehal\Downloads\CANDEV\Form2_2016.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM2
FROM 'C:\Users\nehal\Downloads\CANDEV\Form2_2015.csv'
WITH (FORMAT='CSV')



BULK INSERT FORM3
FROM 'C:\Users\nehal\Downloads\CANDEV\Form3_2019.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM3
FROM 'C:\Users\nehal\Downloads\CANDEV\Form3_2018.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM3
FROM 'C:\Users\nehal\Downloads\CANDEV\Form3_2017.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM3
FROM 'C:\Users\nehal\Downloads\CANDEV\Form3_2016.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM3
FROM 'C:\Users\nehal\Downloads\CANDEV\Form3_2015.csv'
WITH (FORMAT='CSV')



BULK INSERT FORM4
FROM 'C:\Users\nehal\Downloads\CANDEV\Form4_2019.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM4
FROM 'C:\Users\nehal\Downloads\CANDEV\Form4_2018.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM4
FROM 'C:\Users\nehal\Downloads\CANDEV\Form4_2017.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM4
FROM 'C:\Users\nehal\Downloads\CANDEV\Form4_2016.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM4
FROM 'C:\Users\nehal\Downloads\CANDEV\Form4_2015.csv'
WITH (FORMAT='CSV')



BULK INSERT FORM5
FROM 'C:\Users\nehal\Downloads\CANDEV\Form5_2019.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM5
FROM 'C:\Users\nehal\Downloads\CANDEV\Form5_2018.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM5
FROM 'C:\Users\nehal\Downloads\CANDEV\Form5_2017.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM5
FROM 'C:\Users\nehal\Downloads\CANDEV\Form5_2016.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM5
FROM 'C:\Users\nehal\Downloads\CANDEV\Form5_2015.csv'
WITH (FORMAT='CSV')



BULK INSERT FORM6
FROM 'C:\Users\nehal\Downloads\CANDEV\Form6_2019.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM6
FROM 'C:\Users\nehal\Downloads\CANDEV\Form6_2018.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM6
FROM 'C:\Users\nehal\Downloads\CANDEV\Form6_2017.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM6
FROM 'C:\Users\nehal\Downloads\CANDEV\Form6_2016.csv'
WITH (FORMAT='CSV')

BULK INSERT FORM6
FROM 'C:\Users\nehal\Downloads\CANDEV\Form6_2015.csv'
WITH (FORMAT='CSV')

SELECT * FROM FORM6
