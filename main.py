from flask import Flask, request
app = Flask(__name__, static_folder='static', static_url_path='') # Initialize Flask and serve static folder

@app.route('/')
def root():
    # Serve index.html under /
    return app.send_static_file('index.html')

# Start app
if __name__ == "__main__":
    app.run(debug=True)
