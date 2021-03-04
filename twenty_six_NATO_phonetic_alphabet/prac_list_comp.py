

# List Comprehension
# new_list = [new_item for item in list]
# new_list_if = [new_item for item in list if test]

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for k,v in dict.items()}
# new_dict_if = {new_key:new_value for k,v in dict.items() if test}

# numbers = [1, 2, 3]
#
# new_list = [n + 1 for n in numbers]
#
# #For Loop
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)


student_dict = {
    'students': ['Tad', 'Tex', 'Ted'],
    'score':  [77, 87, 94]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# for index , row in student_data_frame.iterrows():
#     print(row)

# for index , row in student_data_frame.iterrows():
#     print(row.students)

for index , row in student_data_frame.iterrows():
    print(row.score)



