from distutils.core import setup

setup(
    name="vpm",
    version="0.0.1",
    author="Aditya NG",
    author_email="adityang5@gmail.com",
    packages=['libvpm'],
    scripts=['bin/vpm'],
    license='LICENSE.txt',
    url='https://github.com/AdityaNG/VPM',
    description="A package manager for Verilog Projects",
    long_description=open('README.txt').read(),
    python_requires='>=3.6',
)