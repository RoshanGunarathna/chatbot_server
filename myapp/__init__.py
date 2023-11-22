from flask import Flask, request, jsonify

from chat import get_response

def create_app():
    app = Flask(__name__)

    @app.get('/')
    def hello_world():
        return 'Hello!'

    @app.post("/predict")
    def pred():
        text = request.get_json().get("message")
        response = get_response(text)
        message = {"answer": response}
        return jsonify(message)

    if __name__ == "__main__":
        app.run(debug=False ,host='0.0.0.0')

    return app

# if __name__ == "__main__":
#     app.run(debug=true)