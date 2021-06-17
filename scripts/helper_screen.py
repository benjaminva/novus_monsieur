
from os import listdir
from os.path import isfile, join

def load_files(mypath):
    return [f for f in listdir(mypath) if isfile(join(mypath, f))]

def load_paths(file):
    """
    loads the paths of the posters  from the specified files to the dictionary
    of [concept: [poster_paths]
    """

    f = open(file, "r")
    lines = f.readlines()
    dict_paths = {}
    for line in lines:
        line = line.strip()
        line = line.replace(", ",",Posters/")
        words = line.split(",")
        dict_paths[words[0]] = words[1:]
    return dict_paths

def save_paths(file, dict_paths):
    f = open(file, "w")
    f.write(dict_paths)

def load_users(file):
    f = open(file, "r")
    lines = f.readlines()
    paths = {}
    for line in lines:
        line = line.strip()
        
        line = line.replace(", ",",Posters/")
        words = line.split(",")
        dict_users[words[0]] = words[1:]
    return dict_users
    users = {"arturo":["circuitos", "calculo"], "benjamin":["circuitos"]}
    #TODO fun load dict from file
