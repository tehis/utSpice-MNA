from MNA.Circuit import *
import json

def printResistors(elements):
    for element in elements:
        print('left = ', element.leftNode)
        print('right = ', element.rightNode) 

def printAddedElements(circuit):
    """
    This method written just for debugging!
    """
    print('---------------------Elements:------------------------')
    print("Resistors:")
    printResistors(circuit.resistors)
    
    print('-----------------capacitors----------------------')
    printResistors(circuit.capacitors)

    print('------------------Inductor-----------------')
    printResistors(circuit.inductors)

    print("-------------------Nodes---------------------")
    for number, node in circuit.nodes.items():
        print("Node number ", number)
        print("Node number: ", node.Number)
        print("connectedResistance: ", node.ResisConnented)
        print('positive indVolt: ', node.PosVolt)
        print("neg IndVolt: ", node.NegVolt)

    print("----------------indep Voltages:----------------")
    for element in circuit.indVolt:
        print("PosTerm: ", element.PosTerm)
        print("negTerm: ", element.NegTerm)

    print('----------------------indep currents-----------------')
    for element in circuit.independentCurrent:
        print('current = ', element.Current)
        print(element.nodes)

    print('-----------------opAmps----------------------')
    for element in circuit.opAmps:
        print('negInput: ', element.NegInput)
        print('posInput: ', element.PosInput)
        print('outNode: ', element.OutNode)


    print('=============================================================')



def getAnswers(circuit):
    nodesVolt = {circuit.nodes[i].Number: str(circuit.nodes[i].volt) for i in range(1, len(circuit.nodes))}
    circIndVolt = {i: [str(indVolt.Voltage), indVolt.PosTerm, indVolt.NegTerm, str(indVolt.Current)] for i in range(1, len(circuit.indVolt)+1) for indVolt in circuit.indVolt}
    circOpAmp = {i: [opAmp.PosInput, opAmp.NegInput, opAmp.OutNode, str(opAmp.cur)] for i in range(1, len(circuit.opAmps)+1) for opAmp in circuit.opAmps}
    circResistors = {f'left{res.leftNode} right{res.rightNode}': [res.Resistance, str(res.Voltage), str(res.Current)] for res in circuit.resistors}
    circCapacitor = {f'left{cap.leftNode} right{cap.rightNode}': [cap.Capacitance, str(cap.Voltage), str(cap.Current)] for cap in circuit.capacitors}
    circinduct = {f'left{ind.leftNode} right{ind.rightNode}': [ind.Inductane, str(ind.Voltage), str(ind.Current)] for ind in circuit.inductors}
    return (nodesVolt, circIndVolt, circOpAmp, circResistors, circCapacitor, circinduct)


def getShowResultAns(circuit):
    result = ""
    for i in range(1, len(circuit.nodes)):
        result += 'nodeNumber: ' + str(circuit.nodes[i].Number) + '\n'
        result += str(circuit.nodes[i].volt) + '\n'
    for indVolt in circuit.indVolt:
        result += 'Independent voltage source:' + '\n'
        result += '     volt: ' + str(indVolt.Voltage) + '\n'
        result += '     posTerm : negTerm ' + str(indVolt.PosTerm) + ' : ' + str(indVolt.NegTerm) + '\n'
        result += '     current: ' + str(indVolt.Current) + '\n'
    for opAmp in circuit.opAmps:
        result += 'opAmp:' + '\n'
        result += 'negIn : posIn ' + str(opAmp.NegInput) + ' : ' + str(opAmp.PosInput) + '\n'
        result += 'outNode: ' + str(opAmp.OutNode) + '\n'
        result += 'cur = ' + str(opAmp.cur) + '\n'

    for res in circuit.resistors:
        result += "Resistors:" + '\n'
        result += "Left : Right" + str(res.leftNode) + ' : ' + str(res.rightNode) + '\n'
        result += 'resistance: ' + str(res.Resistance) + '\n'
        result += 'voltage: ' + str(res.Voltage) + '\n'
        result += 'current: ' + str(res.Current) + '\n'

    for cap in circuit.capacitors:
        result += 'capacitors:' + '\n'
        result += "Left : Right" + str(cap.leftNode) + ' : ' + str(cap.rightNode) + '\n'
        result += 'C: ' + str(cap.Capacitance) + '\n'
        result += 'voltage: ' + str(cap.Voltage) + '\n'
        result += 'current: ' + str(cap.Current) + '\n'
    
    for ind in circuit.inductors:
        result += 'inductors:' + '\n'
        result += "Left : Right" + str(ind.leftNode) + ' : ' + str(ind.rightNode) + '\n'
        result += 'L: ' + str(ind.Inductane) + '\n'
        result += 'voltage: ' + str(ind.Voltage) + '\n'
        result += 'current: ' + str(ind.Current) + '\n'
    return result



def printResults(circuit):
    for i in range(1, len(circuit.nodes)):
        print('nodeNumber: ', circuit.nodes[i].Number)
        print(circuit.nodes[i].volt)
    for indVolt in circuit.indVolt:
        print('Independent voltage source:')
        print('     volt: ', indVolt.Voltage)
        print('     posTerm : negTerm ', indVolt.PosTerm, ' : ', indVolt.NegTerm)
        print('     current: ', indVolt.Current)
    for opAmp in circuit.opAmps:
        print('opAmp:')
        print('negIn : posIn ', opAmp.NegInput, ' : ', opAmp.PosInput)
        print('outNode: ', opAmp.OutNode)
        print('cur = ', opAmp.cur)

    for res in circuit.resistors:
        print("Resistors:")
        print("Left : Right", res.leftNode, ' : ', res.rightNode)
        print('resistance: ', res.Resistance)
        print('voltage: ', res.Voltage)
        print('current: ', res.Current)

    for cap in circuit.capacitors:
        print('capacitors:')
        print("Left : Right", cap.leftNode, ' : ', cap.rightNode)
        print('C: ', cap.Capacitance)
        print('voltage: ', cap.Voltage)
        print('current: ', cap.Current)
    
    for ind in circuit.inductors:
        print('inductors:')
        print("Left : Right", ind.leftNode, ' : ', ind.rightNode)
        print('L: ', ind.Inductane)
        print('voltage: ', ind.Voltage)
        print('current: ', ind.Current)
