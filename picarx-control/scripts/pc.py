#!/usr/bin/env python3
"""
PiCar-X CLI — control the robot car from the command line.

Usage:
  pc.py move <action> [--steps N] [--speed N]
  pc.py turn <direction> [--angle N]
  pc.py cam <pan|tilt> --angle N
  pc.py sensor <type>
  pc.py sound play <file> [--volume N]
  pc.py sound volume <0-100>
  pc.py sound music <file> [--volume N]
  pc.py sound stop
  pc.py calibrate

Examples:
  pc.py move forward --speed 50
  pc.py move backward --speed 40
  pc.py turn left --angle 30
  pc.py cam pan --angle 60
  pc.py sensor distance
  pc.py sensor grayscale
  pc.py sound play ~/Music/horn.wav --volume 80
  pc.py calibrate
"""

import argparse
from time import sleep


def cmd_move(args):
    from picarx import Picarx
    car = Picarx()
    try:
        if args.action == 'forward':
            car.forward(args.speed)
        elif args.action == 'backward':
            car.backward(args.speed)
        sleep(args.duration)
    finally:
        car.stop()


def cmd_turn(args):
    from picarx import Picarx
    car = Picarx()
    try:
        angle = args.angle if args.direction == 'right' else -args.angle
        car.set_dir_servo_angle(angle)
        sleep(0.3)
        car.forward(30)
        sleep(0.8)
        car.set_dir_servo_angle(0)
        sleep(0.3)
    finally:
        car.stop()


def cmd_cam(args):
    from picarx import Picarx
    car = Picarx()
    if args.cam_action == 'pan':
        car.set_cam_pan_angle(args.angle)
    elif args.cam_action == 'tilt':
        car.set_cam_tilt_angle(args.angle)


def cmd_sensor(args):
    if args.sensor_type == 'distance':
        from picarx import Picarx
        car = Picarx()
        d = car.get_distance()
        print(f"{d:.1f}" if d else "None")
    elif args.sensor_type == 'grayscale':
        from robot_hat import ADC, Grayscale_Module
        adc0, adc1, adc2 = ADC("A0"), ADC("A1"), ADC("A2")
        gs = Grayscale_Module(adc0, adc1, adc2, reference=[200, 200, 200])
        sleep(0.3)
        # Warmup + auto-calibrate reference from samples
        samples = []
        for i in range(5):
            data = gs.read()
            if data != [2571, 3085, 3599] and data[0] < 2000:
                samples.append(data)
            sleep(0.1)
        if samples:
            ref = [sum(s[i] for s in samples) // len(samples) for i in range(3)]
            gs.reference(ref)
            print(f"Auto ref: {ref}")
            data = samples[-1]
        else:
            print(f"WARNING: ADC may be corrupted")
            data = [0, 0, 0]
        print(f"Grayscale: {data}")
        status = gs.read_status(data)
        print(f"Line status: {status}")
        is_cliff = any(data[i] <= 500 for i in range(3))
        print(f"Cliff detected: {is_cliff}")


def cmd_sound(args):
    from robot_hat import Music
    music = Music()
    if args.sound_cmd == 'play':
        music.sound_play(args.file, volume=args.volume)
    elif args.sound_cmd == 'volume':
        music.music_set_volume(args.volume)
    elif args.sound_cmd == 'music':
        music.music_set_volume(args.volume or 20)
        music.music_play(args.file)
    elif args.sound_cmd == 'stop':
        music.music_stop()


def cmd_calibrate(args):
    from picarx import Picarx
    car = Picarx()
    print("=== PiCar-X Servo Calibration ===")
    print("This will help you calibrate the steering servo and camera gimbal.")
    print("")

    # Steering servo calibration
    print("--- Steering Servo ---")
    while True:
        val = input("Enter steering offset (-30 to 30, or 'skip'): ").strip()
        if val.lower() == 'skip':
            break
        try:
            angle = int(val)
            car.dir_servo_calibrate(angle)
            print(f"  Steering set to {angle}. Is it centered? (y/n/skip): ", end='')
            ok = input().strip().lower()
            if ok == 'y':
                break
        except ValueError:
            print("  Invalid input.")

    # Camera pan servo calibration
    print("--- Camera Pan Servo ---")
    while True:
        val = input("Enter camera pan offset (-90 to 90, or 'skip'): ").strip()
        if val.lower() == 'skip':
            break
        try:
            angle = int(val)
            car.cam_pan_servo_calibrate(angle)
            print(f"  Cam pan set to {angle}. Is it centered? (y/n/skip): ", end='')
            ok = input().strip().lower()
            if ok == 'y':
                break
        except ValueError:
            print("  Invalid input.")

    # Camera tilt servo calibration
    print("--- Camera Tilt Servo ---")
    while True:
        val = input("Enter camera tilt offset (-35 to 65, or 'skip'): ").strip()
        if val.lower() == 'skip':
            break
        try:
            angle = int(val)
            car.cam_tilt_servo_calibrate(angle)
            print(f"  Cam tilt set to {angle}. Is it centered? (y/n/skip): ", end='')
            ok = input().strip().lower()
            if ok == 'y':
                break
        except ValueError:
            print("  Invalid input.")

    car.reset()
    print("Calibration complete!")


def main():
    parser = argparse.ArgumentParser(description="PiCar-X Robot Car Controller")
    sub = parser.add_subparsers(dest="command")
    sub.required = True

    # move
    move_p = sub.add_parser("move", help="Drive the car")
    move_p.add_argument("action", choices=["forward", "backward"])
    move_p.add_argument("--speed", type=int, default=50, help="Speed 0-100")
    move_p.add_argument("--duration", type=float, default=1.0, help="Duration in seconds")
    move_p.set_defaults(func=cmd_move)

    # turn
    turn_p = sub.add_parser("turn", help="Turn the car")
    turn_p.add_argument("direction", choices=["left", "right"])
    turn_p.add_argument("--angle", type=int, default=30, help="Steering angle 0-30")
    turn_p.set_defaults(func=cmd_turn)

    # cam
    cam_p = sub.add_parser("cam", help="Control camera gimbal")
    cam_p.add_argument("cam_action", choices=["pan", "tilt"])
    cam_p.add_argument("--angle", type=int, required=True, help="Angle (pan: -90~90, tilt: -35~65)")
    cam_p.set_defaults(func=cmd_cam)

    # sensor
    sensor_p = sub.add_parser("sensor", help="Read sensors")
    sensor_p.add_argument("sensor_type", choices=["distance", "grayscale"])
    sensor_p.set_defaults(func=cmd_sensor)

    # sound
    sound_p = sub.add_parser("sound", help="Sound control")
    sound_p.add_argument("sound_cmd", choices=["play", "volume", "music", "stop"])
    sound_p.add_argument("file", nargs="?", help="Sound file path")
    sound_p.add_argument("--volume", type=int, default=None, help="Volume 0-100")
    sound_p.set_defaults(func=cmd_sound)

    # calibrate
    cali_p = sub.add_parser("calibrate", help="Run servo calibration")
    cali_p.set_defaults(func=cmd_calibrate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
