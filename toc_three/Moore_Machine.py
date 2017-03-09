class MooreMachine:

    def __init__(self, name, states, inAlphabet, outAlphabet, inTransition, outTransition, initState):
        self.name = name
        self.states = states
        self.inAlphabet = inAlphabet
        self.outAlphabet = outAlphabet
        self.inTransition = inTransition
        self.outTransition = outTransition
        self.initState = initState
        self._state = initState
        self._output = ""

    def inputTransition(self, inp):
        self._state = self.inTransition[self._state][inp]

    def outputTransition(self, inp):
        self._output = self._output + self.outTransition[self._state][inp]

    def getState(self):
        return self._state

    def input(self, inp):
        self.inputTransition(inp)
