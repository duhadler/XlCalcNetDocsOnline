





.. |vspace| raw:: html

   <br />





.. only:: html


Preface
=========================================


.. only:: html


    XlCalcNet is a numerical library with parts written in Python and other parts written in C\#, C++, C and Pascal, focussing on numerical calculations in multiple precision and data visualisation.

    Since the main goal is to give access to software written in Python (or via PythonNet software written in C\#) from within spreadsheet formulas, a dedicated CPython installation is strongly recommend, to make it easier to configure the interaction with Microsoft Excel, without disturbing existing Python installations.

    The interaction with Microsoft Excel is achieved by running a socket server written in Python, which is called from spreadsheet formulas using the functionality provided by Excel.Dna.

    The code which is necessary to make this work overall contains much more C\# and C/C++ than Python, so the project is not really suitable as a project on PyPI, but is provided as a Github project only. Both the source code and precompiled binaries are included, since compiling all of the source code requires MSYS2, Free Pascal and Visual Studio, which not all Excel users will be familiar with.

    On the Python side XlCalcNet uses Mpmath 4.0 to provide a rich set of functions in arbitrary precision, using not only Mpmath's binary and interval data types, but also Python's built-in Decimal and Fraction data types. If GMP2 is installed, its data types can be used in many cases instead of Mpmath's binary data types, being much faster. Likewise, if Python-Flint is installed, its data types  can be used in many cases instead of Mpmath's interval data types, being much faster, and often also more accurate.

    On the C/C++ side, XlCalcNet uses DAMath, Boost Math, Boost Multiprecision and Eigen to provide numerical functions in single, double, extended, quadruple and octuple precision, which are available to the user both from C\# and Python.

    The XlCalcNet2 library, which is licensed under the LGPL-3.0 and is therefore provided as a separate project, is based on Boost Math, Boost Multiprecision, Eigen, GMP, MPFR, MPC and Flint and provides functions for the same data types as XlCalcNet and also in arbitrary precision.

    XlCalcNet is intended to be used together with existing Python libraries like NumPy, Matplotlib, Pandas, SciPy. It can also be used from recent versions of RStudio and R, using the reticulate package.

