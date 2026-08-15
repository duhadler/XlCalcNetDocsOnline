

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_half_normal: 

Half-normal distribution
===============================================================================


.. py:class:: ctx.dist_half_normal(sigma)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The half-normal distribution is a continuous probability distribution  with  standard deviation `\sigma > 0`, and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis43`, MathWorld :cite:p:`WolframDis43`, :cite:t:`CharfunDis43`, .





|cr|

.. method:: dist_half_normal.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an half-normal distribution:

    .. math:: \text{pdf}_X(x) = {\frac{\sqrt{2}}{\sigma \sqrt{\pi}}} \exp\left( {\frac {x^2 }{2\sigma^2 }} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", half_normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_half_normal.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an half-normal distribution:

    .. math:: \text{cdf}_X(x) = \text{erf}\left(\frac{x}{\sigma \sqrt{2}} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", half_normal(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_half_normal.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an half-normal distribution:

    .. math:: \text{sf}_X(x)  = \text{erfc}\left(\frac{x}{\sigma \sqrt{2}} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", half_normal(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_half_normal.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an half-normal distribution:

    .. math:: \text{qtf}_X(q) =  \sigma \sqrt{2} \cdot \text{erf}^{-1}(q).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", half_normal(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_half_normal.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an half-normal distribution:

    .. math:: \text{isf}_X(q) =  \sigma \sqrt{2} \cdot \text{erfc}^{-1}(q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", half_normal(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_half_normal.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an half-normal distribution:

    .. math::  C_X(t) = M\left( \frac{3}{2},  \frac{1}{2} \frac{-t^2}{2} \right) +  \frac{2 \sqrt{2} \, i t  }{\sqrt{\pi}}   M\left(2,  \frac{3}{2}, \frac{-t^2}{2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", half_normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_half_normal.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an half-normal distribution:

    .. math:: M_X(t) =  M\left( \frac{3}{2},  \frac{1}{2} \frac{t^2}{2} \right) +  \frac{2 \sqrt{2} \, t }{\sqrt{\pi}}  M\left( 2,  \frac{3}{2}, \frac{t^2}{2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", half_normal(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_half_normal.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an half-normal distribution:

    .. math:: K_X(t) = \log \left[  M\left( \frac{3}{2},  \frac{1}{2} \frac{t^2}{2} \right) + \frac{2 \sqrt{2} \, t }{\sqrt{\pi}}  M\left(2,  \frac{3}{2}, \frac{t^2}{2} \right) \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", half_normal(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_half_normal.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an half-normal distribution (Wikipedia). The raw moments are calculated from the central moments.


    .. math::  

        \mu_{X}(r) = \begin{cases}
        \sqrt{\frac{2}{\pi}} k! \alpha^{2k-1} & \text{for } n=2k-1,\\
        (n+1)!! \alpha^n &  \text{for } n \text{ even},
        \end{cases} 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", half_normal(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_half_normal.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an half-normal distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", half_normal(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00



