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

One of the 