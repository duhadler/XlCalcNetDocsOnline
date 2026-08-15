



.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />






|newpage|



.. _rst_mpfunlablib_of_contexts: 

User defined functions based on multiple precision arithmetic (Python)
=============================================================================


Overview
---------------------------------------------


High-level code in xlcalcnet is, as in mpmath, implemented as methods on a "context object". The context implements arithmetic, type conversions and other fundamental operations. The context also holds settings such as precision, and stores cache data. A total of 6 different contexts (with a mostly compatible interface) are provided so that the high-level algorithms can be used with different implementations of the underlying arithmetic, allowing different features and speed-accuracy tradeoffs. 




.. _rst_fpmlib_def: 

Double-precision arithmetic (``fpmlib``)
---------------------------------------------

Although mpmath is generally designed for arbitrary-precision arithmetic, many of the high-level algorithms work perfectly well with ordinary Python ``float`` and ``complex`` numbers, which use hardware double precision (on most systems, this corresponds to 53 bits of precision). Whereas the global functions (which are methods of the ``mp`` object) always convert inputs to mpmath numbers, the ``fp`` object instead converts them to ``float`` or ``complex``, and in some cases employs basic functions optimized for double precision. When large amounts of function evaluations (numerical integration, plotting, etc) are required, and when ``fp`` arithmetic provides sufficient accuracy, this can give a significant speedup over ``mp`` arithmetic.




.. _rst_mpmlib_def: 

Binary floating-point in arbitrary-precision and with arbitrary exponent  (``mpmlib``)
---------------------------------------------------------------------------------------------

The ``mp`` context is what most users probably want to use most of the time, as it supports the most functions, is most well-tested, and is implemented with a high level of optimization. Nearly all examples in this documentation use ``mp`` functions.






.. _rst_ipmlib_def: 

Interval arithmetic in arbitrary-precision and with arbitrary exponent (``ipmlib``)
--------------------------------------------------------------------------------------

The ``iv.mpf`` type represents a closed interval `[a,b]`; that is, the set `\{x : a \le x \le b\}`, where `a` and `b` are arbitrary-precision floating-point values, possibly `\pm \infty`. The ``iv.mpc`` type represents a rectangular complex interval `[a,b] + [c,d]i`; that is, the set `\{z = x+iy : a \le x \le b \land c \le y \le d\}`.

Interval arithmetic provides rigorous error tracking. If `f` is a mathematical function and `\hat f` is its interval arithmetic version, then the basic guarantee of interval arithmetic is that `f(v) \subseteq \hat f(v)` for any input interval `v`. Put differently, if an interval represents the known uncertainty for a fixed number, any sequence of interval operations will produce an interval that contains what would be the result of applying the same sequence of operations to the exact number. The principal drawbacks of interval arithmetic are speed (``iv`` arithmetic is typically at least two times slower than ``mp`` arithmetic) and that it sometimes provides far too pessimistic bounds.





.. _rst_dpmlib_def: 

Decimal floating-point in arbitrary-precision with limited exponent (``dpmlib``)
---------------------------------------------------------------------------------



Additional contexts are used in xlcalcnet to implement its functions for the mpmath data types, and the Decimal data type, which is part of Python. 


Both real numbers (mpf) and complex numbers (mpc) are implemented. 


In CPython, the ``decimal`` module provides support for fast correctly-rounded decimal floating point arithmetic. See https://docs.python.org/3.3/library/decimal.html for a decription of the ``Decimal`` data type.





.. _rst_qpmlib_def: 

Rational numbers (quotients) in arbitrary-precision (``qpmlib``)
---------------------------------------------------------------------------------


The ``qpm`` data type is mostly useful in the context of linear algebra, where it can provide exact results.

Both real numbers (mpf) and complex numbers (mpc) are implemented. 

The internal representation dependes on what else is installed on the system:

If ``apm`` is available, the ``fmpq`` data type is used; otherwise, if ``gpm`` is available, the ``mpq`` data type is used; otherwise, Python's built in ``Fraction`` data type is used.








.. _rst_gpmlib_def: 

Binary floating-point in arbitrary-precision with limited exponent (``gpmlib``)
--------------------------------------------------------------------------------------


gmpy2 is a C-coded Python extension module that supports multiple-precision arithmetic. 

https://gmpy2.readthedocs.io/en/latest/

gmpy2 is the successor to the original gmpy module. The gmpy module only supported the GMP multiple-precision library. gmpy2 adds support for the MPFR (correctly rounded real floating-point arithmetic) and MPC (correctly rounded complex floating-point arithmetic) libraries. gmpy2 also updates the API and naming conventions to be more consistent and support the additional functionality. The following libraries are supported:








.. _rst_apmlib_def: 

Binary balls in arbitrary-precision and with arbitrary exponent  (``apmlib``)
-------------------------------------------------------------------------------------

The ``apm`` context is what most users probably want to use most of the time, as it supports the most functions, is most well-tested, and is implemented with a high level of optimization.


pythonflint is a C-coded Python extension module that supports multiple-precision arithmetic. 




