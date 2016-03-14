'''
Professor, alterei as linhas 98 e 105 dos testes.
Estava recebendo um erro, que foi sanado com essa mudança
'''

import unittest

class PilhaVaziaErro(Exception):
    pass


class Noh():
    def __init__(self, valor, direito=None, esquerdo=None):
        '''
        :param valor: valor do nó
        :param direito: No direito
        :param esquerdo: Nó esquerdo
        Cria um objeto Noh
        '''
        self.direito = direito
        self.esquerdo = esquerdo
        self.valor = valor


class Pilha():

    def __init__(self):
        '''
        Cria uma Pilha
        '''
        self.tam = 0
        self.primeiro = None
        self.topo = None


    def empilhar(self, valor):
        '''
        :param valor: valor do Noh a ser adicionado
        Adiciona um valor à Pilha
        '''
        noh = Noh(valor)
        if self.tam == 0:
            self.primeiro = noh
            self.topo = noh
        else:
            ultimo = self.primeiro
            while ultimo.direito is not None:
                ultimo = ultimo.direito
            noh.esquerdo = ultimo
            ultimo.direito = noh
            self.topo = noh

        self.tam += 1

    def _topo(self):
        '''
        :param valor: valor do Noh a ser adicionado
        Adiciona um valor à Pilha
        '''
        ultimo = self.topo
        return ultimo.valor

    def vazia(self):
        '''
        Verifica se está vazia
        '''
        return not bool(self.tam)

    def desempilhar(self):
        '''
        Remove o último item da Pilha
        '''
        if self.tam == 0:
            raise PilhaVaziaErro()

        ultimo = self.topo
        if self.tam == 1:
            self.topo = None
            self.primeiro = None
        else:
            penultimo = ultimo.esquerdo
            penultimo.direito = None
            self.topo = penultimo
        self.tam -= 1
        return ultimo.valor


class PilhaTestes(unittest.TestCase):
    def test_topo_Pilha_vazia(self):
        pilha = Pilha()
        self.assertTrue(pilha.vazia())
        self.assertRaises(PilhaVaziaErro, pilha.topo)

    def test_empilhar_um_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertFalse(pilha.vazia())
        self.assertEqual('A', pilha._topo())#alterei o nome do método de topo para _topo()

    def test_empilhar_dois_elementos(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.empilhar('B')
        self.assertFalse(pilha.vazia())
        self.assertEqual('B', pilha._topo())#alterei o nome do método de topo para _topo() 

    def test_desempilhar_pilha_vazia(self):
        pilha = Pilha()
        self.assertRaises(PilhaVaziaErro, pilha.desempilhar)

    def test_desempilhar(self):
        pilha = Pilha()
        letras = 'ABCDE'
        for letra in letras:
            pilha.empilhar(letra)

        for letra_em_ordem_reversa in reversed(letras):
            letra_desempilhada = pilha.desempilhar()
            self.assertEqual(letra_em_ordem_reversa, letra_desempilhada)


if __name__ == '__main__':
    unittest.main()
