from flask import Flask
from flask_restful import Resource, Api
from sys import argv

app = Flask(__name__)
api = Api(app)

class Blindness(Resource):
    def get(self):
        return {'module' : 'Blindness detection', 'version': '1.0'}


api.add_resource(Blindness, '/')

if __name__ == '__main__':
	app.run(debug=True, port=argv[1])