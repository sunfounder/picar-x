# import logging
import logging
from typing import Tuple, List
import numpy as np
import cv2
import warnings

# Ignore irrelevant warning from polyfit
warnings.simplefilter('ignore', np.RankWarning)

class CameraLineInterpreter(object):
    def __init__(self) -> None:
        # Set shape of camera frame
        self.frame_shape = (640, 480)
        # Parameters for masking
        self.lower_blue = np.array([60, 40, 40])
        self.upper_blue = np.array([150, 255, 255])
        # Parameters for line detection
        self.rho = 1                        # distance precision in pixels
        self.angular_precision = np.pi/180  # radians
        self.min_threshold = 10             # minimum number of votes
        # Paramter for cropping (how many top pixels to remove height-wise)
        self.crop_num = 280
        pass

    def build_state(self, img: np.array, display: bool)->float:
        # Positive output indicates line is to the left of robot
        # Negative output indicates line is to the right of robot
        # Output is bounded from [-1,1]

        no_line_segments_found = False

        # Change to hsv color space
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # Grab the blue out of the image
        mask = cv2.inRange(hsv_img, self.lower_blue, self.upper_blue)
        # Detect the edges in the image
        edges = cv2.Canny(mask, 200, 400)
        # Crop the image
        cropped = edges[self.crop_num:, :]
        # Detect the line segments
        line_segments_h = cv2.HoughLinesP(cropped, self.rho, self.angular_precision,
            self.min_threshold, np.array([]), minLineLength=8, maxLineGap=4)
        if line_segments_h is None:
            logging.error("No line segments found. Returning 0 for state.")
            no_line_segments_found = True
            state = 0
        else:
            # Transform y coordinates to line up with original image
            line_segments = np.copy(line_segments_h)
            line_segments[:, 0, 1] += self.crop_num
            line_segments[:, 0, 3] += self.crop_num
            # Project line segments so end points are at the ends of the cropped image
            projected_lines = self.project_line_segments(line_segments)
            # Calculate average line from end points
            average_line = np.average(projected_lines, 0).astype('int32')
            # Generate the state based on how far the x value of the top end point
            # of the average line is from the center of the frame
            top_x = average_line[0][2]
            displacement_from_center = top_x - self.frame_shape[0]/2
            # Normalize so output is always bounded [-1,1]
            state = displacement_from_center / (self.frame_shape[0]/2)

        # Display images at different points
        if display:
            cv2.imshow("Raw Image", img)
            cv2.imshow("HSV Image", hsv_img)
            cv2.imshow("Mask Image", mask)
            if not no_line_segments_found:
                cv2.imshow("Edges", edges)
                cv2.imshow("Cropped", cropped)
                # Render line segments onto an image for display
                line_img = np.copy(img)
                for line_seg in line_segments:
                    cv2.line(line_img, line_seg[0][0:2], line_seg[0][2:4], (0, 0, 255), 2)
                cv2.imshow("Lines", line_img)
                # Render projected line segments onto an image for display
                p_line_img = np.copy(img)
                for p_line_seg in projected_lines:
                    cv2.line(p_line_img, p_line_seg[0][0:2], p_line_seg[0][2:4], (0, 0, 255), 1)
                cv2.imshow("Projected Lines", p_line_img)
                # Render final average line onto image for display
                a_line_img = np.copy(img)
                cv2.line(a_line_img, average_line[0][0:2], average_line[0][2:4], (0,255,0), 5)
                cv2.imshow("Final Line", a_line_img)
            # Call waitkey. The program freezes without this call
            _ = cv2.waitKey(1)

        return state

    def project_line_segments(self, line_segments)->List[np.ndarray]:
        endpts_list = []
        for line_segment in line_segments:
            # Grab initial end points
            x1i, y1i, x2i, y2i = line_segment[0]
            # Find slope and intercept of line segment
            slope, intercept = np.polyfit((x1i, x2i), (y1i, y2i), 1)
            # Find the endpoints of the line projected out to the edges of the frame
            x1p, y1p, x2p, y2p = self.make_points(slope, intercept)[0]
            endpts_list.append([[x1p, y1p, x2p, y2p]])
        return endpts_list

        # return [[x1, y1, x2, y2]]

    def average_slope_intercept(self, line_segments):
        # Slope and intercept are with x as a function y
        # AKA: Width as a function of height
        # This keeps the average from diverging from a stable line
        # and makes it possible to keep lines going straight up in the image
        if line_segments is None:
            logging.error('No line_segment segments detected')
            slope, intercept = 0, self.frame_shape[0]/2
            return slope, intercept

        # height, width, _ = frame.shape
        # line_fit = []

        # for line_segment in line_segments[:3]:
        #     for x1, y1, x2, y2 in line_segment:
        #         if x1 == x2:
        #             logging.info('skipping vertical line segment (slope=inf): %s' % line_segment)
        #             continue
        #         slope, intercept = np.polyfit((x1, x2), (y1, y2), 1)
        #         line_fit.append((slope, intercept))

        # fit_average = np.average(line_fit, axis=0)
        # avg_line = self.make_points(frame, fit_average)
        # return avg_line

    def make_points(self, slope, intercept):
        width, height = self.frame_shape
        y1 = height  # bottom of the frame
        y2 = self.crop_num # int(y1 * 1 / 2)  # make points from crop num down

        # bound the coordinates within the frame
        x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
        x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
        return [[x1, y1, x2, y2]]

    def make_points2(self, slope, intercept):
        # Slope and intercept are with x as a function of y
        pass