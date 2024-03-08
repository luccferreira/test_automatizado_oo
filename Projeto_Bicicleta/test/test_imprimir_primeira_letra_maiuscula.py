from Bicicleta.bicicleta import Bicicleta

class TestPrimeiraLetraMaiuscula:
    def test_imprimir_primeira_letra_do_nome_maiuscula(self):
        input = "Lucas"
        esperado = "Lucas"

        LetraMaiusculaTest = Bicicleta(input, "Caloi", 15)
        resultado = LetraMaiusculaTest.imprimirPrimeiraLetraMaisculaDoNome()

        assert resultado == esperado
