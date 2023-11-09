from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, dear Friend!'


@app.route('/page/<int:page_num>')
def content(page_num):
    return f'<h1>Yoo.. It is your page {page_num}</h1>'

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='1919',debug=True)
