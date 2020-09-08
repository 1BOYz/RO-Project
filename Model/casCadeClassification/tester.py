import cv2 as cv
import os


def draw_rectangles(haystack_img, rectangles):
    # define color and type of line
    line_color = (0, 255, 0)
    line_type = cv.LINE_4

    for (x, y, w, h) in rectangles:

        # define the box positions
        top_left = (x, y)
        bottom_right = (x + w, y + h)

        # draw the box
        cv.rectangle(haystack_img, top_left, bottom_right,
                     line_color, lineType=line_type)

    return haystack_img


# load model
cascade_spore = cv.CascadeClassifier('cascade/cascade.xml')
# print(os.listdir("./"))

# load file name
list_file = os.listdir('positive/')
# run test HAAR cascade model with positive pictures
for no_file in range(10):

    # load picture from positive folder
    img = cv.imread('positive/' + list_file[no_file])

    # model detection
    rectangles = cascade_spore.detectMultiScale(img)

    # draw detection result
    detection_image = draw_rectangles(img, rectangles)

    # show picture detection
    cv.imshow('Result', detection_image)
    cv.waitKey()
