# Ignition

<!--- Badges --->
![GitHub last commit (7.9)](https://img.shields.io/github/last-commit/thecesrom/Ignition/7.9)
[![GitHub contributors](https://img.shields.io/github/contributors/thecesrom/Ignition)](https://github.com/thecesrom/Ignition/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/thecesrom/Ignition)](https://github.com/thecesrom/Ignition/blob/7.9/LICENSE)
[![GitHub downloads](https://img.shields.io/github/downloads/thecesrom/Ignition/total)](https://github.com/thecesrom/Ignition/releases)
[![time tracker](https://wakatime.com/badge/github/thecesrom/Ignition.svg)](https://wakatime.com/badge/github/thecesrom/Ignition)
[![Sourcery](https://img.shields.io/badge/Sourcery-enabled-brightgreen)](https://sourcery.ai)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Imports: flake8](https://img.shields.io/badge/%20imports-flake8-%231674b1?style=flat&labelColor=ef8336)](https://flake8.pycqa.org/en/latest/)
[![Join us on GitHub discussions](https://img.shields.io/badge/github-discussions-informational)](https://github.com/thecesrom/Ignition/discussions)

Ignition is a set of packages and modules that allows developers to get code completion for Ignition Scripting API scripting functions in their IDE of choice.

# Releases

Check the [releases page](https://github.com/thecesrom/Ignition/releases) and download the one for your current version.

If you can't find it, feel free to submit your request on our [Discussions](https://github.com/thecesrom/Ignition/discussions).

## Prerequisites

Before you begin, ensure you have met the following requirements:

* You have installed Python 2.5.4 ([download here](https://www.python.org/downloads/release/python-254/))
* You are familiar with [Ignition 7.9 Scripting Functions](https://docs.inductiveautomation.com/display/DOC79/Scripting+Functions)

## Packages

Ignition consists of the following packages:

* java/javax
* system

### java/javax

These are libraries for some Java packages and functions that are imported in `system` packages meant to be used on systems where no JDK can be installed, and the project interpreter is Python 2.7.

### system

Is a package that includes all Ignition Scripting Functions.

## Installation and usage

To use Ignition, download the code targeted to your desired version from the [releases page](https://github.com/thecesrom/Ignition/releases) and add it as a dependency to your scripting project.

Also, once you've downloaded and unzipped the source code you may install it using the `setup.py`:

```bash
$ cd ~/Downloads/v7.9.X
$ python setup.py install --record files.txt 
```

This will install it as package to your Python installation, which will allow you to call Ignition Scripting functions from Python's REPL.

```bash
$ python
Python 2.5.6 (r256, Sep  5 2021, 17:50:57) 
[GCC Apple LLVM 12.0.0 (clang-1200.0.32.29)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import system.gui
>>> print system.gui.__doc__
GUI Functions.

The following functions allow you to control windows and create popup
interfaces.
>>> system.gui.warningBox("This one is a warning.")
['This one is a warning.', 'Warning']
>>> quit()
```

And to uninstall:
```bash
$ cd ~/Downloads/v7.9.X
$ cat files.txt | xargs rm -rf
```

## Contributing to Ignition

To contribute to Ignition, follow these steps:

1. Fork this repository
2. Create a local copy on your machine
3. Create a branch
4. Make your changes and commit them
5. Push to the original branch
6. Create the pull request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to everyone who has contributed to this project.

Up-to-date list of contributors can be found [here](https://github.com/thecesrom/Ignition/graphs/contributors).

## License

See the [LICENSE](https://github.com/thecesrom/Ignition/blob/HEAD/LICENSE).

## Code of conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
