import csv
import os


# list all the files in directory /a1q3
list_dir = os.listdir("./a1q3")

# first array index will be the start file name
start_file_name = list_dir[0]

# get the last of the array of list dir 
# -1 will start from the end in python
# or you can reverse and take the start

last_file_name = list_dir[-1]

# file = open("./a1q3/data36.dat").readlines()
print(list_dir)


def result_file_name(start_file_name, last_file_name):
  # spiting by . => ['data36', 'dat']
  return 'data' + name_bringer(start_file_name.split('.')[0]) + '-' + name_bringer(last_file_name.split('.')[0]) + 'avg.dat'

def name_bringer(alphanumeric_word):
  # getting the last elem [36] or [78]
  return alphanumeric_word.split('data')[-1] 

print(result_file_name(start_file_name, last_file_name))