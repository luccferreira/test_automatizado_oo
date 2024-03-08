from Bicicleta.bicicleta import Bicicleta

class TestImprimir:
    def test_return_atributos_bicicleta(self):
        input = "Lucas"
        input2 = "Caloi"
        input3 = 15
        esperado = ('Lucas', 'Caloi', 15)

        bicicleta_teste = Bicicleta(input, input2, input3)
        resultado = bicicleta_teste.imprirmirAtributosDaBicicleta()

        assert resultado == esperado
