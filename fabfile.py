import os

from fabric.api import local                                      #type: ignore
from fabric.context_managers import lcd                           #type: ignore


PROJECT_REPO = str(input("inserte URL en protocolo HTTP(s): "))
# URL DE ESTE CASO ES: https://github.com/bunger101/my-first-blog.git
# ÚNICAMENTE HACER UN "COPY-PASTE" cuando pida insertar URL.

replaced = PROJECT_REPO.replace("https://github.com/", "")[:-4]
in_list = replaced.split("/")
# "in_list[0]"" es el PROJECT_AUTHOR i "in_list[1]"" es el PROJECT_NAME

PROJECT_NAME = in_list[1]
PROJECT_PATH = f"/home/{in_list[0]}/exe_project/{PROJECT_NAME}"
PYTHON_VENV = f"{PROJECT_PATH}/.venv/bin/python"
PIP_ENV = f"{PROJECT_PATH}/.venv/bin/pip"

def git_clone():
    print("git clone...")
    
    if os.path.exists(PROJECT_PATH):
        print("Repository already exist in local - skipping clone")
    else:
        local(f"git clone {PROJECT_REPO} {PROJECT_PATH}")
    
    
def create_env():
    print("creating virtual environment...")
    
    with lcd(PROJECT_PATH):
        local(f"python3 -m venv .venv")


def install_requirements():
    print("installing requirements...")
    
    with lcd(PROJECT_PATH):
        local(f"{PIP_ENV} install -r requirements.txt")

def make_migrations():
    print("making the migratons...")
    
    with lcd(PROJECT_PATH):
        local(f"{PYTHON_VENV} manage.py makemigrations")

def run_migrations():
    print("installing migrations...")
    
    with lcd(PROJECT_PATH):
        local(f"{PYTHON_VENV} manage.py migrate")

def load_data():
    print("loading data...")
    
    with lcd(PROJECT_PATH):
        local(f"{PYTHON_VENV} manage.py loaddata db.json")

def deploy():
    git_clone()
    create_env()
    install_requirements()
    make_migrations()
    run_migrations()
    load_data()
    
deploy()
