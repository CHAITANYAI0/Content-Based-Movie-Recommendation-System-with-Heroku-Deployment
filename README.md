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

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Running the App Locally
After running the streamlit run app.py command, the app will be accessible on localhost at port 8501. Open your browser and navigate to:

arduino
Copy code
http://localhost:8501
Here, you will be able to interact with the movie recommender system.

Deploying on Heroku
Follow these steps to deploy the app on Heroku:

1. Install the Heroku CLI
If you don't have the Heroku CLI installed, you can install it from here.

2. Create a Heroku App
Log in to your Heroku account and create a new app:

bash
Copy code
heroku login
heroku create your-app-name
3. Add a Git Remote for Heroku
bash
Copy code
heroku git:remote -a your-app-name
4. Prepare for Deployment
Ensure the setup.sh, Procfile, and requirements.txt files are in the root directory of your project. These files are necessary for Heroku to know how to run the application.

5. Deploy the App
Commit your changes and push them to Heroku:

bash
Copy code
git add .
git commit -m "Initial commit"
git push heroku master
6. Open the Deployed App
Once deployed, you can open the app using:

bash
Copy code
heroku open
7. Configuring the App
Heroku needs to know how to handle certain configurations for Streamlit. The setup.sh file will handle creating necessary configurations for the app:

bash
Copy code
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
Ensure the Procfile contains the following to launch the app with gunicorn:

makefile
Copy code
web: gunicorn app:app
Author
Chaitanya Inamdar
GitHub
LinkedIn
Feel free to reach out for any questions or contributions!

markdown
Copy code

### Steps to host on Heroku:
- The project is configured to be deployed using Streamlit and Heroku.
- The `setup.sh`, `Procfile`, and `requirements.txt` are already provided and handle the necessary setup.





You said:
give me this in readme.md file code format
ChatGPT said:
ChatGPT
Here’s the README.md file in proper markdown format that you can directly copy and use:

markdown
Copy code
# Movie Recommender System

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
