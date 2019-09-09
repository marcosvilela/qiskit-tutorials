from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, IBMQ
from qiskit import Aer
from qiskit.tools.visualization import circuit_drawer


#medida única do qbit Q

q = QuantumRegister(1)
c = ClassicalRegister(1)

#O circuito possui apenas uma porta de Medida 

measurement = QuantumCircuit(q, c)

#Aplica a medição do qbit q para o registrador clássico c
measurement.measure(q, c)

#Executar o circuito
execution = execute(measurement, Aer.get_backend('qasm_simulator'), shots=1024)
result = execution.result()


#Printando o resultado
print(result.get_counts(measurement))

#Aplicando a porta Pauli-X para levar o qbit ao estado excitado 

excited_State = QuantumCircuit(q, c)
excited_State.x(q)
excited_State.measure(q, c)

#Executar o circuito
executionX = execute(excited_State, Aer.get_backend('qasm_simulator'), shots=1024)
resultX = executionX.result()

print(resultX.get_counts(excited_State))