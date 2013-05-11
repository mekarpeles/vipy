import curses.textpad
import curses

screen = curses.initscr()

def run():
    screen.border(0)
    screen.addstr(0, 0, "vipy")
    screen.refresh()
    screen.getch()
    screen.clear()
    begin_x = 2
    begin_y = 2
    height = 50
    width = 600
    win = curses.newwin(height, width, begin_y, begin_x)
    tb = curses.textpad.Textbox(win)
    text = tb.edit()
    curses.addstr(4,1,text.encode('utf_8'))
    curses.endwin()

if __name__ == "__main__":
    run()
