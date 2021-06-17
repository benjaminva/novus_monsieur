import pygame as pg
import time
import helper_pantallas as help

def main():
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    font = pg.font.Font(None, 40)
    done = False

    """Load dictionary from files:
    paths{keyConcept: [list of posters paths]}
    """
    paths = help.load_paths("conceptos.txt")
    #TODO fun load dict from file
    users = {"arturo":["redes neuronales", "python"], "benjamin":["redes neuronales"]}
    #TODO fun load dict from file

    usr = "arturo" #activado por sensor
    mensaje = "Bienvenido " + usr
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
        text = font.render(mensaje, True,  (255, 255, 255) ,  (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (700, 400)
        screen.blit(text, textRect)
        pg.display.update()
        time.sleep(2)
        for concept in users[usr]:
            images = paths[concept]
            if images:
                for image in images:
                    img = pg.image.load(image)
                    img = pg.transform.scale(img,(1280,720))
                    screen.blit(img, (50, 70))
                    pg.display.flip()
                    time.sleep( 20 )
        pg.quit()
        quit()

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
