

from flask import Flask, render_template, request

app = Flask(__name__)

# http://127.0.0.1:5500/ 요청시 실행되는 index.html을 랜더링 하기
@app.route("/")
def index():
    return render_template("/index.html")



#res2.html에 가령 db로부터 select 한 데이터 제공해서 출력 유도
# forward 방식으로 msg라는 key에 playdata를 저장해서 html로 출력 위임
# servlet 관점 : request.setAttrubute("msg","playdata")
# 출력 : ${requestScope.msg} 동일한 코드 {{msg}}
@app.route("/app2test", methods=["get"])
def app2test():
    return render_template("res2.html", msg="playdata", data={'one':'가', 'tow':'나'})


# index.html에서 전송되는 client 데이터 즉 web query string값 획득해서 활용
# res2.html로 출력 위임
@app.route("/app2submit", methods=["post","get"])
def app2submit():
    # web query string 획득 및 출력
    # name : <input type="text" name="myname">
    
    #post 방식으로 성공, get방식으론 데이터 획득 불가
    name = request.form.get("myname")
    print("---- app2submit()------",name)
    
    #get 방식으로 성공
    name2 = request.args.to_dict()['myname']
    print("----- app2submit()------",name2)
    
    # res2.html 파일로 리턴
    return render_template("res2.html", msg="playdata", data={'one':'가', 'tow':'나'})


if __name__ == "__main__":
    app.run(debug=True, port=5500)
