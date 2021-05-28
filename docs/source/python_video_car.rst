Video Car
==========================================

现在我们结合 :ref:`Computer Vision` 和 :ref:`Let PiCar-X Move` 来玩耍。

让我们用PiCar-X的第一视角观察世界！用键盘的 O 和 P 调节速度，WSAD调节运动方向。

**code**

.. code-block:: python
    
    import sys
    sys.path.append(r'/home/pi/picar-x/lib')

    from utils import reset_mcu
    reset_mcu()
    from picarx import Picarx
    from utils import run_command
    import datetime

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import numpy as np

    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 24
    camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
    rawCapture = PiRGBArray(camera, size=camera.resolution)  

    power_val = 0
    px = Picarx()

    try:
        while True:
            for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
                img = frame.array
                cv2.imshow("video", img)   
            
                k = cv2.waitKey(1) & 0xFF
                if k == 27:
                    camera.close()
                    continue
                elif k == ord('o'):
                    if power_val <=90:
                        power_val += 10
                        print("power_val:",power_val)  
                elif k == ord('p'):
                    if power_val >=10:
                        power_val -= 10
                        print("power_val:",power_val) 
                elif k == ord('w'):
                    # print("w:",)
                    px.set_dir_servo_angle(0)
                    px.forward(power_val)
                elif k == ord('a'):
                    px.set_dir_servo_angle(-30) 
                    px.forward(power_val)
                elif k == ord('s'):
                    px.set_dir_servo_angle(0) 
                    px.backward(power_val)
                elif k == ord('d'):
                    px.set_dir_servo_angle(30) 
                    px.forward(power_val)
                elif k == ord('f'):    
                    px.stop()  

                elif k == ord('t'):  
                    camera.close()
                    break
                rawCapture.truncate(0)

            print("take a photo wait...")
            picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            picture_path = '/home/pi/Pictures/' + picture_time + '.jpg'

            a_t = "sudo raspistill -t 250  -w 2592 -h 1944 " + " -o " + picture_path

            print(a_t)
            run_command(a_t)

            # Vilib.shuttle_button() 
            camera = PiCamera()
            camera.resolution = (640,480)
            camera.framerate = 24
            camera.image_effect = "none"  #"none","negative","solarize","emboss","posterise","cartoon",
            rawCapture = PiRGBArray(camera, size=camera.resolution)  
    finally:
        px.stop()
        camera.close()


**How it works?** 

这个代码大部分的内容都在 :ref:`Computer Vision` 和 :ref:`Let PiCar-X Move` 中阐述。

你还需要了解以下内容。

.. code-block:: python

    k = cv2.waitKey(1) & 0xFF

``waitKey()`` 是OpenCV等待按键事件的函数。也是HighGUI中唯一可以获取和处理事件的方法。仅当至少创建了一个HighGUI窗口并且该窗口处于活动状态时，该功能才起作用。

* `High-level GUI <https://docs.opencv.org/3.4/d7/dfc/group__highgui.html>`_
* `waitKey - OpenCV <https://docs.opencv.org/3.4/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7>`_

.. code-block:: python

    print("take a photo wait...")
    picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    picture_path = '/home/pi/Pictures/' + picture_time + '.jpg'

    a_t = "sudo raspistill -t 250  -w 2592 -h 1944 " + " -o " + picture_path

    print(a_t)
    run_command(a_t)

这几行代码的效果是在 command line 工具中使用Raspberry Pi相机模块捕获静态照片。
这些代码在主循环外部，只有当OpenCV接收到键盘的 **T** 键被按下时才会跳出循环，执行这些代码。

* `raspistill <https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md>`_