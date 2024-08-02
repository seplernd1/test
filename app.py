from flask import Flask

app = Flask(__name__)

@app.route('/')
def api():
    if request.method=='GET':
        data={
            "message": "Hello"
        }
    
        return data
    if request.method =='POST':
        data = request.body
        return (data=data)

if __name__ == '__main__':
    app.run()
