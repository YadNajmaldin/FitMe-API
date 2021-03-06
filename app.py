from flask import Flask, jsonify, g
from flask_cors import CORS
from resources.fits import fit
import os
import models


DEBUG = True
PORT = 8000

app = Flask(__name__)

# logic for the DB
@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    print("you should see this after each request")
    g.db.close()
    return response

CORS(fit, origins=['http://localhost:3000', 'https://fitme-front-end.herokuapp.com'], supports_credentials=True)

app.register_blueprint(fit, url_prefix='/fits')

if 'ON_HEROKU' in os.environ: 
    print('\non heroku!')
    models.initialize()


# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)


