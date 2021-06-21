import pygame as pg
import time

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

def show_posters_concept(concept, paths, screen, font):
    images = paths[concept]
    if images:
        for image in images:
            img = pg.image.load(image)
            img = pg.transform.scale(img,( 1920, 1080 ) )
            screen.blit(img, ( 0, 0 ))
            print_concept(concept, screen, font)
            pg.display.flip()
            time.sleep( 1 )

def print_concept(concept, screen, font):
    text = font.render("concepto : " + concept, True,  (255, 255, 255) ,  (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (50, 1045)
    screen.blit(text, textRect)

def print_welcome(message, screen, font):
    text = font.render(message, True,  (255, 255, 255) ,  (0, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (700, 400)
    screen.blit(text, textRect)

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
