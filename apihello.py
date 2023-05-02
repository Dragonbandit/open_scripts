#basic api
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    return {'message':'Hello World!'}
@app.route('/<name>')
def name():
  return {'hello'}
if __name__ == '__main__':
    app.run(debug=True, port=5000)
