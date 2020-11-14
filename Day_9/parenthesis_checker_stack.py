import atexit
import io
import sys

def ispar(s):
    brackets={'}':'{',')':'(',']':'['}
    stack=[]
    for char in s:
        if stack and stack[-1]==brackets.get(char):
            stack.pop()
        else:
            stack.append(char)
    if stack:
        return False
    else:
        return True

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s = str(input())
        if ispar(s):
            print("balanced")
        else:
            print("not balanced")