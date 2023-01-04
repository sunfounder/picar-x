.. _py_color_detection:

色検出
==========================================

このプロジェクトは、以前の :ref:`py_computer_vision` プロジェクトに色検出アルゴリズムを追加します。



* :download:`[PDF]Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. note::

     印刷された色は、プリンターのトナーの違い、または印刷用紙のわずかな色の違いなどによって、Ezblock カラー モデルとはわずかに異なる色合いになる場合があります。 これにより、色認識の精度が低下する可能性があります。


.. image:: img/color_card.png
    :width: 600


**コードの実行**


.. note::

    * このプロジェクトでは、カメラ モジュールで撮影した映像を表示するためにRaspberry Piデスクトップにアクセスする必要があります。
    * モニター（またはTV）をPiCar-Xに接続するか、 :ref:`remote_desktop` を参照して VNC または XRDP でアクセスできます。
    * Raspberry Piのデスクトップに入ったらターミナルを開き次のコマンドを入力して実行するか、Pythonエディターで開いて実行します。


.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 color_detect.py

コードを実行するとPiCar-X が赤い色を見つけると画面にフレームを表示します。 コード内の ``'red'`` を別の色に変更して検出することもできます。

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


**どんな動きをするの？**

まず `HSV 色空間 <https://en.wikipedia.org/wiki/HSL_and_HSV>`_ のHの範囲を辞書として定義します。これは次の色判定アルゴリズムに便利です。

.. code-block:: python

    color_dict = {'red':[0,4],'orange':[5,18],'yellow':[22,37],'green':[42,85],'blue':[92,110],'purple':[115,165],'red_2':[165,180]} 

次にサイズ 5x5 の `畳み込みカーネル <https://en.wikipedia.org/wiki/Kernel_(image_processing)>`_ が定義されフィルタリングなどの形態学的操作に使用されます。


.. code-block:: python

    kernel_5 = np.ones((5,5),np.uint8)


次に ``color_detect()`` 関数は4つのステップで画像を処理します:

1. 目的の色のデータを新しいバイナリ イメージ (配列) として抽出します。
2. 高度な形態変換を実行します。
3. バイナリ イメージで輪郭を検索します。
4. 画像上に認識されたオブジェクトのフレームを描画します（見つけた色の周りを四角い枠で囲う）。

.. code-block:: python

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

``img`` 、 ``mask`` 、および ``morphologyEx_img`` は、各ステップの処理結果を直接観察するために3つのウィンドウに表示されます。

.. image:: img/color_detect.png

形態とコンタリングの詳細については次のリソースを参照してください。

* `Opening operation - Wikipedia <https://en.wikipedia.org/wiki/Opening_(morphology)>`_ 
* `morphologyEx - OpenCV <https://docs.opencv.org/4.0.0/d4/d86/group__imgproc__filter.html#ga67493776e3ad1a3df63883829375201f>`_
* `findContours - OpenCV <https://docs.opencv.org/4.0.0/d3/dc0/group__imgproc__shape.html#gadf1ad6a0b82947fa1fe3c3d497f260e0>`_
* `Contour Features - OpenCV <https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html>`_