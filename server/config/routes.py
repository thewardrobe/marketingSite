from flask import request, jsonify

def router(app):
  @app.route('/')
  def index():
    return app.send_static_file('index.html')