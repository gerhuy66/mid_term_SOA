from app import app
@app.route("/test2",methods=['GET'])
def test2():
    return "test module success"