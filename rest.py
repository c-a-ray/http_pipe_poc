from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def print_message():
    message = request.args.get('message')
    print(message)
    return 'success'

if __name__ == '__main__':
    app.run()
