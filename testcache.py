import sys
import os

from fmtstr.fmtfuncs import blue, red, bold, on_red

from fmtstr.terminal import Terminal
from fmtstr.terminalcontrol import TerminalController

import time

if __name__ == '__main__':

    print(blue('hey') + ' ' + red('there') + ' ' + red(bold('you')))
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100

    with TerminalController(sys.stdin, sys.stdout) as tc:
        with Terminal(tc) as t:
            rows, columns = t.tc.get_screen_size()
            t0 = time.time()
            for i in range(n):
                a = [blue(on_red('qwertyuiop'[i%10]*columns)) for _ in range(rows)]
                t.render_to_terminal(a)
            t1 = time.time()
            t2 = time.time()
            for i in range(n):
                a = [blue(on_red('q'[i%1]*columns)) for _ in range(rows)]
                t.render_to_terminal(a)
            t3 = time.time()
            t4 = time.time()
            a = [blue(on_red('q'*columns)) for _ in range(rows)]
            arrays = []
            for i in range(n):
                a[i // columns][i % columns] = 'x'
                arrays.append([fs.copy() for fs in a])
            for i in range(n):
                t.render_to_terminal(arrays[i])
            t5 = time.time()

    s = """ all different: %f\tall identical: %f\tchange on character %f\t%d iterations\t""" % (t1 - t0, t3 - t2, t5 - t4, n)
    os.system('echo `git log --pretty=oneline -n 1` '+s+' >> times.txt')
    print(s)
