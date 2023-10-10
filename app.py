from flask import Flask , render_template , request , jsonify
import prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# api ouvindo solicitações POST e prevendo sentimentos
@app.route('/predict' , methods = ['POST'])
def predict():

    response = ""
    review = request.json.get('customer_review')
    if not review:
        response = {'status' : 'error',
                    'message' : 'Empty Review'}
    
    else:

        # chamando o método predict do módulo de previsão.py
        sentiment , path = prediction.predict(review)
        response = {'status' : 'success',
                    'message' : 'Got it',
                    'sentiment' : sentiment,
                    'path' : path}

    return jsonify(response)


# Criando uma rota que recebe requisição do tipo POST


def save():
    # pegando o valor de date da requisição AJAX
   
    #PEGUE O VALOR DE PRODUCT
   
    #PEGUE O VALOR DE REVIEW
    
    #PEGUE O VALOR DE SENTIMENT
   

    # criando uma variável final separada por vírgulas
   
    
    # ABRA O ARQUIVO CSV
   
    # ESCREVA OS DADOS NO ARQUIVO
    

    # retorne uma mensagem de sucesso
    return jsonify({'status' : 'success' , 
                    'message' : 'Dados Registrados'})


if __name__  ==  "__main__":
    app.run(debug = True)