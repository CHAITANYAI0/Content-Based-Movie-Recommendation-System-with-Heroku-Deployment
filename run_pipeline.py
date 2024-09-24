import os
import subprocess

# Step 1: Run the Jupyter notebook to generate pickle files
def run_notebook(notebook_path):
    try:
        print("Running the Jupyter notebook...")
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path], check=True)
        print("Notebook executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the notebook: {e}")
        raise

# Step 2: Run the Streamlit app
def run_streamlit_app(app_path):
    try:
        print("Starting the Streamlit app...")
        subprocess.run(["streamlit", "run", app_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the Streamlit app: {e}")
        raise

if __name__ == "__main__":
    # Paths to the notebook and Streamlit app
    notebook_file = "Movie-Recommender-system.ipynb"
    app_file = "app.py"

    # Step 1: Run the Jupyter notebook
    run_notebook(notebook_file)

    # Step 2: Start the Streamlit app
    run_streamlit_app(app_file)
