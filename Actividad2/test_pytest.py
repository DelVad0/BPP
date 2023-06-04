import pytest
from maquina_cafe import MaquinaCafe


@pytest.fixture
def maquina():
    return MaquinaCafe()

def test_hacer_cafe_suficiente(maquina):
    assert maquina.hacer_cafe() == "Café servido"

def test_hacer_cafe_insuficiente_cafe(maquina):
    maquina.cantidad_cafe = 5
    assert maquina.hacer_cafe() == "No hay suficiente café o agua"

def test_hacer_cafe_insuficiente_agua(maquina):
    maquina.cantidad_agua = 50
    assert maquina.hacer_cafe() == "No hay suficiente café o agua"

def test_rellenar_cafe(maquina):
    maquina.rellenar_cafe()
    assert maquina.cantidad_cafe == 100

def test_rellenar_agua(maquina):
    maquina.rellenar_agua()
    assert maquina.cantidad_agua == 1000