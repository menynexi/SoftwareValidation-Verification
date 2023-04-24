import easyocr
import os
import subprocess
import platform
import shutil


def pic_image():
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Open a Finder window for the current directory on macOS
    if platform.system() == 'Darwin':
        subprocess.call(['open', '-R', current_dir])
    
    # Get the path to the source image file
    source_path = input("Enter the path to the source image file: ")
    return source_path



def solve_from_picture():
    path = pic_image()
    reader = easyocr.Reader(['en'], gpu= True)
    results = reader.readtext(path,allowlist='0123456789 %/*-+')
    
    # print(results)
    text = ''
    for result in results:
        text+= result[1] + ''
    print(text)
    result = eval(text)
    print(result)
    return result
