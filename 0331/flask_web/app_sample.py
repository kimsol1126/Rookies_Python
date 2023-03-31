from flask import Flask

app = Flask(__name__)

#사용자가 기본경로 http://127.0.0.1:5000 로 접근하면 hello_word() 로 유도(routing)
@app.route('/')
def hello_world():
    return "Hello World"
#사용자가 http://127.0.0.1:5000/user 로 접근하면 user() 로 유도
@app.route('/user')
def user():
    return "User Pages.."

@app.route('/user/<int:id>')
def user_search(id):
    return f"사용자 id는 {id}입니다."

if __name__ == '__main__':
    app.run(debug=True)