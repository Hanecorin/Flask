
from flask import Flask, render_template

#flask 객체 생성
app = Flask(__name__)


# step01
# http://127.0.0.1:5000/playdata
@app.route("/playdata",methods=["get","post"])
def intro():
    print("intro 실행 -------") # 서버 콘솔창에 출력
    return '{"name":"한예찬"}' # client 브라우저에 응답하는 데이터


# step02
# 요청시 res1.html이 실행되는 함수
# http://127.0.0.1:5000/req1
@app.route("/req1", method=["GET"])
def reqres1():
    print("reqres1 실행 ----")
    return render_template("templates/res1.html")
    



if __name__ == "__main__":
    # flask 서버 실행 명령어
    app.run(debug=True) # http://127.0.0.1:5000