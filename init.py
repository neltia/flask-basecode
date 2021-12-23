# flask lib
from flask import Flask
from flask import render_template
# python lib
from datetime import datetime
import hashlib
import os
# file
import config
from views import project
from views import timeline
from views import books


# app config
app = Flask(__name__)
app.config['SECRET_KEY'] = hashlib.sha512(config.secret.encode('utf-8')).hexdigest()
app.register_blueprint(project.blueprint)
app.register_blueprint(timeline.blueprint)
app.register_blueprint(books.blueprint)

# app handler
@app.errorhandler(404)
def page_not_found(error):
    msg = "존재하지 않는 페이지로 접근했습니다."
    return render_template("status_error.html", msg=msg), 404


# default route
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
