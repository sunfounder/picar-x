# Picar-X

Picar-X Python library for Raspberry Pi.

## Links

- Docs: <https://docs.sunfounder.com/projects/picar-x-v20/en/latest/>
- Robot Hat: <https://docs.sunfounder.com/projects/robot-hat-v4/en/latest/>
- Forum: <https://forum.sunfounder.com/>
- Sunfounder: <https://www.sunfounder.com/>

## Installation

```bash
# Install PiCar-X V4
curl -sSL https://raw.githubusercontent.com/sunfounder/sunfounder-installer-scripts/main/install-picar-x-v4.sh | sudo bash

# After installation, finished, and prompt to reboot. input "Y" to reboot.

# After reboot, run the this command to setup the audio.
sudo bash /opt/setup_robot_hat_audio.sh
```

## Debug command list

```bash
cd ~/fusion-hat && sudo pip3 install . --break-system-packages --no-build-isolation --no-deps
sudo pip install ~/robot-hat --break-system-packages --no-build-isolation --no-deps
sudo pip install ~/sunfounder-voice-assistant --break-system-packages --no-build-isolation --no-deps
sudo pip install ~/mammoth_websocket --break-system-packages --no-build-isolation --no-deps
sudo pip install ~/picar-x --force-reinstall --break-system-packages --ignore-installed --no-deps
sudo python3 ~/picar-x/app/app.py

sudo pip uninstall --break fusion_hat -y && sudo pip install --break git+https://github.com/sunfounder/fusion-hat.git@1.1.x

sudo systemctl restart picar-x-app
sudo systemctl stop picar-x-app
sudo systemctl start picar-x-app
journalctl -xefu picar-x-app.service
```

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
