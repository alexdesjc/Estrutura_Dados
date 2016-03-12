import unittest


class PilhaVaziaErro(Exception):
    pass

class Pilha():
    def __init__(self):
        self._lista = []

    def vazia(self):
        return not bool(self._lista)

    def topo(self):
        if self._lista:
            return self._lista[-1]
        raise PilhaVaziaErro()

    def empilhar(self, valor):
        self._lista.append(valor)

    def desempilhar(self):
        try:
            return self._lista.pop()
        except IndexError:
            raise PilhaVaziaErro()


def esta_balanceada(expressao):
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    O Aluno deverá informar a complexidade de tempo e espaço da função
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :param abrindo: characteres que abrem expressões
    :param fechando: characteres que fecham expressões
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    >> Análise de Complexidade: Acho que o algoritmo roda em O(n) em tempo execução,
    por que ele é feito um processamento para cada dado de entrada). Quanto à
    memória, acho que no pior caso(se precisar empilhar todos os caracteres da
    expressão) é O(1), pois é proporcional ao tamanho da expressão(armazena cada
    caracter)
    """
    pilha = Pilha()
    abrindo='{[('
    fechando='}])'
    if expressao and expressao[0] in fechando:#testa se é uma lista de caracteres e se começa com characteres que fecham expressões
        return False

    for char in expressao: #Percorre a string
        if char in abrindo:#Se estiver abrindo uma expressao, deve empilhar o character
            pilha.empilhar(char)
        elif char in fechando:#Se estiver fechando uma expressao, deve desempilhar o ultimo character da pilha e compará-lo com o que estiver fechando
            if char==')' and pilha.desempilhar() != '(':#se os caracteres não condizerem, retorna Falso
                return False
            elif char==']' and pilha.desempilhar() != '[':
                return False
            elif char=='}' and pilha.desempilhar() != '{':
                return False
    if pilha.vazia():#Se não foi passado nenhum caracter, a expressão está balanceada
        return True

class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))
