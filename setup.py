from setuptools import setup, find_packages

setup(name='gym_chess',
      version='0.0.1',
      description='OpenAI Gym environment for Chess, using the game engine of the python-chess module',
      url='https://github.com/Ryan-Rudes/gym-chess',
      author='Ryan Rudes',
      author_email='ryanrudes@gmail.com',
      license='MIT License',
      install_requires=['gym', 'python-chess', 'numpy', 'cairosvg', 'pillow']
)
