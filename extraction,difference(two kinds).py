
import pandas as pd

read_file = pd.read_excel("Book1.xlsx")

read_file.to_csv('Book1.csv',index=False)

book1 = pd.read_csv("Book1.csv")

book1 = pd.DataFrame(book1)

book1.isnull().any()

a = book1['skills'].to_list()
b = book1['Skills2'].to_list()

part1not2 = []
part2not1 = []

for i in range(len(a)):
    a_sent = str(a[i]).split(',')
    a_sent = [item.lower() for item in a_sent]
    b_sent = str(b[i]).split(',')
    b_sent = [item.lower() for item in b_sent]
    part1not2.append(set(a_sent)-set(b_sent))
    part2not1.append(set(b_sent)-set(a_sent))
book1['skills not part of skills1'] = part1not2

book1['skills1 not part of skills'] = part2not1

book1







