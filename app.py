from flask import Flask
from flask_restful import Resource, Api, reqparse
import pymysql.cursors


def Database():
	host = "127.0.0.1"
	user = "root"
	password = "root"
	db = "angrybuddha"
	con = pymysql.connect(host=host, user=user, password=password, db=db, cursorclass=pymysql.cursors.DictCursor)
	return con

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


class SaplingWorld(Resource):
	def get(self):
		# Connect to database
		connection = Database()

		with connection.cursor() as cursor:
			sql = "select * from sapling"
			cursor.execute(sql)
			results = cursor.fetchall()

			data = {}
			data['books'] = []

			for row in results:
				data['books'].append({
					'id': row['id'],
					'isbn': row['isbn'],
					'authors': row['authors'],
					'title': row['title'],
					'average_rating': row['average_rating']
				})

		response = app.response_class(
			response=json.dumps(data),
			status=200,
			mimetype='application/json'
		)
		return response

	def post(self):
		parser.add_argument("name")
		parser.add_argument("latitude")
		parser.add_argument("longitude")
		parser.add_argument("species")
		parser.add_argument("planted_date")
		parser.add_argument("last_watered")
		parser.add_argument("gaurded")
		parser.add_argument("alarm")
		parser.add_argument("last_watered_user")
		parser.add_argument("last_watered_user_time")
		parser.add_argument("planted_by")
		args = parser.parse_args()
		print(args)
		return {"name": args["name"]}


class valunteerWorld(Resource):
	def get(self):
		connection = Database()
		with connection.cursor() as cursor:
			cursor
		valunteer_data = {"id": 1, "name":"Dev", "phone": 913423342}
		return valunteer_data

	def post(self):
		return ack_message

api.add_resource(SaplingWorld, '/sapling')
api.add_resource(valunteerWorld, '/valunteer')

if __name__ == '__main__':
    app.run(debug=True, port=8001)