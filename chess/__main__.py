# author: Christopher Thomas ~ github.com/CCThomas
# created: July 3rd 2017
# version: 0.1.0

import sys

if (sys.version_info < (3, 0)):
    print('Python version 3+ required')
    print('Download Python 3 here:\nhttps://www.python.org/downloads/')
    sys.exit(0)

from chess.io import output
output.run_log("open")


from chess import console
console.dev_console()
