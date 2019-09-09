from qiskit import *
from qiskit.compiler import transpile, assemble
import Qconfig_IBMQ_experience
from qiskit import IBMQ 



apiToken = Qconfig_IBMQ_experience.APItoken

'''
QConfig é um arquivo de configuração, que contém o Token associado a minha conta no IMBQ.
Nessa primeira etapa, veremos as credenciais não sendo salvas em disco
Uma vez que se desativam as contas, não temos mais os backends associados a ela (linha 5)
Essa parte é puramente ilustrativa. Vamos salvar no disco

'''
# IBMQ.enable_account(apiToken)
# print(IBMQ.backends())
# IBMQ.disable_accounts(token=apiToken)
# print(IBMQ.backends())

'''
Agora vamos salvar em disco as credenciais. Rodar uma única vez é o bastante

'''
IBMQ.save_account(apiToken, overwrite=True)
print(IBMQ.stored_accounts())

'''
Uma vez salva no disco, precisamos carregar as credenciais 

'''

IBMQ.load_accounts()
print(IBMQ.backends())

'''
Vamos investigar o backend ibmqx4. Veremos as propriedades dos backends e como acessá-las. São elas:
- provider: Retorna o provedor do backend
- name: Retorna o nome do backend
- status: Retorna o status do backend (operational e pending_jobs)
- configuration: Retorna as configurações do backend
- properties: Retorna as propriedades do backend
- run: Executa uma simulação naquele backend
- jobs: Para backends remotos, retorna a lista de jobs executados naquele backend
- 
'''
backend = IBMQ.get_backend('ibmqx4')
print(backend)
print(backend.name())
print(backend.status())
print(backend.configuration())
print(backend.properties())

'''
Vamos utilizar um exemplo ativo!
Criar um circuito e executá-lo no backend
'''

qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
circuit = QuantumCircuit(qr, cr)
circuit.x(qr[0]) #Pauli-X, inversor
circuit.x(qr[1]) #Pauli-X, inversor
circuit.ccx(qr[0], qr[1], qr[2]) #Porta Toffoli, Controlled-Controlled-X
circuit.cx(qr[0], qr[1]) #Controlled-X, inversor controlado
circuit.measure(qr, cr) #Medidores
print('\n')
print(circuit)

#Compilamos o circuito para gerar um quantum object (qobj) que pode ser executado no backend
qobj = assemble(transpile(circuit,backend=backend), shots=1024)
job = backend.run(qobj)
job.cancel()
print(job.status())
result = job.result()
counts = result.get_counts()
print(counts)