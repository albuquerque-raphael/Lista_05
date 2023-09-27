#Imagine um sistema de gerenciamento de pedidos para um restaurante. Os pedidos dos 
#clientes são colocados em uma fila e procssados na ordem que foram feitos. Use a classe
#de fila para gerenciar os pedidos e processá-los na ordem correta.

ordemPedidos = []

for c in range(12):
    pedido = f'Pedido {c + 1}'
    ordemPedidos.append(pedido)

for pedido in ordemPedidos:
    print(f'Entregando {pedido}')