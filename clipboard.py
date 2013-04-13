#!/usr/bin/env python

"""
Copy text to clipboards (to both of them). 
This solution here is specific to Linux.

For a platform independent solution, you can check out
https://github.com/asweigart/mapitpy/blob/master/pyperclip.py 
(I didn't try it).
"""

import subprocess
import utils


def text_to_clipboards(text):
    """Copy text to both clipboards."""
    to_primary(text)
    to_clipboard(text)
      
#############################################################################
      
def to_primary(text):
    """Write text to 'primary'."""
    xsel_proc = subprocess.Popen(['xsel', '-pi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)

def to_clipboard(text):
    """Write text to 'clipboard'."""
    xsel_proc = subprocess.Popen(['xsel', '-bi'], stdin=subprocess.PIPE)
    xsel_proc.communicate(text)
    
#############################################################################
       
def read_primary():
    """Read content of 'primary'."""
    cmd = 'xsel -po'
    return utils.get_simple_cmd_output(cmd)

def read_clipboard():
    """Read content of 'clipboard'."""
    cmd = 'xsel -bo'
    return utils.get_simple_cmd_output(cmd)

#############################################################################

def clear_both_clipboards():
    """Clear both clipboards."""
    clear_primary()
    clear_clipboard()

def clear_primary():
    """Clear primary."""
    utils.execute_cmd('xsel -pc')

def clear_clipboard():
    """Clear clipboard."""
    utils.execute_cmd('xsel -bc')
    
#############################################################################
    
if __name__ == "__main__":
    text = "this should go on the clipboards"
    print text
    text_to_clipboards(text)
    #
    print 'primary>', read_primary()
    print 'clipboard>', read_primary()
    
