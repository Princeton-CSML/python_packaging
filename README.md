[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/vineetbansal/python_packaging/HEAD)

# Best Practices in Python Packaging 

October 1, 2021\
9:00 am\
Location: 26 Prospect Avenue, Room 103

This workshop is for researchers who are already using Python for their work, but who want to distribute
their software to the broader scientific community by packaging their code for other researchers to easily use.
We will learn about structuring our code as modules and packages, and publishing packages on PyPI and conda,
both of which are commonly used in the life sciences to install open-source software. We will gain insights
into ensuring reproducibility in research through the process of versioning, continuous integration and testing.
Finally, we will look at a sample Python project that puts all these best practices together.

### Before the workshop

We will be using the [Anaconda Python Distribution](https://www.anaconda.com/download) for this course. Anaconda is a popular software that gives us everything we need to get started in Python - the Python 3 interpreter, common Python libraries for scientific computing, plotting and analysis, jupyter Notebooks, and a lightweight IDE (Integrated Development Environment) for more advanced users.

Please ensure that you follow the instructions posted at:
[Workshops that use Jupyter notebooks](https://researchcomputing.princeton.edu/learn/workshops-live-trainings/requirements-picscie-virtual-workshops#jupyter)
and validate your setup using the sample notebook available as part of the instructions.

 Advanced users may just choose to install [Miniconda](https://docs.conda.io/en/latest/miniconda.html). If you do so, please make sure that you have the jupyterlab package installed.
```
conda install jupyterlab 
```

If you are still having trouble installing Anaconda, you may want to try the Binder link in this README to launch the jupyter notebook remotely. Note, however, that you may have limited success with following along most of the tutorial.

#### Other useful preparatory work

- You may want to ensure that you have an account at [GitHub](https://github.com/) as well as [PyPI](https://pypi.org/), as we will be using both to illustrate some CI/CD concepts.

- A final sample package that brings together a lot of what we will discuss is located at [https://github.com/vineetbansal/walrus](https://github.com/vineetbansal/walrus). You may find it useful to clone that repository for the workshop as well. A more advanced version of this package that incorporates C++ extensions is at [https://github.com/vineetbansal/walrus_cpp](https://github.com/vineetbansal/walrus_cpp).

- One the Linux command line, we will be using the `tree` command quite a lot to inspect the contents of several folders. MacOS users may find it helpful to have the following lines in their `$HOME/.bash_profile`, which is a barebones implementation of `tree`:
  ```
  alias tree="find . -print | grep -v "^./.git/" | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
  ```

- The Python interpreter and the Pytest library create cache folders in our filesystem that may get in the way of understanding the files/folders involved while authoring a package. To disable caching, all users may also want to have the following lines in their `$HOME/.bash_profile`, **just for this workshop**, and remove these later.
  ```
  alias pytest="pytest -p no:cacheprovider"
  export PYTHONDONTWRITEBYTECODE=1
  ```

 Remember to run `source ~/.bash_profile` if you make any changes to your `~/.bash_profile`, of course.
