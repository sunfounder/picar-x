# Picar-X

Picar-X Python library for Raspberry Pi.

## Links

- Docs: <https://docs.sunfounder.com/projects/picar-x-v20/en/latest/>
- Robot Hat: <https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/>
- Forum: <https://forum.sunfounder.com/>
- Sunfounder: <https://www.sunfounder.com/>

## Installation

```bash
git clone -b v3.x https://github.com/sunfounder/picar-x.git
cd picar-x
sudo bash install.sh

# Setup peaker and microphone. you may need to run this command again after reboot
sudo bash i2samp.sh
# Reboot when it ask "Would you like to reboot and retry now? (Y/N):"

# After reboot, run the command again.
cd picar-x
sudo bash i2samp.sh
# Enter Y when it ask "Do you wish to test speaker now? [y/N]"

```

## Debug command list

```
cd ~/fusion-hat && sudo pip3 install . --break-system-packages --no-build-isolation --no-deps
cd ~/picar-x && sudo pip3 install . --break-system-packages --no-build-isolation --no-deps
cd ~/picar-x/app && sudo python3 app.py

## Trouble Shooting

----------------------------------------------

## About SunFounder

SunFounder is a technology company focused on Raspberry Pi and Arduino open source community development. Committed to the promotion of open source culture, we strives to bring the fun of electronics making to people all around the world and enable everyone to be a maker. Our products include learning kits, development boards, robots, sensor modules and development tools. In addition to high quality products, SunFounder also offers video tutorials to help you make your own project. If you have interest in open source or making something cool, welcome to join us!

----------------------------------------------

## License

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied wa rranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

{Repository Name} comes with ABSOLUTELY NO WARRANTY; for details run ./show w. This is free software, and you are welcome to redistribute it under certain conditions; run ./show c for details.

SunFounder, Inc., hereby disclaims all copyright interest in the program '{Repository Name}' (which makes passes at compilers).

Mike Huang, 21 August 2015

Mike Huang, Chief Executive Officer

Email: service@sunfounder.com, support@sunfounder.com

----------------------------------------------

## Contact us

website:
    www.sunfounder.com

E-mail:
    service@sunfounder.com, support@sunfounder.com
