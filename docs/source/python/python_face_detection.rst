

.. _py_face_detection:

顔検出
==========================================

このプロジェクトは、:ref:`py_computer_vision` プロジェクトをベースに、顔検出アルゴリズムが追加されています。

.. note::

    このプロジェクトを実行するには、まず :ref:`remote_desktop` を完了する必要があります。


**コードの実行**


.. note::

    * このプロジェクトはRaspberry Piのデスクトップにアクセスして、カメラモジュールで撮影された映像を表示する必要があります。
    * PiCar-Xに画面を接続するか、:ref:`remote_desktop` のチュートリアルを参照してVNCやXRDPでアクセスできます。
    * Raspberry Piのデスクトップ内でターミナルを開き、次のコマンドを入力して実行するか、Pythonエディタで開いて実行します。


.. code-block::

    cd ~/picar-x/example
    sudo python3 human_face_detect.py

コードを実行すると、画面上で顔がチェックされます。

**コード**

.. code-block:: python
    :emphasize-lines: 33

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import time

    def human_face_detect(img):
        resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)         # 計算量を減少させるため、画像のサイズを320 x 240にリサイズ
        gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)    # グレースケールに変換
        faces = face_cascade.detectMultiScale(gray, 1.3, 2)    # グレースケールの画像で顔を検出
        face_num = len(faces)   # 検出された顔の数
        if face_num  > 0:
            for (x,y,w,h) in faces:

                x = x*2   # 画像がオリジナルのサイズの半分に縮小されているため、x、y、w、hを2倍にする必要があります。
                y = y*2
                w = w*2
                h = h*2
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 顔の上に矩形を描く

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
            cv2.imshow("video", img)  #OpenCVでの画像表示
            rawCapture.truncate(0)  # キャッシュのリリース

            k = cv2.waitKey(1) & 0xFF
            # 27はESCキーを意味し、ESCキーを押すと終了する
            if k == 27:
                break

        print('quit ...') 
        cv2.destroyAllWindows()
        camera.close() 

**動作方法**

このプロジェクトと同じパス( ``picar-x/example/`` )に ``haarcascade_frontalhuman face_default.xml`` というファイルを置きます。このファイルはOpenCVでトレーニングされた顔検出モデルのファイルです。

このファイルはOpenCVの **Cascade Classifier** で呼び出されます。

.. code-block:: python

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  

Haar特徴ベースのカスケード分類器を使用した物体検出は、2001年にPaul ViolaとMichael Jonesが「Rapid Object Detection using a Boosted Cascade of Simple Features」という論文で提案した効果的な物体検出方法です。

これは機械学習ベースのアプローチであり、カスケード関数は多くの正の画像と負の画像からトレーニングされ、他の画像で物体を検出するために使用されます。

顔検出を行う際、アルゴリズムはまず、正の画像（顔の画像）と負の画像（顔のない画像）の多量のデータが必要です。そこから、顔の特徴を抽出する必要があります。このため、以下の画像に示されているHaar特徴が使用されます。これは畳み込みカーネルに似ています。各特徴は、白い長方形の下のピクセルの合計を、黒い長方形の下のピクセルの合計から引いた単一の値です。

.. image:: img/haar_features.jpg

* `Cascade Classifier <https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html>`_
* `Cascade Classifier Training <https://docs.opencv.org/3.4/dc/d88/tutorial_traincascade.html>`_

``human_human face_detect()`` 関数は、3つのステップで画像を処理します：

1. 画像をグレースケールに変換。
2. グレースケールの画像で人の顔を検出し、検出された顔の境界矩形を取得。
3. 画像上で認識されたオブジェクトのための枠を描画。

.. code-block:: python

    def human_face_detect(img):
        resize_img = cv2.resize(img, (320,240), interpolation=cv2.INTER_LINEAR)  # 計算量を減少させるため、画像のサイズは減少されます。
        gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)    # 画像をグレースケールに変換。
        faces = face_cascade.detectMultiScale(gray, 1.3, 2)    # 検出された顔の境界矩形を取得。

        face_num = len(faces)   
        max_area = 0
        if face_num  > 0:
            for (x,y,w,h) in faces: # 処理中に画像が縮小されるため、増加は今戻ってきます。
                x = x*2   
                y = y*2
                w = w*2
                h = h*2
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 画像上で認識されたオブジェクトのための枠を描画。
        
        return img

* `detectMultiScale - OpenCV <https://docs.opencv.org/3.4/d1/de5/classcv_1_1CascadeClassifier.html#aaf8181cb63968136476ec4204ffca498>`_
