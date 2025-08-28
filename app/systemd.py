import os
import psutil
import re

def is_running_as_systemd_service():
    """判断当前进程是否作为systemd服务运行"""
    # 检查是否存在systemd特有的环境变量
    if 'INVOCATION_ID' in os.environ and 'JOURNAL_STREAM' in os.environ:
        return True
        
    # 检查父进程是否为systemd
    try:
        ppid = os.getppid()
        parent_process = psutil.Process(ppid)
        if parent_process.name() == 'systemd':
            return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
        
    # 检查cgroup信息
    try:
        with open('/proc/self/cgroup', 'r') as f:
            cgroup_data = f.read()
            if 'system.slice/' in cgroup_data:
                return True
    except IOError:
        pass
        
    return False

def get_systemd_service_name():
    """尝试获取当前systemd服务的名称"""
    # 从环境变量获取
    if 'UNIT' in os.environ:
        return os.environ['UNIT']
        
    # 从cgroup信息获取
    try:
        with open('/proc/self/cgroup', 'r') as f:
            for line in f:
                if 'system.slice/' in line:
                    # 格式通常是: .../system.slice/服务名.service
                    match = re.search(r'system.slice/(.+?\.service)', line)
                    if match:
                        return match.group(1)
    except IOError:
        pass
        
    # 尝试通过systemctl命令获取
    try:
        import subprocess
        result = subprocess.check_output(
            ['systemctl', 'status', str(os.getpid())],
            stderr=subprocess.STDOUT,
            text=True
        )
        match = re.search(r'Loaded: loaded (.+?\.service)', result)
        if match:
            return match.group(1)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
        
    return None

def get_systemd_service_info():
    """获取更详细的systemd服务信息"""
    service_name = get_systemd_service_name()
    if not service_name:
        return None
        
    try:
        import subprocess
        result = subprocess.check_output(
            ['systemctl', 'show', service_name],
            stderr=subprocess.STDOUT,
            text=True
        )
        
        info = {}
        for line in result.split('\n'):
            if '=' in line:
                key, value = line.split('=', 1)
                info[key] = value
        return info
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

if __name__ == "__main__":
    print(f"是否在systemd服务中运行: {is_running_as_systemd_service()}")
    
    service_name = get_systemd_service_name()
    print(f"服务名称: {service_name if service_name else '未知'}")
    
    service_info = get_systemd_service_info()
    if service_info:
        print("\n服务详细信息:")
        print(f"描述: {service_info.get('Description', '未知')}")
        print(f"状态: {service_info.get('ActiveState', '未知')}")
        print(f"启动用户: {service_info.get('User', '未知')}")
        print(f"启动路径: {service_info.get('ExecStart', '未知').split()[0] if 'ExecStart' in service_info else '未知'}")

