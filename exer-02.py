#Você está desenvolvendo um sistema de fila de atendimento para banco. Os cientes entram
#na fila e são atendidos pelos funcionários na ordem de chegada. Use a classe fila para
# simular o atendimento dos clientes

ordemClientes = []

for c in range(10):
    cliente = f'Cliente {c + 1}'
    ordemClientes.append(cliente)

for cliente in ordemClientes:
    print(f'Atendimento: {cliente}')