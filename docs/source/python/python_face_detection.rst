.. _py_face_detection:

Face Detection
==========================================

This project is also based on the :ref:`py_computer_vision` project, with the addition of face detection algorithms.

.. note::

    To run this project, you must first complete :ref:`remote_desktop`.


**Run the Code**


.. note::

    * This project requires access to the Raspberry Pi desktop to view the footage taken by the camera module.
    * You can connect a screen to the PiCar-X or refer to the tutorial :ref:`remote_desktop` to access it with VNC or XRDP.
    * Once inside the Raspberry Pi desktop, open Terminal and type the following command to run it, or just open and run it with a Python editor.


.. code-block::

    cd ~/picar-x/example
    sudo python3 human_face_detect.py

After the code is run, the face will be checked out in the screen.

**Code**

.. code-block:: python
    :emphasize-lines: 33

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time


    def human_face_detect(img):
        resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)         # In order to reduce the amount of calculation, resize the image to 320 x 240 size
        gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)    # Convert to grayscale
        faces = face_cascade.detectMultiScale(gray, 1.3, 2)    # Detect faces on grayscale images
        face_num = len(faces)   # Number of detected faces
        if face_num  > 0:
            for (x,y,w,h) in faces:
                
                x = x*2   # Because the image is reduced to one-half of the original size, the x, y, w, and h must be multiplied by 2.
                y = y*2
                w = w*2
                h = h*2
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # Draw a rectangle on the face
        
        return img


    with PiCamera() as camera:
        print("start human face detect")
        camera.resolution = (640,480)
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
        time.sleep(2)

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
            img = frame.array
            img =  human_face_detect(img) 
            cv2.imshow("video", img)  #OpenCV image show
            rawCapture.truncate(0)  # Release cache
        
            k = cv2.waitKey(1) & 0xFF
            # 27 is the ESC key, which means that if you press the ESC key to exit
            if k == 27:
                break

        print('quit ...') 
        cv2.destroyAllWindows()
        camera.close() 


**How it works?**

In the same path as this project (``picar-x/example/``) , put a file ``haarcascade_frontalhuman face_default.xml``. This file is a face detection model file trained in OpenCV.


This file is called by **Cascade Classifier** of OpenCV.

.. code-block:: python

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001.

This is a machine learning based approach, where a cascade function is trained from a large quantity of positive and negative images, and then used to detect objects in other images. 

When working with face detection, the algorithm will initially need a large quantity of positive images (images of faces) and negative images (images without faces) to train the classifier. From there, the facial features will then need to be extracted. For this, Haar features shown in the below image are used, similar to the convolutional kernel. Each feature is a single value obtained by subtracting the sum of pixels under the white rectangle, from the sum of pixels under the black rectangle.

.. image:: img/haar_features.jpg

* `Cascade Classifier <https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html>`_
* `Cascade Classifier Training <https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html>`_


The ``human_human face_detect()`` function processes pictures in three steps:

1. Convert picture to grayscale.
2. Detect the human face on the grayscale image to obtain the bounding rectangle of the detected face.
3. Draws a frame for the recognized object on the image.

.. code-block:: python

    def human_face_detect(img):
        resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)  # To reduce the amount of calculation, the image size is reduced.
        gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)    # Convert picture to grayscale.
        faces = face_cascade.detectMultiScale(gray, 1.3, 2)    # Obtain the bounding rectangle of the detected face.
        
        face_num = len(faces)   
        max_area = 0
        if face_num  > 0:
            for (x,y,w,h) in faces: # Because the picture is reduced during operation, the increase now go back.
                x = x*2   
                y = y*2
                w = w*2
                h = h*2
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # Draw a frame for the recognized object on the image.
        
        return img

* `detectMultiScale - OpenCV <https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498>`_