from flask import Flask, render_template, url_for, request, jsonify
from makecircuit import add_element_to_circuit
from MNA.Circuit import Circuit
from MNA.ShowResults import printAddedElements

app = Flask(__name__, template_folder='Templates', static_folder='static',  static_url_path='/static')

flask_debug = True

global_circuit = [Circuit()]

@app.route('/sim', methods = ['GET'])
def page():
    global global_circuit
    del global_circuit[0]
    global_circuit.append(Circuit())
    return render_template('index.html')


@app.route('/calculate', methods = ['POST'])
def calculate():
    global global_circuit
    answer = global_circuit[0].calc()
    res = {i: str(e[0]) for i,e in enumerate(answer.tolist())}
    return jsonify(res)

@app.route('/addelement/<name>', methods = ['POST'])
def addelement(name):
    global global_circuit
    data = request.get_json()
    add_element_to_circuit(circuit_list=global_circuit, **data)
    return 'Success'


if __name__ == '__main__':
    app.run(port=8000, debug=flask_debug)
