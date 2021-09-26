import csv
import os

def result_file_name(start_file_name, last_file_name):
  # spiting by . => ['data36', 'dat']
  return 'data' + name_bringer(start_file_name.split('.')[0]) + '-' + name_bringer(last_file_name.split('.')[0]) + 'avg.dat'

def name_bringer(alphanumeric_word):
  # getting the last elem [36] or [78]
  return alphanumeric_word.split('data')[-1] 

def get_the_value_y_for_single_file_and_row_and_store(file_name, current_line):
  print(file_name)
  print('-'*100)

  file = open('./a1q3/'+ file_name).readlines()
  line_numbers = len(file)

  print(line_numbers)
  print('-'*100)
  print(current_line)
  print('-'*100)
  print(file[current_line].split(' ')[0])

  return file[current_line].split(' ')[0]


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
  average_y_holder = []
  # will change
  file = open('./a1q3/data36.dat').readlines()
  # this case all files are 1000 lines
  max_lines_per_file = len(file) 

  for current_line in range(max_lines_per_file):
    for file in list_dir:
      y_value = get_the_value_y_for_single_file_and_row_and_store(file, current_line)
    
      # putting the single 
      # y value into big_chunky_y_array
      big_chunky_y_holder.append(y_value)
      # print(big_chunky_y_holder)
    average = sum(big_chunky_y_holder) / len(big_chunky_y_holder)
    average_y_holder.append(average)

    # nullify the big_chunky_y_holder for new batch
    big_chunky_y_holder = []
    # current line will add up to current_line + 1
    current_line = current_line + 1
  
  print(big_chunky_y_holder)


if __name__ == "__main__":
  main()
  