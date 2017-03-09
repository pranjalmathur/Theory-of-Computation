from Moore_Machine import MooreMachine

name = "Vendoor"
states = ('a', 'b', 'c', 'd')
inAlphabet = ('0', '1')
outAlphabet = ('x1', 'x2', 'x3')

inTransition = {
    'a' : {'0' : 'b', '1' : 'c'},
    'b' : {'0' : 'b', '1' : 'd'},
    'c' : {'0' : 'd', '1' : 'c'},
    'd' : {'0' : 'd', '1' : 'd'}
}

outTransition = {
    'a' : 'x2',
    'b' : 'x1',
    'c' : 'x2',
    'd' : 'x3'
}

initState = 'a'

vm = MooreMachine(name, states, inAlphabet, outAlphabet, inTransition, outTransition, initState)

vm.input('1')

print("State : " + vm.getState())
# vm.input('0')
print("Output : "+vm.getOutput())