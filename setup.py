from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='real-estate-analysis',
    scripts=['bin/mortgage_calculator', 'apps/mortgage_calculator.py'],
    version='1.0',
    packages=['rea','rea.expenses', 'rea.data_sources'],
    license='MIT',
    install_requires=required
    )
