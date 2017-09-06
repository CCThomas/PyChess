# author: Christopher Thomas ~ github.com/CCThomas
# created: Aug 1st 2017
# version: 0.3.0

from gui.window import Window
import sys

if sys.version_info < (3, 0):
    print('Python version 3+ required')
    print('Download Python 3 here:\nhttps://www.python.org/downloads/')
    sys.exit(0)

my_window = Window()
my_window.mainloop()
