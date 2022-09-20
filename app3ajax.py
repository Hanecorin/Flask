# 비동기 요청 가능한 html 파일 실행이 주 목적

from flask import Flask, request,render_template

app = Flask(__name__)
# http://127.0.0.1:5000
@app.route("/")

def intro():
    print("intro() ------------")
    return render_template("ajaxtest.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
