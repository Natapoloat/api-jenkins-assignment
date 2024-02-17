from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"message":"Dogger"}

@app.route("/getcode")
def hello():
    return {"message":"Hello, World!"}

@app.route("/plus/<num1>/<num2>")
def plus(num1,num2):
    return {"result":(float(num1)+float(num2))}

if __name__ == '__main__':
      app.run(port=5000)
