.. _py_face_detection:

顔検出
==========================================

このプロジェクトも :ref:`py_computer_vision` プロジェクトに基づいており、顔検出アルゴリズムが追加されています。

.. note::

    To run this project, you must first complete :ref:`remote_desktop`.


**コードの実行**


.. note::

    * このプロジェクトでは、カメラ モジュールで撮影した映像を表示するためにRaspberry Piデスクトップにアクセスする必要があります。
    * モニター（またはTV）をPiCar-Xに接続するか、 :ref:`remote_desktop` を参照して VNC または XRDP でアクセスできます。
    * Raspberry Piのデスクトップに入ったらターミナルを開き次のコマンドを入力して実行するか、Pythonエディターで開いて実行します。


.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 human_face_detect.py

コードが実行されると顔が見つかると画面に顔の枠が表示されます。

**コード**

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


**どんな動きをするの？**

このプロジェクトと同じパス (``picar-x/example/``) に、ファイル ``haarcascade_frontalhuman face_default.xml`` を置きます。 このファイルはOpenCVでトレーニングされた顔検出モデル・ファイルです。


このファイルはOpenCVの **Cascade Classifier** によって呼び出されます。

.. code-block:: python

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

Haar 特徴ベースのカスケード分類器を使用したオブジェクト検出は、Paul Viola と Michael Jones が 2001 年の論文「単純な特徴のブースト カスケードを使用した迅速なオブジェクト検出」で提案した効果的なオブジェクト検出方法です。

これは機械学習ベースのアプローチであり、カスケード関数が大量の正しい画像と誤りの画像からトレーニングされ、他の画像内のオブジェクトを検出するために使用されます。

顔検出を使用する場合、アルゴリズムは最初に分類子をトレーニングするために大量の正しいイメージ (顔のイメージ) と誤ったイメージ (顔のないイメージ) を必要とします。 そこから顔の特徴を抽出する必要があります。 このために畳み込みカーネルと同様に、下の画像に示す Haar 機能が使用されます。 各特徴は黒い四角形の下のピクセルの合計から白い四角形の下のピクセルの合計を減算することによって得られる単一の値です。

.. image:: img/haar_features.jpg

* `Cascade Classifier <https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html>`_
* `Cascade Classifier Training <https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html>`_


``human_human face_detect()`` 関数は 3 つのステップで画像を処理します:

1. 画像をグレースケールに変換します。
2. グレースケール イメージで人間の顔を検出し、検出された顔の外接する四角形を取得します。
3. 画像上に認識されたオブジェクトのフレームを描画します。

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