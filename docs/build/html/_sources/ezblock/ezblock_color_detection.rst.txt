色検出
===========================

PiCar-X はカメラを内蔵していてEzblock プログラムで物体検出と色認識コードを利用できます。 このセクションではEzblock を使用して色検出のプログラムを作成します。

.. note:: 

    このセクションを試す前にRaspberry Pi カメラの FFC ケーブルが正しくしっかりと接続されていることを確認してください。 FCC ケーブルを確実に接続するための詳細な手順については、:ref:`assembly_instructions` を参照してください。

このプログラムでは、Ezblock 最初に検出される色（の色相彩度値 (HSV) 空間範囲）を指定し、次に OpenCV を使用して（HSV範囲内の）色を処理してバックグラウンド ノイズを除去し、最後に一致した色に関する情報をまとめます。

Ezblockには、PiCar-X用の「赤」「オレンジ」「黄」「緑」「青」「紫」の6色モデルがあります。 次の PDF にカラー カードが用意されており、カラー プリンターで印刷する必要があります。

* :download:`[PDF]Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. image:: img/color_card.png
    :width: 600

.. note::

    印刷された色は、プリンターのトナーの違い、または印刷用紙のわずかな色の違いなどによって、Ezblock カラー モデルとはわずかに異なる色合いになる場合があります。 これにより、色認識の精度が低下する可能性があります。


.. image:: img/ezblock_color_detect.PNG

**ティップス**

.. image:: img/sp210512_121105.png

**Remote Control** のページで。ビデオのモニター画面をドラッグしてリモコン画面に設置します。 ビデオ・モニターの使用方法の詳細については、こちらの Ezblock ビデオに関するチュートリアルを参照してください: :ref:`ezblock:video_latest`。

.. image:: img/sp210512_121125.png

**camera monitor** のブロックを **on** にすると **Remote Control** のページのモニター画面にカメラで捉えている映像を表示できます。 注: **camera monitor** を **off** にするとモニター画面への表示は行われませんが、色検出機能はそのまま動作しています。

.. image:: img/sp210512_134133.png

**color detection** ブロックを使用して、色検出を有効にします。 注: 一度に検出できる（設定できる）色は 1 つだけです。

**例：**

.. note::

    * 次の例を参考にしてプログラムを作成してください。またチュートリアルを参照してください。:ref:`ezblock:create_project_latest`.
    * またはEzBlock Studioの **Examples** 画面から「 **Color Detection** 」を探し **Run** か **Edit** を直接クリックしてください。

.. image:: img/sp210512_134636.png