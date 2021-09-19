from flask import Flask

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    return 'test_key 777777777'

if __name__ == '__main__':
    app.run()
