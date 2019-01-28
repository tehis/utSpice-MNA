from MNA.Circuit import *
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

def add_element_to_circuit(circuit_list, type, value, neg, pos, out = -1):
    if type == "Resistor":
        circuit_list[0].addResistor(pos, neg, value)
        logging.debug(f'ressistors: {circuit_list[0].resistors}')
    elif type == 'Battery':
        if str.isdecimal(value):
            value = float(value)
        circuit_list[0].addIndVolt(value, pos, neg)
        logging.debug(f'battery: {circuit_list[0].indVolt}')
    elif type == 'Current':
        if str.isdecimal(value):
            value = float(value)
        circuit_list[0].addIndCur(pos, neg, value)
        logging.debug(f'current: {circuit_list[0].independentCurrent}')
    elif type == 'Capacitor':
        circuit_list[0].addCapacitor(value, neg, pos)
        logging.debug(f'capacitors: {circuit_list[0].capacitors}')
    elif type == 'Inductor':
        circuit_list[0].addInductor(value, neg, pos)
        logging.debug(f'inductors: {circuit_list[0].inductors}')
    elif type == 'OpAmp':
        circuit_list[0].addOpAmp(neg, pos, out)
        logging.debug(f'opamps: {circuit_list[0].opAmps}')

