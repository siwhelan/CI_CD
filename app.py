from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return """
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 30px;
                }

                h1 {
                    color: #2c3e50;
                }

                p {
                    font-size: 18px;
                    line-height: 1.6;
                    color: #34495e;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Simple Flask Web Application for Demonstrating CI/CD!</h1>
            <p>This application showcases a seamless integration of a CI/CD pipeline using GitHub Actions and Azure Web Apps. The purpose of this app is to help developers understand how code changes can be automatically tested, built, and deployed to a live environment. By exploring this example, you will learn about developing a minimal Flask application, containerizing it using Docker, and setting up a CI/CD pipeline with GitHub Actions and Azure Web Apps.</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
