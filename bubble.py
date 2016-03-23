import unittest

def bubble_sort(seq):
    cont=0
    n=len(seq)
    for x in range(n):
        f=0
        for i in range(n-1):
            cont+=1
            if seq[i]>seq[i+1]:
                seq[i],seq[i+1]=seq[i+1],seq[i]
                f=1
        if f==0:
            break
    return seq# if f==0 else

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], bubble_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], bubble_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], bubble_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))
    def teste_lista_ordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubble_sort([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


if __name__ == '__main__':
    unittest.main()
    
    
    
'''
def bubble_sort(seq):
    cont=0
    n=len(seq)
    for x in range(n):
        f=0
        for i in range(n-1):
            cont+=1
            if seq[i]>seq[i+1]:
                seq[i],seq[i+1]=seq[i+1],seq[i]
                f=1
        if f==0:
            break
    return seq# if f==0 else
'''
