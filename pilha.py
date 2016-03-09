import unittest

class PilhaVaziaErro(object):
    pass

class ListaVaziaErro(Exception):
    pass

class Noh():
    def __init__(self, valor, direito=None,esquerdo=None):
        self.direito = direito
        self.esquerdo = esquerdo
        self.valor = valor

class Lista():
    def __init__(self):
        self.tam = 0
        self.primeiro = None
        self.ultimo = None

    def adicionar(self, valor):
        noh = Noh(valor)
        if self.tam == 0:
            self.primeiro = noh
            self.ultimo = noh
        else:
            ultimo = self.primeiro
            while ultimo.direito is not None:
                ultimo = ultimo.direito
            noh.esquerdo=ultimo
            ultimo.direito = noh
            self.ultimo=noh

        self.tam += 1

    def __len__(self):
        return self.tam

    def __iter__(self):
        noh_atual = self.primeiro
        while noh_atual is not None:
            yield noh_atual.valor
            noh_atual = noh_atual.direito

    def adicionar_a_esquerda(self, valor):
        noh = Noh(valor)
        if self.tam == 0:
            self.primeiro = noh
            self.ultimo = noh
        else:
            primeiro = self.ultimo
            while primeiro.esquerdo is not None:
                primeiro = primeiro.esquerdo
            noh.direito=primeiro
            primeiro.esquerdo = noh
            self.primeiro=noh

        self.tam += 1

    def remover(self):
        if self.tam==0:
            raise ListaVaziaErro()

        ultimo=self.ultimo
        if self.tam==1:
            self.ultimo=None
            self.primeiro=None
        else:
            penultimo=ultimo.esquerdo
            penultimo.direito=None
            self.ultimo=penultimo
        self.tam-=1
        return ultimo.valor

    def remover_a_esquerda(self):
        if self.tam==0:
            raise ListaVaziaErro()

        primeiro=self.primeiro
        if self.tam==1:
            self.ultimo=None
            self.primeiro=None
        else:
            segundo=primeiro.direito
            segundo.esquerdo=None
            self.primeiro=segundo
        self.tam-=1
        return primeiro.valor

class Pilha():
    def __init__(self):
        self = Lista()


class PilhaTestes(unittest.TestCase):
    def test_topo_lista_vazia(self):
        pilha = Pilha()
        self.assertTrue(pilha.vazia())
        self.assertRaises(PilhaVaziaErro, pilha.topo)

    def test_empilhar_um_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertFalse(pilha.vazia())
        self.assertEqual('A', pilha.topo())

    def test_empilhar_dois_elementos(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.empilhar('B')
        self.assertFalse(pilha.vazia())
        self.assertEqual('B', pilha.topo())

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
