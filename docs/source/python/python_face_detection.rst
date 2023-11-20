.. _py_face_detection:

Gesichtserkennung
==========================================

Dieses Projekt basiert ebenfalls auf dem :ref:`py_computer_vision` Projekt und wurde um Algorithmen zur Gesichtserkennung erweitert.

.. note::

    Um dieses Projekt auszuführen, müssen Sie zunächst :ref:`remote_desktop` abschließen.


**Code ausführen**


.. note::

    * Dieses Projekt erfordert Zugriff auf den Raspberry Pi Desktop, um das Filmmaterial des Kameramoduls anzuzeigen.
    * Sie können einen Bildschirm an den PiCar-X anschließen oder sich die Anleitung :ref:`remote_desktop` ansehen, um per VNC oder XRDP darauf zuzugreifen.
    * Sobald Sie sich auf dem Raspberry Pi Desktop befinden, öffnen Sie das Terminal und geben den folgenden Befehl ein, um ihn auszuführen, oder öffnen und führen Sie ihn mit einem Python-Editor aus.


.. code-block::

    cd ~/picar-x/example
    sudo python3 human_face_detect.py

Nachdem der Code ausgeführt wurde, wird das Gesicht auf dem Bildschirm überprüft.

.. **Code**

.. .. code-block:: python
..     :emphasize-lines: 33

..     import cv2
..     from picamera.array import PiRGBArray
..     from picamera import PiCamera
..     import time


..     def human_face_detect(img):
..         resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)         # In order to reduce the amount of calculation, resize the image to 320 x 240 size
..         gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)    # Convert to grayscale
..         faces = face_cascade.detectMultiScale(gray, 1.3, 2)    # Detect faces on grayscale images
..         face_num = len(faces)   # Number of detected faces
..         if face_num  > 0:
..             for (x,y,w,h) in faces:
                
..                 x = x*2   # Because the image is reduced to one-half of the original size, the x, y, w, and h must be multiplied by 2.
..                 y = y*2
..                 w = w*2
..                 h = h*2
..                 cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # Draw a rectangle on the face
        
..         return img


..     with PiCamera() as camera:
..         print("start human face detect")
..         camera.resolution = (640,480)
..         camera.framerate = 24
..         rawCapture = PiRGBArray(camera, size=camera.resolution)  
..         time.sleep(2)

..         for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
..             img = frame.array
..             img =  human_face_detect(img) 
..             cv2.imshow("video", img)  #OpenCV image show
..             rawCapture.truncate(0)  # Release cache
        
..             k = cv2.waitKey(1) & 0xFF
..             # 27 is the ESC key, which means that if you press the ESC key to exit
..             if k == 27:
..                 break

..         print('quit ...') 
..         cv2.destroyAllWindows()
..         camera.close() 


.. **Wie funktioniert es?**

.. Im selben Pfad wie dieses Projekt (``picar-x/example/``) legen Sie eine Datei ``haarcascade_frontalhuman face_default.xml`` ab. Diese Datei ist eine in OpenCV trainierte Modell-Datei zur Gesichtserkennung.

.. Diese Datei wird vom **Kaskaden-Klassifikator** von OpenCV aufgerufen.

.. .. code-block:: python

..     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

.. Die Objekterkennung mit Haar-Feature-basierten Kaskadenklassifikatoren ist eine effektive Methode zur Objekterkennung, die 2001 von Paul Viola und Michael Jones in ihrem Artikel "Rapid Object Detection using a Boosted Cascade of Simple Features" vorgestellt wurde.

.. Dies ist ein Ansatz, der auf maschinellem Lernen basiert. Dabei wird eine Kaskadenfunktion aus einer großen Menge positiver und negativer Bilder trainiert und dann zur Erkennung von Objekten in anderen Bildern verwendet.

.. Bei der Arbeit mit Gesichtserkennung wird der Algorithmus zunächst eine große Menge positiver Bilder (Bilder von Gesichtern) und negativer Bilder (Bilder ohne Gesichter) benötigen, um den Klassifikator zu trainieren. Danach müssen die Gesichtsmerkmale extrahiert werden. Hierfür werden Haar-Features verwendet, ähnlich dem Faltungskern. Jedes Feature ist ein einzelner Wert, der durch Subtraktion der Summe der Pixel unter dem weißen Rechteck von der Summe der Pixel unter dem schwarzen Rechteck ermittelt wird.

.. .. image:: img/haar_features.jpg

.. * `Cascade Classifier <https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html>`_
.. * `Cascade Classifier Training <https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html>`_


.. Die Funktion ``human_face_detect()`` verarbeitet Bilder in drei Schritten:

.. 1. Umwandlung des Bildes in Graustufen.
.. 2. Erkennung des menschlichen Gesichts im Graustufenbild, um das Begrenzungsrechteck des erkannten Gesichts zu erhalten.
.. 3. Zeichnung eines Rahmens um das erkannte Objekt im Bild.

.. .. code-block:: python

..     def human_face_detect(img):
..         resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)  # To reduce the amount of calculation, the image size is reduced.
..         gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)    # Convert picture to grayscale.
..         faces = face_cascade.detectMultiScale(gray, 1.3, 2)    # Obtain the bounding rectangle of the detected face.
        
..         face_num = len(faces)   
..         max_area = 0
..         if face_num  > 0:
..             for (x,y,w,h) in faces: # Because the picture is reduced during operation, the increase now go back.
..                 x = x*2   
..                 y = y*2
..                 w = w*2
..                 h = h*2
..                 cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # Draw a frame for the recognized object on the image.
        
..         return img

.. * `detectMultiScale - OpenCV <https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498>`_