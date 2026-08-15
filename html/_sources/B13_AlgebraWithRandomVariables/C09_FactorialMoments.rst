

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />






|newpage|

Factorial Moments
========================================================



Calculating the factorial moments from the raw moments
---------------------------------------------------------------

.. method:: ctx.factorial_moments_from_rawmoments(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Calculates the factorial moments `\mu'_{[r]}` from the raw moments `\mu'_r` 

    .. math::  \mu'_{[r]} = \sum_{j=0}^r s(r,j) \mu'_j,

    where `s(r,j)` is the Stirling number of the first kind (see :ref:`stirling1() <rst_mpm_stirling1>`).




.. _rst_factorial_moments_from_cumulants: 

Calculating the factorial moments from the cumulants
---------------------------------------------------------------

.. method:: ctx.factorial_moments_from_cumulants(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Calculates the factorial moments `\mu'_{[r]}` from the raw moments `\mu'_r` 

    .. math::  \mu'_{[r]} = \sum_{j=0}^r s(r,j) \mu'_j,

    where `s(r,j)` is the Stirling number of the first kind (see :ref:`stirling1() <rst_mpm_stirling1>`).






