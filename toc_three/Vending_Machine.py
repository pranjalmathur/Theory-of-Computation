from Moore_Machine import MooreMachine

name = "15¢Vendor"
states = ('0', '5', '10', '15')
inAlphabet = ('5', '0')
outAlphabet = ('0', '1')

inTransition = {
    '0' : {'5' : '5', '10' : '10'},
    '5' : {'5' : '10', '10' : '15'},
    '10' : {'5' : '15', '10' : '15'},
    '15' : {'5' : '15', '10' : '15'}
}

outTransition = {
    '0' : '0',
    '5' : '0',
    '10' : '0',
    '15' : '1'
}

initState = '0'

vm = MooreMachine(name, states, inAlphabet, outAlphabet, inTransition, outTransition, initState)

vm.input('5')
print(vm.getOutput())
vm.input('10')
print(vm.getOutput())