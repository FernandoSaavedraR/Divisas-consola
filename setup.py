from setuptools import setup


setup(
    name='exchanges',
    version='0.0.1',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        exc=main:ini
        ''',
)