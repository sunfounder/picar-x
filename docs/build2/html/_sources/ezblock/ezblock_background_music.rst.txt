バックグラウンド・ミュージック
=====================================

PiCar-X をプログラムして効果音やテキスト読み上げ (TTS) を再生するだけでなく、PiCar-X はバックグラウンド ミュージックも再生します。 このプロジェクトでは、 **Slider** ウィジェットを使用して音楽の音量を調整出来ます。

* :ref:`ezblock:remote_control_latest`

Ezblocks リモート コントロール機能の詳細については、:ref:`ezb_remote_control` チュートリアルを参照してください。

**ティップス**

.. image:: img/sp210512_152803.png

**play background music** のブロックは **Start** ファンクションの中にセットしなければいけません。ドロップダウンメニューからPiCar-Xが演奏する音楽を選択できます。
実際に演奏が開始されるのは **set background music volume to** のブロックか **slider [A] get value** のブロックで音量が指定された後からになります。

.. image:: img/sp210512_153123.png

**set background music volume to** のブロックで演奏する音楽の音量を決定します。 **Start** ファンクションの中でもその他の場所でもどちらにでもセットできます。設定できる値は０から１００までとなります。

.. image:: img/sp210512_154708.png

**Remote Control** のページでこのスライドバーをドラッグしてリモコン画面に設置します。演奏している音楽の音量を自由に変更できます。

.. image:: img/sp210512_154259.png

**slider [A] get value** ブロックは **Remote Control** のページで設定した **Slider** バーから演奏する音量を設定できます。 **Start** ファンクション以外のところで使用できます。ここで音量を調整して初めて音楽の演奏が始まります。

**例：** 

.. note::

    * 以下の例を参考にしてプログラムしてください。また次のチュートリアルをご参照ください。:ref:`ezblock:create_project_latest`.
    * またはEzBlock Studioの **Examples** 画面から「 **Background Music** 」 を探し **Run** か **Edit** を直接クリックしてください。

.. image:: img/sp210512_155406.png