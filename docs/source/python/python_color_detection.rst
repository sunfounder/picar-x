
.. _py_color_detection:

Farberkennung
==========================================

Dieses Projekt ergänzt das vorherige Projekt :ref:`py_computer_vision` um einen Algorithmus zur Farberkennung.

* :download:`[PDF] Farbkarten <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. note::

    Aufgrund von Unterschieden im Druckertoner oder dem Druckmedium, wie etwa einem beigefarbenen Papier, kann die gedruckte Farbe geringfügig vom Python-Farbmodell abweichen. Dies kann zu einer weniger präzisen Farberkennung führen.

.. image:: img/color_card.png
    :width: 600

**Code ausführen**

.. note::

    * Für dieses Projekt ist ein Zugriff auf den Raspberry Pi-Desktop erforderlich, um das von der Kameramodul aufgenommene Material zu betrachten.
    * Sie können einen Bildschirm an den PiCar-X anschließen oder die Anleitung :ref:`remote_desktop` konsultieren, um per VNC oder XRDP darauf zuzugreifen.
    * Sobald Sie sich im Raspberry Pi-Desktop befinden, öffnen Sie das Terminal und geben den folgenden Befehl ein, um es auszuführen, oder öffnen und führen Sie es mit einem Python-Editor aus.

.. code-block::

    cd ~/picar-x/example
    sudo python3 color_detect.py

Wird der Code ausgeführt und PiCar-X erfasst ein rotes Objekt, wird dieses umrahmt. Sie können das ``'red'``

.. image:: img/color_detect.png

.. **Code**

.. .. code-block:: python
..     :emphasize-lines: 51

..     import cv2
..     from picamera.array import PiRGBArray
..     from picamera import PiCamera
..     import numpy as np
..     import time

..     color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]}  #Here is the range of H in the HSV color space represented by the color

..     kernel_5 = np.ones((5,5),np.uint8) #Define a 5×5 convolution kernel with element values of all 1.

..     def color_detect(img,color_name):

..         # The blue range will be different under different lighting conditions and can be adjusted flexibly.  H: chroma, S: saturation v: lightness
..         resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  # In order to reduce the amount of calculation, the size of the picture is reduced to (160,120)
..         hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # Convert from BGR to HSV
..         color_type = color_name
        
..         mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )           # inRange()：Make the ones between lower/upper white, and the rest black
..         if color_type == 'red':
..                 mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255)) 
..                 mask = cv2.bitwise_or(mask, mask_2)

..         morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)              # Perform an open operation on the image 

..         # Find the contour in morphologyEx_img, and the contours are arranged according to the area from small to large.
..         _tuple = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)      
..         # compatible with opencv3.x and openc4.x
..         if len(_tuple) == 3:
..             _, contours, hierarchy = _tuple
..         else:
..             contours, hierarchy = _tuple
        
..         color_area_num = len(contours) # Count the number of contours

..         if color_area_num > 0: 
..             for i in contours:    # Traverse all contours
..                 x,y,w,h = cv2.boundingRect(i)      # Decompose the contour into the coordinates of the upper left corner and the width and height of the recognition object

..                 # Draw a rectangle on the image (picture, upper left corner coordinate, lower right corner coordinate, color, line width)
..                 if w >= 8 and h >= 8: # Because the picture is reduced to a quarter of the original size, if you want to draw a rectangle on the original picture to circle the target, you have to multiply x, y, w, h by 4.
..                     x = x * 4
..                     y = y * 4 
..                     w = w * 4
..                     h = h * 4
..                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  # Draw a rectangular frame
..                     cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# Add character description

..         return img,mask,morphologyEx_img

..     with PiCamera() as camera:
..         print("start color detect")
..         camera.resolution = (640,480)
..         camera.framerate = 24
..         rawCapture = PiRGBArray(camera, size=camera.resolution)  
..         time.sleep(2)

..         for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
..             img = frame.array
..             img,img_2,img_3 =  color_detect(img,'red')  # Color detection function
..             cv2.imshow("video", img)    # OpenCV image show
..             cv2.imshow("mask", img_2)    # OpenCV image show
..             cv2.imshow("morphologyEx_img", img_3)    # OpenCV image show
..             rawCapture.truncate(0)   # Release cache
        
..             k = cv2.waitKey(1) & 0xFF
..             # 27 is the ESC key, which means that if you press the ESC key to exit
..             if k == 27:
..                 break

..         print('quit ...') 
..         cv2.destroyAllWindows()
..         camera.close()  


.. **Wie funktioniert es?**

.. Zunächst wird der Bereich von H im `HSV-Farbraum <https://de.wikipedia.org/wiki/HSV-Farbraum>`_ als Wörterbuch definiert, was für den folgenden Algorithmus zur Farberkennung praktisch ist:

.. .. code-block:: python

..     color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]} 

.. Anschließend wird ein `Faltungskern <https://de.wikipedia.org/wiki/Faltungskern>`_ der Größe 5x5 definiert, der für morphologische Operationen wie Filterung eingesetzt wird.

.. .. code-block:: python

..     kernel_5 = np.ones((5,5),np.uint8)

.. Als nächstes führt die Funktion ``color_detect()`` die Bildverarbeitung in vier Schritten durch:

.. 1. Extrahiert die Daten der Ziel-Farbe als neues Binärbild (Array).
.. 2. Führt erweiterte morphologische Transformationen durch.
.. 3. Findet Konturen in einem Binärbild.
.. 4. Zeichnet einen Rahmen um das erkannte Objekt im Bild.


.. .. code-block:: python

..     def color_detect(img,color_name):

..         # The blue range will be different under different lighting conditions and can be adjusted flexibly.  H: chroma, S: saturation v: lightness
..         resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  # In order to reduce the amount of calculation, the size of the picture is reduced to (160,120)
..         hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # Convert from BGR to HSV
..         color_type = color_name
        
..         mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )           # inRange()：Make the ones between lower/upper white, and the rest black
..         if color_type == 'red':
..                 mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255)) 
..                 mask = cv2.bitwise_or(mask, mask_2)

..         morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)              # Perform an open operation on the image 

..         # Find the contour in morphologyEx_img, and the contours are arranged according to the area from small to large.
..         _tuple = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)      
..         # compatible with opencv3.x and openc4.x
..         if len(_tuple) == 3:
..             _, contours, hierarchy = _tuple
..         else:
..             contours, hierarchy = _tuple
        
..         color_area_num = len(contours) # Count the number of contours

..         if color_area_num > 0: 
..             for i in contours:    # Traverse all contours
..                 x,y,w,h = cv2.boundingRect(i)      # Decompose the contour into the coordinates of the upper left corner and the width and height of the recognition object

..                 # Draw a rectangle on the image (picture, upper left corner coordinate, lower right corner coordinate, color, line width)
..                 if w >= 8 and h >= 8: # Because the picture is reduced to a quarter of the original size, if you want to draw a rectangle on the original picture to circle the target, you have to multiply x, y, w, h by 4.
..                     x = x * 4
..                     y = y * 4 
..                     w = w * 4
..                     h = h * 4
..                     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  # Draw a rectangular frame
..                     cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# Add character description

..         return img,mask,morphologyEx_img

.. Die ``img``, ``mask`` und ``morphologyEx_img`` werden in drei Fenstern angezeigt, um die Verarbeitungsergebnisse jedes Schritts direkt zu beobachten.

.. .. image:: img/color_detect.png

.. Für weitere Informationen zu Morphologie und Konturerkennung können Sie die folgenden Ressourcen konsultieren:

.. * `Öffnungsoperation – Wikipedia <https://de.wikipedia.org/wiki/%C3%96ffnungsoperation_(Bildverarbeitung)>`_
.. * `morphologyEx - OpenCV <https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f>`_
.. * `findContours - OpenCV <https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0>`_
.. * `Konturmerkmale - OpenCV <https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html>`_
