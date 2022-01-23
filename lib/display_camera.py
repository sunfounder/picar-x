from os.path import realpath
from filedb import fileDB
from camera import Camera

# Config
config_dir = '/'.join(realpath(__file__).split('/')[:-1])
config_file = fileDB(config_dir+'/.config')

cam = Camera(config_file)

for i in range(100):
    img = cam.get_camera_img()
    cam.display(img)
