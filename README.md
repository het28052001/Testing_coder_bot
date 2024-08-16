# README.md

# Project Setup Instructions

This document outlines the steps to set up the project environment and run the application.

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
   This command activates the virtual environment. Once activated, your terminal session will use the Python interpreter and packages installed in the `venv` directory instead of the global Python installation.

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```
   This command installs all the necessary packages listed in the `requirements.txt` file. These packages are essential for the application to run properly.

4. **Run the Streamlit Application**
   ```bash
   streamlit run main.py
   ```
   This command starts the Streamlit application using the `main.py` file. Streamlit is a framework for building web applications for data science and machine learning projects.