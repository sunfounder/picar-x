.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_treasure:

20. トレジャーハント
============================

このレッスンでは、PiCar-X を **トレジャーハンターロボット** に変身させます。  
部屋に迷路を配置し、6 枚の異なる色のカードをいろいろな角に置きます。  
PiCar-X は **探索・認識** を行い、ターゲットカラーを見つけたときに **お祝いのアクション** をします。

このプロジェクトは、これまでに学んだ 3 つのスキルを組み合わせたものです：

* **コンピュータビジョン** – Pi カメラで色付きカードを検出  
* **キーボード操作** – ロボットを手動で迷路の中を運転  
* **音声フィードバック** – Pico2Wave でターゲットカラーと成功を音声で案内  

ロボットがまるでトレジャーハンターのように **見て・考えて・行動する** 楽しいゲームです！
 
----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールし、その後スクリプト ``i2samp.sh`` を実行します。
* 信頼性の高い色検出のために、:download:`PDF カラーカード <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` をダウンロードして印刷することができます。

----

コードの実行
------------

.. raw:: html

    <run></run>

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 20.treasure_hunt.py

実行すると、次のようなメッセージが表示されます：

.. code-block:: text

    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

その後、ブラウザで ``http://<あなたのIP>:9000/mjpg`` を開くとライブ映像を見ることができます。  
例： ``http://192.168.18.113:9000/mjpg``  

.. image:: img/display.png

ゲームルール
------------

1. ロボットがランダムに **ターゲットカラー** を選び、 **「赤を探して！」** と話します。  
2. キーボードで PiCar-X を操作します：

   * ``w`` = 前進  
   * ``a`` = 左旋回  
   * ``s`` = 後退  
   * ``d`` = 右旋回  
   * ``space`` = ターゲットの繰り返し  
   * ``Ctrl+C`` = 終了  

3. カメラがターゲットカラーのカードを認識すると、PiCar-X は **「よくできました！」** と話します。  
4. 新しいターゲットカラーが選ばれ、ハントが続きます！

コード
-------

.. code-block:: python

    #!/usr/bin/env python3

    from picarx import Picarx
    from vilib import Vilib
    from picarx.tts import Pico2Wave

    from time import sleep
    import threading
    import readchar
    import random

    # -----------------------
    # Settings
    # -----------------------
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    DETECTION_WIDTH_THRESHOLD = 100  # how wide the color blob must be
    DRIVE_SPEED = 80
    TURN_ANGLE = 30

    MANUAL = """
    Press keys to control PiCar-X:
      w: forward    a: turn left    s: backward    d: turn right
      space: repeat target          Ctrl+C: quit
    """

    # -----------------------
    # Init
    # -----------------------
    px = Picarx()

    tts = Pico2Wave()
    tts.set_lang("en-US")

    current_color = "red"
    key = None
    lock = threading.Lock()

    def say(line: str):
        print(f"[SAY] {line}")
        tts.say(line)

    def renew_color_detect():
        """Choose a new target color and start detection."""
        global current_color
        current_color = random.choice(COLORS)
        Vilib.color_detect(current_color)
        say(f"Look for {current_color}!")

    def key_scan_thread():
        """Background thread reading keys."""
        global key
        while True:
            k = readchar.readkey()
            # Map special keys before lowercasing
            if k == readchar.key.SPACE:
                mapped = "space"
            elif k == readchar.key.CTRL_C:
                mapped = "quit"
            else:
                mapped = k.lower()

            with lock:
                key = mapped

            if mapped == "quit":
                return
            sleep(0.01)

    def car_move(k: str):
        if k == "w":
            px.set_dir_servo_angle(0)
            px.forward(DRIVE_SPEED)
        elif k == "s":
            px.set_dir_servo_angle(0)
            px.backward(DRIVE_SPEED)
        elif k == "a":
            px.set_dir_servo_angle(-TURN_ANGLE)
            px.forward(DRIVE_SPEED)
        elif k == "d":
            px.set_dir_servo_angle(TURN_ANGLE)
            px.forward(DRIVE_SPEED)

    def main():
        global key

        # Start camera and web preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)

        print(MANUAL.strip())
        say("Game start!")
        sleep(0.1)
        renew_color_detect()

        # Start keyboard thread (modern style)
        key_thread = threading.Thread(target=key_scan_thread, daemon=True)
        key_thread.start()

        try:
            while True:
                # Check detection: if target color present and wide enough
                if (Vilib.detect_obj_parameter.get("color_n", 0) != 0 and
                    Vilib.detect_obj_parameter.get("color_w", 0) > DETECTION_WIDTH_THRESHOLD):
                    say("Well done!")
                    sleep(0.1)
                    renew_color_detect()

                # Take a snapshot of the last key (and clear it)
                with lock:
                    k = key
                    key = None

                # Handle movement / actions
                if k in ("w", "a", "s", "d"):
                    car_move(k)
                    sleep(0.5)
                    px.stop()
                elif k == "space":
                    say(f"Look for {current_color}!")
                elif k == "quit":
                    print("\n[INFO] Quit requested.")
                    break

                sleep(0.05)

        except KeyboardInterrupt:
            print("\n[INFO] Stopped by user.")
        finally:
            try:
                Vilib.camera_close()
            except Exception:
                pass
            px.stop()
            say("Goodbye!")
            sleep(0.2)

    if __name__ == "__main__":
        main()


しくみ
------------

1. **初期化**

   * モジュールをインポートし、PiCar-X・カメラ・TTS を設定します。  
   * 色リスト、スピード、ステアリング角度を設定します。

2. **ターゲット選択**

   * ``renew_color_detect()`` がランダムにターゲットカラーを選びます。  
   * ロボットが Pico2Wave でターゲットカラーをアナウンスします。

3. **キーボード操作**

   * ``key_scan_thread()`` がバックグラウンドでキー入力を取得します。  
   * キー ``w, a, s, d`` で移動を操作し、``space`` でターゲットの繰り返しを行います。

4. **色検出**

   * カメラが常にターゲットカラーが見えるかどうかをチェックします。  
   * 検出された色のブロブが一定の大きさになると、PiCar-X はお祝いのアクションをします。

5. **メインループ**

   * 移動、検出、フィードバックを連続的に処理します。  
   * 終了時にロボットとカメラをきれいに停止させます。

トラブルシューティング
-----------------------

* **カメラ映像が表示されない場合**

  ``libcamera-hello`` を実行し、Pi カメラが正しく接続されているか確認してください。

* **ロボットが色を検出しない場合**

  カードがはっきり印刷され、十分な明るさで設置されているか確認してください。  
  ``DETECTION_WIDTH_THRESHOLD`` の値を調整してみてください。

* **音声フィードバックがない場合**

  ``pico2wave`` がインストールされているか、音声出力の設定を確認してください。

* **車が動かない場合**

  PiCar-X の電源が入っているか、モーターのキャリブレーションが正しいか確認してください。

----

このレッスンを終えることで、PiCar-X を使った **ミニ・トレジャーハントゲーム** を完成させ、  
**ビジョン・操作・インタラクション** を組み合わせたプロジェクトを構築しました！
