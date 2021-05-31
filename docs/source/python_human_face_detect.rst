Human Face Detect
==========================================

简单的说，这就是在 :ref:`Computer Vision` 的基础上增加了人脸识别的算法。

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

在与该示例的同级目录下，我们放置了一个文件 ``haarcascade_frontalface_default.xml`` ，它是OpenCV中已经经过训练的人脸识别模型文件。

这个文件由 OpenCV 的 Cascade Classifier 调用。

.. code-block:: python

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

基于Haar特征的级联分类器进行对象检测是Paul Viola和Michael Jones在其论文 `Rapid Object Detection using a Boosted Cascade of Simple Features <https://ieeexplore.ieee.org/document/990517>`_ 中于2001年提出的一种有效的对象检测方法。
这是一种基于机器学习的方法，其中从许多正负图像中训练级联函数。然后用于检测其他图像中的对象。
就像卷积核一样， 每个特征都是通过从黑色矩形下的像素总和中减去白色矩形下的像素总和而获得的单个值。

* `Cascade Classifier <https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html>`_
* `Cascade Classifier Training <https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html>`_


接下来让我们注视到 ``human_face_detect()`` ,它将图片进行了三个环节的处理过程：

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