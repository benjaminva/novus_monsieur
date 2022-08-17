import pygame as pg
import time
import random

def load_paths(abs_path, file):
    """
    loads the paths of the posters from the specified files to the dictionary
    of [concept: [poster_paths]]
    """
    f = open(abs_path + file, "r")

    next(f)  #salta la primera linea
    next(f)  #salta la segunda linea

    lines = f.readlines()
    dict_paths = {}

    for line in lines:
        line = line.strip()
        line = line.replace(", ","," + abs_path + "Posters/")
        words = line.split(",")
        dict_paths[words[0]] = words[1:]
    return dict_paths

def show_posters_concept(concept, paths, screen, font,
                         showed_list,
                         poster_dimensions, poster_time,
                         rectangle_location,):
    images = paths[concept]
    random.shuffle(images)
    """
    loads the images for each concepts, shuffles them and displays the posters
    @concept  the key of the hash of the load_path
    @paths  a dictionary containing the [concept]-> list of paths for Posters
    The rest ar setup values.
    """

    if images =! ['']:
        for image in images:
            if not (image in showed_list):
                showed_list.append(image)
                img = pg.image.load(image)
                img = pg.transform.scale(img, poster_dimensions)
                screen.blit(img, ( 0, 0 ))
                print_concept(concept, screen, font, rectangle_location)
                pg.display.flip()
                time.sleep( poster_time )

def print_concept(concept, screen, font, rectangle_location):
    text = font.render("concepto : " + concept, True,  (255, 255, 255) ,  (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = rectangle_location
    screen.blit(text, textRect)

def print_welcome(message, screen, font):
    text = font.render(message, True,  (255, 255, 255) ,  (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (700, 400)
    screen.blit(text, textRect)

def save_paths(file, dict_paths):
    f = open(file, "w")
    f.write(dict_paths)

def load_users(abs_path, file):
    f = open(file, "r")
    lines = f.readlines()
    paths = {}
    for line in lines:
        line = line.strip()

        line = line.replace(", ",",Posters/")
        words = line.split(",")
        dict_users[words[0]] = words[1:]
    return  {"arturo":["redes neuronales", "python", "estadística"],
            "benjamin":["redes neuronales"]}
    #TODO fun load dict from file
