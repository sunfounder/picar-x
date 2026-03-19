import argparse
import asyncio
import websockets
import json
import sys
from typing import Dict, Any

DEFAULT_PORT = 30102
DEFAULT_HOST = "localhost"

class PiCarXClient:
    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT):
        self.host = host
        self.port = port
        self.websocket = None
        self.device_info = {}
        self.last_io_data = {}
        self.connected = False

    async def connect(self):
        uri = f"ws://{self.host}:{self.port}"
        try:
            self.websocket = await websockets.connect(uri)
            self.connected = True
            print(f"Connected to {uri}")
            
            await asyncio.sleep(0.1)
            try:
                message = await asyncio.wait_for(self.websocket.recv(), timeout=1.0)
                if not message.startswith("DATA+") and not message.startswith("SET+"):
                    data = json.loads(message)
                    self.device_info = data
                    print(f"Device info received: {data.get('Name', 'Unknown')}")
            except asyncio.TimeoutError:
                pass
            
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False

    async def disconnect(self):
        if self.websocket:
            await self.websocket.close()
            self.connected = False
            print("Disconnected")

    async def send_command(self, command: Dict[str, Any], silent: bool = False) -> bool:
        if not self.connected or not self.websocket:
            print("Not connected")
            return False

        try:
            message = f"DATA+{json.dumps(command)}"
            await self.websocket.send(message)
            if not silent:
                print(f"Sent command: {command}")
            return True
        except Exception as e:
            print(f"Failed to send command: {e}")
            return False

    async def set_device_config(self, config: Dict[str, Any]) -> bool:
        if not self.connected or not self.websocket:
            print("Not connected")
            return False

        try:
            message = f"SET+{json.dumps(config)}"
            await self.websocket.send(message)
            print(f"Set device config: {config}")
            return True
        except Exception as e:
            print(f"Failed to set device config: {e}")
            return False

    async def receive_data(self):
        if not self.connected or not self.websocket:
            print("Not connected")
            return None

        try:
            message = f"DATA+{json.dumps({})}"
            await self.websocket.send(message)
            
            message = await asyncio.wait_for(self.websocket.recv(), timeout=2.0)
            
            if message.startswith("DATA+"):
                data = json.loads(message[5:])
                if "io_data" in data:
                    self.last_io_data = data["io_data"]
                    return self.last_io_data
                else:
                    print(f"Received DATA but no io_data: {data}")
            else:
                print(f"Received unexpected message: {message[:100]}")
            return None
        except asyncio.TimeoutError:
            print("Timeout waiting for data")
            return None
        except Exception as e:
            print(f"Failed to receive data: {e}")
            return None

    async def get_device_info(self):
        if not self.connected or not self.websocket:
            print("Not connected")
            return None

        try:
            message = await asyncio.wait_for(self.websocket.recv(), timeout=2.0)
            if not message.startswith("DATA+") and not message.startswith("SET+"):
                data = json.loads(message)
                self.device_info = data
                return data
            return None
        except asyncio.TimeoutError:
            return None
        except Exception as e:
            print(f"Failed to get device info: {e}")
            return None

    def print_io_data(self, data: Dict[str, Any]):
        print("\n=== Sensor Data ===")
        
        if "battery_voltage" in data and data["battery_voltage"] is not None:
            print(f"Battery Voltage: {data['battery_voltage']:.2f}V")
        if "charge_state" in data and data["charge_state"] is not None:
            print(f"Charging: {'Yes' if data['charge_state'] else 'No'}")
        if "ultrasonic_distance" in data and data["ultrasonic_distance"] is not None:
            print(f"Ultrasonic Distance: {data['ultrasonic_distance']:.2f}cm")
        
        if "grayscale_data" in data and data["grayscale_data"] is not None:
            print(f"Grayscale Data: {data['grayscale_data']}")
        if "grayscale_data_raw" in data and data["grayscale_data_raw"] is not None:
            print(f"Grayscale Raw: {data['grayscale_data_raw']}")
        if "is_on_line" in data and data["is_on_line"] is not None:
            print(f"On Line: {'Yes' if data['is_on_line'] else 'No'}")
        if "is_on_cliff" in data and data["is_on_cliff"] is not None:
            print(f"On Cliff: {'Yes' if data['is_on_cliff'] else 'No'}")
        if "line_position" in data and data["line_position"] is not None:
            print(f"Line Position: {data['line_position']:.2f}")
        
        if "color_detection" in data and data["color_detection"] is not None:
            cd = data["color_detection"]
            print(f"Color Detection: x={cd['x']:.2f}, y={cd['y']:.2f}, w={cd['w']:.2f}, h={cd['h']:.2f}, n={cd['n']}")
        if "face_detection" in data and data["face_detection"] is not None:
            fd = data["face_detection"]
            print(f"Face Detection: x={fd['x']:.2f}, y={fd['y']:.2f}, w={fd['w']:.2f}, h={fd['h']:.2f}, n={fd['n']}")
        if "traffic_sign_detection" in data and data["traffic_sign_detection"] is not None:
            ts = data["traffic_sign_detection"]
            print(f"Traffic Sign: x={ts['x']:.2f}, y={ts['y']:.2f}, w={ts['w']:.2f}, h={ts['h']:.2f}, type={ts['t']}")
        if "qr_code_detection" in data and data["qr_code_detection"] is not None:
            qr = data["qr_code_detection"]
            print(f"QR Code: x={qr['x']:.2f}, y={qr['y']:.2f}, w={qr['w']:.2f}, h={qr['h']:.2f}, data={qr['d']}")
        
        if "steering_angle" in data and data["steering_angle"] is not None:
            print(f"Steering Angle: {data['steering_angle']:.1f}°")
        if "camera_pan_angle" in data and data["camera_pan_angle"] is not None:
            print(f"Camera Pan: {data['camera_pan_angle']:.1f}°")
        if "camera_tilt_angle" in data and data["camera_tilt_angle"] is not None:
            print(f"Camera Tilt: {data['camera_tilt_angle']:.1f}°")
        
        if "sound_status" in data and data["sound_status"] is not None:
            status_map = {0: "Stopped", 1: "Playing", 2: "Paused"}
            print(f"Sound Status: {status_map.get(data['sound_status'], 'Unknown')}")
        if "music_status" in data and data["music_status"] is not None:
            status_map = {0: "Stopped", 1: "Playing", 2: "Paused"}
            print(f"Music Status: {status_map.get(data['music_status'], 'Unknown')}")
        if "music_volume" in data and data["music_volume"] is not None:
            print(f"Music Volume: {data['music_volume']}")
        
        if "ai_status" in data and data["ai_status"] is not None:
            print(f"AI Status: {data['ai_status']}")
        if "ai_listen_result" in data and data["ai_listen_result"] is not None:
            print(f"AI Listen Result: {data['ai_listen_result']}")
        if "ai_think_result" in data and data["ai_think_result"] is not None:
            print(f"AI Think Result: {data['ai_think_result']}")
        
        if "vosk_listening" in data and data["vosk_listening"] is not None:
            print(f"Vosk Listening: {'Yes' if data['vosk_listening'] else 'No'}")
        if "vosk_listen_result" in data and data["vosk_listen_result"] is not None:
            print(f"Vosk Listen Result: {data['vosk_listen_result']}")
        
        if "alert" in data and data["alert"] is not None:
            print(f"Alert: {data['alert']}")
        print("====================\n")


async def async_main():
    parser = argparse.ArgumentParser(description="PiCar-X WebSocket Command Line Interface")
    
    parser.add_argument("--host", default=DEFAULT_HOST, help="WebSocket server host")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="WebSocket server port")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    move_parser = subparsers.add_parser("move", help="Control car movement")
    move_parser.add_argument("power", type=int, default=None, help="Motor power (-100 to 100)")
    move_parser.add_argument("steering", type=int, default=None, help="Steering angle (-30 to 30)")
    
    camera_pan_parser = subparsers.add_parser("camera-pan-tilt", help="Control camera pan tile angle")
    camera_pan_parser.add_argument("pan", type=int, default=None, help="Camera pan angle (-90 to 90)")
    camera_pan_parser.add_argument("tilt", type=int, default=None, help="Camera tilt angle (-30 to 30)")
    
    sound_parser = subparsers.add_parser("sound", help="Play sound effect")
    sound_parser.add_argument("index", type=int, choices=[0, 1], help="Sound effect index")
    
    music_parser = subparsers.add_parser("music", help="Play music")
    music_parser.add_argument("index", type=int, choices=[0, 1, 2], help="Music index")
    
    music_control_parser = subparsers.add_parser("music-control", help="Control music playback")
    music_control_parser.add_argument("control", type=int, choices=[0, 1, 2], help="0=stop, 1=play, 2=pause")
    
    volume_parser = subparsers.add_parser("volume", help="Set music volume")
    volume_parser.add_argument("level", type=int, help="Volume level (0-100)")
    
    line_tracking_parser = subparsers.add_parser("line-tracking", help="Line tracking mode")
    line_tracking_parser.add_argument("enable", type=int, choices=[0, 1], help="0=disable, 1=enable")
    line_tracking_parser.add_argument("power", type=int, default=None, help="Power level (0-100)")
    
    obstacle_parser = subparsers.add_parser("obstacle", help="Obstacle avoidance mode")
    obstacle_parser.add_argument("enable", type=int, choices=[0, 1], help="0=disable, 1=enable")
    obstacle_parser.add_argument("power", type=int, default=None, help="Power level (0-100)")
    
    following_parser = subparsers.add_parser("following", help="Following mode")
    following_parser.add_argument("enable", type=int, choices=[0, 1], help="0=disable, 1=enable")
    following_parser.add_argument("power", type=int, default=None, help="Power level (0-100)")
    following_parser.add_argument("mode", type=str, default=None, choices=["face", "red", "orange", "yellow", "green", "blue", "purple"], 
                                      help="Following mode")
    
    led_parser = subparsers.add_parser("led", help="Control LED")
    led_parser.add_argument("enable", type=int, choices=[0, 1], help="0=off, 1=on")
    
    action_parser = subparsers.add_parser("action", help="Perform action")
    action_parser.add_argument("action", choices=["shake head", "nod", "wave hands", "resist", "act cute", 
                                                 "rub hands", "think", "twist body", "celebrate", "depressed", "stop"],
                              help="Action to perform")
    
    ai_think_parser = subparsers.add_parser("ai-think", help="AI think")
    ai_think_parser.add_argument("prompt", help="Prompt for AI to think about")
    
    ai_think_image_parser = subparsers.add_parser("ai-think-image", help="AI think with image")
    ai_think_image_parser.add_argument("prompt", help="Prompt for AI to think about with image")
    
    ai_say_parser = subparsers.add_parser("ai-say", help="AI say")
    ai_say_parser.add_argument("text", help="Text for AI to say")
    
    piper_say_parser = subparsers.add_parser("piper-say", help="Piper TTS say")
    piper_say_parser.add_argument("text", help="Text for Piper to say")
    piper_say_parser.add_argument("model", help="Piper model name")
    
    # vosk_language_parser = subparsers.add_parser("vosk-language", help="Set Vosk language")
    # vosk_language_parser.add_argument("language", help="Vosk language code")
    
    # vosk_listen_parser = subparsers.add_parser("vosk-listen", help="Vosk listen")
    # vosk_listen_parser.add_argument("enable", type=int, choices=[0, 1], help="0=stop, 1=start")
    
    data_parser = subparsers.add_parser("data", help="Get sensor data")
    data_parser.add_argument("--watch", action="store_true", help="Watch data continuously")
    data_parser.add_argument("--interval", type=float, default=0.5, help="Watch interval in seconds")
    
    info_parser = subparsers.add_parser("info", help="Get device info")
    
    stop_parser = subparsers.add_parser("stop", help="Stop all actions")
    
    reset_parser = subparsers.add_parser("reset", help="Reset car position")
    
    test_parser = subparsers.add_parser("test", help="Test connection")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    client = PiCarXClient(args.host, args.port)
    
    if not await client.connect():
        sys.exit(1)

    try:
        if args.command == "move":
            data = {}
            if args.power is not None:
                data["motor"] = args.power
            if args.steering is not None:
                data["steering"] = args.steering
            await client.send_command(data)
        
        elif args.command == "camera-pan-tilt":
            data = {}
            if args.pan is not None:
                data["camera_pan"] = args.pan
            if args.tilt is not None:
                data["camera_tilt"] = args.tilt
            await client.send_command(data)
        
        elif args.command == "sound":
            await client.send_command({"play_sound": args.index})
        
        elif args.command == "music":
            await client.send_command({"play_music": args.index})
        
        elif args.command == "music-control":
            await client.send_command({"music_control": args.control})
        
        elif args.command == "volume":
            await client.send_command({"music_volume": args.level})
        
        elif args.command == "line-tracking":
            data = {"line_tracking": args.enable}
            if args.power is not None:
                data["line_tracking_power"] = args.power
            await client.send_command(data)
        
        elif args.command == "obstacle":
            data = {"obstacle_avoidance": args.enable}
            if args.power is not None:
                data["obstacle_avoidance_power"] = args.power
            await client.send_command(data)
        
        elif args.command == "following":
            data = {"following": args.enable}
            if args.mode is not None:
                data["following_mode"] = args.mode
            if args.power is not None:
                data["following_power"] = args.power
            await client.send_command(data)
        
        elif args.command == "led":
            await client.send_command({"led": args.enable})
        
        elif args.command == "action":
            action_map = {"stop": "[STOP]"}
            action = action_map.get(args.action, args.action)
            await client.send_command({"do_action": action})
        
        elif args.command == "ai-think":
            if args.prompt.lower() == "stop":
                await client.send_command({"ai_think": "[STOP]"})
            else:
                await client.send_command({"ai_think": args.prompt})
        
        elif args.command == "ai-think-image":
            if args.prompt.lower() == "stop":
                await client.send_command({"ai_think_with_image": "[STOP]"})
            else:
                await client.send_command({"ai_think_with_image": args.prompt})
        
        elif args.command == "ai-say":
            if args.text.lower() == "stop":
                await client.send_command({"ai_say": "[STOP]"})
            else:
                await client.send_command({"ai_say": args.text})
        
        elif args.command == "piper-say":
            await client.send_command({"piper_say": args.text, "piper_set_model": args.model})
        
        # elif args.command == "vosk-language":
        #     if args.language.lower() == "stop":
        #         await client.send_command({"vosk_set_language": "[STOP]"})
        #     else:
        #         await client.send_command({"vosk_set_language": args.language})
        
        # elif args.command == "vosk-listen":
        #     await client.send_command({"vosk_listen": args.enable})
        
        elif args.command == "info":
            info = await client.get_device_info()
            if info:
                print("\n=== Device Info ===")
                for key, value in info.items():
                    print(f"{key}: {value}")
                print("===================\n")
        
        elif args.command == "stop":
            await client.send_command({"motor": 0})
            await client.send_command({"ai_think": "[STOP]"})
            await client.send_command({"ai_say": "[STOP]"})
            await client.send_command({"do_action": "[STOP]"})
            await client.send_command({"line_tracking": 0})
            await client.send_command({"obstacle_avoidance": 0})
            await client.send_command({"following": 0})
            await client.send_command({"vosk_listen": 0})
            print("All actions stopped")
        
        elif args.command == "reset":
            await client.send_command({"motor": 0})
            await client.send_command({"steering": 0})
            await client.send_command({"camera_pan": 0})
            await client.send_command({"camera_tilt": 0})
            print("Car position reset")
        
        elif args.command == "test":
            print("Testing connection...")
            print(f"Device info: {client.device_info}")
            data = await client.receive_data()
            if data:
                print("Successfully received data!")
                client.print_io_data(data)
            else:
                print("Failed to receive data")
        
        elif args.command == "data":
            if args.watch:
                print(f"Watching sensor data (Ctrl+C to stop)...")
                try:
                    while True:
                        data = await client.receive_data()
                        if data:
                            client.print_io_data(data)
                        await asyncio.sleep(args.interval)
                except KeyboardInterrupt:
                    print("\nStopped watching")
            else:
                data = await client.receive_data()
                if data:
                    client.print_io_data(data)
        
    finally:
        await client.disconnect()

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
