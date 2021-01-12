from distutils.core import setup

setup(
    name="vivp",
    version="0.0.1",
    author="Aditya NG",
    author_email="adityang5@gmail.com",
    packages=['libvivp'],
    scripts=['bin/vivp'],
    license='LICENSE.txt',
    url='https://github.com/AdityaNG/VIVP',
    description="A package manager for Verilog Projects",
    long_description=open('README.txt').read(),
    python_requires='>=3.6',
)