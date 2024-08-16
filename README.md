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
   This command activates the virtual environment. Once activated, any Python or pip commands will use the packages installed in this environment instead of the global Python environment.

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```
   This command installs all the necessary packages listed in the `requirements.txt` file. These packages are essential for running the application successfully.

4. **Run the Application**
   ```bash
   streamlit run main.py
   ```
   This command starts the Streamlit application by running the `main.py` file. Streamlit is a framework for building web applications for machine learning and data science projects.