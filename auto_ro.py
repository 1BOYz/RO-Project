import queue
import time
import cv2 as cv
import keyboard
import autoit
from vision import Vision
from threading import Thread

view_spore = Vision('spore')


def vision(main_queue):
    view_spore.view_screen(main_queue)


def program_start():
    global main_queue
    main_queue = queue.Queue()

    while(True):
        vision(main_queue)
        if main_queue.qsize() > 0:
            print('In queue have' + str(main_queue.qsize()))
            element = main_queue.get()
            print(element['rectangles'])
            if element['type'] == 'monster':
                print('monster found on ' +
                      str(element['rectangles'][0][0] + int(element['rectangles'][0][2] / 2)) + ',' + str(element['rectangles'][0][1] + int(element['rectangles'][0][3] / 2)))
                autoit.mouse_click("left",
                                   element['rectangles'][0][0] + int(element['rectangles'][0][2] / 2), element['rectangles'][0][1] + int(element['rectangles'][0][3] / 2), 1)
                time.sleep(4)
        else:
            time.sleep(1)

        if keyboard.is_pressed('Esc'):
            print("\nyou pressed Esc, so exiting...")
            break


if __name__ == '__main__':
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)
    program_start()
