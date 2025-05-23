from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'mensagem': 'Bem-vinda à API!'})

@app.route('/status')
def status():
    return jsonify({'status': 'online', 'versao': '1.0'})

@app.route('/sobre')
def sobre():
    return jsonify({
        'desenvolvedora': 'Andressa',
        'objetivo': 'Projeto inicial de Flask para estudo'
    })

if __name__ == '__main__':
    app.run(debug=True)
