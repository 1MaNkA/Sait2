import os

from flask import Flask
from blog_app.config import Config

app = Flask(__name__)

app.config.from_object(Config)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))
from blog_app import routes