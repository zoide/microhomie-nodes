# file AUTO GENERATED by make_metadata.py, do NOT edit
import sys
# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
from setuptools import setup
sys.path.append("..")
import sdist_upip

setup(name='microhomie-node-mem',
      version='0.3.0',
      description='Memory node for the Homie v2 MicroPython framework.',
      long_description=open('README.rst').read(),
      url='https://github.com/microhomie/microhomie-nodes',
      author='Rafael Römhild',
      author_email='rafael@microhomie.com',
      maintainer='Microhomie Developers',
      maintainer_email='contact@microhomie.com',
      license='MIT',
      cmdclass={'sdist': sdist_upip.sdist},
      packages=['homie.node'],
      install_requires=['microhomie'])
