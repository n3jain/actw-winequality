# ACT-W Machine Learning 101

This workshop intends to help you get your feet wet with machine learning.
By no means will this workshop make you a machine learning expert -- you'll
definitely walk out here with deep holes in your knowledge of machine learning.
However, the hope is that you get enough bits of information that you can fill
in the gaps as you continue to learn in the future.

If you want an easier installation time, I recommend installing
[Anaconda](https://www.continuum.io/downloads). Anaconda ships with all the
libraries we will be using. However, I'll provide some brief installation
instructions of everything. This should install `Jupyter Notebook` -- open
this to get started. Otherwise, carry on with a more difficult (but flexible)
installation (note: not for the faint of heart if you do not have a package
manager installed).

To start, you'll need python and a few python libraries installed.

Make sure you have python 3 installed, if not, download and install here:
[Python Downloads](https://www.python.org/downloads/)

Open a terminal / command shell 
Check your python version: `which python`
Make sure this is a version greater than 3! If not, you may have another
version of python installed or some PATH variable may be incorrectly set.

Execute the following to install the libraries we'll be using:
```
pip install numpy pandas sklearn jupyter
```

This should install all necessary dependencies.

From there you should be able to execute `jupyter notebook` which will start
a local notebook server and then you can open the
`Act-W Machine Learning Workshop.ipynb` file. We'll do all of our work from
there.


All data was taken from the [UCI ML Repo](http://archive.ics.uci.edu/ml/datasets/Wine+Quality).
