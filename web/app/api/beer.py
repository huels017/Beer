from flask_restful import Resource

class Beer(Resource):
    def get(self):
        response = 'Made with beer in Minneapolis. Remember to code responsibly!'
        return response
