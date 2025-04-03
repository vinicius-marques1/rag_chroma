import magic
import os

for dirpath, dirnames, filenames in os.walk('./django-ecommerce'):

    # print the type of the file
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        print(f'\tFile: {filename}')
        print(magic.from_file(filepath, mime=True))
        print('-' * 20)