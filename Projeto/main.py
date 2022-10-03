#Servidor
from flask import Flask, jsonify,make_response,request
from db import db, Informacoes 

     
app = Flask(__name__)
app.config['JSON_SORT_KEYS']=False
 
@app.route('/')
def home():
    return 'Hello ESP8266, from Flask'

@app.route('/informacoes', methods=['GET'])
def get_inf():    
    
    my_cursor = db.cursor()    
    my_cursor.execute('select * from informacoes')
    meus_dados = my_cursor.fetchall()# cursor retorna lista de dados capturados
    
    
    print (meus_dados)
    return make_response(
        jsonify(
            mensagem='Informacoes ESP',
            dados=meus_dados
        )
    )


#aqui recebe dados da API, ou seja dados vem da esp via post 
@app.route('/informacoes', methods=['POST'])
def create_inf():
    dados=request.json
    my_cursor = db.cursor()    
    sql='INSERT INTO informacoes (dados) VALUES ('')'
    my_cursor.execute(sql)
    db.commit()
    
   
    return make_response(
        jsonify(
            mensagem='Dados cadastrados com sucesso',
            dados=dados
        )
    )
    
 
 

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.105', port= 5000) ##colocar ip da máquina ou setar como host='0.0.0.0'


