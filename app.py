import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': 55}

if __name__ == '__main__':
    app.run(port=5000, debug=True)
