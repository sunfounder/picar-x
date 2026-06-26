.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _play_python:

Python で遊ぼう
=======================

Python でプログラミングを始めたい初心者の方は、Raspberry Pi OS の基本操作と Python の基本スキルを少し身につけておくとスムーズです。  
このセクションでは、Raspberry Pi のセットアップから PiCar-X の走行制御、コンピュータビジョンの活用、さらに音声・AI 連携まで、段階的に学ぶことができます。

.. _quick_guide_python:

1. Python クイックガイド
---------------------------

Raspberry Pi の環境構築方法を学びます。  
Raspberry Pi OS のインストール、Wi-Fi の設定、リモートアクセスの有効化など、Python コードを簡単に実行できるように準備します。  
すでに Raspberry Pi の基本操作やコマンドラインに慣れている方は、このパートをスキップして次へ進んでもかまいません。

.. toctree:: 
    :maxdepth: 1
    
    ../_shared/pi_start/need_components
    ../_shared/pi_start/install_os_trixie
    ../_shared/pi_start/power_supply_robot_hat
    ../_shared/pi_start/set_up_pi
    install_all_modules
    py_servo_adjust

2. 基本的な動き
-----------------------

PiCar-X を組み立てたら、まずはシンプルな移動プログラムから始めましょう。  
モーターの制御、前進・後退・旋回の操作、障害物回避やライントレースなどの基本的なセンサーの使い方を学びます。

.. toctree:: 
    :maxdepth: 1
    
    python_calibrate
    python_move
    python_keyboard
    python_avoid
    python_cliff
    python_line_track

3. コンピュータビジョン
----------------------

PiCar-X に「見る力」を与えましょう。  
このセクションでは、顔追跡、録画、物体とのインタラクション、ビデオ制御やモバイルアプリによる操作など、カメラを活用したさまざまな楽しいプロジェクトを紹介します。

.. toctree:: 
    :maxdepth: 1

    python_computer_vision
    python_stare_at_you
    python_record
    python_bull_fight
    python_video_car
    control_by_app

