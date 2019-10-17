from setuptools import setup


setup(
    name='exchanges',
    version='0.1.0',
    py_modules=['main',],
    install_requires=[
        'Click',
    ],
    packages=["commands","services","classes",],
    entry_points='''
        [console_scripts]
        exc=main:ini
        ''',
)