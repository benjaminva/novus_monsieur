import pygame as pg
import time
import helper_screen as hp




def main():
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    font = pg.font.Font(None, 40)
    done = False

    paths = hp.load_paths("conceptos.txt")

    users = {"arturo":["redes neuronales", "python"], "benjamin":["redes neuronales"]}
    #TODO fun load dict from file

    usr = "arturo" #activado por sensor
    message = "Bienvenido " + usr
    print()

    """sort randomly each poster and display a new poster to the student.
       text file with student hashes of seen projects
       while no new event, display all of the posters,
        if listener evernt:  if many users mix the posters 1 and 1.
            greet user
            load corresponding list of posters.
            update user presence in screen.
    """

    """
    Nombre
    2 sec
    Video
    duracion video
    Poster
    60 segundos
    """

    while not done:
        hp.print_welcome(message, screen, font)
        pg.display.update()
        time.sleep(2)
        for concept in users[usr]:
            hp.show_posters_concept(concept, paths, screen)
        pg.quit()
        quit()

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
