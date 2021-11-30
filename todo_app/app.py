from flask import Flask, request
from flask.templating import render_template
from .data import session_items as ses
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = ses.get_items()
    return render_template('index.html', items=items)

@app.route('/add-item', methods=['POST'])
def add_item_route():
    item = request.form['title']
    ses.add_item(item)
    items=ses.get_items()
    return render_template("index.html", items=items)
    
