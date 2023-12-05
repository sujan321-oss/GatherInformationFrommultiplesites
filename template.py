from pathlib import Path
import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="extractingInformationFromUrl"

list_of_files=[
    ".github/workflows/.gitkeep",
f'src//{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

    
]



for filepath in list_of_files:

    dir,file=os.path.split(filepath)
    
    if dir!="":
        os.makedirs(dir,exist_ok=True)
        logging.info("Directory created")
    
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info("Creating the empty file {filepath}")

    else:
        logging.info("File already exist")
         
    



