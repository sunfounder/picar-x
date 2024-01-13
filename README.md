
# PiCar-X Examples

This was forked from the main project [Picar-x](https://github.com/Sunfounder/picar-x.git).These are the python scripts to interact with your picar.

## About this kit

Added 00.my_car.py that includes the driving functions with camera movement. Also, I put in the music feature and the ability to talk via the command line. Lastly, I have added the file picarAssistant.py that has ChatGPT functionality with the picar.txt as the functionality. Does require a small usb microphone to interact.

## About PiCar-X:
PiCar-X is the car that is built based on the Raspberry Pi, with the functions, including line following,human following, color following, obstacle avoidance, horn,  remote control and use the web page to control.

## Usage

Before running the example, stop ezblock service.

```python
sudo service ezblock stop
```

Then run the example

```bash
cd examples
sudo python3 xxx.py
```

Stop running the example by using <kbd>Ctrl</kbd>+<kbd>C</kbd>

## Camera

Click this link to view the real-time dynamics of the Raspberry Pi camera

http://192.168.18.120:9000/mjpg

Note to replace it with the IP address of your own Raspberry Pi


## Debug

To edit, rewrite your own code, or just want to get debug messages. run the command：

```python
sudo nano xxx.py
```

After your code is done, exit the text compiler via <kbd>Ctrl</kbd>+<kbd>X</kbd> and run the command:

```python
sudo python3 xxx.py
```
