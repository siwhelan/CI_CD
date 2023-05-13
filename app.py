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
                    line-height: 1.6;
                    color: #34495e;
                }
                h1 {
                    color: #2c3e50;
                    font-size: 32px;
                    margin-bottom: 20px;
                }
                p {
                    font-size: 18px;
                    margin-bottom: 20px;
                }
                ol {
                    font-size: 18px;
                    margin-bottom: 20px;
                    padding-left: 20px;
                }
                li {
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
            <h1>
                This is a simple Flask Web Application for Demonstrating CI/CD!
            </h1>
            <p>
                This application showcases a seamless integration of a CI/CD pipeline
                using GitHub Actions and Azure Web Apps. The purpose of this app is to
                help developers understand how code changes can be automatically tested,
                built, and deployed to a live environment. By exploring this example,
                you will learn about developing a minimal Flask application,
                containerising it using Docker, and setting up a CI/CD pipeline with
                GitHub Actions and Azure Web Apps.
            </p>
            <p>The workflow of this pipeline includes the following steps:</p>
            <ol>
                <li><b>Get the code</b>: Retrieve the source code from the main branch 
                of the GitHub repository.</li>

                <li><b>Prepare the environment</b>: Set up the necessary Python and Docker tools 
                required for building and deploying the app.</li>

                <li><b>Check code formatting with Black</b>: Ensure all Python files adhere to the
                standard code formatting rules as defined by the Black formatter.</li>

                <li><b>Build and push Docker image</b>: Create a Docker container image of the 
                Flask application and push it to Docker Hub.</li>

                <li><b>Deploy to Azure Web App</b>: Automatically deploy the application to an 
                Azure Web App, making it accessible via a domain.</li>
            </ol>

            <p>
                This pipeline automates the process of building, testing, and deploying
                the Flask application, allowing developers to focus on writing code and
                implementing new features. Any changes made to the application will trigger
                the pipeline, ensuring that the live environment is always up-to-date.
            </p>
            <p>
                The source code can be found here -
                <a href="https://github.com/siwhelan/CI_CD">https://github.com/siwhelan/CI_CD</a>
            </p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
