# VPM

<img src="https://github.com/AdityaNG/VPM/blob/main/docs/img/demo1.png?raw=true" width="600">


Verilog Package Manager. A simple package manager for all your verilog projects

## Installing

Install with pip (python>=3.6):

```bash
$ pip install git+https://github.com/AdityaNG/VPM.git
```

## Creating a Verilog Package

cd into the desired directory run the following; you will be prompted to enter your package Name, list of Authors and an optional remote URL

```bash
$ vpm -s .   # setup
```
To install dependencies : 
```bash
$ vpm -i https://github.com/...
```
To remove dependencies : 
```bash
$ vpm -i https://github.com/...
```
All dependencies are stored at `project_directory/.vpackage/repos/`

## Contributing
If you see something that you know you can help fix or implement, do contact me at :
1. Mail : adityang5@gmail.com
2. Discord : <to be added>

## License

This software is released under the [GNU GPL v3 license](LICENSE).