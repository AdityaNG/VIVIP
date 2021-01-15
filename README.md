# VIVP

<img src="https://github.com/AdityaNG/VIVP/blob/main/docs/img/example1.png?raw=true" width="600">

VIVP Installs Verilog Packages
Verilog Package Manager. A simple package manager for all your verilog projects.

Packages installed by vivp can be included using the "`include" directive as shown above 

## Installing

Install with pip (python>=3.6):

```bash
$ python3 -m pip install vivp
```

To install the very latest version [may be buggy]
```bash
$ pip install git+https://github.com/AdityaNG/VIVP.git
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
$ vivp -r https://github.com/...
```
All dependencies are stored at `project_directory/.vpackage/repos/`
To view the list of dependencies installed and the modules they offer, use the --list or -l option
<img src="https://github.com/AdityaNG/VIVP/blob/main/docs/img/example2.png?raw=true" width="600">

To run your project, first add the list of testbent files and then eecute with -e: 
```bash
$ vivp -add_testbench testbench.v
$ vivp -e
```

<img src="https://github.com/AdityaNG/VIVP/blob/main/docs/img/demo1.png?raw=true" width="600">

## Contributing
If you see something that you know you can help fix or implement, do contact me at :
1. Mail : adityang5@gmail.com
2. Discord : to be added

Please read [Contributing](https://github.com/AdityaNG/VIVP/blob/main/CONTRIBUTING.md).

### TODO List
1. (DONE) Add a run command
2. Add support fom non vpackage projects
3. Add .vpackage/* to .gitignore
4. Install / Remove command triggers a FULL cache clear and re-download. This needs to be optimized
5. Recursive imports need to be implemented with a dependency tree check
6. Make use of version control to download a specific version of a package
7. Unit tests to see if package is functional
8. Make website on git to give introduction, show list of modules on git, look pretty, SEO : https://adityang.github.io/VIVP/

## License

This software is released under the [MIT License](https://github.com/AdityaNG/VIVP/blob/main/LICENSE.txt).