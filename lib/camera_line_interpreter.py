# import logging
import logging
import numpy as np
import cv2

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
        # Paramter for cropping
        self.crop_num = 200
        pass

    def build_state(self, img: np.array, display: bool)->float:
        # Positive output indicates line is to the left of robot
        # Negative output indicates line is to the right of robot
        # Output is bounded from [-1,1]

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
        # Transform y coordinates to line up with original image
        line_segments = np.copy(line_segments_h)
        line_segments[:, 0, 1] += self.crop_num
        line_segments[:, 0, 3] += self.crop_num
        # Calculate average line
        avg_line = self.calculate_avg_line(line_segments)
        print("i:",img.shape)
        line_points = self.make_points(frame=img, line=avg_line)


        # Display images at different points
        if display:
            cv2.imshow("Raw Image", img)
            cv2.imshow("HSV Image", hsv_img)
            cv2.imshow("Mask Image", mask)
            cv2.imshow("Edges", edges)
            cv2.imshow("Cropped", cropped)
            # Render line segments onto an image for display
            line_img = np.copy(img)
            for line_seg in line_segments:
                cv2.line(line_img, line_seg[0][0:2], line_seg[0][2:4], (0, 0, 255), 2)
            # print(line_segments[0][0][0:2])
            # print(type(line_segments[0][0][0:2][1]))
            # import sys; sys.exit()
            cv2.line(line_img, line_points[0][0:2], line_points[0][2:4], (0, 255, 0), 5)
            cv2.imshow("Lines", line_img)


            _ = cv2.waitKey(1)

        state = 0
        return state

    def calculate_avg_line(self, line_segments: np.array):
        # Average lines along endpoints
        avg_line_segment = np.average(line_segments, axis=0)
        avg_line_segment = avg_line_segment.astype('int')

        # Unpack line
        x1, y1, x2, y2 = avg_line_segment[0]
        print("Average line segment")
        print(x1, y1, x2, y2)

        # Make average line endpoints align with the overall detected line
        if x1 == x2:
            logging.info("x1 == x2 | Manually generating average line.")
            # avg_line = np.array([[x1, self.crop_num, x2, 640]])
        else:
            logging.info("x1 != x2 | Generating line through polyfit.")
            slope, intercept = np.polyfit((x1, x2), (y1, y2), 1)
            # avg_line = self.make_points(slope, intercept)
        return slope, intercept

    # def make_points(self, slope, intercept):
    #     width, height = self.frame_shape
    #     y1 = height  # bottom of the frame
    #     y2 = self.crop_num  # make points from crop of the frame down
    #     # print(slope, intercept)
    #     # import sys; sys.exit(0)

    #     print("-intercepts", intercept)
    #     print(y1 - intercept)
    #     print(y2 - intercept)

    #     print('/slope', slope)
    #     print((y1-intercept)/slope)
    #     print((y2-intercept)/slope)

    #     # bound the coordinates within the frame
    #     x1 = np.int32((y1 - intercept)/slope)
    #     x2 = np.int32((y2 - intercept)/slope)
    #     # y1 = max(-width, min(2 * width, int((x1 - intercept) / slope)))
    #     # y2 = max(-width, min(2 * width, int((x2 - intercept) / slope)))
    #     print("avg", x1, x2, y1, y2)
    #     # import sys; sys.exit()
    #     return [[x1, y1, x2, y2]]

    def make_points(self, frame, line):
        print(frame.shape)
        height, width, _ = frame.shape
        slope, intercept = line
        y1 = height  # bottom of the frame
        y2 = int(y1 * 1 / 2)  # make points from middle of the frame down

        # bound the coordinates within the frame
        x1 = max(-width, min(2 * width, int((y1 - intercept) / slope)))
        x2 = max(-width, min(2 * width, int((y2 - intercept) / slope)))
        return [[x1, y1, x2, y2]]
