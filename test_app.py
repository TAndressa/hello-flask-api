from app import app

def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_home():
    resposta = client().get('/')
    assert resposta.status_code == 200
    assert resposta.get_json() == {'mensagem': 'Bem-vinda à API!'}

def test_status():
    resposta = client().get('/status')
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert 'status' in dados
    assert dados['status'] == 'online'

def test_sobre():
    resposta = client().get('/sobre')
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados['desenvolvedora'] == 'Andressa'
