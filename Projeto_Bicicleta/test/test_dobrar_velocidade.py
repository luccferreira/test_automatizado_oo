from Bicicleta.bicicleta import Bicicleta

class TestDobrarVelocidade:
    def test_dobrar_velocidade(self):
        input = 15
        esperado = 30

        dobra_velocidade = Bicicleta("Lucas", "Caloi", 15)
        resultado = dobra_velocidade.dobrarAVelocidadeDaBicicleta()

        assert resultado == esperado
