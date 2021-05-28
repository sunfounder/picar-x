Computer Vision
==========================================

接下来我们正式进入计算机视觉的领域！

为了更好的进行接下来的实验。你需要 :ref:`View RPi Desktop by VNC` ,并且在树莓派的Terminal中运行示例（而非通过SSH远程执行）。


**Code**

.. code-block:: python

    # coding=utf-8
    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera

    #init camera
    camera = PiCamera()
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


**How it works?** 

我们使用了 ``PiCamera`` 来获取照片。This package provides a pure Python interface to the Raspberry Pi camera.

* `PiCamera Docs <https://picamera.readthedocs.io/en/latest/index.html>`_

其最简单的使用方法如下。 Capturing an image to a file is as simple as specifying the name of the file as the output of whatever ``capture()`` method you require.

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')

而在我们的示例中，我们更确切的使用了 **capturing timelapse sequences** 的方法。这是为了使OpenCV能够获取连续的画面。

With this method, the camera captures images continually until you tell it to stop. Images are automatically given unique names and you can easily control the delay between captures.

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    sleep(2)    

    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s' % filename)
        sleep(10) #  capture images with a 10s delay between each shot

In order to capture OpenCV objects, we’ll capture an image to a `BytesIO` stream (Python’s in-memory stream class), then convert the stream to a `numpy` array and read the array with OpenCV:

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

To avoid the JPEG encoding and decoding (which is lossy) and potentially speed up the process, you can now use the classes in the `picamera.array` module. As OpenCV images are simply `numpy` arrays arranged in BGR order, one can use the `PiRGBArray` class and simply capture with the `'bgr'` format (given that RGB and BGR data is the same size and configuration, just with reversed color planes)

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


结合 capturing timelapse sequences 的方法，将 these 3-dimensional RGB arrays show by OpenCV.

.. code-block:: python

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera

    #init camera
    camera = PiCamera()
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

用OpenCV读取视频流还有其他的方法，我们采用这个方法可以较好的适用于接下来的Color detection等任务。
更多玩法请查看 `OpenCV-Python Tutorials <https://docs.opencv.org/4.0.0/d6/d00/tutorial_py_root.html>`_ .


