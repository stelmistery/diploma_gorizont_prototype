# diploma_gorizont_prototype
The prototype of the diploma project "SOL Horizon"

To start the project we need [python](https://www.python.org/) version 3.8 and higher install . Next, we need to install python-venv and to create a virtual environment with the python interpreter. 

linux debian/ubuntu:
```bash
sudo apt install python3-venv
```

Switch to the directory where you would like to store your Python 3 virtual environments. Within the directory run the following command to create your new virtual environment:
```bash
python venv my-project-env
```
The command above creates a directory called my-project-env, which contains a copy of the Python binary, the Pip package manager, the standard Python library and other supporting files

To start using this virtual environment, you need to activate it by running the activate script:
```bash
source my-project-env/bin/activate
```
Next, we need to install all the necessary dependencies and libraries
```bash
pip3 install -r requirements.txt
```

After the operations done, create the migration with the command:
```bash
python manage.py makemigrations
```
Еhen we migrate all migrations:
```bash
python manage.py migrate
```

Start the server:
```bash
python manage.py runserver
```

## LICENSE
Copyright (c) 2020 [WIL ASCENSION](https://vk.com/elvladosios)

