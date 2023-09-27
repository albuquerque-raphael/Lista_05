#Imagine que você está desenvovlendo um navegador web simplificado. Use uma pilha para
#armazenar o histórico da páginas visiadas pelo usuário e implementar as funcionalidades
#de voltar e avançar na navegação.

class Navegacao:
    def __init__(self):
        self.historico = []
        self.pagina_atual = -1

    def informar_pagina(self):
        if self.pagina_atual == -1:
            print('Nenhuma página visitada ainda.')
        else:
            print(f'Você está na página {self.historico[self.pagina_atual]}')

    def abrir_nova_pagina(self):
        self.pagina_atual += 1
        self.historico = self.historico[:self.pagina_atual] 
        self.historico.append(f'Página {self.pagina_atual + 1}')
        self.informar_pagina()

    def voltar(self):
        if self.pagina_atual == 0:
            print('Você está na primeira página.')
        elif self.pagina_atual == -1:
            print('Nenhuma página visitada ainda.')
        else:
            self.pagina_atual -= 1
            print(f'Você voltou para a página {self.historico[self.pagina_atual]}')

    def avancar(self):
        if self.pagina_atual == len(self.historico) - 1:
            print('Você está na última página.')
        elif self.pagina_atual == -1:
            print('Nenhuma página visitada ainda.')
        else:
            self.pagina_atual += 1
            print(f'Você avançou para a página {self.historico[self.pagina_atual]}')


nav = Navegacao()
nav.informar_pagina()
nav.abrir_nova_pagina()
nav.avancar()
nav.voltar()
nav.voltar()
nav.avancar()
nav.abrir_nova_pagina()
