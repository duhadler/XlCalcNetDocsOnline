

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />






|newpage|

Moment generating function
========================================================

See also Wikipedia :cite:p:`WikipediaDef10`.



Calculating the moment-generating function from the  pdf
-------------------------------------------------------------------------------

.. method:: ctx.mgf_from_pdf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



     The moment-generating function's definition expands to

    .. math::  M_{X}(t)=\operatorname {E} \left[e^{tX}\right]=\int _{-\infty }^{\infty }e^{tx}f_{X}(x)\,\mathrm{d} x




Calculating the moment-generating function from the  characteristic function
-------------------------------------------------------------------------------

.. method:: ctx.mgf_from_cf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    The characteristic function `\varphi _{X}(t)` is related to the moment-generating function via `\varphi _{X}(t)=M_{iX}(t)=M_{X}(it)`: the characteristic function is the moment-generating function of `iX` or the moment generating function of `X` evaluated on the imaginary axis. This function can also be viewed as the Fourier transform of the probability density function, which can therefore be deduced from it by inverse Fourier transform.



Calculating the moment-generating function from the cumulant-generating function
----------------------------------------------------------------------------------------

.. method:: ctx.mgf_from_cgf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    The cumulant-generating function is defined as the logarithm of the moment-generating function; some instead define the cumulant-generating function as the logarithm of the characteristic function, while others call this latter the second cumulant-generating function.



Calculating the moment-generating function from the probability-generating function
----------------------------------------------------------------------------------------

.. method:: ctx.mgf_from_pgf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    The probability-generating function is defined as `G(z)=E\left[z^{X}\right]`. This immediately implies that `G(e^{t})=E\left[e^{tX}\right]=M_{X}(t).`



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



Calculating the moment-generating function from the raw moments
----------------------------------------------------------------------------------------

.. method:: ctx.mgf_from_rawmoments(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    .. math::  M_{X}(t) = 1+tm_{1}+{\frac {t^{2}m_{2}}{2!}}+{\frac {t^{3}m_{3}}{3!}}+\cdots +{\frac {t^{n}m_{n}}{n!}}+\cdots 

    where `m_{n}` is the nth moment. Differentiating `M_{X}(t) i` times with respect to `t` and setting 
    `t = 0`, we obtain the ith moment about the origin.





