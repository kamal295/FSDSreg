#to convert folder into pacakages(or project into pacakages)
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() #for reading line by line in req.txt
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name="Regression Project",
    version='0.0.1',
    author='kamalakannan',
    author_email='kamalroosewelt@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    pacakages=find_packages()

)