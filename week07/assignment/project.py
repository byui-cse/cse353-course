"""
Course: CSE 353
Lesson Week: 07
File: project.py
Author: <Your name>
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cv2

  
# --------------------------------------------------------------------------
def drawMatches(image_1, image_1_keypoints, image_2, image_2_keypoints, matches):
    """ Draws the matches between the image_1 and image_2.

    Do not edit this function, it is provided for you for visualization purposes.

    Args:
    image_1 (numpy.ndarray): The first image (can be color or grayscale).
    image_1_keypoints (list): The image_1 keypoints, the elements are of type
                              cv2.KeyPoint.
    image_2 (numpy.ndarray): The image to search in (can be color or grayscale)
    image_2_keypoints (list): The image_2 keypoints, the elements are of type
                              cv2.KeyPoint.

    Returns:
    output (numpy.ndarray): An output image that draws lines from the input
                            image to the output image based on where the
                            matching features are.
    """
    # Compute number of channels.
    num_channels = 1
    if len(image_1.shape) == 3:
        num_channels = image_1.shape[2]
    # Separation between images.
    margin = 10
    # Create an array that will fit both images (with a margin of 10 to
    # separate the two images)
    joined_image = np.zeros((max(image_1.shape[0], image_2.shape[0]),
                            image_1.shape[1] + image_2.shape[1] + margin,
                            3), dtype=np.uint8)
    if num_channels == 1:
        for channel_idx in range(3):
            joined_image[:image_1.shape[0],
                         :image_1.shape[1],
                         channel_idx] = image_1
            joined_image[:image_2.shape[0],
                         image_1.shape[1] + margin:,
                         channel_idx] = image_2
    else:
        joined_image[:image_1.shape[0], :image_1.shape[1]] = image_1
        joined_image[:image_2.shape[0], image_1.shape[1] + margin:] = image_2

    for match in matches:
        image_1_point = (int(image_1_keypoints[match.queryIdx].pt[0]),
                         int(image_1_keypoints[match.queryIdx].pt[1]))
        image_2_point = (int(image_2_keypoints[match.trainIdx].pt[0] +
                             image_1.shape[1] + margin),
                         int(image_2_keypoints[match.trainIdx].pt[1]))

        rgb = (int(np.random.rand() * 255), int(np.random.rand() * 255), int(np.random.rand() * 255))
        cv2.circle(joined_image, image_1_point, 5, rgb, thickness = 5)
        cv2.circle(joined_image, image_2_point, 5, rgb, thickness = 5)
        cv2.line(joined_image, image_1_point, image_2_point, rgb, thickness = 3)

    return joined_image


# --------------------------------------------------------------------------
def findMatchesBetweenImages(image_1, image_2, nf=500, sf=1.2, wta=2, st=cv2.ORB_HARRIS_SCORE, ps=31):
    matches = None       # type: list of cv2.DMath
    image_1_kp = None    # type: list of cv2.KeyPoint items
    image_1_desc = None  # type: numpy.ndarray of numpy.uint8 values.
    image_2_kp = None    # type: list of cv2.KeyPoint items.
    image_2_desc = None  # type: numpy.ndarray of numpy.uint8 values.

    orb = cv2.ORB_create(nfeatures=nf, scaleFactor=sf, WTA_K=wta, scoreType=st, patchSize=ps)

    # START ******************************************************

    # WRITE YOUR CODE HERE. Do NOT share code with other students!
    # Sharing code is an automatic zero for the assignment.
    # Read the required reading.

    # END ********************************************************

    # I coded the return statement for you. You are free to modify it -- just
    # make sure the tests pass.
    return image_1_kp, image_2_kp, matches[:10]



# --------------------------------------------------------------------------
def main():
    # TODO Load images
    # TODO Call findMatchesBetweenImages
    # TODO Call drawMatches
    # TODO save resulting image (In order to add to the project document)
    pass



if __name__ == "__main__":
    # execute only if run as a script
    main()
