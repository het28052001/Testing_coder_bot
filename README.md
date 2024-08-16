# README.md

# Project Title

## Description

This project is designed to help you set up a Python environment and run a Streamlit application. Follow the steps below to get started.

## Steps to Set Up the Project

1. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   ```
   This command creates a new virtual environment named `venv`. A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus several additional packages.

2. **Activate the Virtual Environment**
   ```bash
   source venv/bin/activate
   ```
   This command activates the virtual environment. Once activated, your terminal session will use the Python interpreter and packages from the `venv` directory, isolating your project dependencies from the global Python installation.

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```
   This command installs all the necessary packages listed in the `requirements.txt` file. These packages are essential for running the application and should be installed in the virtual environment.

4. **Run the Streamlit Application**
   ```bash
   streamlit run main.py
   ```
   This command starts the Streamlit application by running the `main.py` file. Streamlit will open a new tab in your web browser where you can interact with the application.