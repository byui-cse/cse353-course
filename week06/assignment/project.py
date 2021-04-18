"""
Course: CSE 353
Author: <Enter You Name>

Instructions:

- Impliment the TODO tasks.

"""
import numpy as np
import cv2
import glob
import os

def write_diff_matrix(diff, start_frame, end_frame):
    """This function normalizes the difference matrices so that they can be shown as images."""
    new_image = (((diff - diff.min()) / (diff.max() - diff.min())) * 255).astype(np.uint8)
    cv2.circle(new_image, (end_frame, start_frame), 2, 255)
    cv2.circle(new_image, (start_frame, start_frame), 2, 255)
    cv2.imwrite('diff-matrix.png', new_image)


def extract_frames(file, subpath, new_size):
    # Only use to extract frames from a video once!!
    # Create a VideoCapture object and read from input file
    # If the input is the camera, pass 0 instead of the video file name
    video = cv2.VideoCapture(file)

    # Check if camera opened successfully
    if (video.isOpened() == False):
        print("Error opening video stream or file")

    dstpath = os.getcwd() + '//' + subpath + '//'

    if not os.path.exists(dstpath):
        os.makedirs(dstpath)

    frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video.get(cv2.CAP_PROP_FPS)
    print(frame_width, frame_height, frame_count, fps, frame_width / frame_height)

    # Read until video is completed
    count = 1
    while (video.isOpened()):

        # Capture frame-by-frame
        ret, frame = video.read()
        if ret == True:
            new_frame = cv2.resize(frame, new_size)
            # cv2.imshow('Frame', new_frame)

            filename = dstpath + f'frame-{str(count).zfill(4)}.png'
            print(filename)

            cv2.imwrite(filename, new_frame)
            count += 1

        # Break the loop
        else:
            break

    # When everything done, release the video capture object
    video.release()

    # Closes all the frames
    cv2.destroyAllWindows()


def load_image_files(subpath):
    path = os.getcwd() + '/' + subpath
    files = [f for f in glob.glob(path + "**/*.png", recursive=False)]
    files.sort()
    return files



def image_compare(image1, image2):
    sum_diff = np.sum(cv2.absdiff(image1, image2))
    return sum_diff



def main():
    """ Main function """

    # Use: extract_frames(file, subpath, new_size) to create frames for your video
    #      Use once for a new video file.
    # Example: extract_frames('loop.mp4', 'loops', (300, int(300 / 1.7777778)))

    files = load_image_files('candle')  # Replace with your video files

    # print(files)
    num_files = len(files)
    print('Number of files =', num_files)

    # TODO - Create 2D numpy array (NxN) to hold image comparison values


    # TODO - Call image_compare for all frames (ie., indexes i and j)
    #        Call the function write_diff_matrix() with that array to
    #        save it to a file.


    # TODO - Find the smallest difference between frames.
    #        You want to select frames that are as far apart as makes sense.


    # TODO - Show the start and end frame of your loop.  Comment out the follow and
    #        adjust the code to save your first and last frame of your longest loop.
	#
    # Here is an example how it could be used.
    # cv2.imshow(f'Start Frame - {start_frame}', image)
    # cv2.imshow(f'End Frame - {end_frame}', image)


    # TODO - Output your loop
    #        a) 4 times of your found loop or until you have at least a 20 second video.
    #        b) must blend between the end and start frames when you loop
    #        c) you will be uploading your final video to DropBox, OneDrive, Youtube, GDrive, etc...
    #           and submitting a link to it.



if __name__ == "__main__":
    # execute only if run as a script
    main()
