from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
#from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# @app.route("/get_my_ip", methods=["GET"])
# def get_my_ip():
#     return jsonify({'ip': request.remote_addr}), 200

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/camera")
def camera():

    return render_template("camera.html")

if __name__ == "__main__":
    app.debug=True
    app.run(host="10.11.200.39", port="5050") # app.run(port=5001)... Here we can set any port. but default port=5000
