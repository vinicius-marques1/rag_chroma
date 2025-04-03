import os

# walk through the directory
for dirpath, dirnames, filenames in os.walk('/mnt/c/Users/vinic/Documents/Biblioteca/'):
    # print the directory path
    print(f'Found directory: {dirpath}')
    # print the subdirectories
    for dirname in dirnames:
        print(f'\tSubdirectory: {dirname}')
    # print the filenames
    for filename in filenames:
        print(f'\tFile: {filename}')