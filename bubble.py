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

No seu caso vc implementou uma melhoria em seu código. Vc sempre elimina o último elemento de sua nova lista. Então ele virá 
(n-1)+(n-2)+(n-3)...1 = (n-1+1)*(n-1)/2=(n**2-n)/2. Veja que ele ainda é O(n**2) nesse caso. 
O pior caso acontece quando o menor elemento mínimo é o ultimo elemento. Nos outros casos vc pode atingir o break antes e a fórmula não vai funcionar.
Veja que no seu caso n=10 o 0 é minimo e ultimo. Exatamente (10**2-10)/2 dá exatamente os 45 que vc encontrou.
Para n=20 vc tem o mesmo caso de 0 ser mínimo e último elemento. Portando (20**2-20)/2=380/2=190, justamente o valor impresso também.

Perceba que quanto maior o n, menos relevante fica a parcela (-n). Para 10 ela apresentou-se 10%, para 20, pouco mais de 5%.
Ou seja, quando N é bem grande, vc pode ignorar essa parcela

Conseguiu entender?
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
