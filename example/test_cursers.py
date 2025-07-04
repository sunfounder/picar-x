import curses

def main(stdscr):
    # 初始化颜色
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # 白底黑字（设置背景）
    curses.init_pair(2, curses.COLOR_RED, -1)                     # 红字（保留原有背景）
    curses.init_pair(3, curses.COLOR_GREEN, -1)                   # 绿字（保留原有背景）
    
    # 清屏
    stdscr.clear()
    
    # 步骤1：写入带白色背景的文字
    y, x = 5, 10
    stdscr.addstr(y, x, "这是一行带白色背景的文字", curses.color_pair(1))
    stdscr.refresh()
    stdscr.getch()  # 按任意键继续
    
    # 步骤2：在原有背景上覆盖新文字（保留背景色）
    stdscr.addstr(y, x, "覆盖文字", curses.color_pair(2))  # 红字，背景不变
    stdscr.refresh()
    stdscr.getch()  # 按任意键继续
    
    # 步骤3：只修改部分字符的前景色（保留背景）
    stdscr.addstr(y, x+6, "部分更新", curses.color_pair(3))  # 绿字，背景不变
    stdscr.refresh()
    stdscr.getch()  # 按任意键继续
    
    # 步骤4：使用chgat()显式保留背景色
    stdscr.addstr(y+2, x, "原始文字", curses.color_pair(1))  # 先写入白底黑字
    stdscr.chgat(y+2, x, 2, curses.color_pair(2) | curses.A_BOLD)  # 只改前2个字符为红字加粗
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)