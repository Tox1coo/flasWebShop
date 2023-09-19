from flask import Flask
from flask import render_template
import requests
app = Flask(__name__)

BASE_URL = "https://fakestoreapi.com/products"

request = requests.get(BASE_URL)

result = request.json()

print(result)
@app.route('/')
def home():  # put application's code here
    return render_template("pages/index.html",
                            title = "FlaskShop"
                           )


if __name__ == '__main__':
    app.run(debug = True)
