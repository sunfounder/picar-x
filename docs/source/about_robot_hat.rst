Robot HATについて
========================

.. image:: img/picar_x_pic7.png

**Left/Right Motor Port**
    * 2チャンネルXH2.54モーターポート。
    * 左側のポートがGPIO 4に、右側のポートがGPIO 5に接続されています。

**I2C Pin**
    * Raspberry Piの2チャンネルI2C ピン。

**PWM Pin**
    * 12チャンネルPWM ピン、P0-P12。

**ADC Pin**
    * 4チャンネルADCピン、A0-A3。

**Digital Pin**
    * 4チャンネルデジタルピン、D0-D3。

**Battery Indicator**
    * 7.8V以上の電圧がある場合、2つのLEDが点灯します。
    * 6.7V～7.8Vの範囲で1つのLEDが点灯します。
    * 6.7V以下では、全てのLEDが消灯します。

**USR LED**
    * プログラミングから利用できます。 (「1」を設定するとLEDが点灯し、「0」を設定するとLEDが消灯します。)

**RST Button**
    * RSTボタンを短く押すと実行中のプログラムがリセットされます。

**USR Button**
    * USRボタンの機能はプログラで利用できます。 （押すと「0」が、離すと「1」が設定されます。）

**Power Switch**
    * ロボットHATの電源をON/OFFします。
    * 電源ポートに電源を接続すると、Raspberry Piが起動します。ただし、ロボットHATを有効にするために、電源スイッチをONにする必要があります。

**Power Port**
    * 7-12V PH2.0 2 ピン電源入力。
    * Raspberry PiとRobot HATを同時に給電します。



.. note::
    詳細については `Robot HAT Documentation <https://robot-hat.readthedocs.io/en/latest/index.html>`_ を参照してください。

