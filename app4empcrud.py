from flask import Flask, request,render_template
from dto import EmpDTO
from dao import EmpDAO

app = Flask(__name__)

@app.route("/")

def intro():
    print("intro() ------------")
    return render_template("empcrud.html")


@app.route('/insert', methods=['POST'])

def insert():
    
    empno = request.form.get("empno")
    ename = request.form.get("ename")
    sal = request.form.get("sal")
    emp = EmpDTO(empno, ename, sal)
    empDao = EmpDAO()
    empDao.empinsert(emp)
    
    # return emp 에러
    # ? EmpDTO 객체의 내용값을 json 포멧으로 재구성 후 반환
    # empcrud.html에서 insertEmp() 함수 정상 실행
    return '{"k1" : "test"}' #ajax 기반의 응답은 json 포멧으로 응답

if __name__ == "__main__":
    app.run(debug=True, port=5000)

