#!/usr/bin/env python3
import curses
from picarx.picarx import PiCarX
from statistics import median
from threading import Thread, Lock
from time import sleep

# Border character constants
ACS_ULCORNER = chr(0x256D)  # Upper left corner ╭
ACS_URCORNER = chr(0x256E)  # Upper right corner ╮
ACS_LLCORNER = chr(0x2570)  # Lower left corner ╰
ACS_LRCORNER = chr(0x256F)  # Lower right corner ╯

class Calibration:
    """Main class for PiCar-X calibration tool, supporting grayscale sensor and servo/motor calibration"""
    
    # Operation modes
    MODE_GRAYSCALE = 0
    MODE_SERVO = 1

    # Color definitions
    COLOR_TITLE = 1
    COLOR_STATUS = 2
    COLOR_HIGHLIGHT = 3
    COLOR_WARNING = 4
    COLOR_ERROR = 5
    COLOR_NORMAL = 6
    COLOR_BORDER = 7
    COLOR_STATUS_ERROR = 8
    COLOR_STATUS_NORMAL = 9
    COLOR_STATUS_WARNING = 10
    
    # Interface constants
    CONTENT_WIDTH = 80
    CONTENT_HEIGHT = 23
    MIN_WIDTH = CONTENT_WIDTH
    MIN_HEIGHT = CONTENT_HEIGHT + 2
    TAB_WIDTH = 20

    # Calibration constants
    SERVO_STEP = 0.1
    DATA_SAMPLE_TIMES = 10
    MOTOR_POWER = 20

    # Others
    HELP_MESSAGE = "Press [Tab] to switch modes | [Ctrl+C] to exit "
    
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.car = PiCarX()
        self.current_mode = self.MODE_GRAYSCALE
        self.modes = ["Grayscale", "Servos & Motors"]
        self.running = False
        self.info_thread = None
        self.grayscale_read_lock = Lock()
        self.current_height, self.current_width = self.stdscr.getmaxyx()
        
        # Grayscale calibration parameters
        self.tilt_offset = self.car.camera_tilt_servo.offset()
        self.pan_offset = self.car.camera_pan_servo.offset()
        self.steering_offset = self.car.steering_servo.offset()
        self.left_reversed = self.car.motors.left_reversed
        self.right_reversed = self.car.motors.right_reversed
        self.dark_value = None
        self.light_value = None
        self.cliff_threshold = self.car.grayscale.cliff_threshold
        self.status = ""
        self.line_position = ""
        
        # Initialize curses environment
        self._init_curses()
        self.initial_draw()

    def is_too_small(self):
        height, width = self.stdscr.getmaxyx()
        return  height < self.MIN_HEIGHT or width < self.MIN_WIDTH

    def _init_curses(self):
        """Initialize curses environment settings"""
        curses.curs_set(0)          # Hide cursor
        curses.noecho()             # Disable input echoing
        curses.start_color()        # Enable color support
        
        # Initialize color pairs
        curses.init_pair(self.COLOR_TITLE, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(self.COLOR_STATUS, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(self.COLOR_BORDER, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(self.COLOR_HIGHLIGHT, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(self.COLOR_WARNING, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(self.COLOR_ERROR, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(self.COLOR_NORMAL, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(self.COLOR_STATUS_ERROR, curses.COLOR_RED, curses.COLOR_WHITE)
        curses.init_pair(self.COLOR_STATUS_NORMAL, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(self.COLOR_STATUS_WARNING, curses.COLOR_YELLOW, curses.COLOR_WHITE)
        
        self.stdscr.nodelay(1)  # Non-blocking input

    def get_median_data(self, times=DATA_SAMPLE_TIMES):
        """Get median samples from grayscale sensors
        
        Args:
            times: Number of samples to take
        
        Returns:
            List containing median values from left, middle, and right sensors
        """
        samples = [[], [], []]  # Left, middle, right
        
        for _ in range(times):
            with self.grayscale_read_lock:
                left, middle, right = self.car.get_grayscale_data(raw=True)
            samples[0].append(left)
            samples[1].append(middle)
            samples[2].append(right)
            sleep(0.01)
        
        return [median(samples[i]) for i in range(3)]

    def calculate_cliff_threshold(self):
        """Automatically calculate cliff detection threshold"""
        samples = []
        for _ in range(10):
            with self.grayscale_read_lock:
                samples += self.car.get_grayscale_data()
            sleep(0.01)
        
        self.cliff_threshold = max(samples) * 1.5
        self.cliff_threshold = round(self.cliff_threshold)
        self.update_region('gs_cliff', "Cliff Threshold", self.cliff_threshold)
        self.update_log("Cliff threshold set to: {}".format(self.cliff_threshold))

    def check_window_resize(self):
        """Check if window size has changed and update dimensions"""
        try:
            height, width = self.stdscr.getmaxyx()
            if height != self.current_height or width != self.current_width:
                self.current_height, self.current_width = height, width
                self.initial_draw()
                return True
        except curses.error:
            pass
        return False

    def initial_draw(self):
        """Draw or redraw the entire interface"""
        self.stdscr.clear()
        
        self._calculate_content_area()

        # Check if window is large enough
        if self.is_too_small():
            self._draw_window_too_small_message()
            return

        self._draw_title()
        self._draw_borders()
        self._draw_tabs()
        self._initialize_mode_content()
        self.update_status_bar()
        self.stdscr.refresh()
        
    def _draw_window_too_small_message(self):
        """Display message when window size is insufficient"""
        height, width = self.stdscr.getmaxyx()
        msg = f"Please resize terminal (at least 80x25), current size: {width}x{height}"
        msg_width = len(msg)
        center_y = height // 2
        msg_x = (width - msg_width) // 2
        border_start_x = msg_x - 2
        border_start_y = center_y - 2
        border_end_x = msg_x + msg_width + 2
        border_end_y = center_y + 2

        self.stdscr.clear()

        self.stdscr.addstr(center_y, msg_x, msg, curses.color_pair(self.COLOR_ERROR))

        # Draw boarder
        self.stdscr.attron(curses.color_pair(self.COLOR_BORDER))
        self.stdscr.hline(border_start_y, border_start_x, curses.ACS_HLINE, msg_width + 4)
        self.stdscr.hline(border_end_y, border_start_x, curses.ACS_HLINE, msg_width + 4)
        self.stdscr.vline(border_start_y, border_start_x, curses.ACS_VLINE, 4)
        self.stdscr.vline(border_start_y, border_end_x, curses.ACS_VLINE, 4)
        self.stdscr.addstr(border_start_y, border_start_x, ACS_ULCORNER)
        self.stdscr.addstr(border_start_y, border_end_x, ACS_URCORNER)
        self.stdscr.addstr(border_end_y, border_start_x, ACS_LLCORNER)
        self.stdscr.addstr(border_end_y, border_end_x, ACS_LRCORNER)
        self.stdscr.attroff(curses.color_pair(self.COLOR_BORDER))

        self.stdscr.refresh()
        
    def _calculate_content_area(self):
        """Calculate coordinates for content area and display regions"""
        height, width = self.stdscr.getmaxyx()
        start_y = (height - self.CONTENT_HEIGHT) // 2
        end_y = start_y + self.CONTENT_HEIGHT
        content_start_x = (width - self.CONTENT_WIDTH) // 2
        content_end_x = content_start_x + self.CONTENT_WIDTH - 1
        
        self.content_area = (start_y, content_start_x, end_y, content_end_x)
        
        # Define display regions
        self.regions = {
            'title': (0, 0),
            'tab': (start_y+1, content_start_x),
            'instructions': (start_y+3, content_start_x),
            'gs_dark': (start_y + 15, content_start_x + 2),
            'gs_light': (start_y + 16, content_start_x + 2),
            'gs_cliff': (start_y + 17, content_start_x + 2),
            'gs_raw': (start_y + 18, content_start_x + 2),
            'gs_calibrated': (start_y + 19, content_start_x + 2),
            'gs_status': (start_y + 20, content_start_x + 2),
            'gs_position': (start_y + 21, content_start_x + 2),

            'steering': (start_y + 17, content_start_x + 2),
            'pan': (start_y + 18, content_start_x + 2),
            'tilt': (start_y + 19, content_start_x + 2),
            'lmotor': (start_y + 20, content_start_x + 2),
            'rmotor': (start_y + 21, content_start_x + 2),
            'status_bar': (-1, 0)  # Bottom row
        }
        
    def _draw_title(self):
        """Draw main title bar"""
        height, width = self.stdscr.getmaxyx()
        title = f"PiCar-X Calibration Tool"
        title_bar = title.center(width)
        self.stdscr.addstr(0, 0, title_bar, curses.color_pair(self.COLOR_TITLE))

    def _draw_borders(self):
        """Draw borders for content area"""
        start_y, start_x, end_y, end_x = self.content_area
        start_y = start_y + 2
        end_y = end_y - 1
        
        self.stdscr.attron(curses.color_pair(self.COLOR_BORDER))
        self.stdscr.hline(start_y, start_x, curses.ACS_HLINE, end_x - start_x)  # Top
        self.stdscr.hline(end_y, start_x, curses.ACS_HLINE, end_x - start_x)  # Bottom
        self.stdscr.vline(start_y, start_x, curses.ACS_VLINE, end_y - start_y)  # Left
        self.stdscr.vline(start_y, end_x, curses.ACS_VLINE, end_y - start_y)  # Right
        
        # Draw corners
        self.stdscr.addch(start_y, end_x, ACS_URCORNER)
        self.stdscr.addch(end_y, start_x, ACS_LLCORNER)
        self.stdscr.addch(end_y, end_x, ACS_LRCORNER)
        self.stdscr.attroff(curses.color_pair(self.COLOR_BORDER))

    def _draw_tabs(self):
        """Draw mode selection tabs"""
        start_y, start_x, end_y, end_x = self.content_area
        tab_y, _ = self.regions["tab"]
        tab_end_y = tab_y + 1
        tab_start_y = tab_y - 1

        for i, mode in enumerate(self.modes):
            current_tab_start_x = start_x + i * (self.TAB_WIDTH + 1)
            current_tab_end_x = current_tab_start_x + self.TAB_WIDTH + 1
            mode = mode.center(self.TAB_WIDTH)
            print(f"{mode}")
            self.stdscr.attron(curses.color_pair(self.COLOR_NORMAL))
            self.stdscr.addstr(tab_y, current_tab_start_x + 1, mode)
            self.stdscr.attron(curses.color_pair(self.COLOR_BORDER))
            self.stdscr.hline(tab_start_y, current_tab_start_x, curses.ACS_HLINE, self.TAB_WIDTH+2)
            self.stdscr.vline(tab_y, current_tab_start_x, curses.ACS_VLINE, 1)
            self.stdscr.vline(tab_y, current_tab_end_x, curses.ACS_VLINE, 1)
            self.stdscr.addch(tab_start_y, current_tab_start_x, ACS_ULCORNER)
            self.stdscr.addch(tab_start_y, current_tab_end_x, ACS_URCORNER)

        # Active tab style
        active_start_x = start_x + self.current_mode * (self.TAB_WIDTH + 1)
        active_end_x = active_start_x + self.TAB_WIDTH + 1
        self.stdscr.addch(tab_start_y, active_start_x, ACS_ULCORNER)
        self.stdscr.addch(tab_start_y, active_end_x, ACS_URCORNER)
        # add tab left bottom corner and top left corner except the first one
        if self.current_mode != 0:
            self.stdscr.addch(tab_end_y, active_start_x, ACS_LRCORNER)
            self.stdscr.addch(tab_end_y, start_x, ACS_ULCORNER)
        self.stdscr.addch(tab_end_y, active_end_x, ACS_LLCORNER)
        self.stdscr.hline(tab_end_y, active_start_x+1, " ", self.TAB_WIDTH)

    def _initialize_mode_content(self):
        """Initialize content display for current mode"""
        if self.current_mode == self.MODE_GRAYSCALE:
            self._draw_mode_instructions(self._get_grayscale_instructions())
            self._initialize_grayscale_regions()
        else:
            self._draw_mode_instructions(self._get_servo_instructions())
            self._initialize_servo_regions()

    def _draw_mode_instructions(self, instructions):
        """Draw mode-specific operation instructions"""
        start_y, start_x, end_y, end_x = self.content_area
        instruction_start_y = self.regions['instructions'][0]
        
        self.stdscr.attron(curses.color_pair(self.COLOR_NORMAL))
        for y, line in enumerate(instructions):
            current_y = instruction_start_y + y
            if current_y < end_y:
                display_line = line[:end_x - start_x - 2]
                self.stdscr.addstr(current_y, start_x + 1, display_line)

    def _get_grayscale_instructions(self):
        """Get operation instructions for grayscale calibration mode"""
        return [
            "  - Place all 3 sensors on DARK area and press [Q] to set dark values",
            "  - Place all 3 sensors on LIGHT area and press [W] to set light values",
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

    def _get_servo_instructions(self):
        """Get operation instructions for servo/motor calibration mode"""
        return [
            "  - Use W/A/S/D to adjust camera up/down/left/right offsets",
            "  - Use Q/E to adjust steering servo left/right offsets",
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

    def _initialize_grayscale_regions(self):
        """Initialize data display regions for grayscale calibration mode"""
        self.update_region('gs_dark', "Dark Values", self.dark_value or 'Not set')
        self.update_region('gs_light', "Light Values", self.light_value or 'Not set')
        self.update_region('gs_cliff', "Cliff Threshold", self.cliff_threshold)
        self.update_region('gs_raw', "Raw Values", "")
        self.update_region('gs_calibrated', "Calibrated Values", "")
        self.update_region('gs_status', "Status", self.status)
        self.update_region('gs_position', "Line Position", self.line_position)

    def _initialize_servo_regions(self):
        """Initialize data display regions for servo/motor calibration mode"""
        self.update_region('steering', "Steering Servo Offset", f"{self.car.steering_servo.offset():.2f}")
        self.update_region('pan', "Camera Pan Servo Offset", f"{self.car.camera_pan_servo.offset():.2f}")
        self.update_region('tilt', "Camera Tilt Servo Offset", f"{self.car.camera_tilt_servo.offset():.2f}")
        self.update_region('lmotor', "Left Motor Reversed", f"{self.car.motors.left_reversed}")
        self.update_region('rmotor', "Right Motor Reversed", f"{self.car.motors.right_reversed}")

    def update_region(self, region_name, name, value, attr=None):
        """Update display content for specified region
        
        Args:
            region_name: Name of the region
            name: Display name
            value: Display value
            attr: Text attributes
        """
        if attr is None:
            attr = curses.color_pair(self.COLOR_NORMAL)
        height, width = self.stdscr.getmaxyx()
        y, x = self.regions[region_name]
        
        # Handle bottom row
        if y == -1:
            y = height - 1
        
        if y > height:
            return

        name_width = 25
        value_width = 45
        if isinstance(value, float):
            value_text = f"{value:.2f}"
        else:
            value_text = str(value)
        
        # Clear and update region
        self.stdscr.addstr(y, x, ' ' * (name_width + value_width), curses.color_pair(self.COLOR_NORMAL))
        self.stdscr.addstr(y, x, f"{name:>{name_width}}: {value_text:<{value_width}}", attr)

    def update_status_bar(self):
        """Update bottom status bar"""
        try:
            height, width = self.stdscr.getmaxyx()
            if height < 1 or width < 1:
                return
                
            status_bar = self.HELP_MESSAGE.rjust(width)
            self.stdscr.addstr(height - 1, 0, status_bar, curses.color_pair(self.COLOR_STATUS))
        except curses.error:
            pass  # Handle window resize errors

    def update_log(self, msg, level='info'):
        """Update log with specified message"""
        height, width = self.stdscr.getmaxyx()
        width -= len(self.HELP_MESSAGE)

        if len(msg) > width:
            msg = msg[:width-3]
            msg += '...'

        if height < 1 or width < 1:
            return
        if level == "info":
            attr = curses.color_pair(self.COLOR_STATUS_NORMAL)
        elif level == "warning":
            attr = curses.color_pair(self.COLOR_STATUS_WARNING)
        elif level == "error":
            attr = curses.color_pair(self.COLOR_STATUS_ERROR)
        else:
            attr = curses.color_pair(self.COLOR_STATUS_NORMAL)
        
        self.stdscr.addstr(height-1, 0, msg, attr)

    def update_display(self, grayscale_raw_data=None):
        """Update dynamic display content
        
        Args:
            grayscale_raw_data: Raw data from grayscale sensors
        """
        if self.check_window_resize():
            return
        
        if self.is_too_small():
            return
            
        if self.current_mode == self.MODE_GRAYSCALE:
            self._update_grayscale_display(grayscale_raw_data)
        else:
            self._update_servo_display()
            
        self.stdscr.noutrefresh()
        curses.doupdate()

    def _update_grayscale_display(self, grayscale_raw_data=None):
        """Update display content for grayscale calibration mode"""
        # Update dark values with status color
        if self.dark_value is None:
            attr = curses.color_pair(self.COLOR_WARNING)
            text = 'Not set'
        elif self.is_dark_light_error():
            attr = curses.color_pair(self.COLOR_ERROR)
            text = self.dark_value
        else:
            attr = curses.color_pair(self.COLOR_HIGHLIGHT)
            text = self.dark_value
        self.update_region('gs_dark', "Dark Values", text, attr)
        
        # Update light values with status color
        if self.light_value is None:
            attr = curses.color_pair(self.COLOR_WARNING)
            text = 'Not set'
        elif self.is_dark_light_error():
            attr = curses.color_pair(self.COLOR_ERROR)
            text = self.light_value
        else:
            attr = curses.color_pair(self.COLOR_HIGHLIGHT)
            text = self.light_value
        self.update_region('gs_light', "Light Values", text, attr)
        
        # Update other values
        self.update_region('gs_cliff', "Cliff Threshold", self.cliff_threshold)
        self.update_region('gs_raw', "Raw Values", grayscale_raw_data)
        
        if grayscale_raw_data:
            calibrated_values = self.car.grayscale.calibrate_data(grayscale_raw_data)
            self.update_region('gs_calibrated', "Calibrated Values", calibrated_values)

        
        # Update status with appropriate color
        attr = curses.color_pair(self.COLOR_HIGHLIGHT) if "On line" in self.status else \
               curses.color_pair(self.COLOR_ERROR) if "Cliff" in self.status else \
               curses.color_pair(self.COLOR_WARNING)
        self.update_region('gs_status', "Status", self.status, attr)
        self.update_region('gs_position', "Line Position", self.line_position)

    def _update_servo_display(self):
        """Update display content for servo/motor calibration mode"""
        self.update_region('steering', "Steering Servo Offset", self.steering_offset)
        self.update_region('pan', "Camera Pan Servo Offset", self.pan_offset)
        self.update_region('tilt', "Camera Tilt Servo Offset", self.tilt_offset)
        self.update_region('lmotor', "Left Motor Reversed", self.left_reversed)
        self.update_region('rmotor', "Right Motor Reversed", self.right_reversed)

    def update_sensor_status(self):
        """Background thread to continuously update sensor status and display"""
        while self.running:
            if self.current_mode == self.MODE_GRAYSCALE:
                with self.grayscale_read_lock:
                    left, middle, right = self.car.get_grayscale_data(raw=True)
                
                # Check line and cliff status
                calibrated_data = self.car.grayscale.calibrate_data([left, middle, right])
                if self.car.is_on_cliff(data=calibrated_data):
                    self.status = "Cliff detected!"
                elif self.car.is_on_line(data=calibrated_data):
                    position = self.car.get_line_position(data=calibrated_data)
                    self.line_position = self._get_line_position_text(position)
                    self.status = "On line"
                else:
                    self.status = "Off line"
                
                self.update_display([left, middle, right])
            else:
                self.update_display()  # Update servo display periodically
            
            sleep(0.1)  # Reduce CPU usage

    def _get_line_position_text(self, position):
        """Generate visual text for line position
        
        Args:
            position: Normalized line position value (-1.0 to 1.0)
        
        Returns:
            String with visual indicator of line position
        """
        pos_text = [" "] * 21  # 21 character positions
        pos_idx = int((position + 1) * 10)  # Convert to index (0-20)
        pos_idx = max(0, min(20, pos_idx))  # Clamp to valid range
        pos_text[pos_idx] = "█"  # Place indicator
        
        return f"Position: {''.join(pos_text)} ({position:.2f})"

    def run(self):
        """Main execution loop"""
        self.running = True
        self.info_thread = Thread(target=self.update_sensor_status)
        self.info_thread.start()

        try:
            while True:
                # Check for window resize first
                if self.check_window_resize():
                    self.initial_draw()
                    self.update_display()
                
                key = self.stdscr.getch()
                self._handle_key_press(key)
                
                # Apply grayscale calibration if both values are set
                if self.dark_value and self.light_value and not self.is_dark_light_error():
                    self.car.calibrate_grayscale(self.light_value, self.dark_value)
                    self.update_log("Grayscale calibration applied")
                
                # Clear input buffer to prevent key event accumulation
                curses.flushinp()
                sleep(0.05)
        except KeyboardInterrupt:
            pass
        finally:
            self.running = False
            self.info_thread.join()

    def _handle_key_press(self, key):
        """Handle key press events
        
        Args:
            key: Key code
        """
        # Handle mode switching
        if key == ord('\t'):
            self.current_mode = (self.current_mode + 1) % len(self.modes)
            self.initial_draw()
            return
            
        # Handle mode-specific keys
        if self.current_mode == self.MODE_GRAYSCALE:
            self._handle_grayscale_keys(key)
        else:
            self._handle_servo_keys(key)

    def _handle_grayscale_keys(self, key):
        """Handle key presses for grayscale calibration mode"""
        key_handlers = {
            ord('q'): self._set_dark_value,
            ord('w'): self._set_light_value,
            ord('e'): self.calculate_cliff_threshold
        }
        
        if key in key_handlers:
            key_handlers[key]()

    def _set_dark_value(self):
        """Set dark values for grayscale sensors"""
        self.dark_value = self.get_median_data()
        self.update_region('gs_dark', "Dark Values", self.dark_value, curses.color_pair(self.COLOR_HIGHLIGHT))
        self.update_log("Dark value set to: {}".format(self.dark_value))

    def _set_light_value(self):
        """Set light values for grayscale sensors"""
        self.light_value = self.get_median_data()
        self.update_region('gs_light', "Light Values", self.light_value, curses.color_pair(self.COLOR_HIGHLIGHT))
        self.update_log("Light value set to: {}".format(self.light_value))

    def _handle_servo_keys(self, key):
        """Handle key presses for servo/motor calibration mode"""
        if key in (ord('w'), ord('s')):
            if key == ord('w'):
                self.tilt_offset -= self.SERVO_STEP
            elif key == ord('s'):
                self.tilt_offset += self.SERVO_STEP
            self.tilt_offset = round(self.tilt_offset, 2)
            self.car.set_camera_tilt_offset(self.tilt_offset)
            self.update_log("Tilt offset adjusted to: {}".format(self.tilt_offset))
        elif key in (ord('a'), ord('d')):
            self.pan_offset = self.car.camera_pan_servo.offset()
            if key == ord('a'):
                self.pan_offset -= self.SERVO_STEP
            elif key == ord('d'):
                self.pan_offset += self.SERVO_STEP
            self.pan_offset = round(self.pan_offset, 2)
            self.car.set_camera_pan_offset(self.pan_offset)
            self.update_log("Pan offset adjusted to: {}".format(self.pan_offset))
        elif key in (ord('q'), ord('e')):
            self.steering_offset = self.car.steering_servo.offset()
            if key == ord('q'):
                self.steering_offset -= self.SERVO_STEP
            elif key == ord('e'):
                self.steering_offset += self.SERVO_STEP
            self.steering_offset = round(self.steering_offset, 2)
            self.car.set_steering_offset(self.steering_offset)
            self.update_log("Steering offset adjusted to: {}".format(self.steering_offset))
        elif key in (ord('z'), ord('c')):
            if key == ord('z'):
                self.left_reversed = not self.left_reversed
                self.car.set_left_motor_reverse(self.left_reversed)
                self.update_log("Left motor reversed: {}".format(self.left_reversed))
            elif key == ord('c'):
                self.right_reversed = not self.right_reversed
                self.car.set_right_motor_reverse(self.right_reversed)
                self.update_log("Right motor reversed: {}".format(self.right_reversed))

            # Test motor direction briefly
            self.car.forward(self.MOTOR_POWER)
            sleep(0.5)
            self.car.stop()

    def is_dark_light_error(self):
        """Check if dark or light values are in error state"""
        if self.dark_value is None or self.light_value is None:
            return False
        for i in range(3):
            if self.dark_value[i] > self.light_value[i]:
                self.update_log(f"Error: Dark value must be less than light value", level="error")
                return True
        return False

def main():
    """Main function to start calibration program"""
    try:
        stdscr = curses.initscr()
        calibrator = Calibration(stdscr)
        calibrator.run()
    except KeyboardInterrupt:
        print("Program exited by user")
    finally:
        curses.endwin()  # Ensure proper cleanup

if __name__ == "__main__":
    main()
