#!/bin/bash

set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# Get username of 1000
USERNAME=$(getent passwd 1000 | cut -d: -f1)
HOME=$(getent passwd 1000 | cut -d: -f6)

install_app() {
    echo "####### Install picar-x-app"
    echo "[Unit]
Description=picarx service
After=multi-user.target

[Service]
Type=simple
WorkingDirectory=/home/$USERNAME/picar-x/app
ExecStart=python3 app.py

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/picar-x-app.service
    systemctl enable picar-x-app.service
    systemctl daemon-reload
    echo "####### picar-x-app installed"
}

if [ "$1" == "app" ]; then
    install_app
    exit 0
fi

# Install dependencies
echo "####### Install dependencies"
sudo apt update
sudo apt install -y python3-pip python3-dev python3-venv python3-pyaudio sox
sudo apt install -y libatlas-base-dev libjasper-dev libqtgui4 libqt4-test

# Install fusion-hat
echo "####### Install fusion-hat"
cd $HOME
git clone https://github.com/sunfounder/fusion-hat.git
cd $HOME/fusion-hat
python3 install.py

# Install vilib
echo "####### Install vilib"
cd $HOME
git clone https://github.com/sunfounder/vilib.git
cd $HOME/vilib
python3 install.py

# Install picar-x
echo "####### Install picar-x"
cd $HOME/picar-x
pip3 install ./ --break-system-packages

# Create dir for config
mkdir -p /opt/picar-x
chown -R $USERNAME:$USERNAME /opt/picar-x
chmod -R 755 /opt/picar-x

# Whether to install picar-x-app-service
read -p "Do you want to install picar-x-app-service? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    install_app
fi

echo "Finished"