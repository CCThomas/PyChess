# author: Christopher Thomas ~ github.com/CCThomas
# author: Brandon Wong ~ github.com/BW0ng
# created: July 3td 2017
# version: 0.0.0

import sys

if (sys.version_info < (3, 0)):
    print('Python version 3+ required')
    print('Download Python 3 here:\nhttps://www.python.org/downloads/')
    sys.exit(0)

from chess.io import output
output.run_log("open")


from chess import console
console.dev_console()
