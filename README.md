# UCSC Lecture Hall Acoustics
This project, developed for the MCS3202 - Simulation and Modelling Master's module, focuses on Room Impulse Analysis to simulate and analyze the acoustic properties of a lecture hall. 

Sure! Here is the complete installation guide in Markdown format:

```markdown
# Installation Guide for Python Project

## Prerequisites
- Ensure you have Python installed (Python 3.6+ recommended). You can download Python from the [official website](https://www.python.org/downloads/).

## Step 1: Clone the Repository
First, you need to clone the project repository from GitHub (or any other source control management tool).

```sh
git clone <git@github.com:kulathilake/ucsc-lecture-hall-acoustics.git>
cd <ucsc-lecture-hall-acoustics>
```

## Step 2: Create a Virtual Environment
Create a virtual environment using `venv`. This helps to isolate project dependencies from the global Python installation.

```sh
python -m venv venv
```

This command creates a directory named `venv` in your project folder.

## Step 3: Activate the Virtual Environment
Activate the virtual environment. The activation command varies depending on your operating system.

- **On Windows:**

  ```sh
  .\venv\Scripts\activate
  ```

- **On macOS/Linux:**

  ```sh
  source venv/bin/activate
  ```

After activation, you should see `(venv)` at the beginning of your command prompt, indicating that the virtual environment is active.

## Step 4: Install Project Dependencies
Install the project dependencies listed in the `requirements.txt` file.

```sh
pip install -r requirements.txt
```

This command reads the `requirements.txt` file and installs all the required packages.

## Step 5: Verify the Installation
To ensure everything is set up correctly, you can run a simple Python script or a command to check if the dependencies are installed properly.

For example:

```sh
python -m pip list
```

This command lists all the installed packages in the virtual environment.

## Step 6: Deactivate the Virtual Environment
Once you are done working in the virtual environment, you can deactivate it using the following command:

```sh
deactivate
```

This returns you to your normal shell environment.

```