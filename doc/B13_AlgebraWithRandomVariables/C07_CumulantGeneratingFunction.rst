

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />






|newpage|

Cumulant generating function
========================================================

See also Wikipedia :cite:p:`WikipediaDef11`.



Calculating the cumulant-generating function from the  characteristic function
-------------------------------------------------------------------------------

.. method:: ctx.cgf_from_cf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    The characteristic function `\varphi _{X}(t)` is related to the moment-generating function via `\varphi _{X}(t)=M_{iX}(t)=M_{X}(it)`: the characteristic function is the moment-generating function of `iX` or the moment generating function of `X` evaluated on the imaginary axis. This function can also be viewed as the Fourier transform of the probability density function, which can therefore be deduced from it by inverse Fourier transform.



Calculating the cumulant-generating function from the moment-generating function
----------------------------------------------------------------------------------------

.. method:: ctx.cgf_from_mgf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    The cumulant-generating function is defined as the logarithm of the moment-generating function; some instead define the cumulant-generating function as the logarithm of the characteristic function, while others call this latter the second cumulant-generating function.


Calculating the cumulant-generating function from the probability-generating function
----------------------------------------------------------------------------------------

.. method:: ctx.cgf_from_pgf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    The cumulant-generating function is defined as the logarithm of the moment-generating function; some instead define the cumulant-generating function as the logarithm of the characteristic function, while others call this latter the second cumulant-generating function.




Calculating the cumulant-generating function from the cumulants
----------------------------------------------------------------------------------------

.. method:: ctx.cgf_from_cumulants(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    The cumulants `\kappa_n` are obtained from a power series expansion of the cumulant generating function: 

    .. math::  K(t)=\sum _{n=1}^{\infty }\kappa _{n}{\frac {t^{n}}{n!}}=\mu t+\sigma ^{2}{\frac {t^{2}}{2}}+\cdots .

    This expansion is a Maclaurin series, so the n-th cumulant can be obtained by differentiating the above expansion n times and evaluating the result at zero:

    .. math::  \kappa _{n}=K^{(n)}(0).

	

