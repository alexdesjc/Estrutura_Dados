'''
***Adicionei teste de lista ordenada e o teste de lista
desordenada com vinte elementos;
***Havia dois testes com o nome def teste_lista_binaria(self),
mudei um deles para def teste_lista_desordenada;
>>Complexidade:
O bubbleSort roda em o de n ao quadrado em tempo de execução
no pior caso e o(1) em memória, Mas no pior caso (quando já
está ordenado) é o(n) em tempo de execução e o(1) em memória
>>[no meu código, especificamente, nos prints constam apenas 45
loopings para n=10, porém quando n=20(teste_lista_desordenada_vinte)
constam 190 loops. Como eu analiso essa complexidade?]
'''

import unittest

def bubble_sort(seq):
    cont=0
    n=len(seq)
    for x in range(n-1,0,-1):
        flag=0
        for i in range(x):
            cont+=1
            if seq[i]>seq[i+1]:
                seq[i],seq[i+1]=seq[i+1],seq[i]
                flag=1
        if flag==0:
            break
    print("loops: ", cont)
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_desordenada_vinte(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], bubble_sort([11, 12, 13, 14, 15, 16, 17, 18, 19, 9, 7, 1, 8, 5, 10, 3, 6, 4, 2, 0]))

    def teste_lista_ordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    unittest.main()
