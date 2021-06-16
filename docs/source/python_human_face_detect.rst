Human Face Detect
==========================================

To put it simply, this is to add a human face recognition algorithm based on :ref:`Computer Vision`.

**Code**

.. code-block:: python
    :emphasize-lines: 33

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

    def human_face_detect(img):
        resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)    
        gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY) 
        faces = face_cascade.detectMultiScale(gray, 1.3, 2)   

        face_num = len(faces)  
        max_area = 0
        if face_num  > 0:
            for (x,y,w,h) in faces:
                x = x*2  
                y = y*2
                w = w*2
                h = h*2
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
        
        return img

    #init camera
    print("start human face detect")
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 24
    rawCapture = PiRGBArray(camera, size=camera.resolution)  

    for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): 
        img = frame.array
        img =  human_face_detect(img) 
        cv2.imshow("video", img)  
        rawCapture.truncate(0) 
    
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            camera.close()
            break


**How it works?**

In the same directory as this example, we put a file ``haarcascade_frontalhuman face_default.xml`` , which is a trained human face recognition model file in OpenCV.

This file is called by Cascade Classifier of OpenCV.

.. code-block:: python

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

Haar feature-based cascade classifier is an effective object detection method put forward by Paul Viola and Michael Jones in 2001 in their paper entitled `Rapid Object Detection using a Boosted Cascade of Simple Features <https://ieeexplore.ieee.org/document/990517>`_.
This is a method premised on machine learning, in which cascade functions are trained from numerous positive and negative images, and then used to detect objects in other images.
Just like convolution kernel, each feature is a single value acquired by subtracting the pixel sum under the white rectangle from the pixel sum under the black rectangle. 

* `Cascade Classifier <https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html>`_
* `Cascade Classifier Training <https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html>`_


Next, let's focus on ``human_human face_detect()`` , which processes pictures in three steps:

1. Convert picture to grayscale.
2. Detect the human face on the grayscale image to obtain the bounding rectangle of the detected face.
3. Draw a frame for the recognized object on the image.

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