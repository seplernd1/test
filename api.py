from flask import Flask

app = Flask(__name__)

@app.route('/')
def api():
    data={
        "message": "Hello"
    }
    
    return data

if __name__ == '__main__':
    app.run()