def EvaluatePostfix(exp):
    stack=[]
    d= frozenset(("+","-","*","/"))
    for i in exp:
        if i in d:
            v2=int(stack.pop())
            v1=int(stack.pop())
            
            if i =="+":
                stack.append(v1+v2)
                
            elif i =="-":
                stack.append(v1-v2)
                
            elif i=="*":
                stack.append(v1*v2)
                
            else:
                stack.append(v1/v2)
                
        else:
            stack.append(i)
            
    return int(stack[0])

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        print('{0:g}'.format(float(EvaluatePostfix(exp))))