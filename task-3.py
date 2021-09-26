import csv
import os

def result_file_name(start_file_name, last_file_name):
  # spiting by . => ['data36', 'dat']
  return 'data' + name_bringer(start_file_name.split('.')[0]) + '-' + name_bringer(last_file_name.split('.')[0]) + 'avg.dat'

def name_bringer(alphanumeric_word):
  # getting the last elem [36] or [78]
  return alphanumeric_word.split('data')[-1] 

def get_the_value_y_for_single_file_and_row_and_store(file_name, current_row):
  print(file_name)
  file = open('./a1q3/'+ file_name).readlines()
  print(file)

def main():
  # file = open("./a1q3/data36.dat").readlines()
  # print(list_dir)

  # list all the files in directory /a1q3
  list_dir = os.listdir("./a1q3")
  
  # first array index will be the start file name
  start_file_name = list_dir[0]

  # get the last of the array of list dir 
  # -1 will start from the end in python
  # or you can reverse and take the start

  last_file_name = list_dir[-1]

  # got to create this file
  result_file = result_file_name(start_file_name, last_file_name)
  print(result_file_name(start_file_name, last_file_name))

  big_chunky_y_holder = []
  current_row = 0

  for file in list_dir:
    y_value = get_the_value_y_for_single_file_and_row_and_store(file, current_row)
    
    # putting the single 
    # y value into big_chunky_y_array
    big_chunky_y_holder.append(y_value)
    print(big_chunky_y_holder)


if __name__ == "__main__":
  main()
  