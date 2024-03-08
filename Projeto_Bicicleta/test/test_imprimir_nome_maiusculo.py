from Bicicleta.bicicleta import Bicicleta

class TestImprimirMaisculo:
    def test_imprimir_nome_todo_maiusculo(self):
        input = "lucas"
        esperado = "LUCAS"

        nome_teste = Bicicleta(input, "Caloi", 15)
        resultado = nome_teste.imprimirNomeMaiusculo()

        assert resultado == esperado

