.. _py_color_detection:

色の検出
==========================================

このプロジェクトでは、前の :ref:`py_computer_vision` プロジェクトに色検出アルゴリズムを追加します。

* :download:`[PDF]カラーカード <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. note::

    印刷された色は、プリンタートナーの違いや印刷材料、例えば茶色の紙などのために、Pythonのカラーモデルと微妙に色合いが異なる場合があります。これにより、色認識の精度が低下する可能性があります。

.. image:: img/color_card.png
    :width: 600

**コードを実行する**

.. note::

    * このプロジェクトは、カメラモジュールで撮影された映像を表示するためにRaspberry Piデスクトップへのアクセスが必要です。
    * PiCar-Xにスクリーンを接続するか、:ref:`remote_desktop` のチュートリアルを参照して、VNCやXRDPを使用してアクセスできます。
    * Raspberry Piデスクトップ内で、ターミナルを開いて以下のコマンドを入力して実行するか、Pythonエディタで開いて実行してください。

.. code-block::

    cd ~/picar-x/example
    sudo python3 color_detect.py

コードを実行すると、PiCar-Xが赤い物体を捉えた場合、それを枠で囲みます。コード内の ``'red'`` を別の色に変更して、その色を検出することもできます。

.. image:: img/color_detect.png

**コード**

.. code-block:: python
    :emphasize-lines: 51

    import cv2
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    import numpy as np
    import time

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]}  #Here is the range of H in the HSV color space represented by the color

    kernel_5 = np.ones((5,5),np.uint8) #Define a 5×5 convolution kernel with element values of all 1.

    def color_detect(img,color_name):

        # The blue range will be different under different lighting conditions and can be adjusted flexibly.  H: chroma, S: saturation v: lightness
        resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  # In order to reduce the amount of calculation, the size of the picture is reduced to (160,120)
        hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # Convert from BGR to HSV
        color_type = color_name
        
        mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )           # inRange()：Make the ones between lower/upper white, and the rest black
        if color_type == 'red':
                mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255)) 
                mask = cv2.bitwise_or(mask, mask_2)

        morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)              # Perform an open operation on the image 

        # Find the contour in morphologyEx_img, and the contours are arranged according to the area from small to large.
        _tuple = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)      
        # compatible with opencv3.x and openc4.x
        if len(_tuple) == 3:
            _, contours, hierarchy = _tuple
        else:
            contours, hierarchy = _tuple
        
        color_area_num = len(contours) # Count the number of contours

        if color_area_num > 0: 
            for i in contours:    # Traverse all contours
                x,y,w,h = cv2.boundingRect(i)      # Decompose the contour into the coordinates of the upper left corner and the width and height of the recognition object

                # Draw a rectangle on the image (picture, upper left corner coordinate, lower right corner coordinate, color, line width)
                if w >= 8 and h >= 8: # Because the picture is reduced to a quarter of the original size, if you want to draw a rectangle on the original picture to circle the target, you have to multiply x, y, w, h by 4.
                    x = x * 4
                    y = y * 4 
                    w = w * 4
                    h = h * 4
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  # Draw a rectangular frame
                    cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# Add character description

        return img,mask,morphologyEx_img

    with PiCamera() as camera:
        print("start color detect")
        camera.resolution = (640,480)
        camera.framerate = 24
        rawCapture = PiRGBArray(camera, size=camera.resolution)  
        time.sleep(2)

        for frame in camera.capture_continuous(rawCapture, format="bgr",use_video_port=True):# use_video_port=True
            img = frame.array
            img,img_2,img_3 =  color_detect(img,'red')  # Color detection function
            cv2.imshow("video", img)    # OpenCV image show
            cv2.imshow("mask", img_2)    # OpenCV image show
            cv2.imshow("morphologyEx_img", img_3)    # OpenCV image show
            rawCapture.truncate(0)   # Release cache
        
            k = cv2.waitKey(1) & 0xFF
            # 27 is the ESC key, which means that if you press the ESC key to exit
            if k == 27:
                break

        print('quit ...') 
        cv2.destroyAllWindows()
        camera.close()  



**どのように動作するか？**

まず、 `HSV色空間 <https://en.wikipedia.org/wiki/HSL_and_HSV>`_ のHの範囲が辞書として定義されており、これは後続の色判定アルゴリズムで便利です：

.. code-block:: python

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]} 

次に、5x5のサイズの `畳み込みカーネル <https://en.wikipedia.org/wiki/Kernel_(image_processing)>`_ が定義され、このカーネルはフィルタリングのような形態学的操作に使用されます。

.. code-block:: python

    kernel_5 = np.ones((5,5),np.uint8)

続いて、 ``color_detect()`` 関数は、画像を以下の4つのステップで処理します：

1. 目的の色のデータを新しい二値画像（配列）として抽出します。
2. 高度な形態学的変換を実行します。
3. 二値画像の輪郭を検出します。
4. 画像上で認識されたオブジェクトのフレームを描きます。

.. code-block:: python

    def color_detect(img,color_name):

        # 藍色の範囲は異なる照明条件下で異なり、柔軟に調整することができる。H：色相、S：彩度、V：明度
        resize_img = cv2.resize(img, (160,120), interpolation=cv2.INTER_LINEAR)  # 計算量を削減するため、画像のサイズを(160,120)に縮小する
        hsv = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)              # BGRからHSVへの変換
        color_type = color_name
        
        mask = cv2.inRange(hsv,np.array([min(color_dict[color_type]), 60, 60]), np.array([max(color_dict[color_type]), 255, 255]) )           # inRange()：下限/上限の間は白に、それ以外は黒にする
        if color_type == 'red':
                mask_2 = cv2.inRange(hsv, (color_dict['red_2'][0],0,0), (color_dict['red_2'][1],255,255)) 
                mask = cv2.bitwise_or(mask, mask_2)

        morphologyEx_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5,iterations=1)              # 画像にオープン操作を実行

        # morphologyEx_imgの輪郭を検出し、輪郭は面積が小さい順に配置される。
        _tuple = cv2.findContours(morphologyEx_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)      
        # opencv3.xとopencv4.xに対応
        if len(_tuple) == 3:
            _, contours, hierarchy = _tuple
        else:
            contours, hierarchy = _tuple
        
        color_area_num = len(contours) # 輪郭の数をカウント

        if color_area_num > 0: 
            for i in contours:    # すべての輪郭を走査
                x,y,w,h = cv2.boundingRect(i)      # 輪郭を認識オブジェクトの左上隅の座標および幅と高さに分解

                # 画像に矩形を描く（画像、左上隅の座標、右下隅の座標、色、線の幅）
                if w >= 8 and h >= 8: # 画像が元のサイズの4分の1に縮小されているため、元の画像に目的を囲む矩形を描く場合、x、y、w、hを4倍にする必要があります。
                    x = x * 4
                    y = y * 4 
                    w = w * 4
                    h = h * 4
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  # 矩形フレームを描く
                    cv2.putText(img,color_type,(x,y), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)# 文字の説明を追加

        return img,mask,morphologyEx_img

``img`` 、 ``mask`` 、および ``morphologyEx_img`` は3つのウィンドウに表示され、各ステップの処理結果を直接観察することができます。

.. image:: img/color_detect.png

形態学と輪郭に関する詳細は、以下のリソースを参照してください：

* `オープニング操作 - Wikipedia <https://en.wikipedia.org/wiki/Opening_(morphology)>`_ 
* `morphologyEx - OpenCV <https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f>`_
* `findContours - OpenCV <https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0>`_
* `輪郭の特性 - OpenCV <https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html>`_
