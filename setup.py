
from setuptools import find_packages, setup

setup(
    name="financebot",
    version="0.0.1",
    author="Dasari Srinivas",
    author_mail="srinivasdasari2023@gmail.com",
    packages = find_packages(),
    install_requires=["langchain","langchain-openai","langchain-astradb",
                      "dataset" , "pypdf" , "python-dotenv" ,"flask"]
)