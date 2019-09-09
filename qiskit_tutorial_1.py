import numpy as np 
from qiskit import *
from qiskit import BasicAer
from qiskit.visualization import plot_histogram
'''
Elementos constituintes do Circuito

Registrador Quântico: Utilizado para guardar as informações dos qbits
Circuito Quântico: Objeto que permite aplicar transformações aos qbits do registrador q
'''
q = QuantumRegister(3, 'q') #registrador com 3 qbits
c = ClassicalRegister(3, 'c') #registrador clássico com 3 bits
circuit = QuantumCircuit(q) #circuito que age sobre o registrador q
circuit2 = QuantumCircuit(q, c)
'''

Depois de criado o Circuito, pode-se inserir Portas, que são operações que 
manipulam os registradores. 

As portas mais simples são as seguintes:
 - Pauli-X, que inverte o estado de um qbit (x(|0>) = |1> e x(|1>) = |0>)
 - Pauli-Y, que rotaciona o qbit ao redor do eixo Y da Esfera de Bloch em PI radianos
 - Pauli-Z, que rotaciona o qbit ao redor do eixo Z da Esfera de Bloch em PI radianos
 - Hadamard, que cria uma superposição entre dois estados
 - CNOT, um inversor controlável 

'''
circuit.x(q[0])  #output: |1>
# print(circuit) #printa o circuito no estilo ASCII

'''
Vamos começar criando o estado Greenberg-Horne-Zeilinger (GHZ)
Esse estado é uma superposição de todos os qbits no estado |1> e todos os qbits no estado |0>
Para criar esse estado, é necessário utilizar 3 portas quânticas: H para criar superposição e dois CNOTs para inverter alguns estados

'''
circuit2.h(q[0])
circuit2.cx(q[0], q[1])
circuit2.cx(q[0], q[2])


'''
Vamos executar esse circuito GHZ utilizando o backend openQASM. Para isso, precisamos
criar registradores clássicos que irão guardar o valor medido do qbit

'''

circuit2.barrier(q)
circuit2.measure(q, c)
print(circuit2)
backend_sim = BasicAer.get_backend('qasm_simulator')
job_sim = execute(circuit2, backend_sim, shots=2048)
result_sim = job_sim.result()
counts = result_sim.get_counts(circuit2)
print(counts)

'''
Visualizações: Lembrar que, no cmd, essa visualizações retornam um Figure do matplotlib, e precisam ser salvas para a pasta em vez de aparecerem na tela

'''
circuit2.draw(output='mpl', filename='circuit.png')
plot_histogram(counts).savefig('histogram.png')
