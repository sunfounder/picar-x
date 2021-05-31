Color Detect
==========================================

简单的说，这就是在 :ref:`Computer Vision` 的基础上增加了颜色识别的算法。


**Code**

.. code-block:: python
    :emphasize-lines: 51

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import numpy as np

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]}  

    kernel_5 = np.ones((5,5),np.uint8) 

    def color_detect(img,color_name):

        resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  
        hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)             

        color_type = color_name
        
        mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )        
        if color_type == 'red':
                mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255)) 
                mask = cv2.bitwise_or(mask, mask_2)

        morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)            

        contours, hierarchy = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)    

        color_area_num = len(contours) 

        if color_area_num > 0: 
            for i in contours:   
                x,y,w,h = cv2.boundingRect(i)      

                if w >= 8 and h >= 8: 
                    x = x * 4
                    y = y * 4 
                    w = w * 4
                    h = h * 4
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  
                    cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)

        return img,mask,morphologyEx_img

    #init camera
    print("start color detect")
    camera = PiCamera()
    camera.resolution = (640,480)
    camera.framerate = 24
    rawCapture = PiRGBArray(camera, size=camera.resolution)  

    for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):
        img = frame.array
        img,img_2,img_3 =  color_detect(img,'red')  
        cv2.imshow("video", img)    
        cv2.imshow("mask", img_2)   
        cv2.imshow("morphologyEx_img", img_3)   
        rawCapture.truncate(0)  
    
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            camera.close()
            break


**How it works?**

首先，我们将 `HSV颜色空间 <https://en.wikipedia.org/wiki/HSL_and_HSV>`_ 中的H的范围定义为一个字典，以便于接下来的色彩判断算法。

.. code-block:: python

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]} 

然后，定义了一个大小为5x5的 `convolution kernel <https://en.wikipedia.org/wiki/Kernel_(image_processing)>`_ ,我们将把它用于形态学运算（滤波）。

.. code-block:: python

    kernel_5 = np.ones((5,5),np.uint8)


接下来让我们注视到 ``color_detect()`` ,它将图片进行了四个环节的处理过程：

1. Extract the data of the target color as a new binary image (array).
2. Performs advanced morphological transformations. 
3. Finds contours in a binary image.
4. Draw a frame for the recognized object on the image.

.. code-block:: python

    def color_detect(img,color_name):

        resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  # To reduce the amount of calculation, the image size is reduced.
        hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)  # Convert color from BGR to HSV

        color_type = color_name

        ### Extract the data of the target color as a new binary image (array).
        mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )  
        if color_type == 'red':     
                mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255)) 
                mask = cv2.bitwise_or(mask, mask_2)   # In HSV, red is divided into two sections, which need to be combined.

        ### Performs advanced morphological transformations        
        morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)   # Perform open operation      

        ### Finds contours in a binary image.
        contours, hierarchy = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
        color_area_num = len(contours) # Count the number of contours

        if color_area_num > 0: 
            for i in contours:   
                x,y,w,h = cv2.boundingRect(i) # Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height.

                ### Draw a frame for the recognized object on the image
                if w >= 8 and h >= 8: # Because the picture is reduced during operation, the increase now go back
                    x = x * 4
                    y = y * 4 
                    w = w * 4
                    h = h * 4
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  # Draw a frame
                    cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2) # Add description

        return img,mask,morphologyEx_img

我们将 ``img`` , ``mask`` , ``morphologyEx_img`` 用三个窗口显示出来，以直接观察各个环节的处理结果。

.. image:: img/color_detect.png

* `Opening operation - Wikipedia <https://en.wikipedia.org/wiki/Opening_(morphology)>`_ 
* `morphologyEx - OpenCV <https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f>`_
* `findContours - OpenCV <https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0>`_
* `Contour Features - OpenCV <https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html>`_