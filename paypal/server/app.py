from flask_app import app
import flask_app.routes as routes
from flask_cors import CORS

CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
