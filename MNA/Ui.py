from .Circuit import *
import MNA.ShowResults as ShowResults


# if __name__ == '__main__':
#     circut = Circuit()
def UIans(circuit, statement):
    # while True:
        # element = input().split()
    element = statement.split()
    if element[0] == 'R':
        leftNode = int(element[1])
        rightNode = int(element[2])
        resistance = float(element[3])
        circuit[0].addResistor(rightNode, leftNode, resistance)
    elif element[0] == 'IV':
        posTerm = int(element[1])
        negTerm = int(element[2])
        try:
            voltage = float(element[3])
        except ValueError:
            voltage = element[3]
            print("Alternate source")
        circuit[0].addIndVolt(voltage, posTerm, negTerm)
    elif element[0] == 'IC':
        comeIn = int(element[1])
        comeOut = int(element[2])
        try:
            cur = float(element[3])
        except ValueError:
            cur = element[3]
            print('Aternate  source')
        circuit[0].addIndCur(comeIn, comeOut, cur)

    elif element[0] == 'OA':
        posInputNode = int(element[1])
        negInputNode = int(element[2])
        outInputNode = int(element[3])
        circuit[0].addOpAmp(negInputNode, posInputNode, outInputNode)
    
    elif element[0] == 'C':
        if not circuit[0]._Circuit__alternate:
            raise ValueError("There isn't any source!")
        left = int(element[1])
        right = int(element[2])
        capacitance = float(element[3])
        circuit[0].addCapacitor(capacitance, left, right )

    elif element[0] == 'L':
        if not circuit[0]._Circuit__alternate:
            raise ValueError("There isn't any source!")
        left = int(element[1])
        right = int(element[2])
        inductance = float(element[3])
        circuit[0].addInductor(inductance, left, right)

    elif element[0] == 'calculate':
        circuit[0].calc()
        ShowResults.printAddedElements(circuit[0])
        ShowResults.printResults(circuit[0])
        return ShowResults.getShowResultAns(circuit[0])
        #     break
        # else:
        #     break
