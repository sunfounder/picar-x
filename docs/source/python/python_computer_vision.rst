.. _py_computer_vision:

コンピュータビジョン
==========================================

次のプロジェクトは正式にコンピュータビジョンの分野に入ります！

次の4つの実験を実行するには、:ref:`remote_desktop` を完了させておくことを確認してください。SSH経由のリモート接続ではカメラの画像は表示されません。

**コードを実行する**

.. note::

    * このプロジェクトはRaspberry Piのデスクトップにアクセスして、カメラモジュールで撮影した映像を表示する必要があります。
    * PiCar-Xにスクリーンを接続するか、:ref:`remote_desktop` のチュートリアルを参照してVNCまたはXRDPでアクセスできます。
    * Raspberry Piのデスクトップ内でターミナルを開き、以下のコマンドを入力して実行するか、Pythonエディターで開いて実行してください。

.. code-block::

    cd ~/picar-x/example
    sudo python3 computer_vision.py

コードを実行すると、デスクトップにウィンドウが表示され、撮影された画像が表示されます。

.. **コード**

.. .. code-block:: python

..     import cv2
..     from picamera.array import PiRGBArray
..     from picamera import PiCamera
..     import time

..     with PiCamera() as camera:
..         camera.resolution = (640, 480)  
..         camera.framerate = 24
..         rawCapture = PiRGBArray(camera, size=camera.resolution)  
..         time.sleep(2)

..         for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True): 
..             img = frame.array
..             cv2.imshow("video", img)  # OpenCVで画像を表示
..             rawCapture.truncate(0)  # キャッシュを解放

..             k = cv2.waitKey(1) & 0xFF
..             if k == 27:
..                 break

..         print('終了 ...') 
..         cv2.destroyAllWindows()
..         camera.close()  

.. **動作の仕組みは？** 

.. ``PiCamera`` を使用して写真を取得します。このパッケージはRaspberry Piカメラへの純粋なPythonインターフェースを提供します。

.. * `PiCamera Docs <https://picamera.readthedocs.io/en/latest/index.html>`_

.. ファイルに画像をキャプチャするには、必要な ``capture()`` メソッドの出力としてファイルの名前を指定するだけです。

.. .. code-block::

..     from time import sleep
..     from picamera import PiCamera

..     with PiCamera() as camera:
..         camera.resolution = (640, 480)
..         camera.start_preview()
..         # カメラのウォームアップ時間
..         sleep(2)
..         camera.capture('foo.jpg')

.. このプロジェクトは **timelapse sequencesのキャプチャ** メソッドを使用しています。このメソッドにより、OpenCVで連続したフレームを取得できます。

.. このメソッドを使用すると、カメラは停止するように指示されるまで画像を連続してキャプチャします。画像には自動的に一意の名前が付けられます。 ``sleep(x)`` 関数はキャプチャ間の遅延を制御します。

.. .. code-block::

..     from time import sleep
..     from picamera import PiCamera

..     with PiCamera() as camera:
..         camera.resolution = (640, 480)
..         camera.start_preview()
..         sleep(2)    

..         for filename in camera.capture_continuous('img{counter:03d}.jpg'):
..             print('Captured %s' % filename)
..             sleep(10) # 10秒の遅延を持たせて画像をキャプチャ

.. OpenCVオブジェクトをキャプチャするには、Pythonのインメモリストリームクラスである ``BytesIO`` に画像をキャプチャします。BytesIOはストリームを ``numpy`` 配列に変換し、プログラムはOpenCVで配列を読み取ります。

.. * `What is Numpy? <https://numpy.org/doc/stable/user/whatisnumpy.html>`_

.. .. code-block:: python

..     import io
..     import time
..     import picamera
..     import cv2
..     import numpy as np

..     # インメモリストリームを作成
..     stream = io.BytesIO()
..     with picamera.PiCamera() as camera:
..         camera.start_preview()
..         time.sleep(2)
..         camera.capture(stream, format='jpeg')
..     # ストリームからnumpy配列を作成
..     data = np.fromstring(stream.getvalue(), dtype=np.uint8)
..     # 配列から画像を"デコード"し、色を保持
..     image = cv2.imdecode(data, 1)
..     # OpenCVはBGR順のデータで配列を返す。RGBが必要な場合は以下を使用
..     image = image[:, :, ::-1]

.. JPEGのエンコードとデコードの損失を避けるために、 ``picamera.array`` モジュール内のクラスを使用します。これにより、画像処理の速度も向上する可能性があります。

.. OpenCVの画像はBGR順の単純な ``numpy`` 配列であるため、 ``PiRGBArray`` クラスと ``‘bgr’`` 形式で簡単にキャプチャできます。注意: RGBデータとBGRデータは同じサイズと構成ですが、色のプレーンが逆転しています。

.. * `PiRGBArray <https://picamera.readthedocs.io/en/release-1.13/api_array.html#pirgbarray>`_

.. .. code-block:: python

..     import time
..     import picamera
..     import picamera.array
..     import cv2

..     with picamera.PiCamera() as camera:
..         camera.start_preview()
..         time.sleep(2)
..         with picamera.array.PiRGBArray(camera) as stream:
..             camera.capture(stream, format='bgr')
..             # この時点で、画像はstream.arrayとして利用可能
..             image = stream.array


.. timelapse sequencesのキャプチャ方法と組み合わせて、これらの3次元RGB配列はOpenCVで表示されます。

.. .. code-block:: python

..     import cv2
..     from picamera.array import PiRGBArray
..     from picamera import PiCamera

..     # カメラ初期化
..     with PiCamera() as camera:
..         camera.resolution = (640,480)
..         camera.framerate = 24
..         rawCapture = PiRGBArray(camera, size=camera.resolution)  

..         for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True): # use_video_port=True
..             img = frame.array
..             cv2.imshow("video", img)  # OpenCVでの画像表示
..             rawCapture.truncate(0)  # キャッシュ解放

..             # ESCキーをクリックして終了
..             k = cv2.waitKey(1) & 0xFF
..             if k == 27:
..                 camera.close()
..                 break

.. OpenCVでビデオストリームを読み取る方法は他にも多くあります。これらの例で使用されている方法は、次の4つのPiCar-Xのタスク、例えば:ref:`py_color_detection` や :ref:`py_face_detection` に適しています。

.. ビデオストリームの使用方法の詳細は、以下を参照してください: `OpenCV-Python Tutorials <https://docs.opencv.org/4.0.0/d6/d00/tutorial_py_root.html>`_。
