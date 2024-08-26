from flask import Flask

app = Flask(__name__)

# Definir uma rota raiz (página iniical) e a função que será executaqda a requisitar
@app.route('/')
def hello_worl():
    return 'Hello World'

if __name__ == '__main__':
    app.run(debug=True)