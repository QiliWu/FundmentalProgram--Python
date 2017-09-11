# -*- coding: utf-8 -*-
import os

def rename_files():
    # os.listdir(), get file names from a folder
    file_list = os.listdir(r"D:\\03-CS\\prank") # can't read chinese directory
    print (file_list)

    #os.getcwd() : get current working directory
    current_path = os.getcwd()
    print (current_path)   #the result is D:\\03-CS

    #os.chdir(path): change current working directory to path
    os.chdir(r"D:\\03-CS\\prank")

    # for each file, rename its file name
    for file_name in file_list:
    #os.rename(old, new) : change the old file_name to new one
    #string.translate(table, deletechars): Return a copy of the string S
    # in which each character has been mapped through the given translation table.
    # table = None means delete
    # here, delete all digit characters in the file_name
        os.rename(file_name, file_name.translate(None,'0123456789'))

    os.rename('beijing.jpg','delhi.jpg')


rename_files()
