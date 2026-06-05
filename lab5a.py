#!/usr/bin/env python3
# Author ID: Nilavan Selvakumar

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open('data.txt', 'r')
    read_data = f.read()
    f.close()
    return read_data

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open('data.txt', 'r')
    lines = f.readlines()
    f.close()
    
    new_lines = []
    for i in lines:
        new_lines.append(i.strip('\n'))
    return new_lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
