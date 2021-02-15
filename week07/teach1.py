"""
Course: CSE 353
Lesson Week: 07
File: teach1.py
Author: Brother Comeau
"""

import numpy as np 
import cv2

# -----------------------------------------------------------------------------
def template_matching(temp_file, base_file):
    img_rgb = cv2.imread(base_file)
    w, h = img_rgb.shape[:2]
    ratio = w / h

    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(temp_file, 0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    count = 0
    for pt in zip(*loc[::-1]):
        count += 1
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    print('Number of locations found =', count)
    cv2.imwrite('template_matching.png', img_rgb)

    final = cv2.resize(img_rgb, (600, int(600.0 * ratio)))
    cv2.imshow('template matching', final)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


def main():
    """ Main function """
    template_matching('clip-temp.jpg', 'clips.jpg')

if __name__ == '__main__':
    main()
            
