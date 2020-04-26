from setuptools import setup

setup(
    name='anyapi',
    version='0.1',
    py_modules=['api'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        anyapi-server=api.api:main
    ''',
)