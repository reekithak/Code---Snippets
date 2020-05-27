
import pandas as pd

read_file = pd.read_excel("Book1.xlsx")

read_file.to_csv('Book1.csv',index=False)


book1 = pd.read_csv("Book1.csv")

book1 = pd.DataFrame(book1)

book1.isnull().any()

unique = []

a = book1['skills'].to_list()
b = book1['Skills2'].to_list()

common = []

for i in range(len(a)):
    a_sent = str(a[i]).split(',')
    a_sent = [item.lower() for item in a_sent]
    b_sent = str(b[i]).split(',')
    b_sent = [item.lower() for item in b_sent]
    common.append(set(a_sent).intersection(set(b_sent)))
    unique.append(set(a_sent).symmetric_difference(set(b_sent)))



book1['unique'] = unique

book1['common'] = common

book1







