#Você está desenvolvendo um sistema de fila de impressão para uma empresa. Os documentos
#sao adicionados à fila de impressos na ordem em que foram recebidos. Implemente um
#programa em python que use a classe de fila para simular esse processo.

ordemImpressao = []

for c in  range (5):
    documento = str(f'Documento {c + 1}')
    ordemImpressao.append(documento)
    
for documento in ordemImpressao:
    print(f'Imprimindo {documento}')