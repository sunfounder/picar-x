颜色检测 - Python
==========================================

该项目将在之前的 :ref:`计算机视觉` 项目中添加颜色检测算法。

* :download:`[PDF]颜色卡 <https://gitee.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. note::

    由于打印机碳粉或打印介质（如棕褐色纸）的差异，打印的颜色可能与 Python 颜色模型的色调略有不同。 这会导致不太准确的颜色识别。

.. image:: img/block/color_card.png
    :width: 600


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 color_detect.py

**代码**

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


**这个怎么运作？**

首先将 `HSV颜色空间 <https://en.wikipedia.org/wiki/HSL_and_HSV>`_ 中H的范围定义为字典，方便后面的颜色判断算法：

.. code-block:: python

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]} 

然后，定义大小为 5x5 的 `卷积核 <https://en.wikipedia.org/wiki/Kernel_(image_processing)>`_ ，将用于形态学操作，如过滤。

.. code-block:: python

    kernel_5 = np.ones((5,5),np.uint8)


接下来， ``color_detect()`` 函数将分四步处理图片：

1. 提取目标颜色的数据作为新的二值图像（数组）。
2. 执行高级形态变换。
3. 在二值图像中寻找轮廓。
4. 在图像上为识别的对象绘制一个框架。

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

``img`` , ``mask`` , ``morphologyEx_img`` 显示在三个窗口中，可以直接观察每一步的处理结果。

.. image:: img/color_detect.png

.. 有关形态学和轮廓绘制的更多信息，请参考以下资源：

.. * `Opening operation - Wikipedia <https://en.wikipedia.org/wiki/Opening_(morphology)>`_ 
.. * `morphologyEx - OpenCV <https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f>`_
.. * `findContours - OpenCV <https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0>`_
.. * `Contour Features - OpenCV <https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html>`_