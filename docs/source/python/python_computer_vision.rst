.. _py_computer_vision:

画像解析
==========================================

この次のプロジェクトは画像解析（コンピュータ ビジョン）の分野に正式に参入します。

次の4つの実験を実行するには :ref:`remote_desktop` の設定が完了していることを確認してください。 SSH経由のリモート接続ではカメラの画像は表示できません。


**コードの実行**

.. note::

    * このプロジェクトではカメラで撮影した映像を表示するためにRaspberry Piのデスクトップにアクセスする必要があります。
    * モニターをPiCar-Xに直接接続するかチュートリアル :ref:`remote_desktop` を参照してVNCまたはXRDPでアクセスできます。
    * Raspberry Piのデスクトップに入ったらターミナルを開き次のコマンドを入力して実行するか、Pythonエディターで開いて実行します。

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 computer_vision.py

コードが実行されるとデスクトップにウィンドウが開きカメラが捉えた映像が表示されます。

**コード**

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

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
            img = frame.array
            cv2.imshow("video", img)  # OpenCV image show
            rawCapture.truncate(0)  # Release cache
            
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        print('quit ...') 
        cv2.destroyAllWindows()
        camera.close()  


**どんな動きをするの？** 

写真は ``PiCamera`` で取得します。 このパッケージはRaspberry PiのカメラへのPythonインターフェイスを提供します。

* `PiCameraの説明 <https://picamera.readthedocs.io/en/latest/index.html>`_

画像をファイルにキャプチャするには、必要な ``capture()`` メソッドの出力にファイルの名前を指定するだけです。

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        # Camera warm-up time
        sleep(2)
        camera.capture('foo.jpg')

このプロジェクトでは **capturing timelapse sequences** メソッドを使用します。 このメソッドによりOpenCVは連続フレームを取得できます。


このメソッドではカメラは停止するように指示されるまで連続して画像を取得し続けています。 画像には自動的に一意の名前が付けられます。 ``sleep(x)`` 関数はキャプチャ間の遅延を制御します。

.. code-block:: python

    from time import sleep
    from picamera import PiCamera

    with PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        sleep(2)    

        for filename in camera.capture_continuous('img{counter:03d}.jpg'):
            print('Captured %s' % filename)
            sleep(10) #  capture images with a 10s delay between each shot

OpenCV オブジェクトをキャプチャするために画像は Python のメモリ内ストリーム クラス ``BytesIO`` にキャプチャされます。 BytesIOはストリームを ``numpy`` 配列に変換し、プログラムはOpenCVで配列を読み取ります。

* `Numpyとは? <https://numpy.org/doc/stable/user/whatisnumpy.html>`_

.. code-block:: python

    import io
    import time
    import picamera
    import cv2
    import numpy as np

    # Create the in-memory stream
    stream = io.BytesIO()
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')
    # Construct a numpy array from the stream
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    # "Decode" the image from the array, preserving colour
    image = cv2.imdecode(data, 1)
    # OpenCV returns an array with data in BGR order. If you want RGB instead
    # use the following...
    image = image[:, :, ::-1]

JPEG のエンコードとデコードによる損失を回避するには ``picamera.array`` モジュールのクラスを使用します。 これにより、画像処理の速度も向上する可能性があります。

OpenCV 画像は単純に``numpy`` 配列をBGR順に並べたものなので ``PiRGBArray`` クラスを単純に``‘bgr’`` f形式でキャプチャします。 注: RGB データと BGR データは同じサイズと構成ですが、カラー プレーンが逆になっています。

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
            # At this point the image is available as stream.array
            image = stream.array


タイムラプス・シーケンスをキャプチャする方法と組み合わせて、これらの3次元RGB配列をOpenCVで表示します。

.. code-block:: python

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera

    #init camera
    with PiCamera() as camera:
        camera.resolution = (640,480)
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): # use_video_port=True
            img = frame.array
            cv2.imshow("video", img)  # OpenCV image show
            rawCapture.truncate(0)  # Release cache

            # click ESC key to exit.
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                camera.close()
                break

OpenCVでビデオ ストリームを読み取る方法は他にもたくさんあります。 これらの例で使用されているものは、次の 4 つの PiCar-X タスク (:ref:`py_color_detection` や :ref:`py_face_detection` など) により適しています。

ビデオ ストリームを使用するその他の方法については `OpenCV-Python Tutorials <https://docs.opencv.org/4.0.0/d6/d00/tutorial_py_root.html>`_ を参照してください。


