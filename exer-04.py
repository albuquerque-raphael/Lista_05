#Você está criando um aplicativo de lista de tarefas pendentes. As tarefas são adicionadas à fila
#e concluídas uma por uma. Use a classe fila para implementar a lista de tarefas e concluí-las na 
#ordem que foram adicionadas.

ordemTarefas = []

for c in range (10):
    tarefa = str(f'Tarefas {c + 1}')
    ordemTarefas.append(tarefa)
    
for tarefa in ordemTarefas:
    print(f'Concluindo {tarefa}')