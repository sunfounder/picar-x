
# PiCar-X Examples

PiCar-X examples

Quick Links:

- [PiCar-X Examples](#picar-x-examples)
  - [About this kit](#about-this-kit)
  - [About PiCar-X:](#about-picar-x)
  - [Download](#download)
  - [Usage](#usage)
  - [Camera](#camera)
  - [Debug](#debug)
  - [Update](#update)
  - [Trouble Shootings](#trouble-shootings)
  - [About SunFounder](#about-sunfounder)
  - [About Ezblock](#about-ezblock)
  - [License](#license)
  - [Contact us](#contact-us)

## About this kit

We are happy to see your issus and pull request. Feel free to be apart.

## About PiCar-X:
PiCar-X is the car that is built based on the Raspberry Pi, with the functions, including line following,human following, color following, obstacle avoidance, horn,  remote control and use the web page to control.

## Download

Download this repository to your Raspberry Pi:

```shell
git clone https://github.com/sunfounder/picar-x.git
```

## Usage

Before running the example, stop ezblock sercive

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

## Update
2021-1-21
 -Add the Japanese user manual
 -Upate the English user manual

2020-6-12
 -New Release

## Trouble Shootings

## About SunFounder
SunFounder is a technology company focused on Raspberry Pi and Arduino open source community development. Committed to the promotion of open source culture, we strives to bring the fun of electronics making to people all around the world and enable everyone to be a maker. Our products include learning kits, development boards, robots, sensor modules and development tools. In addition to high quality products, SunFounder also offers video tutorials to help you make your own project. If you have interest in open source or making something cool, welcome to join us!

## About Ezblock

Ezblock is a technology company focused on Raspberry Pi and Arduino open source community development. Committed to the promotion of open source culture, we strives to bring the fun of electronics making to people all around the world and enable everyone to be a maker. Our products include learning kits, development boards, robots, sensor modules and development tools. In addition to high quality products, Ezblock also offers video tutorials to help you make your own project. If you have interest in open source or making something cool, welcome to join us!

## License

This is the code for PiCar-X.
This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied wa rranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

PiCar-X examples comes with ABSOLUTELY NO WARRANTY; for details checkout [LICENCE](LICENCE). This is free software, and you are welcome to redistribute it under certain conditions; checkout [LICENCE](LICENCE) for details.

SunFounder, Inc., hereby disclaims all copyright interest in the program 'PiCar-X examples' (which makes passes at compilers).

Mike Huang, 21 August 2015

Mike Huang, Chief Executive Officer

Email: service@sunfounder.com

## Contact us

website:
    ezblock.cc

E-mail:
    service@sunfounder.com