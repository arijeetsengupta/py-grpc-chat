## gRPC Chat Application:

This is a simple chat application using gRPC framework coded in Python as the deliverable for our Advanced OS course Assignment I.

This is a standalone application whose UI is created using the Tkinter package in python. All gRPC methods have also been implemented in Python.

#### Features:
1. Register new user
2. Login using credentials
3. Check list of active users
4. One-one chat with any active user
5. (Advanced feature- broadcast) All users can chat with each other on the common chatroom


#### Setting Up The Environment:

1. Download and install python (https://www.python.org/downloads/). Ensure to add it to PATH variable during installation.

2. Setting up the virtual environment (optional- to be done only if you want to install the packages in an isolated environment)

    To set up the environment, ensure the virtualenv package has been installed. This can be added to your Python instance with:
    
    ```bash
    pip install virtualenv
    ```
    
    Once virtualenv has been installed. Create the virutal environment for the application:
    
    ```bash
    python -m venv env
    ```
    
    Then activate the virtual environment:
    
    ```bash
    source env/bin/activate
    ```
  3. Unzip the source code and open the containing directory from the terminal
  4. To install dependencies, run:
  
      ```bash
      pip install -r requirements.txt
        ```
  5. To start the chat server:

        ```bash
        python server.py
        ```

  6. Running the chat client (ensure to change server IP address in config.json file before running client):
        ```bash
        python client.py
        ```