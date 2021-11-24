视频车
==========================================

该程序将提供帕克的第一人称视角！ 使用键盘 WSAD 键控制移动方向，使用 O 和 P 调整速度。

**代码**

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


**这个怎么运作？**

大部分代码在 :ref:`计算机视觉` 和 :ref:`让帕克动起来` 中进行了描述。在这基础上，添加了 OpenCV ``waitKey()`` 函数。


.. code-block:: python

    k = cv2.waitKey(1) & 0xFF

``waitKey()`` 是一个等待按键事件的函数，也是HighGUI中唯一获取和处理事件的方法。 此功能仅在至少一个 HighGUI 窗口已创建并处于活动状态时有效。

* `High-level GUI <https://docs.opencv.org/3.4/d7/dfc/group__highgui.html>`_
* `waitKey - OpenCV <https://docs.opencv.org/3.4/d7/dfc/group__highgui.html#ga5628525ad33f52eab17feebcfba38bd7>`_

.. code-block:: python

    print("take a photo wait...")
    picture_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    picture_path = '/home/pi/Pictures/' + picture_time + '.jpg'

    a_t = "sudo raspistill -t 250  -w 2592 -h 1944 " + " -o " + picture_path

    print(a_t)
    run_command(a_t)

这些代码行的目的是使用树莓派相机模块捕捉静态照片。

这些代码在主循环的外部，当 OpenCV 收到键盘上的 **T** 键时会执行它们，这会中断主循环。

* `raspistill <https://www.raspberrypi.org/documentation/usage/camera/raspicam/raspistill.md>`_