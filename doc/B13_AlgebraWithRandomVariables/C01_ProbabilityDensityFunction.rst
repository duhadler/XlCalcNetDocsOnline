

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />






Probability density function (pdf)
========================================================




Calculating the pdf from the cdf
-------------------------------------------------------------------------------

.. method:: ctx.pdf_from_cdf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Returns `\text{pdf}_X(x)` from the cumulative distribution function (cdf) of a random variable `X`:

    .. math:: \text{pdf}_X(x) = \frac{\mathrm{d}}{\mathrm{d}x} \text{cdf}_X(x).


    Using this method can be a viable option when the cdf, but not the pdf, is available in closed form.




.. _rst_gil_pelaez_pdf: 

Calculating the pdf from the characteristic function
-------------------------------------------------------------------------------

.. method:: ctx.pdf_from_cf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Calculates the pdf as the inverse Fourier transform of its characteristic function.

    The PDF of Y is the inverse Fourier transform of its characteristic function,

    .. math:: \text{pdf}_X(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{ity} C_X(t) \mathrm{d} y  = \frac{1}{\pi} \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t.

    where `\Re (z)` denotes the real part of `z`. We also have


    .. math:: \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t = \int_{0}^{\infty} \Re \left ( C_X(t) \right ) \cos(t x) \mathrm{d} t +   \int_{0}^{\infty} \Im \left (  C_X(t) \right ) \sin(t x) \mathrm{d} t.

    Using the right-hand side of this equation allows for efficient use of the quadrature formula of Fillon, with the half-period  `\omega = \pi/x`.




