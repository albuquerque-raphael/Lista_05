#Em um programa de edição de texto, implemente a funcinalidade de 'Desfazer e 'Refazer'
#usando uma pilha para armazenar um histórico de comandos executados pelo usuário.

class texto:
    def __init__(self, msg=''):
        self.conteudo = msg
        self.desfeitos = []
        self.pilha_conteudo = self.conteudo.split()
        self.mostrar_texto()
        
    def mostrar_texto(self):
        for palavra in self.pilha_conteudo:
            print(palavra, end=' ')
            print('\n')
            
    def escrever(self, msg):
        nova_msg = msg.split()
        for palavra in nova_msg:
            self.pilha_conteudo.append(palavra)
            self.mostrar_texto()
    
    def desfazer(self):
        self.desfeitos.append(self.pilha_conteudo[-1])
        self.pilha_conteudo.pop()
        self.mostrar_texto()
        
    def refazer(self):
        if len(self.desfeitos) == 0:
            print('Não há comando para refazer')
        else:
            self.pilha_conteudo.append(self.desfeitos[-1])
            self.mostrar_texto()
            
            
txt = texto('Aqui estamos na labuta ')
txt.escrever('Adicionando mais uma linha')
txt.desfazer()
txt.refazer()