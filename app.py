from flask import Flask, request
import mysql.connector

db = mysql.connector.connect(
    host="db", # nom du container mysql dans docker-compose.yml
    port=3306, # port écouté par défaut
    user="root",
    password="abc123",
    database="tp1"
)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'ok'

@app.route('/citation', methods=['POST'])
def citation():
    content = request.json # json == corps (body) de la requête désérialisé en un dict python
    # print(content['text'])
    # print(type(content)) # <class 'dict'>

    cursor = db.cursor()
    query = "insert into citation (text, author) values (%s, %s)"
    values = (content['text'], content['author'])
    cursor.execute(query, values)
    db.commit()

    return 'ok'

app.run(host='0.0.0.0', port=8080)




