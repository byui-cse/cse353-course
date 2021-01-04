"""
Course: CS312
File: testfunctions.py
Description: 

    This class is used to test your project.

    DO NOT MODIFY THIS CODE!!
    
    Don't submit this file with your project code
"""

import numpy as np
import cv2
import os
from os import path

class Tests:

    def __init__(self, student_file):
        """ init testing object """
        self.report_size = 70
        print('*' * self.report_size)
        self.student_file = student_file
        self.runs = {}
        self.passed_count = 0
        self.failed_count = 0

        # Delete any test files
        self.removefile('test-border-5.png')
        self.removefile('test-border-20.png')
        self.removefile('test-image2.png')
        self.removefile('test-image2-bw.png')
        self.removefile('test-50.png')
        self.removefile('test-100.png')
        self.removefile('test-124.png')


    def removefile(self, file):
        if (path.exists(file)):
            os.remove(file)


    def finished(self):
        """ End of testing """
        print('-' * self.report_size)
        print(f'Testing student file: {os.path.basename(self.student_file)}')
        print('-' * self.report_size)
        for count, key in enumerate(self.runs):
            print(f'{(count + 1):>2}) {key:<30}: {self.runs[key]}')
        print('*' * self.report_size)
        print(f'Passed: {self.passed_count}, Failed: {self.failed_count}')
        print('*' * self.report_size)


    def failed(self, test, message):
        self.failed_count += 1
        self.runs[test] = 'Failed: ' + message


    def passed(self, test):
        self.passed_count += 1
        self.runs[test] = 'Passed'


    def test1(self, function):
        test = 'Convert Image'
        src = 'src-image1.jpg'
        dst = 'test-image2.png'

        # Remove dst filename from directory
        if (path.exists(dst)):
            os.remove(dst)

        # Read some pixels from the src image
        src_image = cv2.imread(src)
        # print(src_image.shape)

        if (not function(src, dst)):
            self.failed(test, 'False was returned')
            return

        # Check if file exists
        if (not path.exists(dst)):
            self.failed(test, 'dst file does not exist')
            return

        # Load image and verify it's shape is correct
        dst_image = cv2.imread(dst)
        # print(dst_image.shape)

        if (src_image.shape != dst_image.shape):
            self.failed(test, ' dst file different shape')
            return

        for x, y in [(120, 20), (20, 109), (54, 88)]:
            if (not np.array_equal(src_image[x, y], dst_image[x, y])):
                self.failed(test, 'dst image different pixel value')
                return

        self.passed(test)


    def test2(self, function):
        test = 'Convert Image - file exist'
        src = 'tempel.jpg'
        dst = 'test-image-out.png'

        if (function(src, dst)):
            self.failed(test, 'True was returned')
        else:
            self.passed(test)


    def test3(self, function):
        test = 'Convert Image - BW'
        src = 'src-image2.jpg'
        dst = 'test-image2-bw.png'

        # Remove dst filename from directory
        if (path.exists(dst)):
            os.remove(dst)

        # Read some pixels from the src image
        src_image = cv2.imread(src)
        # print(src_image.shape)

        if (not function(src, dst)):
            self.failed(test, 'False was returned')
            return

        # Check if file exists
        if (not path.exists(dst)):
            self.failed(test, 'dst file does not exist')
            return

        # Load image and verify it's shape is correct
        dst_image = cv2.imread(dst)
        # print(dst_image.shape)

        if (src_image.shape != dst_image.shape):
            self.failed(test, ' dst file different shape')
            return

        for x, y in [(120, 20), (20, 109), (54, 88)]:
            if (not np.array_equal(src_image[x, y], dst_image[x, y])):
                self.failed(test, 'dst image different pixel value')
                return

        self.passed(test)


    def test4(self, function, scale):
        test = f'Scale - {scale}'
        src = 'src-image1.jpg'
        dst = f'test-{int(scale)}.png'

        # Remove dst filename from directory
        if (path.exists(dst)):
            os.remove(dst)

        # Read some pixels from the src image
        src_image = cv2.imread(src)
        if (src_image is None):
            self.failed(test, 'None was returned')
            return

        src_shape = src_image.shape
        # print(src_image.shape)

        if (not function(src, dst, scale)):
            self.failed(test, 'False was returned')
            return

        # Check if file exists
        if (not path.exists(dst)):
            self.failed(test, 'Dst file does not exist')
            return

        # Load image and verify it's shape is correct
        dst_image = cv2.imread(dst)
        dst_shape = dst_image.shape
        # print(dst_image.shape)

        dst_shape_scale = []
        dst_shape_scale.append(int(src_shape[0] * scale / 100))
        dst_shape_scale.append(int(src_shape[1] * scale / 100))
        dst_shape_scale.append(int(src_shape[2]))

        # print('dst_shape_scale =', dst_shape_scale)

        for i in range(3):
            if (dst_shape_scale[i] != dst_shape[i]):
                self.failed(test, 'dst image wrong size')
                return                

        self.passed(test)



    def test5(self, function, width, color):
        test = f'Border - {width}'
        src = 'src-image1.jpg'
        dst = f'test-border-{int(width)}.png'

        # Remove dst filename from directory
        if (path.exists(dst)):
            os.remove(dst)

        # Read some pixels from the src image
        src_image = cv2.imread(src)
        if (src_image is None):
            self.failed(test, 'None was returned')
            return

        src_shape = src_image.shape 
        # print(src_image.shape)

        src_pixel1 = src_image[0, 0]
        src_pixel2 = src_image[src_shape[0] - 1, src_shape[1] - 1]

        if (not function(src, dst, width, color)):
            self.failed(test, 'False was returned')
            return

        # Check if file exists
        if (not path.exists(dst)):
            self.failed(test, 'Dst file does not exist')
            return

        # Load image and verify it's shape is correct
        dst_image = cv2.imread(dst)
        dst_shape = dst_image.shape
        # print(dst_image.shape)

        dst_shape_scale = []
        dst_shape_scale.append(int(src_shape[0] + width * 2))
        dst_shape_scale.append(int(src_shape[1] + width * 2))
        dst_shape_scale.append(int(src_shape[2]))

        # print('dst_shape_scale =', dst_shape_scale)

        for i in range(3):
            if (dst_shape_scale[i] != dst_shape[i]):
                self.failed(test, 'dst image wrong size')
                return                

        # Test pixel colors
        dst_pixel1 = dst_image[0, 0]
        dst_pixel2 = dst_image[dst_shape[0] - 1, dst_shape[1] - 1]

        if ((dst_pixel1[0] != color[0]) or (dst_pixel1[1] != color[1]) or (dst_pixel1[2] != color[2])):
            self.failed(test, 'dst pixel is wrong')
            return                

        if ((dst_pixel2[0] != color[0]) or (dst_pixel2[1] != color[1]) or (dst_pixel2[2] != color[2])):
            self.failed(test, 'dst pixel is wrong')
            return                

        dst_pixel3 = dst_image[width, width]
        dst_pixel4 = dst_image[dst_shape[0] - width - 1, dst_shape[1] - width - 1]

        if (not np.array_equal(src_pixel1, dst_pixel3)):
            self.failed(test, 'dst image different pixel value')
            return

        if (not np.array_equal(src_pixel2, dst_pixel4)):
            self.failed(test, 'dst image different pixel value')
            return


        self.passed(test)

