import pytest
from controle_remoto import app, ControleRemoto

#teste para a classe
def test_mudar_canal_valido():
    controle = ControleRemoto()
    resposta = controle.mudar_de_canal(5)
    assert resposta == ({"message": f"Canal alterado para 5"},200)
    assert controle.canal == 5
    
def test_mudar_canal_invalido():
    controle = ControleRemoto()
    resposta = controle.mudar_de_canal(-1)
    assert resposta == ({"erro":"Canal inválido" }, 400)
    assert controle.canal == 1
    
#teste para API
@pytest.fixture
def client():
    app.config["TEFSTING"]=True
    with app.test_client() as client:
        yield client
    
def test_pegar_canal(client):
    resposta = client.get("/canal")
    assert resposta.status_code == 200
    assert resposta.json == {"canal_atual":1}
    
def test_alterar_canal(client):
    resposta = client.post("/canal",json={"canal": 10})
    assert resposta.status_code == 200
    assert resposta.json == {"message":"Canal alterado para 10"}
    
def test_alterar_canal_invalido(client):
    resposta = client.post("/canal",json={"canal": -1})
    assert resposta.status_code == 400
    assert resposta.json == {"erro":"Canal inválido" }, 400