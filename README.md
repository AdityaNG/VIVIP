# VIVP

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
$ vivp -s .   # setup
```
To install dependencies : 
```bash
$ vivp -i https://github.com/...
```
To remove dependencies : 
```bash
$ vivp -i https://github.com/...
```
All dependencies are stored at `project_directory/.vpackage/repos/`

## Contributing
If you see something that you know you can help fix or implement, do contact me at :
1. Mail : adityang5@gmail.com
2. Discord : to be added

Please read [Contributing](https://github.com/AdityaNG/VPM/blob/main/CONTRIBUTING.md).

### TODO List
1. Add a run command
2. Install / Remove command triggers a FULL cache clear and re-download. This needs to be optimized
3. Recursive imports need to be implemented with a dependency tree check
4. Make use of version control to download a specific version of a package
5. Unit tests to see if package is functional

## License

This software is released under the [MIT License](https://github.com/AdityaNG/VPM/blob/main/LICENSE.txt).