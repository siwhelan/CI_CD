from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return """
    <html>
        <head>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 30px;
                    line-height: 1.6;
                    color: #333;
                    background-color: #f7f7f7;
                }
                h1 {
                    color: #5c5c5c;
                    font-size: 36px;
                    margin-bottom: 20px;
                    border-bottom: 2px solid #5c5c5c;
                    padding-bottom: 10px;
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
                a {
                    color: #0076d6;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
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
                <li><b>Get the code</b> 📚: Retrieve the source code from the main branch of the GitHub repository.</li>
                <li><b>Prepare the environment</b> ⚙️: Set up the necessary Python and Docker tools required for building and deploying the app.</li>
                <li><b>Check code formatting with Black</b> 🎨: Ensure all Python files adhere to the standard code formatting rules as defined by the Black formatter.</li>
                <li><b>Perform CodeQL Analysis</b> 🔍: Initialize the CodeQL engine, auto build the project, and perform a comprehensive code analysis to identify potential security vulnerabilities.</li>
                <li><b>Build and push Docker image</b> 🐳: Create a Docker container image of the Flask application and push it to Docker Hub.</li>
                <li><b>Deploy to Azure Web App</b> 🚀: Automatically deploy the application to an Azure Web App, making it accessible via a domain.</li>
            </ol>

            <p>In addition to the steps explained above, this pipeline also includes a security aspect - the CodeQL Analysis. 
            CodeQL is a semantic code analysis engine, used mainly for finding security vulnerabilities in code. 
            It treats code as data, allowing you to explore code in a detailed and relational manner.</p>

            <p>The CodeQL Analysis in this pipeline includes the following steps:</p>

            <ol>
                <li><b>Initialize CodeQL</b>: This step initializes the CodeQL engine on the runner. 
                It downloads the CodeQL CLI and the CodeQL packs that correspond to the languages detected in the repository.</li>
                <li><b>Autobuild</b>: CodeQL has an autobuild step that attempts to build any compiled languages in the project. 
                This is not always necessary, depending on the language and nature of the project.</li>
                <li><b>Perform CodeQL Analysis</b>: This step performs the actual CodeQL analysis. After the analysis is complete, 
                the action creates a SARIF output file storing any results found by the queries.</li>
            </ol>

            <p>Once the analysis is complete, the results are uploaded to GitHub, 
            and you can see them in the Security tab of the repository.
            CodeQL helps in identifying potential vulnerabilities early in the development lifecycle, 
            thereby improving the security posture of the application.</p>


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
