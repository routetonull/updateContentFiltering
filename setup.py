from setuptools import setup

setup(
    name='updateContentFiltering',
    version='0.1',
    py_modules=['updateContentFiltering'],
    install_requires=[
        'Click',
        'meraki',
    ],
    entry_points='''
        [console_scripts]
        updateContentFiltering=updateContentFiltering:cli
    ''',
)