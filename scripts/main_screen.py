import pygame as pg
import time
import sys
import random
import os
import helper_screen as hp

def get_screen_setup():

    if sys.argv[1] == "local":
        abs_path = "/home/ng/Desktop/novus_monsieur/scripts/"
        poster_dimensions = ( 1920, 1080 ) # size of the poster
        rectangle_location = (50, 1045) # position where the concpet shows
        poster_time = 1   # seconds each poster is displayed
        sensors = False
    else :
        abs_path =  "/home/becario/Desktop/novus_monsieur/scripts/"
        poster_dimensions = ( 3840, 2160 )
        rectangle_location = (50, 1045)
        poster_time = 2
        sensors = False

    return (abs_path, poster_dimensions, rectangle_location, poster_time, sensors)



def main():

    os.environ["SDL_VIDEODRIVER"] = "dummy"
    abs_path, poster_dimensions, rectangle_location, poster_time, sensors =  get_screen_setup()

    screen = pg.display.set_mode(( 1920, 1080 ))
    font = pg.font.Font(None, 40)
    done = False

    paths = hp.load_paths(abs_path, "conceptos.txt")

    if sensors:
        users = load_users(abs_path, "users.txt")
    else:
        users = {"Default":paths.keys()}
    while not done:
        if sensors:
            usr = get_user()
            hp.print_welcome(message, screen, font)
        else:
            usr = "Default"

        pg.display.update()
        time.sleep(2)

        showed_list = []
        concepts = list(users[usr])
        random.shuffle(concepts)

        for concept in concepts:
            hp.show_posters_concept(concept, paths, screen, font,
                                    showed_list,
                                    poster_dimensions, poster_time,
                                    rectangle_location)
        print(len(showed_list))
        pg.quit()
        quit()

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
