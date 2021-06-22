Computer Vision
==========================================

Next we officially enter the field of computer vision!

To better perform the next experiments, you need to complete :ref:`View RPi Desktop by VNC`, and open a terminal to run the projects (not remotely via SSH).


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

We get photos with ``PiCamera``. This package provides a pure Python interface to the Raspberry Pi camera.

* `PiCamera Docs <https://picamera.readthedocs.io/en/latest/index.html>`_

The simplest way to use it is as below. Capturing an image to a file is as simple as specifying the name of the file as the output of whatever ``capture()`` method you require.

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')

In our project, we are more precisely using the **capturing timelapse sequences** method. This is to enable OpenCV to acquire sequential frames.

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

In order to capture OpenCV objects, we'll capture an image to a ``BytesIO`` stream (Python's in-memory stream class), then convert the stream to a ``numpy`` array and read the array with OpenCV:

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

To avoid the JPEG encoding and decoding (which is lossy) and potentially speed up the process, you can now use the classes in the `picamera.array` module.

As OpenCV images are simply `numpy` arrays arranged in BGR order, one can use the `PiRGBArray` class and simply capture with the `'bgr'` format (given that RGB and BGR data is the same size and configuration, just with reversed color planes).


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


Combined with the method of capturing timelapse sequences, these 3-dimensional RGB arrays are shown by OpenCV.

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

There are other ways to read video streams with OpenCV, and the one we use is better suited for the next tasks such as Color detection.

For more ways, please check `OpenCV-Python Tutorials <https://docs.opencv.org/4.0.0/d6/d00/tutorial_py_root.html>`_.


