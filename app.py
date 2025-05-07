from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/soma', methods=['POST'])
def soma():
    """
    Soma dois números
    ---
    parameters:
      - name: a
        in: formData
        type: number
        required: true
      - name: b
        in: formData
        type: number
        required: true
    responses:
      200:
        description: Resultado da soma
    """
    a = float(request.form['a'])
    b = float(request.form['b'])
    return jsonify({'resultado': a + b})

@app.route('/multiplicacao', methods=['POST'])
def multiplicacao():
    """
    Multiplica dois números
    ---
    parameters:
      - name: a
        in: formData
        type: number
        required: true
      - name: b
        in: formData
        type: number
        required: true
    responses:
      200:
        description: Resultado da multiplicação
    """
    a = float(request.form['a'])
    b = float(request.form['b'])
    return jsonify({'resultado': a * b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)