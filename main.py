import curses
import curses.panel as panel

def main(stdscr):
    stdscr.clear()

    stdscr.addstr(f'Hello, World!')

    stdscr.refresh()
    stdscr.getkey()

# curses.wrapper(main)


def createField(width, height):
	field = ['#'+' '*(width-2)+'#' for i in range(height-1)]
	field.append('#'*width)
	return field

def getPiece():
	return '*\n***'

def showPieceOverField(field, piece, x, y):
	pass

for i in createField(20, 80):
	print(i)
