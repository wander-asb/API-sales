from flask import Flask, render_template, request, jsonify
import joblib


#app
app = Flask(__name__)

#Carregar o modelo e transformadores do disco
model = joblib.load('')
le_feature_1= joblib.load('')
le_feature_2 = joblib.load('')

#Define a rota principal para a página e aceita apenas requisições GET
@app.route('/', methods = ['GET'])
def index():
    #Renderiza a página inicial usando o template.pkl 
    return render_template('template.html')

@app.route('/predict', methods=['POST'])
def predict