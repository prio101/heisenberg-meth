import os
import math

def create_file():
  f = open('./result_set_quiz_5', 'x')
  f.close()

def get_so_result(co_ordinates_sulfer, co_ordinates_oxygen):  
  co_ordinates_sulfer_x = co_ordinates_sulfer[0]
  co_ordinates_sulfer_y = co_ordinates_sulfer[1]
  co_ordinates_sulfer_z = co_ordinates_sulfer[2]
  result_set = []
  for elem in co_ordinates_oxygen:
    co_ordinates_oxygen_x = elem[0]
    co_ordinates_oxygen_y = elem[1]
    co_ordinates_oxygen_z = elem[2]  
    result = math.sqrt(pow( (co_ordinates_sulfer_x - co_ordinates_oxygen_x ), 2) + pow( (co_ordinates_sulfer_y - co_ordinates_oxygen_y ),2) + pow((co_ordinates_sulfer_z - co_ordinates_oxygen_z ),2) )
    result_set.append(result)
  return result_set

def find_s_o_bonds(file, line_number):
  sulfer_atomic_number = 16
  oxygen_atomic_number = 8
  current_line = line_number
  co_ordinates_sulfer = []
  co_ordinates_oxygen = []
  dump_data_arr = []
  for current_line in file:
    second_col = file[current_line].split(' ')[1]
    if(sulfer_atomic_number in second_col):      
      co_ordinates_sulfer = file[current_line].split(' ')[-3:]
      dump_data_arr.append(file[current_line])
    elif(oxygen_atomic_number in second_col):
      co_ordinates_oxygen = file[current_line].split(' ')[-3:]  
      dump_data_arr.append(file[current_line])
    else:
      'I am Pickle-Rick'
  so_bonds_result_arr = get_so_result(co_ordinates_sulfer, co_ordinates_oxygen)

  create_file()
  file = open('./result_set_quiz_5', 'a')  
  
def get_the_immidiate_lines_blocks(file, line_number):
  line_number_for_the_separator_count = 0
  separator_line_threshold = 3
  separator = '-'*69
  current_line = line_number    

  for current_line in file:    
    if(separator in file[current_line] and line_number_for_the_separator_count <= separator_line_threshold):
      line_number_for_the_separator_count = line_number_for_the_separator_count + 1

    while(line_number_for_the_separator_count < 3):
      find_s_o_bonds(file, current_line)

def read_the_messy_files(files_list):
  key_words = 'Input orientation:'  

  line_for_input_orientation = 0
  
  for file_name in files_list:
    file = open(file_name, 'r').readlines()
    line_lengths = len(file)

    for line_number in range(line_lengths):
      if key_words in file[line_number]:
        line_for_input_orientation = line_number
        get_the_immidiate_lines_blocks(file, line_for_input_orientation)

def main():
  folder_name = 'a1q5'
  path_name = './'

  files_list = os.listdir(path_name+folder_name)
  read_the_messy_files(files_list)

if __name__ == "__main__":
  main()
