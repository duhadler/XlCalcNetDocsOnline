

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />






|newpage|

Characteristic function
========================================================


Calculating the characteristic function from the pdf (continuous distribution)
-------------------------------------------------------------------------------


.. method:: ctx.cf_from pdf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Let `X` denote a continuous univariate random variable with probability density function (PDF) `\text{pdf}_X(x)`, cumulative distribution function (CDF) `\text{cdf}_X(x)`, and moment generating function `M_X(t)`. The characteristic function of the distribution of `X`, given by the Fourier transform of its PDF, is defined as

    .. math:: C_X(t) = \operatorname{E} \left [e^{itX} \right] = M_X(it) = \int_{-\infty}^{\infty} e^{itx} \text{pdf}_X(x) \mathrm{d} x.

    Note however that the characteristic function of a distribution always exists, even when the probability density function or moment-generating function do not.




Calculating the characteristic function from the pmf (lattice distribution)
-------------------------------------------------------------------------------

.. method:: ctx.cf_from pmf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    For a discrete distribution on the nonnegative integers, it is defined as

    .. math::  C_X(t) = \operatorname{E}[e^{itX}] = \sum_{j=0}^{\infty} e^{ijt} \text{pmf}(j)

    See Johnson(2005), p. 50




Calculating the characteristic function from the quantile function
-------------------------------------------------------------------------------

.. method:: ctx.cf_from qtf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    .. math:: C_X(t) = \operatorname{E} \left[ e^{itX} \right] =  \int_{0}^{1} e^{it \: \text{qtf}_X(p)} dp.







Calculating the characteristic function from the raw moments
----------------------------------------------------------------------------------------

.. method:: ctx.cf_from_rawmoments(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Formally, we can write

    .. math:: C_X(t) = 1 + \sum_{k=1}^{\infty} \mu'_X(k) \frac{i^k t^k}{k!}

    .. math:: C_X(t) = 1 + \sum_{k=1}^{\infty} \operatorname {E} \left[X^{k}\right] \frac{i^k t^k}{k!}


    See also http://mathworld.wolfram.com/RawMoment.html for an expression involving cumulants.





