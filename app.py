from flask import Flask  # Import Flask framework

app = Flask(__name__)  # Create a Flask web application

@app.route('/')  # Define a route (URL path)
def home():
    return "MOhit !! You are gonna make it big!"  # Return this text when accessed

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Start the app on port 5000

