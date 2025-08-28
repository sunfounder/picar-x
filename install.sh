#!/bin/bash

LOG_FILE="./install.log"
if [ -f "$LOG_FILE" ]; then
    rm $LOG_FILE
fi
touch $LOG_FILE

log() {
    echo "$1"
    echo "$1" >> $LOG_FILE
}

ERROR_HAPPENED=false
ERROR_LOGS=""

# Check root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root"
  exit 1
fi

# Get username of 1000
USERNAME=$(getent passwd 1000 | cut -d: -f1)
HOME=$(getent passwd 1000 | cut -d: -f6)

run() {
    local cmd="$1"
    local info="$2"
    local delay=0.1
    local spinstr='⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'  # 更精细的旋转字符
    local i=0
    
    # 隐藏光标
    tput civis
    
    # 在后台执行命令
    eval $cmd > /tmp/cmd_output.log 2>&1 &
    local pid=$!
    
    # 显示旋转光标和详细信息
    while [ -d /proc/$pid ]; do
        local char=${spinstr:$i:1}
        printf "\r\033[36m[%s]\033[0m %s" "$char" "$info"
        i=$(( (i+1) % ${#spinstr} ))
        sleep $delay
    done
    
    # 等待命令完成并显示结果
    wait $pid
    local result=$?
    
    # 恢复光标
    tput cnorm
    
    if [ $result -eq 0 ]; then
        printf "\r\033[32m[✓]\033[0m %s\n" "$info"
        echo "[✓] $info" >> $LOG_FILE
    else
        printf "\r\033[31m[✗]\033[0m %s\n" "$info"
        ERROR_HAPPENED=true
        ERROR_LOGS+=`cat /tmp/cmd_output.log`
        echo "[✗] $info" >> $LOG_FILE
    fi
    
    # 清理临时文件
    cat /tmp/cmd_output.log >> $LOG_FILE
    rm -f /tmp/cmd_output.log
    
    return $result
}

install_app() {
    log "#### Install picar-x-app ####"
    echo "[Unit]
Description=picarx service
After=multi-user.target

[Service]
Type=simple
WorkingDirectory=/home/$USERNAME/picar-x/app
ExecStart=python3 app.py

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/picar-x-app.service
    run "systemctl enable picar-x-app.service" "Enable picar-x-app service"
    run "systemctl daemon-reload" "Reload systemd daemon"
    run "systemctl start picar-x-app.service" "Start picar-x-app service"
    log "picar-x-app installed"
}

# Check how many arguments
if [ "$#" -eq 1  ]; then
    if [ "$1" == "app" ]; then
        install_app
        exit 0
    fi
fi

# Install dependencies
log "#### Install dependencies ####"
run "sudo apt-get update" "Update apt"
run "sudo apt-get install -y python3-pip python3-dev python3-venv python3-pyaudio sox" "Install python3-pip python3-dev python3-venv python3-pyaudio sox"
# sudo apt install -y libatlas-base-dev libjasper-dev libqtgui4 libqt4-test

# Install fusion-hat
log "#### Install fusion-hat ####"
run "cd $HOME" "Change directory to $HOME"
run "rm -rf $HOME/fusion-hat" "Remove fusion-hat if exists"
run "git clone --depth=1 -b 1.1.x https://github.com/sunfounder/fusion-hat.git" "Clone fusion-hat"
run "cd $HOME/fusion-hat" "Change directory to $HOME/fusion-hat"
run "python3 install.py" "Install fusion-hat"

# Install vilib
log "#### Install vilib ####"
run "cd $HOME" "Change directory to $HOME"
run "rm -rf $HOME/vilib" "Remove vilib if exists"
run "git clone https://github.com/sunfounder/vilib.git" "Clone vilib"
run "cd $HOME/vilib" "Change directory to $HOME/vilib"
run "python3 install.py" "Install vilib"

# Install picar-x
log "#### Install Picar-x ####"
run "cd $HOME/picar-x" "Change directory to $HOME/picar-x"
run "pip3 install ./ --break-system-packages" "Install picar-x"

# Create dir for config
run "mkdir -p /opt/picar-x" "Create dir for config"
run "chown -R $USERNAME:$USERNAME /opt/picar-x" "Change ownership of /opt/picar-x to $USERNAME:$USERNAME"
run "chmod -R 755 /opt/picar-x" "Change permissions of /opt/picar-x to 755"

# Whether to install picar-x-app-service
log "Whether to install picar-x-app-service"
read -p "Do you want to install picar-x-app-service? (y/n) " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
    install_app
fi

if [ "$ERROR_HAPPENED" = false ]; then
    log "Finished"
else
    echo "Error happened: $ERROR_LOGS"
    echo "Please check $LOG_FILE for more details."
    exit 1
fi
