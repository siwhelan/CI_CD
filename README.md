# A simple Flask Web App demonstrating CI/CD 🚀🔧🔄

This repository contains a minimal Flask web application designed to showcase a CI/CD pipeline using GitHub Actions and Azure Web Apps. The purpose of this project is to help developers understand how code changes can be automatically tested, built, and deployed to a live environment.

## Application Overview

The Flask application is a single-page web app that provides a brief introduction to the CI/CD pipeline and its purpose. The application is containerized using Docker, which simplifies deployment and ensures that it runs consistently across different environments.

## CI/CD Pipeline Workflow

The pipeline is built using GitHub Actions and Azure Web Apps, and includes the following steps:

1. **📚 Get the code**: Retrieve the source code from the main branch of the GitHub repository.
2. **⚙️ Prepare the environment**: Set up the necessary Python and Docker tools required for building and deploying the app.
3. **🎨 Check code formatting with Black**: Ensure all Python files adhere to the standard code formatting rules as defined by the Black formatter.
4. **🔍 Perform CodeQL Analysis**: Initialize the CodeQL engine, auto build the project, and perform a comprehensive code analysis to identify potential security vulnerabilities.
5. **🐳 Build and push Docker image**: Create a Docker container image of the Flask application and push it to Docker Hub.
6. **🚀 Deploy to Azure Web App**: Automatically deploy the application to an Azure Web App, making it accessible via a domain.


This pipeline automates the process of building, testing, and deploying the Flask application, allowing developers to focus on writing code and implementing new features. Any changes made to the application will trigger the pipeline, ensuring that the live environment is always up-to-date.


