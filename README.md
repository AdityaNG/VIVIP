# VIVP

<a href="https://pypi.org/project/vivp/"> <img src="https://img.shields.io/pypi/v/vivp.svg"></a>
<a href="https://pypi.org/project/vivp/"> <img src="https://img.shields.io/pypi/dm/vivp.svg"></a>
<a href="https://vivp.readthedocs.io/en/latest/"> <img src="https://readthedocs.org/projects/vivp/badge/?version=latest"></a>
[![Coverage Status](https://coveralls.io/repos/github/AdityaNG/VIVP/badge.svg)](https://coveralls.io/github/AdityaNG/VIVP)

<img src="https://github.com/AdityaNG/VIVP/blob/main/docs/img/VIvP_logo.png?raw=true" width="600">

VIvP is a simple package manager for all your Verilog projects. 


## Installing

Install with pip (python>=3.6):

```bash
$ python3 -m pip install vivp
```

To install the very latest version [may be buggy]
```bash
$ pip install git+https://github.com/AdityaNG/VIVP.git
```

More documentation can be found at : https://vivp.readthedocs.io/en/latest/index.html

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