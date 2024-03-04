from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {"message":"dogger"}

@app.route("/getcode")
def hello():
    return {"message":"Hello, World!2"}

@app.route("/plus/<num1>/<num2>")
def plus(num1,num2):
    return {"result":(float(num1)+float(num2))}

@app.route("/is_prime/<int:x>")
def prime(x):
    if x <= 1:
        return {'result' : False}
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return {'result' : False}
    return {'result' : True}

if __name__ == '__main__':
      app.run(port=5000)
