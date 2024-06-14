from flask import Flask, request, jsonify, render_template
import pandas as pd
import datetime
import tensorflow as tf

app = Flask(__name__)

# Carregue o modelo de predição de sentimentos aqui, se necessário.
# model = tf.keras.models.load_model('caminho_para_o_modelo')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review = data.get('review', '')
    
    # Faça a predição do sentimento aqui usando o modelo carregado.
    # sentiment = model.predict(review)
    
    # Mock de predição para exemplo
    sentiment = 'positivo' if 'bom' in review else 'negativo'
    
    response = {
        'review': review,
        'sentiment': sentiment,
        'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(response)

@app.route('/save', methods=['POST'])
def save():
    data = request.json
    df = pd.DataFrame([data])
    
    with open('reviews.csv', 'a') as f:
        df.to_csv(f, header=f.tell()==0, index=False)
    
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
