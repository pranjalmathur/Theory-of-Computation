# Reads postfix regex to convert to infix to form fragments
def parse_postfix(regex):
    stack = []
    for c in regex:
        if c == '.':
            e2 = stack.pop()
            e1 = stack.pop()
            e1.connect_to(e2.start)
            stack.append(Fragment(e1.start, e2.outs))
        elif c == '|':
            e2 = stack.pop()
            e1 = stack.pop()
            state = State.createSwitch()
            state.out1.next = e1.start
            state.out2.next = e2.start
            outs = [e for e in e1.outs]
            outs.extend(e2.outs)
            stack.append(Fragment(state, outs))
        elif c == '?':
            e1 = stack.pop()
            state = State.createSwitch()
            state.out1.next = e1.start
            outs = [state.out2]
            outs.extend(e1.outs)
            stack.append(Fragment(state, outs))
        elif c == '*':
            e1 = stack.pop()
            state = State.createSwitch()
            state.out1.next = e1.start
            e1.connect_to(state)
            stack.append(Fragment(state, [state.out2]))
        elif c == '+':
            e1 = stack.pop()
            state = State.createSwitch()
            state.out1.next = e1.start
            e1.connect_to(state)
            stack.append(Fragment(e1.start, [state.out2]))
        else:
            state = State.createChar(c)
            stack.append(Fragment(state, [state.out1]))
    e = stack.pop()
    if len(stack) > 0:
        print('Something happened. Not working')
    e.connect_to(MATCHSTATE)
    return e

# Defines the transition arrow to next state
class Next(object):
    def __init__(self):
        self.next = None

# Defines the state with at max 2 outgoing arrows
class State(object):
    Char, Switch, End = range(3)

    def __init__(self):
        self.char = None
        self.type = None
        self.out1 = Next()
        self.out2 = Next()

    @staticmethod
    def createChar(c):
        s = State()
        s.type = State.Char
        s.char = c
        return s

    @staticmethod
    def createSwitch():
        s = State()
        s.type = State.Switch
        return s

    @staticmethod
    def createMatch():
        s = State()
        s.type = State.End
        return s

    def __str__(self):
        if self.type == State.End:
            return 'MATCHSTATE'
        elif self.type == State.Char:
            return 'CHAR(' + self.char + ')'
        elif self.type == State.Switch:
            return 'SWITCH'

MATCHSTATE = State.createMatch()


    