#!/usr/bin/env python3
import curses
from picarx import PiCarX
from statistics import median
from threading import Thread, Lock
from time import sleep

ACS_ULCORNER = chr(0x256D)  # 左上角 ╭
ACS_URCORNER = chr(0x256E)  # 右上角 ╮
ACS_LLCORNER = chr(0x2570)  # 左下角 ╰
ACS_LRCORNER = chr(0x256F)  # 右下角 ╯

class Calibration:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.car = PiCarX()
        self.current_mode = 0  # 0: 灰度校准, 1: 伺服电机校准
        self.modes = ["Grayscale Calibration", "Servo & Motor Calibration"]
        self.running = False
        self.info_thread = None
        self.grayscale_read_lock = Lock()
        
        # 灰度校准变量
        self.dark_value = None
        self.light_value = None
        self.cliff_threshold = self.car.grayscale.cliff_threshold
        self.status = "Waiting for operation..."
        self.line_position = ""
        
        # 伺服电机校准变量
        self.servo_step = 0.1
        self.power = 30
        self.motor_runs = False
        
        # 初始化curses
        curses.curs_set(0)  # 隐藏光标
        curses.noecho()
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)   # 标题颜色
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # 正常文本
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)# 警告文本
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)   # 错误文本
        curses.init_pair(5, curses.COLOR_WHITE, -1) # 内容背景色（使用终端默认背景）
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_WHITE)  # 选中标签高亮
        curses.init_pair(7, curses.COLOR_CYAN, -1)  # 非活动标签边框(使用CYAN替代GRAY)
        curses.init_pair(8, curses.COLOR_CYAN, -1)   # 内容区域边框
        
        self.stdscr.nodelay(1)  # 非阻塞输入
        self.current_height, self.current_width = self.stdscr.getmaxyx()
        self.content_width = 80
        self.content_height = 18
        
        # 首次绘制界面
        self.initial_draw()

    def get_median_data(self, times=10):
        """获取传感器数据的中位数"""
        left_datas = []
        middle_datas = []
        right_datas = []
        
        for _ in range(times):
            with self.grayscale_read_lock:
                g0, g1, g2 = self.car.get_grayscale_data(raw=True)
            left_datas.append(g0)
            middle_datas.append(g1)
            right_datas.append(g2)
            sleep(0.01)
        
        return [median(left_datas), median(middle_datas), median(right_datas)]

    def calculate_cliff_threshold(self):
        """计算悬崖检测阈值"""
        datas = []
        for _ in range(10):
            with self.grayscale_read_lock:
                datas += self.car.get_grayscale_data()
            sleep(0.01)
        
        self.cliff_threshold = max(datas) * 1.5
        self.cliff_threshold = round(self.cliff_threshold)
        self.update_region('data3', "Cliff Threshold", self.cliff_threshold)

    def check_window_resize(self):
        """检查窗口大小是否变化"""
        height, width = self.stdscr.getmaxyx()
        if height != self.current_height or width != self.current_width:
            self.current_height, self.current_width = height, width
            self.initial_draw()
            return True
        return False

    def initial_draw(self):
        """绘制或重新绘制整个界面"""
        self.stdscr.clear()
        height, width = self.current_height, self.current_width
        
        # 计算内容区域偏移量
        self.offset_x = max(0, (width - self.content_width) // 2)
        
        # 检查窗口是否足够大
        min_height = 25
        min_width = 80
        
        if height < min_height or width < min_width:
            self.stdscr.addstr(0, 0, f"Please resize terminal (at least {min_width}x{min_height})", curses.color_pair(4))
            self.stdscr.refresh()
            return
        
        # 计算内容区域垂直居中位置
        self.content_start_y = max(1, (height - self.content_height) // 2)
        
        # 动态计算内容区域坐标，确保垂直居中
        content_height = 25  # 增加内容区域高度以避免重叠
        start_y = max(3, (height - content_height) // 2) + 1
        end_y = start_y + content_height
        self.content_width = 80  # 固定内容框宽度为80
        self.content_area = (start_y, (width - self.content_width) // 2, end_y, (width - self.content_width) // 2 + self.content_width - 1)
        start_y, start_x, end_y, end_x = self.content_area
        
        # 绘制内容区域底色背景
        for y in range(start_y, end_y):
            self.stdscr.addstr(y, start_x, ' ' * (end_x - start_x), curses.color_pair(5))
        
        # 屏幕区域定义
        # 调整区域坐标以适应内容边框
        self.regions = {
            'title': (0, 0),
            'tag': (start_y+1, start_x),
            'instructions': (start_y+4, start_x),
            'data1': (start_y + 17, start_x + 2),
            'data2': (start_y + 18, start_x + 2),
            'data3': (start_y + 19, start_x + 2),
            'data4': (start_y + 20, start_x + 2),
            'data5': (start_y + 21, start_x + 2),
            'data6': (start_y + 22, start_x + 2),
            'data7': (start_y + 23, start_x + 2),
            'log': (-2, 0),
            'status_bar': (-1, 0)
        }
        
        # 绘制标题
        title = "PiCar-X Calibration Tool"
        title_bar = title.center(width, '-')
        self.stdscr.addstr(0, 0, title_bar, curses.color_pair(1))
        
        # 绘制浏览器式标签页和内容边框
        content_end_y, content_end_x = self.stdscr.getmaxyx()
        content_end_y -= 2
        content_end_x -= 2

        # 绘制内容区域边框
        self.stdscr.attron(curses.color_pair(8))
        # 上边框
        self.stdscr.hline(start_y, start_x, curses.ACS_HLINE, end_x - start_x)
        # 下边框
        self.stdscr.hline(end_y, start_x, curses.ACS_HLINE, end_x - start_x)
        # 左边框
        self.stdscr.vline(start_y, start_x, curses.ACS_VLINE, end_y - start_y)
        # 右边框
        self.stdscr.vline(start_y, end_x, curses.ACS_VLINE, end_y - start_y)
        # 四个角
        self.stdscr.addch(start_y, start_x, ACS_ULCORNER)
        self.stdscr.addch(start_y, end_x, ACS_URCORNER)
        self.stdscr.addch(end_y, start_x, ACS_LLCORNER)
        self.stdscr.addch(end_y, end_x, ACS_LRCORNER)
        self.stdscr.attroff(curses.color_pair(8))

        # 标签页宽度最大化，两个占满内容区域宽度
        tab_width = self.content_width // 2
        # 标签页与内容框左对齐
        tab1_start_x = start_x + 1
        tab2_start_x = tab1_start_x + tab_width

        tab_start_y = self.regions["tag"][0]
        self.stdscr.attron(curses.color_pair(7))
        # Draw tag text
        self.stdscr.addstr(tab_start_y, tab1_start_x, f'{self.modes[0].center(tab_width - 2)}')
        self.stdscr.addstr(tab_start_y, tab2_start_x, f'{self.modes[1].center(tab_width - 2)}')
        # 绘制从标签页到内容区域的垂直线
        self.stdscr.vline(tab_start_y, tab2_start_x-1, curses.ACS_VLINE, 1, curses.color_pair(8))
        # Draw change tab connections
        if self.current_mode == 0:
            self.stdscr.hline(tab_start_y+1, tab2_start_x, curses.ACS_HLINE, tab_width-2, curses.color_pair(8))
            self.stdscr.addch(start_y, tab2_start_x-1, ACS_URCORNER)
            self.stdscr.addch(tab_start_y+1, tab2_start_x-1, ACS_LLCORNER)
            self.stdscr.addch(tab_start_y+1, end_x, ACS_URCORNER)
        else:
            self.stdscr.hline(tab_start_y+1, tab1_start_x, curses.ACS_HLINE, tab_width-1, curses.color_pair(8))
            self.stdscr.addch(start_y, tab2_start_x-1, ACS_ULCORNER)
            self.stdscr.addch(tab_start_y+1, tab2_start_x-1, ACS_LRCORNER)
            self.stdscr.addch(tab_start_y+1, start_x, ACS_ULCORNER)

        # 根据当前模式在内容区域内绘制不同内容
        if self.current_mode == 0:
            self.draw_grayscale_mode()
        else:
            self.draw_servo_motor_mode()
        
        # 绘制底部状态栏
        self.update_status_bar()
        self.stdscr.refresh()

    def update_log(self, text):
        """更新日志区域"""
        y, x = self.regions['log']
        self.stdscr.addstr(y, x, " " * (self.content_width - 2))
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()

    def draw_grayscale_mode(self):
        """绘制灰度传感器校准界面"""
        # 绘制使用说明
        instructions = [
            "  - Place all 3 sensors on the DARK area and press [Q] to set dark values",
            "  - Place all 3 sensors on the LIGHT area and press [W] to set light values",
            "  - Press [E] to calculate cliff detection threshold automatically",
            "",
            "      ▓▓▓▓▓▓▓▓▓▓▓▓▓              ┌───────────┐                 ┌─────┐  ",
            "      ▓▓▓┌─────┐▓▓▓              │  ┌─────┐  │                 └┌───┐┘",
            "      ▓▓▓└┌───┐┘▓▓▓              └──└┌───┐┘──┘           ┌──┌─┐─│   │─┌─┐──┐",
            "      ┌─┐ │   │ ┌─┐              ┌─┐ │   │ ┌─┐           │  │ │=│   │=│ │  │",
            "      │ │=│   │=│ │              │ │=│   │=│ │           │  └─┘ │   │ └─┘  │",
            "      └─┘ │   │ └─┘              └─┘ │   │ └─┘           │     /     \     │",
            "           [Q]                        [W]                        [E]",
            ""
        ]
        
        # 调整内容绘制位置以适应边框
        start_y, start_x, end_y, end_x = self.content_area
        instruction_start_y = self.regions['instructions'][0]

        self.stdscr.attron(curses.color_pair(5))
        for y, line in enumerate(instructions):
            current_y = instruction_start_y + y
            if current_y < end_y:
                x = start_x + 1
                display_line = line[:end_x - start_x - 2]
                self.stdscr.addstr(current_y, x, display_line)

            # 计算数据区域起始Y坐标（最后一条指令下方2行）
        self.update_region('data1', "Dark Values", f"{self.dark_value if self.dark_value is not None else 'Not set'}")
        self.update_region('data2', "Light Values", f"{self.light_value if self.light_value is not None else 'Not set'}")
        self.update_region('data3', "Cliff Threshold", f"{self.cliff_threshold:.2f}")
        self.update_region('data4', "Raw Values", "")
        self.update_region('data5', "Calibrated Values", "")
        self.update_region('data6', "Status", f"{self.status}")
        self.update_region('data7', "Line Position", f"{self.line_position}")

    def draw_servo_motor_mode(self):
        """绘制伺服电机校准界面"""
        # 绘制使用说明
        instructions = [
            "  - Use W/A/S/D to adjust the up/down/left/right offsets of the camera",
            "  - Use Q/E to adjust the left/right offsets of steering servo",
            "  - Use Z/C to toggle left/right motor reversal",
            "",
            "                                                  ┌─────┐",
            "                 [W]                              └┌───┐┘",
            "                  ▲                            ┌─┐ │   │ ┌─┐",
            "                ├───┤                     [Q]◀ │ │=│   │=│ │ ▶[E]",
            "           [A]◀ │ O │ ▶[S]                     └─┘ │   │ └─┘",
            "                └┬─┬┘                          ┌─┐/     \┌─┐",
            "                  ▼                       [Z]⇅ │ ││     ││ │ ⇅[C]",
            "                 [D]                           └─┘│     │└─┘",
            "                                                  └─────┘",
            ""
        ]
        
        # 调整内容绘制位置以适应边框
        start_y, start_x, end_y, end_x = self.content_area
        instruction_start_y = self.regions['instructions'][0]

        self.stdscr.attron(curses.color_pair(5))
        for y, line in enumerate(instructions):
            current_y = instruction_start_y + y
            if current_y < end_y:
                x = start_x + 1
                display_line = line[:end_x - start_x - 2]
                self.stdscr.addstr(current_y, x, display_line)

        # 计算数据区域起始Y坐标（最后一条指令下方2行）
        # 初始化各区域
        self.update_region('data1', "Steering Servo Offset", f"{self.car.steering_servo.offset():.2f}")
        self.update_region('data2', "Camera Pan Servo Offset", f"{self.car.camera_pan_servo.offset():.2f}")
        self.update_region('data3', "Camera Tilt Servo Offset", f"{self.car.camera_tilt_servo.offset():.2f}")
        self.update_region('data4', "Left Motor Reversed", f"{self.car.motors.left_reversed}")
        self.update_region('data5', "Right Motor Reversed", f"{self.car.motors.right_reversed}")

    def update_region(self, region_name, name, value, attr=0):
        """更新指定区域的内容"""
        height, width = self.current_height, self.current_width
        y, x = self.regions[region_name]

        name_width = 25
        value_width = 45
        value_text = str(value)
        
        # 处理底部行
        if y == -1:
            y = height - 1
        
        # 确保不超出屏幕范围
        if y < height:
            # Clear the region
            self.stdscr.addstr(y, x, ' ' * (name_width+value_width), curses.color_pair(5))
            self.stdscr.addstr(y, x, f"{name:>{name_width}}: {value_text:<{value_width}}", attr | curses.color_pair(5))

    def update_status_bar(self):
        """更新底部状态栏"""
        try:
            current_height, current_width = self.stdscr.getmaxyx()
            if current_height < 1 or current_width < 1:
                return
            status_bar = " Press [Tab] to switch modes | [Ctrl+C] to exit "
            status_bar = status_bar.center(current_width, ' ')
            self.stdscr.addstr(current_height - 1, 0, status_bar, curses.A_REVERSE)
        except curses.error:
            pass

    def update_display(self, grayscale_raw_data=None):
        """更新显示内容"""
        if self.check_window_resize():
            return
        
        height, width = self.current_height, self.current_width
        min_height = 25
        min_width = 80
        
        if height < min_height or width < min_width:
            self.stdscr.clear()
            self.stdscr.addstr(0, 0, f"Please resize terminal (at least {min_width}x{min_height})", curses.color_pair(4))
            self.stdscr.refresh()
            return
        
        # 根据当前模式更新显示
        if self.current_mode == 0:
            self.update_grayscale_display(grayscale_raw_data)
        else:
            self.update_servo_motor_display()
        
        self.stdscr.noutrefresh()
        curses.doupdate()

    def update_grayscale_display(self, grayscale_raw_data=None):
        """更新灰度校准显示"""
        # 更新暗色值
        text = self.dark_value if self.dark_value is not None else 'Not set'
        attr = curses.color_pair(2) if self.dark_value is not None else curses.color_pair(3)
        self.update_region('data1', "Dark Values", text, attr)
        
        # 更新亮色值
        text = self.light_value if self.light_value is not None else 'Not set'
        attr = curses.color_pair(2) if self.light_value is not None else curses.color_pair(3)
        self.update_region('data2', "Light Values", text, attr)
        
        # 更新悬崖阈值
        self.update_region('data3', "Cliff Threshold", self.cliff_threshold)
        
        # 获取并检查原始值
        self.update_region('data4', "Raw Values", grayscale_raw_data)
        
        # 获取并检查校准值
        calibrated_values = self.car.grayscale.calibrate_data(grayscale_raw_data)
        self.update_region('data5', "Calibrated Values", calibrated_values)
        
        # 更新状态
        attr = curses.color_pair(2) if "On line" in self.status else \
                curses.color_pair(4) if "Cliff" in self.status else \
                curses.color_pair(3)
        self.update_region('data6', "Status", self.status, attr)
        
        # 检查并更新线路位置
        self.update_region('data7', "Line Position", self.line_position)

    def update_servo_motor_display(self):
        """更新伺服电机校准显示"""
        self.update_region('data1', "Steering Servo Offset", f"{self.car.steering_servo.offset():.2f}")
        self.update_region('data2', "Camera Pan Servo Offset", f"{self.car.camera_pan_servo.offset():.2f}")
        self.update_region('data3', "Camera Tilt Servo Offset", f"{self.car.camera_tilt_servo.offset():.2f}")
        self.update_region('data4', "Left Motor Reversed", f"{self.car.motors.left_reversed}")
        self.update_region('data5', "Right Motor Reversed", f"{self.car.motors.right_reversed}")

    def update_sensor_status(self):
        """更新传感器状态信息"""
        while self.running:
            if self.current_mode == 0:
                with self.grayscale_read_lock:
                    grayscale_raw_data = self.car.get_grayscale_data(raw=True)
                calibrated_data = self.car.grayscale.calibrate_data(grayscale_raw_data)
                
                if self.car.is_on_cliff(data=calibrated_data):
                    self.status = "Cliff detected!"
                elif self.car.is_on_line(data=calibrated_data):
                    position = self.car.get_line_position(data=calibrated_data)
                    self.line_position = self._get_line_position_text(position)
                    self.status = "On line"
                else:
                    self.status = "Off line"
                
                self.update_display(grayscale_raw_data)
            else:
                # 伺服电机模式下定期更新显示
                self.update_display()
                
            
            sleep(0.1)

    def _get_line_position_text(self, position):
        """生成线路位置的可视化文本"""
        pos_text = [" "]*21
        pos_idx = int((position + 1) * 10)
        pos_idx = max(0, min(20, pos_idx))
        pos_text[pos_idx] = "█"
        return f"Position: {''.join(pos_text)} ({position:.2f})"

    def run(self):
        """主运行循环"""
        self.running = True
        self.info_thread = Thread(target=self.update_sensor_status)
        self.info_thread.start()

        try:
            while True:
                key = self.stdscr.getch()
                if key == ord('\t'):  # Tab键切换模式
                    self.current_mode = 1 - self.current_mode
                    self.initial_draw()
                elif key == ord('q') and self.current_mode == 0:  # 设置暗值
                    self.dark_value = self.get_median_data()
                elif key == ord('w') and self.current_mode == 0:  # 设置亮值
                    self.light_value = self.get_median_data()
                elif key == ord('e') and self.current_mode == 0:  # 计算悬崖阈值
                    self.calculate_cliff_threshold()
                elif self.current_mode == 1:  # 舵机电机校准模式
                    if key == ord('w'):  # 摄像头向上
                        offset = self.car.camera_tilt_servo.offset() 
                        offset -= self.servo_step
                        self.car.set_camera_tilt_offset(offset)
                    elif key == ord('s'):  # 摄像头向下
                        offset = self.car.camera_tilt_servo.offset()
                        offset += self.servo_step
                        self.car.set_camera_tilt_offset(offset)
                    elif key == ord('a'):  # 摄像头向左
                        offset = self.car.camera_pan_servo.offset()
                        offset -= self.servo_step
                        self.car.set_camera_pan_offset(offset)
                    elif key == ord('d'):  # 摄像头向右
                        offset = self.car.camera_pan_servo.offset()
                        offset += self.servo_step
                        self.car.set_camera_pan_offset(offset)
                    elif key == ord('q'):  # 转向舵机向左
                        offset = self.car.steering_servo.offset()
                        offset -= self.servo_step
                        self.car.set_steering_offset(offset)
                    elif key == ord('e'):  # 转向舵机向右
                        offset = self.car.steering_servo.offset()
                        offset += self.servo_step
                        self.car.set_steering_offset(offset)
                    elif key == ord('z'):  # 左电机反转切换
                        reversed = self.car.motors.left_reversed
                        reversed = not reversed
                        self.car.set_left_motor_reverse(reversed)
                        self.car.forward(10)
                        sleep(2)
                        self.car.stop()
                    elif key == ord('c'):  # 右电机反转切换
                        reversed = self.car.motors.right_reversed
                        reversed = not reversed
                        self.car.set_right_motor_reverse(reversed)
                        self.car.forward(10)
                        sleep(2)
                        self.car.stop()

                # 检查是否可以校准
                if self.dark_value is not None and self.light_value is not None:
                    self.car.calibrate_grayscale(self.light_value, self.dark_value)
                
                # 清空输入缓冲区，防止按键事件堆积
                curses.flushinp()
                sleep(0.1)
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            self.info_thread.join()


def main():
    """主函数，启动校准程序"""
    try:
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        calibrator = Calibration(stdscr)
        calibrator.run()
    except KeyboardInterrupt:
        print("程序已退出")
    finally:
        # 确保资源正确释放
        curses.endwin()


if __name__ == "__main__":
    main()
