.. _py_computer_vision:

Computer Vision
==========================================

Mit diesem nächsten Projekt steigen wir offiziell in den Bereich der Computer Vision ein!

Um die nächsten vier Experimente durchzuführen, stellen Sie sicher, dass Sie die :ref:`remote_desktop` Anleitung abgeschlossen haben. Eine Remote-Verbindung via SSH reicht nicht aus, um die Kamerabilder anzuzeigen.

**Code ausführen**

.. note::

    * Dieses Projekt erfordert Zugang zum Raspberry Pi Desktop, um die Aufnahmen des Kameramoduls zu sehen.
    * Sie können einen Bildschirm an den PiCar-X anschließen oder die Anleitung :ref:`remote_desktop` befolgen, um via VNC oder XRDP darauf zuzugreifen.
    * Nachdem Sie den Raspberry Pi Desktop geöffnet haben, öffnen Sie das Terminal und führen Sie den folgenden Befehl aus oder starten Sie ihn direkt über einen Python-Editor.

.. code-block::

    cd ~/picar-x/example
    sudo python3 computer_vision.py

Nachdem der Code ausgeführt wurde, wird ein Fenster auf Ihrem Desktop geöffnet, in dem die Aufnahme zu sehen ist.

**Code**

.. code-block:: python

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time

    with PiCamera() as camera:
        camera.resolution = (640, 480)  
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
        time.sleep(2)

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):  
            img = frame.array
            cv2.imshow("video", img)  
            rawCapture.truncate(0)  

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        print('quit ...')  
        cv2.destroyAllWindows()
        camera.close()  

**Wie funktioniert das?**

Fotos werden mit ``PiCamera`` gemacht. Dieses Paket stellt eine rein Python-basierte Schnittstelle zur Raspberry Pi Kamera zur Verfügung.

* `PiCamera Dokumentation <https://picamera.readthedocs.io/en/latest/index.html>`_

Das Speichern eines Bildes in einer Datei erfordert nur die Angabe des Dateinamens als Ausgabe für die entsprechende ``capture()`` Methode.

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        sleep(2)
        camera.capture('foo.jpg')

In diesem Projekt wird die Methode zur **Zeitrafferaufnahme** verwendet. Diese Methode ermöglicht es OpenCV, sequenzielle Frames zu erfassen.

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        sleep(2)    

        for filename in camera.capture_continuous('img{counter:03d}.jpg'):
            print('Captured %s' % filename)
            sleep(10)  

Um OpenCV-Objekte zu erfassen, wird ein Bild in Pythons im Speicher liegende Stream-Klasse ``BytesIO`` erfasst. BytesIO wird den Stream in ein ``numpy``-Array umwandeln, und das Programm wird das Array mit OpenCV lesen:

* `Was ist Numpy? <https://numpy.org/doc/stable/user/whatisnumpy.html>`_

.. code-block:: python

    import io
    import time
    import picamera
    import cv2
    import numpy as np

    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data, 1)
    image = image[:, :, ::-1]

Um die Verluste bei JPEG-Kodierung und -Dekodierung zu vermeiden, verwenden Sie die Klassen im ``picamera.array`` Modul. Dadurch könnte auch die Bildverarbeitungsgeschwindigkeit erhöht werden.

Da OpenCV-Bilder einfach ``numpy`` -Arrays sind, die in BGR-Reihenfolge angeordnet sind, wird die Klasse ``PiRGBArray`` verwendet und einfach im ``'bgr'`` -Format erfasst. Hinweis: RGB-Daten und BGR-Daten haben die gleiche Größe und Konfiguration, weisen jedoch umgekehrte Farbebenen auf.

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
            image = stream.array

In Kombination mit der Methode zur Zeitrafferaufnahme werden diese 3-dimensionalen RGB-Arrays von OpenCV angezeigt.

.. code-block:: python

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (640,480)
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):  
            img = frame.array
            cv2.imshow("video", img)  
            rawCapture.truncate(0)  

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                camera.close()
                break

Es gibt viele weitere Möglichkeiten, Videostreams mit OpenCV zu lesen. Die in diesen Beispielen verwendeten sind besonders gut geeignet für die nächsten vier PiCar-X Aufgaben, wie z.B. :ref:`py_color_detection` und :ref:`py_face_detection`.

Für weitere Möglichkeiten zur Verwendung von Videostreams siehe: `OpenCV-Python Tutorials <https://docs.opencv.org/4.0.0/d6/d00/tutorial_py_root.html>`_.

