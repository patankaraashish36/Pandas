# import pandas as pd
# import numpy as np
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}

# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


# df = pd.DataFrame(data, index=labels)

# # print(df)

# # Select the rows the age is between 2 and 4 (inclusive).
# # print(df["age"].between(2,4))
# print(df.loc[:,"age"].between(2,4))

# print(/10)
for variable_1 in range(1,0,-1):
    print("executed")


numbers_list = [98,45,60,71,90]
count = 10
for number in numbers_list:
    if number % 10 == 0:
        count -= 1
        continue
    counter = 0
    while counter < 2:
        last_digit = number % 10
        number = number // 10
        if last_digit > 4:
            count += 1
            break
        count += 1
        counter += 1
print(count)


num1=16
num2=6
while(num1>=2):
    if(num1>num2):
        num1=num1/2
    else:
        print(num1)
        break

print(98%10)