# A função min_max deverá rodar em O(n) e o código não pode usar nenhuma
# lib do Python (sort, min, max e etc)
# Não pode usar qualquer laço (while, for), a função deve ser recursiva
# Ou delegar a solução para uma função puramente recursiva
import unittest

def min_max(seq):
    '''
    :param seq: uma sequencia
    :return: (min, max)

    Retorna tupla cujo primeiro valor mínimo (min) é o valor
    mínimo da sequencia seq.
    O segundo é o valor máximo (max) da sequencia através dos
    métodos max(seq,n) e min(seq,n)
    >>"Mesmo tendo lido o artigo compartilhado no grupo, estou
    com dificuldades com análise de complexidade de algorítmo,
    na próxima aula, se possível, tento tirar essa dúvida. Acho 
    que esse algorítmo roda em 2*O(n), pois chama dois métodos
    recursivos. Tentei fazer em um só método, mas me enrolei
    muito, e então resolvi fazer em dois. Acabei atrasando a
    entrega por causa disso." 
    '''
    if not seq:#tratando lista vazia
       return None,None

    def max(seq,n):
        '''
        :param seq: uma sequencia
        :param n: tamanho do vetor
        :return: max

        Retorna valor máximo da lista
        '''
        if(n==1):#tratando lista_len_1
            return seq[0]
        else:
            x=max(seq,n-1)
            if x>seq[n-1]:
                return x
            else:
                return seq[n-1]
    def min(seq,n):
        '''
        :param seq: uma sequencia
        :param n: tamanho do vetor
        :return: min

        Retorna valor mínimo da lista
        '''
        if(n==1):#tratando lista_len_1
            return seq[0]
        else:
            x=min(seq,n-1)
            if x<seq[n-1]:
                return x
            else:
                return seq[n-1]

    return min(seq,len(seq)), max(seq,len(seq))#chama os métodos min e max

class MinMaxTestes(unittest.TestCase):

    def test_lista_vazia(self):
        self.assertEqual((None, None), min_max([]))

    def test_lista_len_1(self):
        self.assertEqual((1, 1), min_max([1]))

    def test_lista(self):
        self.assertEqual((6, 56), min_max([9,6,54,32,56,44]))

    def test_lista_consecutivos(self):
        self.assertEqual((0, 500), min_max(list(range(501))))


if __name__ == '__main__':
    unittest.main()
