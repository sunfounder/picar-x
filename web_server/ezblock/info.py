from ezblock.utils import getIP
class Info():
    file_dir = "/opt/ezblock"
    info = {
        "name": "",
        "libs": [],
        "ip": "",
    }
    DEBUG = False # Set to True to see debug infomation

    def __init__(self):
        pass

    def debug(self, msg, end='\n'):
        if self.DEBUG:
            print(msg, end=end)

    def _check_info_file(self):
        import os
        all_files = os.listdir(self.file_dir)
        if '.info' in all_files:
            self.debug("info file exist, skip")
            return True
        else:
            self.debug("info file missing, creating.")
            with open('%s/.info'%self.file_dir, 'w') as f:
                f.write('')

    def set(self, name, value):
        self._check_info_file()
        with open('%s/.info'%self.file_dir, 'r') as f:
            lines = f.readlines()
        is_exist = False
        for i in range(len(lines)):
            line = lines[i]
            if line.startswith('%s: '%name):
                if name != "libs":
                    lines[i] = "%s: %s\n"%(name, value)
                    is_exist = True
                    break
                else:
                    _temp = line.replace('libs: ', '').split("==")
                    _value = value.split("==")
                    if len(_value) == 2 and len(_temp) == 2:
                        lib = _value[0]
                        _lib = _temp[0]
                        if lib == _lib:
                            lines[i] = "%s: %s\n"%(name, value)
                            is_exist = True
                            break
        if not is_exist:
            lines.append("%s: %s\n"%(name, value))
        content = ''.join(lines)
        with open('%s/.info'%self.file_dir, 'w') as f:
            f.write(content)

    def set_library(self, name, ver):
        self.set("libs", "%s==%s"%(name,ver))

    def get(self):
        self._check_info_file()
        ip = getIP()
        if ip:
            self.set("ip", ip)
        self.debug("get info")
        with open('%s/.info'%self.file_dir, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if ": " in line:
                line = line.strip().split(": ")
                arg = line[0]
                val = line[1]
                if arg in self.info:
                    if isinstance(self.info[arg], list):
                        self.info[arg].append(val)
                    else:
                        self.info[arg] = val
        self.debug(self.info)
        return self.info
