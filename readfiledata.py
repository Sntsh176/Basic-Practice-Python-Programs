"""
reading data from file 

"""

# !/usr/bin/env python3
# https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

categories = {}
parts = [] 

def upsertCategories(line):
    global categories
    if line in categories.keys(): 
        categories.update({line : categories.get(line) + 1})
    else:
        categories.update({line:1})

if __name__ == "__main__":
    open_file = open('categories_images.txt', 'r') # with open('nameslist.txt') as open_file
    lines = open_file.readlines()

    for line in lines:
        parts = line.split('/')
        upsertCategories(parts[2])

    for k, v in categories.items(): 
        print(str(k) + ' : ' + str(v))
    open_file.close() 
