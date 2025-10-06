from setuptools import find_packages, setup
from typing import List

HYPEN_DOT_E="-e ."

def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)
    return requirements        




setup(
name='MLproject',
version='0.0.1',
author='Dheeraj',
author_email='22dheerajpra@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')
)