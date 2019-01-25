from MNA.Circuit import *

def add_element_to_circuit(circuit_list, type, value, neg, pos, out = -1):
    if type == "Resistor":
        circuit_list[0].addResistor(pos, neg, value)
    elif type == 'Battery':
        circuit_list[0].addIndVolt(value, pos, neg)
    elif type == 'Current':
        circuit_list[0].addIndCur(pos, neg, value)
    elif type == 'Capacitor':
        circuit_list[0].addCapacitor(value, neg, pos)
    elif type == 'Inductor':
        circuit_list[0].addInductor(value, neg, pos)
    elif type == 'OpAmp':
        circuit_list[0].addOpAmp(neg, pos, out)

