import pandas
import pandas as pd

# pip install pandas

data = pd.read_csv('records.csv', delimiter=",")
print(data)
#      name branch  year  cgpa
# 0   radek    coe     3   0.0
# 1   radek    coe     3   0.0
# 2   Zosia    cos     2   9.0
# 3    Asia    cot     4   9.1
# 4  Monika    cob     5  11.0
# 5   Zenek    coo     7  11.5

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['radek' 'coe' 3 0.0]
#  ['radek' 'coe' 3 0.0]
#  ['Zosia' 'cos' 2 9.0]
#  ['Asia' 'cot' 4 9.1]
#  ['Monika' 'cob' 5 11.0]
#  ['Zenek' 'coo' 7 11.5]]
print(data.values[0])  # ['radek' 'coe' 3 0.0]
print(data.items)
# <bound method DataFrame.items of      name branch  year  cgpa
# 0   radek    coe     3   0.0
# 1   radek    coe     3   0.0
# 2   Zosia    cos     2   9.0
# 3    Asia    cot     4   9.1
# 4  Monika    cob     5  11.0
# 5   Zenek    coo     7  11.5>
