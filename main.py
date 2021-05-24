import configparser
import os
import pathlib
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import appdirs

INI_PATH_FILE_NAME = "inipath.txt"
INI_PATH_FILE_PATH = appdirs.user_config_dir("desmume-path-editor")


def get_ini_path():
    try:
        ini_path_file = open(os.path.join(INI_PATH_FILE_PATH, INI_PATH_FILE_NAME), 'r')
        path = ini_path_file.read()
        ini_path_file.close()
        return path
    except (FileNotFoundError, IOError):
        print("First time running, please choose the path to the desmume.ini file...")
        Tk().withdraw()
        path = askopenfilename(title="Choose desmume.ini path")
        while path == "":
            print("Please choose the path to the desmume.ini file...")
            path = askopenfilename(title="Choose desmume.ini path")
        if not os.path.exists(INI_PATH_FILE_PATH):
            os.makedirs(INI_PATH_FILE_PATH)
        ini_path_file = open(os.path.join(INI_PATH_FILE_PATH, INI_PATH_FILE_NAME), 'w')
        ini_path_file.write(path)
        ini_path_file.close()
        return path


ini_file_path = get_ini_path()
current_dir = pathlib.Path().absolute()

ds_file_name = ""

for file_name in os.listdir(current_dir):
    tokens = file_name.split('.')
    if len(tokens) < 2:
        continue
    extension = tokens[-1]
    if extension == 'nds':
        ds_file_name = file_name
        break
if ds_file_name == "":
    print("No DS rom file found in the current directory.",
          "Please run this script from a directory that contains a .nds file.")
    input()
    exit(1)
print("nds rom", ds_file_name, "found.")
print("ini file found at", ini_file_path)
parser = configparser.ConfigParser()

try:
    parser.read(ini_file_path)
    print("Editing ini...")
    parser.set("PathSettings", "States", current_dir.__str__())
    parser.set("PathSettings", "Screenshots", os.path.join(current_dir.__str__(), "screenshots"))
    parser.set("PathSettings", "StateSlots", current_dir.__str__())
    parser.set("PathSettings", "Cheats", current_dir.__str__())
    parser.set("PathSettings", "SramImportExport", current_dir.__str__())
    with open(ini_file_path, 'w') as configfile:
        parser.write(configfile)
    print("Done.")
except Exception as e:
    os.remove(os.path.join(INI_PATH_FILE_PATH, INI_PATH_FILE_NAME))
    print(e)
    print("\nInvalid ini file.")
    input("Press enter to exit...")
    exit(1)
else:
    print("Running rom")
    os.system('"' + os.path.join(current_dir, ds_file_name) + '"')
