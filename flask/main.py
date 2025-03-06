from flask import Flask
from routes.home import home_routes
from routes.cliente import cliente_route

app = Flask(__name__)

app.register_blueprint(home_routes)
app.register_blueprint(cliente_route, url_prefix='/cliente')

app.run(debug=True)  # to start the server