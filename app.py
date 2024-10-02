from flask import Flask # Flask is a class in flask
app=Flask(__name__) # object of flask class

@app.route("/")
def hello():
  return "Hello py"
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)
