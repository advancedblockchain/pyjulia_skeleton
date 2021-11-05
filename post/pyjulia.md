# Setting up a Mixed Python/Julia Project on GitHub

This post will demonstrate the setup of a minimal GitHub repo containing both Python and Julia codes.
Julia, as a language, is most often used for abstract mathematics and scientific computing, and writing math codes without proper testing is a sure way to invite pain and frustration.
As such, we will focus on helping you set up a repository with mixed python and Julia codes and implementing automated testing.

Julia is a high-level, high-performance, dynamic programming language that is optimized for scientific computing.
It is a general-purpose programming language with a type system that is dynamically typed and dynamically dispatched, which makes it significantly faster than other interpreted languages such as Python and Ruby.
However, most of the scientific community, especially in the fields of data science and machine learning, have well-established python libraries.
Additionally, as great as Julia is for scientific computing, it is still difficult to beat the universality of python.
As such, a Julia-only model is often a good choice for a research project, but it is not a good choice for a production system that has to integrate with existing libraries and frameworks.

`PyJulia` is a Python wrapper for Julia that provides a high-level interface to Julia.
The mechanics of embedding Julia in Python code using `PyJulia` has been covered in other posts [here](https://towardsdatascience.com/how-to-embed-your-julia-code-into-python-to-speed-up-performance-e3ff0a94b6e)
and [here](https://towardsdatascience.com/run-native-julia-code-with-python-92d3e1079385).
This post will focus on the best practices of connecting the Julia and Python codes in a new code base, as well as configuring GitHub actions to run automated continuous integration (CI) workflows for your mixed Python+Julia code.

# Installing and configuring PyJulia for a project

To get started, you will need to make sure that Python and Julia are installed on your machine.
After that, you need to make sure you have the package manager for each language installed.
The easiest way to install PyJulia is via [PyPI](https://pypi.org/project/PyJulia/) using the `pip` command:
```sh
pip install julia
```

Once you have installed PyJulia, you can use its built-in `install` command to install the required `PyCall` Julia package and perform the necessary setup:
```python
import julia
julia.install()
```

According to the `PyJulia`'s documentation, the Python interpreter from `conda` is statically linked to `libpython` and `PyJulia` does not fully support such Python interpreters yet.
The recommended workaround is to pass `compiled_modules=False` to the Julia constructor once to disable Julia's precompilation cache mechanism.
```python
from julia.api import Julia
jl = Julia(compiled_modules=False)
```
Note this does affect performance, so you may consider switching to a different Python interpreter if performance is an issue.
More information on this issue can be found [here](https://pyjulia.readthedocs.io/en/latest/troubleshooting.html).

Now you can test your PyJulia installation by running the following code to test your installation.
```python
from julia import Main
Main.println("Hello, world!")
```

For most Python + Julia projects, you will also need to install dependencies for both languages.
In python, simply run `pip install -r requirements.txt` to install the dependencies.
In Julia, you can install the dependencies from the `Project.toml` file by running
```bash
julia --project=. -e "using Pkg; Pkg.build();"
```
assuming the current directory (`.`) contains the `Project.toml` file.  For the present example we will just have the `Example` package dependency as a placeholder.

Once the dependencies tree has been built, you can access this particular Julia environment from within your Python code by running:

```python
from julia import Pkg
Pkg.activate("<Proj_Dir>")
```
Where `<Proj_Dir>` is the directory where you have the `Project.toml` file.


# Setting up a Mixed Python + Julia Project

Now we have all the individual pices, the skeleton of a mixed Python + Julia project can look something like this:
```
.
├── Project.toml
├── requirements.txt
├── setup.cfg
├── setup.py
├── src
│   ├── py_jl
│   │   ├── julia_funcs.jl
│   │   └── julia_funcs.py
└── tests
    └── test_julia.py

```

Here the `setup.py` and `setup.cfg` files are used to install the present package as `py_jl`.

The `setup.cfg` also contains additional information about how to run tests using `pytest`.

```
% cat setup.cfg
[metadata]
name = py_jl

[options]
zip_safe = False
packages = find_namespace:
include_package_data = True
package_dir =
    =src

[options.packages.find]
where = src
exclude =
    tests

[tool:pytest]
norecursedirs =
    dist
    build
    .tox
testpaths = ./tests/
python_files = test_*.py%                                                                                                                                      
```

The full code is hosted on [GitHub](https://github.com/jmmshn/pyjulia_skeleton)