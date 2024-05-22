.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _control_by_app:

13. Controlled by the APP
==================================

The SunFounder controller is used to control Raspberry Pi/Pico based robots.

The APP integrates Button, Switch, Joystick, D-pad, Slider and Throttle Slider widgets; Digital Display, Ultrasonic Radar, Grayscale Detection and Speedometer input widgets.

There are 17 areas A-Q , where you can place different widgets to customize your own controller.

In addition, this application provides a live video streaming service.

Let's customize a PiCar-X controller using this app.

**How to do?**

#. Install the ``sunfounder-controller`` module.

    The ``robot-hat``, ``vilib``, and ``picar-x`` modules need to be installed first, for details see: :ref:`install_all_modules`.


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Run the code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 13.app_control.py

#. Install `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ from **APP Store(iOS)** or **Google Play(Android)**.


#. Open and create a new controller.

    Create a new controller by clicking on the + sign in the SunFounder Controller APP.

    .. image:: img/app1.PNG

    There are preset controllers for some products in the Preset section, which you can use as needed. Here, we select **PiCar-X**.

    .. image:: img/app_control_preset.jpg

#. Connect to PiCar-x.

    When you click the **Connect** button, it will automatically search for robots nearby. Its name is defined in ``picarx_control.py`` and it must be running at all times.

    .. image:: img/app9.PNG
    
    Once you click on the product name, the message "Connected Successfully" will appear and the product name will appear in the upper right corner.

    .. image:: img/app10.PNG

    .. note::

        * You need to make sure that your mobile device is connected to the same LAN as PiCar-X.
        * If it doesn't search automatically, you can also manually enter the IP to connect.

        .. image:: img/app11.PNG

#. Run this controller.

    Click the **Run** button to start the controller, you will see the footage of the car shooting, and now you can control your PiCar-X with these widgets.

    .. image:: img/app12.PNG
    
    Here are the functions of the widgets.

    * **A**: Show the current speed of the car.
    * **E**: turn on the obstacle avoidance function.
    * **I**: turn on the line following function.
    * **J**: voice recognition, press and hold this widget to start speaking, and it will show the recognized voice when you release it. We have set ``forward``, ``backard``, ``left`` and ``right`` 4 commands in the code to control the car.
    * **K**: Control forward, backward, left, and right motions of the car.
    * **Q**: turn the head(Camera) up, down, left and right.
    * **N**: Turn on the color recognition function.
    * **O**: Turn on the face recognition function.
    * **P**: Turn on the object recognition function, it can recognize nearly 90 kinds of objects, for the list of models, please refer to: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.


