.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_avoid:

4. Obstacle Avoidance
=============================

In this project, PiCar-X will detect obstacles in front of it while moving forward, 
and when the obstacles are too close, it will change the direction of moving forward.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py
    
After running the code, PiCar-X will walk forward. 

If it detects that the distance of the obstacle ahead is less than 20cm, it will go backward. 

If there is an obstacle within 20 to 40cm, it will turn left.

If there is no obstacle in the direction after turning left or the obstacle distance is greater than 25cm, 
it will continue to move forward.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to source code path like ``picar-x/example``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time
    
    POWER = 50
    SafeDistance = 40   # > 40 safe
    DangerDistance = 20 # > 20 && < 40 turn around, 
                        # < 20 backward
    
    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
           
            while True:
                distance = round(px.ultrasonic.read(), 2)
                print("distance: ",distance)
                if distance >= SafeDistance:
                    px.set_dir_servo_angle(0)
                    px.forward(POWER)
                elif distance >= DangerDistance:
                    px.set_dir_servo_angle(30)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-30)
                    px.backward(POWER)
                    time.sleep(0.5)
    
        finally:
            px.forward(0)
    
    
    if __name__ == "__main__":
        main()

**How it works?**

* Importing the Picarx Module and Initializing Constants: 

    This section of the code imports the ``Picarx`` class from the ``picarx`` module, which is essential for controlling the Picarx robot. Constants like ``POWER``, ``SafeDistance``, and ``DangerDistance`` are defined, which will be used later in the script to control the robot's movement based on distance measurements.

    .. code-block:: python

        from picarx import Picarx
        import time

        POWER = 50
        SafeDistance = 40 # > 40 safe
        DangerDistance = 20 # > 20 && < 40 turn around,
        # < 20 backward

* Main Function Definition and Ultrasonic Sensor Reading:

    The ``main`` function is where the Picarx robot is controlled. An instance of ``Picarx`` is created, which activates the robot's functionalities. The code enters an infinite loop, constantly reading the distance from the ultrasonic sensor. This distance is used to determine the robot's movement.

    .. code-block:: python
        
        def main():
        try:
        px = Picarx()

            while True:
                distance = round(px.ultrasonic.read(), 2)
                # [Rest of the logic]

* Movement Logic Based on Distance:

    The robot's movement is controlled based on the ``distance`` read from the ultrasonic sensor. If the ``distance`` is greater than ``SafeDistance``, the robot moves forward. If the distance is between ``DangerDistance`` and ``SafeDistance``, it slightly turns and moves forward. If the ``distance`` is less than ``DangerDistance``, the robot reverses while turning in the opposite direction.

    .. code-block:: python

        if distance >= SafeDistance:
            px.set_dir_servo_angle(0)
            px.forward(POWER)
        elif distance >= DangerDistance:
            px.set_dir_servo_angle(30)
            px.forward(POWER)
            time.sleep(0.1)
        else:
            px.set_dir_servo_angle(-30)
            px.backward(POWER)
            time.sleep(0.5)

* Safety and Cleanup with the 'finally' Block:

    The ``try...finally`` block ensures safety by stopping the robot's motion in case of an interruption or error. This is a crucial part for preventing uncontrollable behavior of the robot.

    .. code-block:: python
        
        try:
        # [Control logic]
        finally:
        px.forward(0)

* Execution Entry Point:

    The standard Python entry point ``if __name__ == "__main__":`` is used to run the main function when the script is executed as a standalone program.

    .. code-block:: python
        
        if name == "main":
            main()

In summary, the script uses the Picarx module to control a robot, utilizing an ultrasonic sensor for distance measurement. The robot's movement is adapted based on these measurements, ensuring safe operation through careful control and a safety mechanism in the finally block.
