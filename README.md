# Content-Based-Movie-Recommendation-System-with-Heroku-Deployment

This repository contains the implementation of a Movie Recommender System using Streamlit. The model recommends movies to users based on their preferences.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the App Locally](#running-the-app-locally)
5. [Deploying on Heroku](#deploying-on-heroku)
6. [Author](#author)

## Project Structure
Here is an overview of the files provided in this repository:
- `app.py`: The main Streamlit app to run the movie recommender system.
- `Movie-Recommender-system.ipynb`: Jupyter notebook containing the model and training code.
- `requirements.txt`: Lists the Python dependencies needed to run the app.
- `setup.sh`: Shell script to configure Heroku for Streamlit deployment.
- `Procfile`: Specifies the command to run the app on Heroku.

## Prerequisites
Before you proceed, ensure you have the following installed:
- Python 3.8 or higher
- Git
- Streamlit
- Heroku CLI (if deploying on Heroku)

## Installation
Follow these steps to install the required dependencies and run the app:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommender-system.git
   cd movie-recommender-system


Install the required Python packages using requirements.txt:

## Running the App Locally

1. Install the required Python packages using `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

3. After running the above command, the app will be accessible on localhost at port 8501. Open your browser and navigate to:

    ```bash
    http://localhost:8501
    ```

Here, you will be able to interact with the movie recommender system.

## Deploying on Heroku

Follow these steps to deploy the app on Heroku:

### 1. Install the Heroku CLI

If you don't have the Heroku CLI installed, you can install it from [here](https://devcenter.heroku.com/articles/heroku-cli).

### 2. Create a Heroku App

Log in to your Heroku account and create a new app:

```bash
heroku login
heroku create your-app-name
```

# Streamlit App Deployment on Heroku

This guide outlines the steps to deploy a Streamlit app to Heroku.

## 1. Add a Git Remote for Heroku
Make sure you have the Heroku CLI installed. Then run the following command to add your Heroku app as a remote:

```bash
heroku git:remote -a your-app-name
```

## 2. Prepare for Deployment

Ensure the following files are in the root directory of your project:

setup.sh: This file contains configuration steps for your app.
Procfile: Tells Heroku how to run your application.
requirements.txt: Lists all the required Python libraries.

## 3. Deploy the App

Commit your changes and push them to Heroku using the following commands:

```bash
git add .
git commit -m "Initial commit"
git push heroku master
```

## 4. Open the Deployed App

Once the app is deployed, you can open it using the following command:

```bash
heroku open
```

## 5. Configuring the App

Heroku needs to know how to handle certain configurations for Streamlit. The setup.sh file will handle creating necessary configurations for the app:

```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = \$PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
```

Ensure the Procfile contains the following to launch the app with gunicorn:

```bash
web: gunicorn app:app
```


Feel free to reach out for any questions or contributions!

