import os

def 


def get_the_immidiate_lines_blocks(file, line_number):
  line_number_for_the_separator_count = 0
  separator_line_threshold = 3
  separator = '-'*69
  current_line = line_number    

  for current_line in file:    
    if(separator in file[current_line] and line_number_for_the_separator_count <= separator_line_threshold):
      line_number_for_the_separator_count = line_number_for_the_separator_count + 1

    while(line_number_for_the_separator_count < 3):
      find_s_o_bonds()

def read_the_messy_files(files_list):
  length_of_files = len(files_list)
  key_words = 'Input orientation:'
  
  line_for_input_orientation = 0
  
  for file_name in files_list:
    file = open(file_name, 'r').readlines()
    line_lengths = len(file)

    for line_number in range(line_lengths):
      if key_words in file[line_number]:
        line_for_input_orientation = line_number
        get_the_immidiate_lines_blocks(file, line_for_input_orientation)
    
  
  return 1



def main():
  folder_name = 'a1q5'
  path_name = './'

  files_list = os.listdir(path_name+folder_name)
  res = read_the_messy_files(files_list)






if __name__ == "__main__":
  main()