

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_voigt_profile: 


Voigt Profile Distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_voigt_profile(n1, n2, lambda, **kwargs)


    The Voigt profile is a probability distribution given by a convolution of a Cauchy-Lorentz distribution and a Gaussian distribution. It is often used in analyzing data from spectroscopy or diffraction.

    These functions return PDF, CDF, and ICDF of the Voigt profile distribution with location
    `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis56`.




|cr|

.. method:: dist_voigt_profile.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Voigt profile distribution:

    .. math:: \text{pdf}_X(x) = V(x; \sigma, \gamma) = \frac{\Re[w(z)]}{\sigma \sqrt{2 \pi}}, \quad \text{where } z = \frac{x + i\gamma}{\sigma \sqrt{\pi}}.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_voigt_profile(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_voigt_profile.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Voigt profile distribution:

    .. math:: \text{cdf}_X(x) = \Re \left[ \frac{1}{2} + \frac{\text{erf}(z)}{2} + \frac{i z^2}{\pi} {}_2F_2 \left( 1,1; \tfrac{3}{2}, 2; -z^2  \right)    \right].



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_voigt_profile(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_voigt_profile.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Voigt profile distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_voigt_profile(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_voigt_profile.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Voigt profile distribution:

    .. math:: \text{qtf}_X(q) =  \text{no closed form}.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_voigt_profile(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_voigt_profile.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Voigt profile distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_voigt_profile(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_voigt_profile.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Voigt profile distribution:

    .. math::  C_X(t) = e^{-\gamma |t| -\sigma^2 t^2 /2}.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_voigt_profile(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_voigt_profile.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.


	

|cr|

.. method:: dist_voigt_profile.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.




|cr|

.. method:: dist_voigt_profile.moments(k)

    Returns ``NaN``, since moments do not exist.



|cr|

.. method:: dist_voigt_profile.cumulants(k)

    Returns ``NaN``, since cumulants do not exist.






