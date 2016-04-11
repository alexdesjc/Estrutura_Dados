
def busca_binaria(seq, procurado):
    """
    Deve retornar o índice onde o elemento deveriar ser inserido em lista ordenada
    :param procurado: elemento a ser procurado
    :param seq: sequencia a ser pesquisada
    :return: int
    Análise de Complexidade: O(n) em tempo e O(1) em espaço
    """
    inicio=0
    fim=len(seq)-1
    while inicio<=fim:
        meio=(inicio+fim)//2
        if procurado > seq[meio]:
            inicio = meio + 1
        elif procurado<seq[meio]:
            fim = meio-1
        else:
            while meio > 0 and seq[meio] == seq[meio-1]:
                meio-=1
            return meio
    return inicio
import unittest

class BuscaBinariaTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertEqual(0, busca_binaria([], 1))
        self.assertEqual(0, busca_binaria([], 2))
        self.assertEqual(0, busca_binaria([], 3))

    def teste_lista_unitaria(self):
        self.assertEqual(0, busca_binaria([1], 0))
        self.assertEqual(0, busca_binaria([1], 1))
        self.assertEqual(1, busca_binaria([1], 2))
        self.assertEqual(1, busca_binaria([1], 3))
        self.assertEqual(1, busca_binaria([1], 4))

    def teste_lista_nao_unitaria(self):
        lista = list(range(10))
        self.assertEqual(0, busca_binaria(lista, -2))
        self.assertEqual(0, busca_binaria(lista, -1))
        for i in lista:
            self.assertEqual(i, busca_binaria(lista, i))
        self.assertEqual(10, busca_binaria(lista, 10))
        self.assertEqual(10, busca_binaria(lista, 11))
        self.assertEqual(10, busca_binaria(lista, 12))

    def teste_lista_elementos_repetidos(self):
        lista = [0, 0, 1, 1, 1, 2, 2, 2]
        self.assertEqual(2, busca_binaria(lista, 1))
        self.assertEqual(5, busca_binaria(lista, 2))
