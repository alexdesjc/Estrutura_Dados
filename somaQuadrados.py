from collections import Counter
import copy

cache={0:[0]}
def soma_quadrados(n):
    if n==0:
        return [0]
    q=[]
    max=1
    while(max*max<=n):
        q.append(max*max)
        max+=1
    while len(q)>0:
        num=n

        quadrado=q.copy()
        aux=quadrado.pop()
        vetor=[]
        while(num>0):
            if num in cache.keys() and num is not n:
                vetor= vetor + cache[num]
                num=0
            else:
                if len(quadrado)>0:
                    if num-aux<0:
                       aux=quadrado.pop()
                    else:
                        num-=aux
                        vetor.append(aux)
                        if(num<quadrado[-1]):
                            aux=quadrado.pop()
                else:
                    num-=aux
                    vetor.append(aux)
        if n not in cache.keys():
            cache[n]=copy.copy(vetor)
        elif len(vetor)<len(cache[n]):
            cache[n]=copy.copy(vetor)
        q.pop()

    return cache[n]


import unittest


class SomaQuadradosPerfeitosTestes(unittest.TestCase):
    def teste_0(self):
        self.assert_possui_mesmo_elementos([0], soma_quadrados(0))

    def teste_01(self):
        self.assert_possui_mesmo_elementos([1], soma_quadrados(1))

    def teste_02(self):
        self.assert_possui_mesmo_elementos([1, 1], soma_quadrados(2))

    def teste_03(self):
        self.assert_possui_mesmo_elementos([1, 1, 1], soma_quadrados(3))

    def teste_04(self):
        self.assert_possui_mesmo_elementos([4], soma_quadrados(4))

    def teste_05(self):
        self.assert_possui_mesmo_elementos([4, 1], soma_quadrados(5))

    def teste_11(self):
        self.assert_possui_mesmo_elementos([9, 1, 1], soma_quadrados(11))

    def teste_12(self):
        self.assert_possui_mesmo_elementos([4, 4, 4], soma_quadrados(12))

    def assert_possui_mesmo_elementos(self, esperado, resultado):
        self.assertEqual(Counter(esperado), Counter(resultado))
