from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def print(self):
        print(self.container)


def reverse_string(val):
    s = Stack()

    for ch in val:
        s.push(ch)

    str = ""
    while s.size() > 0:
        str += s.pop()
    print(str)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            stack.push(ch)
        if ch ==')' or ch == ']' or ch =='}':
            if stack.size() == 0:
                return False
            # if is_match(ch,stack.pop()) == False:
            if not is_match(ch, stack.pop()):
                return False
    return stack.size() == 0

stack = deque()
stack.append("https://www.techbeamers.com/")
stack.append("https://medium.com/")
stack.append("https://www.simplilearn.com/")
stack.append("https://ayakatsubouchi.github.io/portfolio2/")
print(stack)
# stack.pop()
print(stack)
reverse_string("We will conquere COVID-19")

s = Stack()
s.push(5)
s = Stack()
s.push(5)
s.print()
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))