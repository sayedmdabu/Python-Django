# import sys
# sys.path.append('/user/shanta/Documents/My-Modules')
# # import my_module
# # import my_module as mm
# from my_module import find_index, test


# courses = ['History', 'Math', 'Physics', 'CompSci']

# # index = my_module.find_index(courses, 'Math')
# # index = mm.find_index(courses, 'Math')
# index = find_index(courses, 'Math')

# # print(index)
# # print(test)

# print(sys.path)
####################################
# import random

# courses = ['History', 'Math', 'Physics', 'CompSci']

# random_course = random.choice(courses)

# print(random_course)

###################################
# import os
# print(os.getcwd())
# print(os.__file__)


############################
import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))
