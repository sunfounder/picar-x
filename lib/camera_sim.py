from os import listdir
from os.path import realpath
import cv2

class Camera(object):
    def __init__(self, config_file) -> None:
        # Grab directory of test images
        self.test_img_dir = '/'.join(realpath(__file__).split('/')[:-2]) + "/test_images/"
        img_names = listdir(self.test_img_dir)
        self.image_dirs = [self.test_img_dir + img_name for img_name in img_names]
        pass

    def set_pan_angle(self, value):
        pass

    def set_tilt_angle(self, value):
        pass

    def control_based_on_camera(self, control_func, display: bool)->None:
        control_break = False
        while not control_break:
            img = cv2.imread(self.image_dirs[3])
            control_break = control_func(img, display)
        return None
