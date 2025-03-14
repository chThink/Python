# 📡 Controle Remoto API

Este projeto implementa uma API Flask para simular um **controle remoto**. A API permite **consultar** e **alterar** o canal da TV.

---

## 📌 **1. Tecnologias Utilizadas**

- Python 3+
- Flask
- Pytest (para testes)

---

## 🚀 **2. Instalação e Configuração**

### 2.1. **Clonar o repositório**

```bash
  git clone git@github.com:chThink/Python.git
  cd controle_remoto
```

### 2.2. **Criar um ambiente virtual (opcional, mas recomendado)**

```bash
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 2.3. **Instalar as dependências**

```bash
  pip install -r requirements.txt
```

---

## 📡 **3. Executando a API**

### 3.1. **Rodar o servidor Flask**

```bash
  python controle_remoto.py
```

O servidor será iniciado em `http://127.0.0.1:5000`

---

## 🔄 **4. Endpoints da API**

### 📍 **4.1. Obter o canal atual**

- **Rota:** `GET /canal`
- **Exemplo de resposta:**

```json
{
  "canal_atual": 1
}
```

### 📍 **4.2. Alterar o canal**

- **Rota:** `POST /canal`
- **Corpo da requisição (JSON):**

```json
{
  "canal": 5
}
```

- **Resposta esperada:**

```json
{
  "mensagem": "Canal alterado para 5"
}
```

- **Caso um canal inválido seja enviado:**

```json
{
  "erro": "Canal inválido"
}
```

---

## 🧪 **5. Executando os Testes**

### 5.1. **Rodar os testes unitários com `pytest`**

```bash
pytest test_controle_remoto.py
```

Se todos os testes passarem, verá uma saída semelhante a esta:

```
======= test session starts =======
collected 5 items

test_controle_remoto.py .....  ✅✅✅✅✅

tests passed in 0.5s
```

---

## 💡 **6. Melhorias Futuras**

- Adicionar um histórico de canais assistidos.
- Criar um sistema de volume.
- Implementar suporte para múltiplos usuários.

---

## 📄 **7. Licença**

Este projeto está sob a licença MIT.

📬 **Dúvidas ou sugestões?** Sinta-se à vontade para contribuir! 😊🚀
