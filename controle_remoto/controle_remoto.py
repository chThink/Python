from flask import Flask,jsonify,request

app = Flask(__name__)

class ControleRemoto:
    def __init__(self):
        self.canal = 1
        
    def mudar_de_canal(self, novo_canal):
        if isinstance(novo_canal,int) and novo_canal > 0:
            self.canal = novo_canal
            return {"message": f"Canal alterado para {self.canal}"},200
        else:
            return {"erro":"Canal inválido" },400
        
controle = ControleRemoto()

#Rota para o canal atual
@app.route("/canal",methods=["GET"])
def pegar_canal():
    return jsonify({"canal_atual": controle.canal})

@app.route("/canal", methods=["POST"])
def alterar_canal():
    dados = request.json
    novo_canal = dados.get("canal")
    resposta = controle.mudar_de_canal(novo_canal)
    if(resposta[1] == 400):
        return jsonify(resposta[0]), resposta[1]
    return jsonify(resposta[0]), resposta[1]


if __name__ == "__main__":
    app.run(debug=True)