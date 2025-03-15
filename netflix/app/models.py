from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = "clientes"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    plano = db.Column(db.String(20), nullable=True)
    
    def __init__(self, name="null", email="null", plano="null"):
        self.name = name 
        self.email = email
        planos = ["basic", "premium", "null"]
        
        if plano in planos:
            self.plano = plano
            return 
        else:
            raise ValueError("Plano inválido! Escolha entre 'basic' ou 'premium'.")
        
    def to_dict(self):
        return {"name": self.name, "email": self.email, "plano": self.plano}