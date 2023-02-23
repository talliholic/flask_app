from flask import Flask
# from flask_cors import CORS
# import mysql.connector

# mydb = mysql.connector.connect(
#     host = "151.106.97.0",
#     user = "u679110385_iperez",
#     password = "Kay20071***314",
#     database = "u679110385_eflkids"
# )

app = Flask(__name__)
app.secret_key = 'super secret key'
# CORS(app)

# class User:
#     def __init__(self):
#         self.cursor = mydb.cursor(dictionary=True)

#     def read(self, id):
#         self.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
#         return self.cursor.fetchone()

@app.route("/", methods=["GET"])
def read_user():    
#     user = User()       
    return "test"
