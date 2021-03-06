from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()
    
setup(
   name='NumberToWords',
   version='1.0.0',
   description='A module to extract a number from a string and convert to text',
   author='Jonathan George',
   author_email='jonogeorge@gmail.com',
   packages=['NumberToWords'], 
   install_requires=['re', 'logging','functools'], 
)