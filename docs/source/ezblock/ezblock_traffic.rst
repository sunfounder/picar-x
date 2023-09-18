交通標識の検出
===============================

色や顔の検出に加えて、PiCar-Xは交通標識の検出も行うことができます。

今回は、この交通標識の検出機能とライン追従機能を組み合わせてみましょう。
PiCar-Xにラインを追跡させ、その前にStopサインを置くと、それは停止します。Forwardサインを前に置くと、前進し続けます。

**ヒント**

#. PiCarは、以下のPDFに含まれる4つの異なる交通標識モデルを認識します。

    .. image:: img/taffics_sign.png

    * :download:`[PDF]交通標識カード <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/traffic-sign-cards.pdf>`

#. **Set ref to ()** ブロックは、グレースケールのしきい値を設定するために使用されます。実際の状況に応じてそれを変更する必要があります。:ref:`test_grayscale` を実行して、白と黒の表面でのグレースケールモジュールの値を見ることができます。そして、その中間の値をこのブロックに入力します。

**例**

.. note::

    * 以下の画像に従ってプログラムを書くことができます。チュートリアルを参照してください: :ref:`ezblock:create_project_latest`。
    * EzBlock Studioの **Examples** ページで同じ名前のコードを見つけ、 **Run** または **Edit** を直接クリックしてください。

.. image:: img/sp210513_101526.png

.. image:: img/sp210513_110948.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png
