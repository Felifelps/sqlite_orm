from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sqlite_orm",
    version="0.1.0",
    author="Felifelps",
    author_email="felifelps.dev@gmail.com",
    description="A simple ORM for SQLite databases in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Felifelps/sqlite_orm",  # Substitua pela URL do repositório do GitHub
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)