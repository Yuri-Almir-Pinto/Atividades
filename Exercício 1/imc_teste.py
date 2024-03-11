import imc

class TestIMC():
    def test_calcular_imc(self):
        assert imc.calcular_imc(80, 1.8) == 24.691358024691358
        assert imc.calcular_imc(50, 1.50) == 22.22222222222222
        assert imc.calcular_imc(50, 0) is None
        assert imc.calcular_imc(-1, 1.9) is None
        assert imc.calcular_imc(60, -3) is None
        assert imc.calcular_imc("batata", 5) is None
        assert imc.calcular_imc(60, "batata") is None

    def test_descrever_imc(self):
        assert imc.descrever_imc(5) == "Magreza"
        assert imc.descrever_imc(23) == "Normal"
        assert imc.descrever_imc(27) == "Sobrepeso"
        assert imc.descrever_imc(33) == "Obesidade grau 1"
        assert imc.descrever_imc(37) == "Obesidade grau 2"
        assert imc.descrever_imc(45) == "Obesidade grau 3"
        assert imc.descrever_imc(-999) == "Magreza"