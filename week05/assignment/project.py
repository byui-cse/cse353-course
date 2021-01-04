"""
Course: CSS 353
File: project05.py
Description: 

    Using OpenCV to constuct video transitions

    - Both videos "snow.mp4" and "beach.mp4" are the same length and size.
      Download the videos with the link below.

	https://webmailbyui-my.sharepoint.com/:f:/g/personal/comeaul_byui_edu/EpbA6x-qesxCgYuh6IaHrxMB8PTFdEIvqqnvI69eTeM6iQ?e=fPG2QE

    - Create 3 different videos with a transition.  A transition will transition between
      each video - moving from one video to the other in the final video you create.
    - The new video will consist of a transtion from one video to the other for the full length of the video.
    - The transitions must be different in a meaningful way.
    - No random transitions.
    - You can only use OpenCV, Numpy, os packages (Scipy too, but you don't need it)

    Read the requirements for the project in Canvas
"""

import numpy as np
import cv2
import os
from os import path


def transition1(src_video1, src_video2, dst_file_name):
    """ Create a new video with a transition and save that video to 'dst_file_name' """
    # TODO - Add your code here
    pass



def transition2(src_video1, src_video2, dst_file_name):
    """ Create a new video with a transition and save that video to 'dst_file_name' """
    # TODO - Add your code here
    pass



def transition3(src_video1, src_video2, dst_file_name):
    """ Create a new video with a transition and save that video to 'dst_file_name' """
    # TODO - Add your code here
    pass



def play_video(filename):
    """ Displays a video to the screen - Don't change this code """
    if (not path.exists(filename)):
        print(f"The video file: {filename} doesn't exist")
        return
    
    video = cv2.VideoCapture(filename)

    # Check if camera opened successfully
    if (video.isOpened() == False):
        print(f"Error opening video stream or file: {filename}")
        return

    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video.get(cv2.CAP_PROP_FPS))

    # Read until video is completed
    video_title = f'Video {filename}, {frame_width}x{frame_height}, fps = {fps}'
    while (video.isOpened()):
        ret, frame = video.read()
        if ret == True:
            # Display the resulting frame
            cv2.imshow(video_title, frame)
            cv2.waitKey(1000 // fps)
        else:
            break

    # When everything done, release the video capture object
    video.release()

    # Closes all the frames
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def main():
    """ Main function """

    # Clean up
    if os.path.exists("new-video1.mp4"):
        os.remove("new-video1.mp4")

    if os.path.exists("new-video2.mp4"):
        os.remove("new-video2.mp4")

    if os.path.exists("new-video3.mp4"):
        os.remove("new-video3.mp4")

    # Video files
    src_file1 = 'snow.mp4'
    src_file2 = 'beach.mp4'

    # Transition functions
    transition1(src_file1, src_file2, 'new-video1.mp4')
    play_video('new-video1.mp4')

    transition2(src_file1, src_file2, 'new-video2.mp4')
    play_video('new-video2.mp4')

    transition3(src_file1, src_file2, 'new-video3.mp4')
    play_video('new-video3.mp4')



if __name__ == "__main__":
    # execute only if run as a script
    main()
