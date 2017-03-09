from Moore_Machine import MooreMachine

name = "15¢Vendor"
states = ('0', '5', '10', '15')
inAlphabet = ('5', '10')
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

# Driver program part

def getInput(num):
    num = num % len(inAlphabet)
    return inAlphabet[num]

output = ""

while(True):
    inp = int(input("0: '5', 1: '10' \n"))
    vm.input(getInput(inp))
    output = vm.getOutput()
    print("Output : "+output)
    if(output[len(output)-1] == '1'): break

print("Enjoy the coffee")