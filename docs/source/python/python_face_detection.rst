.. _py_face_detection:

8. Stare at You
==========================================

This project is also based on the :ref:`py_computer_vision` project, 
with the addition of face detection algorithms.

When you appear in front of the camera, it will recognize your face and adjust its gimbal to keep your face in the center of the frame.

You can view the screen at ``http://<your IP>:9000/mjpg``.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 8.stare_at_you.py

When the code is run, the car's camera will always be staring at your face.

**Code**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from vilib import Vilib

    px = Picarx()

    def clamp_number(num,a,b):
        return max(min(num, max(a, b)), min(a, b))

    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.face_detect_switch(True)
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['human_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['human_x']
                coordinate_y = Vilib.detect_obj_parameter['human_y']
                
                # change the pan-tilt angle for track the object
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                sleep(0.05)

            else :
                pass
                sleep(0.05)

    if __name__ == "__main__":
        try:
        main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**How it works?**

These lines of code in ``while True`` make the camera follow the face.

.. code-block:: python

    while True:
        if Vilib.detect_obj_parameter['human_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['human_x']
            coordinate_y = Vilib.detect_obj_parameter['human_y']
            
            # change the pan-tilt angle for track the object
            x_angle +=(coordinate_x*10/640)-5
            x_angle = clamp_number(x_angle,-35,35)
            px.set_cam_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = clamp_number(y_angle,-35,35)
            px.set_cam_tilt_angle(y_angle)

1. Check if there is a detected human face

    .. code-block:: python

        Vilib.detect_obj_parameter['human_n'] != 0

2. If a human face is detected, obtain the coordinates ( ``coordinate_x`` and ``coordinate_y`` ) of the detected face.

3. Calculate new pan and tilt angles ( ``x_angle`` and ``y_angle`` ) based on the detected face's position and adjust them to follow the face.

4. Limit the pan and tilt angles within the specified range using the ``clamp_number`` function.

5. Set the camera's pan and tilt angles using ``px.set_cam_pan_angle()`` and ``px.set_cam_tilt_angle()`` .