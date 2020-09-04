import numpy as np
import cv2 as cv
import time
from PIL import ImageGrab
from detection import Detection


class Vision:

    def __init__(self, name_viewer):
        self.viewer = name_viewer
        self.detector_viewer = Detection(name_viewer)

    def view_screen(self, main_queue):
        # capture screen for detect monster and return position of monster
        image = np.array(ImageGrab.grab())
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        # model detection
        rectangles = self.detector_viewer.detect_monster(image)

        # draw detection result
        detection_image = self.detector_viewer.draw_rectangles(
            image, rectangles)

        # show picture detection
        # cv.imshow('Result', detection_image)
        # cv.waitKey()

        # put position of monster to queue
        if rectangles == ():
            print('Not found monsters')
        else:
            print('Have monsters')
            list_detect = {}
            list_detect['type'] = 'monster'
            list_detect['rectangles'] = rectangles
            main_queue.put(list_detect)
