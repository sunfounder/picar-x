.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

计算机视觉
==========================================

这个下一个项目将正式进入计算机视觉领域！

要执行接下来的四个实验，请确保已完成远程桌面。 通过 SSH 的远程连接不会显示摄像机图像。


**运行代码**

.. note::

    * 这个项目需要访问树莓派的桌面来查看相机模块拍摄的画面。
    * 你可以将屏幕连接到PiCar-X上，或者参考教程 :ref:`remote_desktop`，用VNC或XRDP访问它。
    * 一旦进入树莓派的桌面，打开Terminal并输入以下命令来运行它，或者直接用Python编辑器打开并运行它。

    
.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 computer_vision.py

代码运行后，你将在窗口上看到摄像头模块拍摄的画面。

**代码**

.. code-block:: python

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time


    with PiCamera() as camera:
        camera.resolution = (640, 480)  
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
        time.sleep(2)

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
            img = frame.array
            cv2.imshow("video", img)  # OpenCV image show
            rawCapture.truncate(0)  # Release cache
            
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        print('quit ...') 
        cv2.destroyAllWindows()
        camera.close()  


**这个怎么运作？**

照片是用 ``PiCamera`` 获得的。 这个包为树莓派相机提供了一个纯 Python 接口。

* `PiCamera Docs <https://picamera.readthedocs.io/en/latest/index.html>`_

将图像捕获到文件只需要将文件名指定为所需的任何 ``capture()`` 方法的输出。

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        camera.capture('foo.jpg')

该项目使用 **capturing timelapse sequences** 函数。这种方法使 OpenCV 能够获取连续帧。

使用这种方法，相机会不断捕捉图像，直到被告知停止。 图像会被自动赋予唯一的名称。 ``sleep(x)`` 函数控制捕获之间的延迟。

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        sleep(2)    

        for filename in camera.capture_continuous('img{counter:03d}.jpg'):
            print('Captured %s' % filename)
            sleep(10) #  capture images with a 10s delay between each shot

为了捕获 OpenCV 对象，图像将被捕获到 Python 的内存流类： ``BytesIO``。 BytesIO 会将流转换为 ``numpy`` 数组，程序将使用 OpenCV 读取该数组：

* `What is Numpy? <https://numpy.org/doc/stable/user/whatisnumpy.html>`_

.. code-block:: python

    import io
    import time
    import picamera
    import cv2
    import numpy as np

    # Create the in-memory stream
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    # Construct a numpy array from the stream
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    # "Decode" the image from the array, preserving colour
    image = cv2.imdecode(data, 1)
    # OpenCV returns an array with data in BGR order. If you want RGB instead
    # use the following...
    image = image[:, :, ::-1]

为了避免 JPEG 编码和解码的损失，请使用 picamera.array 模块中的类。 这也有可能提高图像处理的速度。

由于 OpenCV 图像只是按 BGR 顺序排列的 ``numpy`` 数组， ``PiRGBArray`` 类，并且简单地使用 ``bgr`` 格式捕获。 注：RGB 数据和 BGR 数据大小相同，配置相同，但颜色平面相反。

* `PiRGBArray <https://picamera.readthedocs.io/en/release-1.13/api_array.html#pirgbarray>`_

.. code-block:: python

    import time
    import picamera
    import picamera.array
    import cv2

    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        with picamera.array.PiRGBArray(camera) as stream:
            camera.capture(stream, format='bgr')
            # At this point the image is available as stream.array
            image = stream.array

结合捕捉延时序列的方法，这些3维RGB数组由OpenCV展示。

.. code-block:: python

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera

    #init camera
    with PiCamera() as camera:
        camera.resolution = (640,480)
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
            img = frame.array
            cv2.imshow("video", img)  # OpenCV image show
            rawCapture.truncate(0)  # Release cache

            # click ESC key to exit.
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                camera.close()
                break

还有许多其他方法可以使用 OpenCV 读取视频流。 这些示例中使用的那些更适合接下来的四个 PiCar-X 任务，例如 :ref:`color_dectect_py` 和 :ref:`face_dectect_py`。

更多视频流使用方式请参考： `OpenCV-Python教程 <https://docs.opencv.org/4.0.0/d6/d00/tutorial_py_root.html>`_ 。


