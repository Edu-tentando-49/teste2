# if __name__ = '__main__':
#   input = 'ABC'
#   chars = list(input)
#    print(chars)    # ['A', 'B', 'C']
from unittest import TestCase
from typing import List


def quebra_string(string: str) -> List[str]:
    return string.split()

class QuebraStringTestCase(TestCase):
    def test_sucesso(self) -> None:
        frase = 'Ola mundo'
        retorno = quebra_string(frase)
        esperado = ['Ola', 'mundo']
        self.assertEqual(retorno, esperado)

if __name__ == '__main__':
    print(quebra_string('ola mundo'))
