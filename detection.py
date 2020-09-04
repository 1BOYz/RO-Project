import cv2 as cv
import numpy as np


class Detection:
    detector = None

    def __init__(self, name_object):
        self.detector = cv.CascadeClassifier('xml/' + name_object + '.xml')

    def detect_monster(self, image):
        # model detection
        rectangles = self.detector.detectMultiScale(image)
        return rectangles

    def draw_rectangles(self, image, rectangles):
        # define color and type of line
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:

            # define the box position
            top_left = (x, y)
            bottom_right = (x + w, y + h)

            # draw the box
            cv.rectangle(image, top_left, bottom_right,
                         color=line_color, lineType=line_type)

        return image
