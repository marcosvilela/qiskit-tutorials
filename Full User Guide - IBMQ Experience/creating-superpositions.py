from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, IBMQ
from qiskit import Aer
from qiskit.tools.visualization import circuit_drawer

'''
Criando superposições: Aplicando uma porta de Hadamard em um qbit inicialmente no estado |0> e veremos uma superposição, i.e., quando observado, o qbit
estará metade das vezes no estado |0> e metade no estado |1>

'''

#Registradores

q = QuantumRegister(1)
c = ClassicalRegister(1)

#Criando o circuito que aplica uma porta de Hadamard ao registrador q

circuit = QuantumCircuit(q, c)
circuit.h(q)
circuit.measure(q, c)


#Execução
execution = execute(circuit, Aer.get_backend('qasm_simulator'), shots=1024)
result = execution.result()


#Print the results
print(result.get_counts(circuit))
