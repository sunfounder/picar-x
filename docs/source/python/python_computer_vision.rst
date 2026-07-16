.. _py_computer_vision:

7. 计算机视觉
=======================

通过本项目，我们将正式进入计算机视觉领域！

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 7.computer_vision.py

**查看视频画面**

代码运行后，终端将显示以下提示信息：

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

然后在浏览器中输入 ``http://<你的 IP>:9000/mjpg``，即可查看视频画面，例如： ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

程序运行后，您将在终端看到以下提示：

* 输入键以调用功能！
* q: 拍照
* 1: 检测颜色：红色
* 2: 检测颜色：橙色
* 3: 检测颜色：黄色
* 4: 检测颜色：绿色
* 5: 检测颜色：蓝色
* 6: 检测颜色：紫色
* 0: 关闭颜色检测
* r: 扫描二维码
* f: 开启/关闭人脸检测
* s: 显示检测到的物体信息

请根据提示激活对应功能：

    * **拍照**

        在终端输入 ``q`` 并按回车。当前摄像头拍摄的画面将被保存（如果颜色检测功能已开启，标记框也会显示在保存的图片中）。
        您可以在 Raspberry Pi 的 ``/home/{username}/Pictures/`` 目录中查看这些照片。
        使用工具（例如 :ref:`filezilla`）可以将照片传输到您的电脑。

    * **颜色检测**

        输入数字 ``1~6`` 将检测红、橙、黄、绿、蓝、紫中的一种颜色。输入 ``0`` 可关闭颜色检测。

        .. image:: img/DTC2.png

        .. note:: 您可以下载并打印PDF 色卡 :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` 用于颜色检测。


    * **人脸检测**

        输入 ``f`` 开启人脸检测。

        .. image:: img/DTC5.png

    * **二维码检测**

        输入 ``r`` 启动二维码识别。在二维码被识别前无法执行其他操作。二维码的解码信息会显示在终端中。

        .. image:: img/DTC4.png

    * **显示检测信息**

        输入 ``s`` 将在终端显示目标检测信息（包括颜色检测和人脸检测）。信息包括目标的中心坐标（X, Y）和大小（宽度、高度）。

**代码**

.. code-block:: python

    from pydoc import text
    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import threading
    import readchar
    import os

    flag_face = False
    flag_color = False
    qr_code_flag = False

    manual = '''
    Input key to call the function!
        q: Take photo
        1: Color detect : red
        2: Color detect : orange
        3: Color detect : yellow
        4: Color detect : green
        5: Color detect : blue
        6: Color detect : purple
        0: Switch off Color detect
        r: Scan the QR code
        f: Switch ON/OFF face detect
        s: Display detected object information
    '''

    color_list = ['close', 'red', 'orange', 'yellow',
                  'green', 'blue', 'purple',
    ]

    def face_detect(flag):
        print("Face Detect:" + str(flag))
        Vilib.face_detect_switch(flag)


    def qrcode_detect():
        global qr_code_flag
        if qr_code_flag == True:
            Vilib.qrcode_detect_switch(True)
            print("Waitting for QR code")

        text = None
        while True:
            temp = Vilib.detect_obj_parameter['qr_data']
            if temp != "None" and temp != text:
                text = temp
                print('QR code:%s'%text)
            if qr_code_flag == False:
                break
            sleep(0.5)
        Vilib.qrcode_detect_switch(False)


    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        username = os.getlogin()

        path = f"/home/{username}/Pictures/"
        Vilib.take_photo(name, path)
        print('photo save as %s%s.jpg'%(path,name))


    def object_show():
        global flag_color, flag_face

        if flag_color is True:
            if Vilib.detect_obj_parameter['color_n'] == 0:
                print('Color Detect: None')
            else:
                color_coodinate = (Vilib.detect_obj_parameter['color_x'],Vilib.detect_obj_parameter['color_y'])
                color_size = (Vilib.detect_obj_parameter['color_w'],Vilib.detect_obj_parameter['color_h'])
                print("[Color Detect] ","Coordinate:",color_coodinate,"Size",color_size)

        if flag_face is True:
            if Vilib.detect_obj_parameter['human_n'] == 0:
                print('Face Detect: None')
            else:
                human_coodinate = (Vilib.detect_obj_parameter['human_x'],Vilib.detect_obj_parameter['human_y'])
                human_size = (Vilib.detect_obj_parameter['human_w'],Vilib.detect_obj_parameter['human_h'])
                print("[Face Detect] ","Coordinate:",human_coodinate,"Size",human_size)


    def main():
        global flag_face, flag_color, qr_code_flag
        qrcode_thread = None

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)
        print(manual)

        while True:
            # readkey
            key = readchar.readkey()
            key = key.lower()
            # take photo
            if key == 'q':
                take_photo()
            # color detect
            elif key != '' and key in ('0123456'):  # '' in ('0123') -> True
                index = int(key)
                if index == 0:
                    flag_color = False
                    Vilib.color_detect('close')
                else:
                    flag_color = True
                    Vilib.color_detect(color_list[index]) # color_detect(color:str -> color_name/close)
                print('Color detect : %s'%color_list[index])
            # face detection
            elif key =="f":
                flag_face = not flag_face
                face_detect(flag_face)
            # qrcode detection
            elif key =="r":
                qr_code_flag = not qr_code_flag
                if qr_code_flag == True:
                    if qrcode_thread == None or not qrcode_thread.is_alive():
                        qrcode_thread = threading.Thread(target=qrcode_detect)
                        qrcode_thread.setDaemon(True)
                        qrcode_thread.start()
                else:
                    if qrcode_thread != None and qrcode_thread.is_alive():
                    # wait for thread to end
                        qrcode_thread.join()
                        print('QRcode Detect: close')
            # show detected object information
            elif key == "s":
                object_show()

            sleep(0.5)


    if __name__ == "__main__":
        main()

**工作原理**

以下函数是摄像头启动和显示功能的关键部分：

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

与“目标检测”相关的功能如下：

* ``Vilib.face_detect_switch(True)``：开启/关闭人脸检测。
* ``Vilib.color_detect(color)``：颜色检测，每次仅支持一种颜色检测。可用参数为： ``"red"`` , ``"orange"`` , ``"yellow"`` , ``"green"`` , ``"blue"`` , ``"purple"`` 。
* ``Vilib.color_detect_switch(False)``：关闭颜色检测。
* ``Vilib.qrcode_detect_switch(False)``：开启/关闭二维码检测，返回二维码的解码数据。
* ``Vilib.gesture_detect_switch(False)``：开启/关闭手势检测。
* ``Vilib.traffic_sign_detect_switch(False)``：开启/关闭交通标志检测。

检测到的目标信息存储在字典 ``detect_obj_parameter = Manager().dict()`` 中，
可在主程序中使用如下方式调用：

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

以下是字典键及其用途：

* ``color_x``：检测到的颜色块中心坐标 x 值，范围 0~320。
* ``color_y``：检测到的颜色块中心坐标 y 值，范围 0~240。
* ``color_w``：检测到的颜色块宽度，范围 0~320。
* ``color_h``：检测到的颜色块高度，范围 0~240。
* ``color_n``：检测到的颜色块数量。
* ``human_x``：检测到的人脸中心坐标 x 值，范围 0~320。
* ``human_y``：检测到的人脸中心坐标 y 值，范围 0~240。
* ``human_w``：检测到的人脸宽度，范围 0~320。
* ``human_h``：检测到的人脸高度，范围 0~240。
* ``human_n``：检测到的人脸数量。
* ``traffic_sign_x``：检测到的交通标志中心坐标 x 值，范围 0~320。
* ``traffic_sign_y``：检测到的交通标志中心坐标 y 值，范围 0~240。
* ``traffic_sign_w``：检测到的交通标志宽度，范围 0~320。
* ``traffic_sign_h``：检测到的交通标志高度，范围 0~240。
* ``traffic_sign_t``：检测到的交通标志内容，值为 `['stop','right','left','forward']`。
* ``gesture_x``：检测到的手势中心坐标 x 值，范围 0~320。
* ``gesture_y``：检测到的手势中心坐标 y 值，范围 0~240。
* ``gesture_w``：检测到的手势宽度，范围 0~320。
* ``gesture_h``：检测到的手势高度，范围 0~240。
* ``gesture_t``：检测到的手势内容，值为 `["paper","scissor","rock"]`。
* ``qr_data``：检测到的二维码内容。
* ``qr_x``：检测到的二维码中心坐标 x 值，范围 0~320。
* ``qr_y``：检测到的二维码中心坐标 y 值，范围 0~240。
* ``qr_w``：检测到的二维码宽度，范围 0~320。
* ``qr_h``：检测到的二维码高度，范围 0~240。
