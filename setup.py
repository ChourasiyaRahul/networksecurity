'''
The setup.py file is an essential part of packaging and
distributing Python projects. It is used by setuptools to define 
the configuration of your project, such as its metadata, dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",'r')as file:
            lines = file.readlines() #read lines ffrom file
            ## process each lines
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("Requirements.txt file not found")


    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Chourasiya Rahul",
    author_email="rkchourasiya970@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)