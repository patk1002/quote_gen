from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
        # return "Hello World in html!\n"
        return jsonify("Hello World in json!\n")

if __name__ == "__main__":
    app.run(debug=True)

# Use 'curl -v http:127.0.0.1:5000' to see output without browser
