from setuptools import setup, find_packages

setup(
    name='milib-ejemplo',
    version='0.0.1',
    author='Tu Nombre',
    author_email= "tuemail@ejemplo.com",
    description="Una librería de prueba para subir a Nexus",
    packages=find_packages(),
    classifiers=[
        "Prrogramming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",7
    ],
    python_requires='>=3.6',
)