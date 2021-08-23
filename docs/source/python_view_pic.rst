Computer Vision
==========================================

This next project will officially enter the field of computer vision!

To perform the next four experiments, make sure to have completed the :ref:`Remote Desktop`. A remote connection via SSH will not display the camera images.

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

Photos are obtained with ``PiCamera``. This package provides a pure Python interface to the Raspberry Pi camera.

* `PiCamera Docs <https://picamera.readthedocs.io/en/latest/index.html>`_

Capturing an image to a file only requires specifying the name of the file to the output of whatever ``capture()`` method was required.

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('foo.jpg')

This project uses the **capturing timelapse sequences** method. This method enables OpenCV to acquire sequential frames.


With this method, the camera captures images continually until it is told to stop. Images are automatically given unique names. The ``sleep(x)`` function controls the delay between captures.

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

In order to capture OpenCV objects, an image will be captured to Python’s in-memory stream class: ``BytesIO`` . The BytesIO will convert the stream to a ``numpy`` array, and the program will read the array with OpenCV:

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

To avoid the losses with JPEG encoding and decoding, use the classes in the ``picamera.array`` module. This will also potentially increase the speed of image processing.

As OpenCV images are simply ``numpy`` arrays arranged in BGR order, the ``PiRGBArray`` class, and simply capture with the ``‘bgr’`` format. Note: RGB data and BGR data are the same size and configuration, but have reversed color planes.

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

There are many other ways to read video streams with OpenCV. The ones used in these examples are better suited for the next four PiCar-X tasks, such as :ref:`Color Detection` and :ref:`Face Detection`.

For more ways to use video streams, please reference:  `OpenCV-Python Tutorials <https://docs.opencv.org/4.0.0/d6/d00/tutorial_py_root.html>`_.


