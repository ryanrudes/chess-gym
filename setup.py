from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='chess_gym',
      version='0.0.3',
      description='OpenAI Gym environment for Chess, using the game engine of the python-chess module',
      url='https://github.com/Ryan-Rudes/gym-chess',
      author='Ryan Rudes',
      author_email='ryanrudes@gmail.com',
      license='MIT License',
      install_requires=['gym', 'python-chess', 'numpy', 'cairosvg', 'pillow'],
      long_description=long_description,
      long_description_content_type="text/markdown",
)
