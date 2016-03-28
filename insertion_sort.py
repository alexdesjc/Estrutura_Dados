'''
***Adicionei teste de lista ordenada e o teste de lista
desordenada com vinte elementos;
***Havia dois testes com o nome def teste_lista_binaria(self),
mudei um deles para def teste_lista_desordenada;
>>Complexidade:
O insertion roda em o de n ao quadrado no pior caso, e o(n) no
melhor caso em tempo de execução; e no pior caso é o(1) em memória
'''

import unittest

def insertion_sort(seq):
    for k in range(1, len(seq)):
        x = seq[k]
        j=k-1
        while j>=0 and seq[j]>x:
            seq[j + 1] = seq[j]
            j=j-1
            seq[j + 1]=x
    return seq

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

    def teste_lista_desordenada_vinte(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], insertion_sort([11, 12, 13, 14, 15, 16, 17, 18, 19, 9, 7, 1, 8, 5, 10, 3, 6, 4, 2, 0]))

    def teste_lista_ordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

if __name__ == '__main__':
    unittest.main()
