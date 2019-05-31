---
title: Python Simple Package Structure
description: Let me show you a simple workflow for structuring your package.
image: https://via.placeholder.com/320x240
# toc: true
---

## Motivation

Before we start a bit of motivation why I needed to write this when great guides like [The Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/) and [Minimal Structure](http://python-packaging.readthedocs.io/en/latest/minimal.html) exist.

The Hitchhiker's guide is a long read but a good read especially if you're wondering how you should [structure your project](http://docs.python-guide.org/en/latest/writing/structure/). Unfortunately the guide does not dwell on how you should code the preamble of your code (e.g., `from package import module`, `sys.path.append(...)` ) which is my next step was to consult the Minimal Structure. Unfortunately the Minimal Structure is too minimal ignoring the general case that your package may often have more than just one python file (excluding `__init__.py`). The preamble for greater than one python file is surprisingly a bit more complex than minimal structure.


## Module vs Package
> If you are very experienced with how Python handles packages and modules then head to [Getting Started](#getting-started)

A Python file that is to be imported is a Python module while a Python package is the directory where the module lives in and requires a `__init__.py` file (often just an empty file) inside that directory to be considered a package by Python. Take for instance the general statement,

```python
import package as pkg # access module via `pkg.module` and some variable `var` inside module via `pkg.module.var`
from package import module # access some variable inside module via `module.var`
from package.module import var # access immediately some variable via `var` rather than `module.var`
```

So a package exactly like a folder and module refers to the file that holds all of your functions, classes, variables, etc.

## Getting Started

Let's create a folder for our project (I'll use `Project/`). I will be making a simple mystats program called `mystats` that takes some data and do some math to it. Let's create the following structure:

```bash
Project
├── LICENSE
├── Makefile
├── README.md
├── setup.py
├── mystats
│   ├── __init__.py
│   ├── math.py
│   └── stats.py
└── test
    └── test.py
```

* Inside the `mystats` package:
    * `stats.py`: The main file, the heart of the package.
    * `math.py`: A helper module separated from `stats` to promote modularity (often a good idea to separate your programs into components)
    * `__init__.py`: The file that allows `mystats/` be a Python package and runs everytime we import `mystats`.
* You guessed it `test` folder is for our test environment.
* Let's not worry about the other files, those will be explained later.

Notice that we don't have a `main.py` file at the root directory. `main.py` is only necessary if you're creating an executable program (called via `python path/to/Project/main.py`). So `main.py` is optional and often not included when you're trying to make a package.

In `mystats/math.py` let's implement a simple function that sums all element of an array,

```python
# mystats/math.py
def sum(arr):
    sum = 0
    for x in arr:
        sum += x

    return sum
```

In `mystats/stats.py` let's implement the average function,

```python
# mystats/stats.py
from mystats import math

def avg(data):
    """ Take the average of an array `data`. """
    return math.sum(data) / len(data)d
```

Pay attention to the first line. You may be tempted to use `import math` or even `from . import math`. Don't, because those statements relies on relative path (i.e., relative to the package folder) which errors out when your working directory is outside of this package folder. We'd like our program to work on every working directory and on every computer (that has Python 3.x).

Now for the `__init__.py` **we do not leave it empty**,

```python
from .stats import *
```

To understand why this is essential to a package see [Understanding \_\_init\_\_.py](#Understanding-__init__.py) otherwise move onto [Testing Your Program](#testing-your-program)

### Understanding \_\_init\_\_.py <!-- TODO: Make collapsible (bootstrap) -->

If we must access an actual variable inside a module via `package.module.something` you have probably seen a really simple way such as:

```python
import numpy as np

arr = np.sum([1,2,3])
```


In the example above it looks like `numpy` is a package since we directly imported `numpy` however we're treating `numpy` as if it was a module since we can immediately do `numpy.sum` which `sum` obviously a function. The truth is `numpy` not really a package but more module-like at least its no longer useful to call it a package. This is thanks to the `__init__.py` file. The `__init__.py` is a file that gets run everytime we import a package (e.g., `import package` or `from package ...`).

Back to our `mystats` package. To access `sum` if `__init__.py` was empty we must use:

```python
# cwd is project root
import mystats as st

data = [1,2,3]
st.stats.sum(data)
```

To ignore the need for stating `st.stats.sum ==> st.sum` we simply tell `__init__.py` to just dump everything from `stats.py` when importing the package `mystats`,

```python
# mystats/__init__.py
from .stats import *

# To only import sum
from .stats import sum
```

> **Note**: `.stats` is used instead of `stats` to strictly refer to the module that exist in the current package `mystats` and not any other package/modules in the global environment.

We now see that everytime we import `mystats` we also import all or just `sum` from `stats` module to the console thus rendering `mystats` a module-like with the ability of simply importing via `st.sum`.

## Testing Your Program

Okay, we've implemented some simple functions and it should be working. Let's go ahead and test our program out in `test/test.py`. Ideally our test should represent typical usage of our program which should not need any special syntax just like using `numpy`.

```python
import mystats as st

# Sanity Test

data = [1,2,3]
expected = 2.0
actual = st.avg(data)

if actual == expected:
    print("SUCCESS: The average is {}".format(actual))
else:
    print("FAIL: Oh no, your average is {} but it should be {}.".format(actual, expected))
```

Running this file anywhere you will get an error,

```bash
[.../Project/]
$ python test/test.py

Traceback (most recent call last):
  File "test/test.py", line 1, in <module>
    import mystats as st
ModuleNotFoundError: No module named 'mystats'


[.../Project/test]
$ python test.py

Traceback (most recent call last):
  File "test.py", line 1, in <module>
    import mystats as st
ModuleNotFoundError: No module named 'mystats'
```

This error occurs because Python cannot find `mystats` anywhere inside your terminal's environment variable `PYTHONPATH` or inside Python's environment `sys.path` (both variables are shared, Python imports `PYTHONPATH` and default paths to `sys.path` everytime you run Python). Open up Python and run. You'll see where Python are reading its packages:

```python
>>> import sys
>>> sys.path
[..., '/path/to/python3.x/site-packages']
```

To fix this error you have 3 options:

1. **Not recommended:** Place your package into one of the `sys.path`

    I do not recommend this because these paths are often managed by your system.
2. Set PYTHONPATH variable to your project directory. I will not make the instructions because the method differs on your operating system and terminal environment. So Google away or use step 3.
3. **Recommended:** Add the following lines to the very top of all your test files,
```python
import sys
from pathlib import Path # installed by default by Python 3.x
PROJECT_PATH = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_PATH))
```
```python
# Rest of your code
import mystats as st
...
```

* `__file__` : Refers to the absolute filepath for instance `/path/to/Project/test/test.py`
* `some_path.parents[1]` : Returns the second parent (or grandparent) of `some_path` which is `/path/to/Project`
* Other people recommend using the `os` module which to me looks like a total nightmare which I can never memorize.

```python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```
* I find the `pathlib.Path` more useful and intuitive than `os` to parse paths.
Regardless which option you choose, you should now be able toconfirm that your program works.

## Setup your Program for Distribution

Since your program works, we will now make sure your users/clients can install them easily and understand the usage easily. Recall our project structure,

```bash
Project
├── mystats
│   ├── __init__.py
│   ├── math.py
│   └── stats.py
├── Makefile
├── README.md
├── LICENSE
└── setup.py
```

To understand the other files I recommend taking a look at [Hitchhiker's Guide on Structuring Your Project](http://docs.python-guide.org/en/latest/writing/structure/). I will briefly summarize:

* `README.md`(Optional): Description, instructions, informations for your user. Printed at the front page of your GitHub repository
* `setup.py` (Optional): Required only for packaging.
* `Makefile` (Optional): Script your commands called by `make command_name`. Often used to consolidate test, git, installation commands.
* `LICENSE` (Optional): Required only for legal issues.

I will describe three common options in distributing your program.

- [Compiled Package on the Go](#compiled-package-on-the-go)
- [Setup on the Go](#setup-on-the-go)
- [Setup Anywhere - Upload Your Package to PyPI](#setup-anywhere-with-pypi)

### Compiled Package on the Go

Your project folder is already compiled in a Python sense so just place the whole project folder (or zip it up) and send them to your users.

* **Pros**
    * No extra step to distribute or compile
    * Easily accessible and editable
* **Cons**
    * Users must edit PYTHONPATH or append `sys.path` to use it.
    * Users must install any Python dependencies.

This is great for distributing development code to your team, but not optimal for users especially if they are beginners at Python.


### Setup on the Go

To create a setup file on the go we need `setup.py` and the Python module `setuptools` (installed by default)

```python
from setuptools import setup

setup(name='mystats',
      version='0.1.0',
      description='Easily calculate some statistics',
      url='http://github.com/ketozhang/mystats',
      author='Keto Zhang',
      author_email='keto.zhang@gmail.com',
      packages=['mystats'],
      python_requires='>=3',
      install_requires=[] # any packages you want your users to automatically install goes here, I'll leave this blank
      )
```

See [Setuptools documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use) for more instructions and fields.

You are now done, you can send your whole project folder or zip it up to your users. They must run the following command to install,

```python
# In the project folder

python setup.py install # or
pip install . # popular package management system often installed by default
```

Your package folder (`mystats`) is usually installed into on of the default paths in `sys.path` which is `'/path/to/python3.x/site-packages'`

* **Pros**
    * Users don't need to deal with the Python paths.
* **Cons**
    * Requires manually downloading and installation.

### Setup Anywhere - Upload Your Package to PyPI

[PyPI](https://pypi.org/) is the default Package Index where you can host your packages on their servers for free. This allows your users to simply install your packages simply by knowing the name of your package:

```bash
pip install mystats
```

> **Note**: Make sure to update and install pip and twine (`pip install --upgrade pip twine`). Pip is the package manager and twine controls secure upload to PyPI. `python setup.py upload` has been deprected from the old PyPI domain pypi.python.org.

First, head to [https://pypi.org/](https://pypi.org/) and register an acccount if you don't have one.

Next, we zip our distribution with some meta information. There are two methods:

*  **Old way** : Source distribution which outputs two directories. Pay attention to the directory `dist/` that includes a tarball (`.tar.gz`) file with your distribution and meta information.
```bash
python setup.py sdist
```
* **New way**: [Wheel](https://pythonwheels.com/) is the new standard of distribution which outputs three directories. Pay attention to directory `dist/` which includes wheel file (`.whl`) and tarball.
```python
python setup.py sdist bdist_wheel
```

Finally we upload your package (everything inside `dist/`) to PyPI which will also check if your package name is taken (`python setup.py register` is deprecated):

```bash
twine upload dist/*
```

If you get an error it's likely due to your package name being taken or you put your credential in wrong.
