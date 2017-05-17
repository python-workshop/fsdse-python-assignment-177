import sys
from comb_paren_build import paren


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
test(paren(0))

