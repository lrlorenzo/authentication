from flask import Flask

from login_controller import login_controller

app = Flask(__name__)
app.register_blueprint(login_controller, url_prefix='/auth_api')

if __name__ == '__main__':
    app.run(port=5002, debug=True)