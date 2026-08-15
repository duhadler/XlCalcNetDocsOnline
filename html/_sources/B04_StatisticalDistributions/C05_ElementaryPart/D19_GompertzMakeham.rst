

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_gompertz: 

Gompertz-Makeham distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_gompertz(a, b, lambda1=0, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Gompertz-Makeham distribution is a continuous probability distribution with parameters `a > 0, b > 0`, `\lambda \ge 0`, and the support interval `(0, +\infty)`. The hazard function has the form `\text{hf}_X(x) = a  e^{bx} + \lambda`.


    See also: Wikipedia :cite:p:`WikipediaDis66`, MathWorld :cite:p:`WolframDis66`, :cite:t:`Jodra2013`, :cite:t:`Riffi2018`.




|cr|

.. method:: dist_gompertz.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: \text{pdf}_X(x) = \text{hf}_X(x) \cdot \text{sf}_X(x) = (a  e^{bx} + \lambda) \cdot \exp \left[-\lambda x -\frac{a}{b} \left( e^{bx} - 1 \right)  \right]


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_gompertz(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_gompertz.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: \text{cdf}_X(x) = 1 - \exp \left[-\lambda x -\frac{a}{b} \left( e^{bx} - 1 \right)  \right] = -\mathrm{expm1}\left[-\lambda x -\frac{a}{b} \left(\mathrm{expm1}(bx) \right)  \right]


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_gompertz(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_gompertz.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: \text{sf}_X(x) = \exp \left[-\lambda x -\frac{a}{b} \left( e^{bx} - 1 \right)  \right] = \exp \left[-\lambda x -\frac{a}{b} \left(\mathrm{expm1}(bx) \right)  \right]


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_gompertz(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_gompertz.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: \text{qtf}_X(q) = {\begin{cases}
            \dfrac{1}{b} \mathrm{log1p}\left(-\dfrac{b}{a} \: \mathrm{log1p}(-q) \right) & {\text{for }}\lambda = 0,\\
            \dfrac{a}{b \lambda} - \dfrac{1}{\lambda} \mathrm{log1p}(-q) - \dfrac{1}{b} W_0\left( \dfrac{a}{\lambda} e^{a/\lambda} \cdot \mathrm{pow1p} (-q, -b/\lambda) \right) & {\text{for }} \lambda > 0,
            \end{cases}}

    where `W_0` denotes the principal branch of the Lambert `W` function (see ...).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_gompertz(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gompertz.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: \text{isf}_X(q) = {\begin{cases}
            \dfrac{1}{b} \mathrm{log1p}\left(-\dfrac{b}{a} \log(q) \right) & {\text{for }}\lambda = 0,\\
            \dfrac{a}{b \lambda} - \dfrac{1}{\lambda} \log(q) - \dfrac{1}{b} W_0\left( \dfrac{a}{\lambda} e^{a/\lambda} \cdot q^{-b/\lambda} \right) & {\text{for }} \lambda > 0,
            \end{cases}}

    where `W_0` denotes the principal branch of the Lambert `W` function (see ...).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_gompertz(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gompertz.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: C_X(t) = e^d \left(d \cdot E_{p(it)}(d) + \frac{\lambda}{b} E_{1+p(it)}(d)  \right), \quad \text{where } p(it) = \frac{\lambda-it}{b} \text{and } d=\frac{a}{b}.

    Here `E_p(z)` denotes the exponential integral, defined as `E_p(z) = z^{p-1} \Gamma(1-p,z) = z^{p-1} e^{-z} U(p,p,z)`. `\Gamma(\cdot)` denotes the incomplete gamma function (see ...), and `U(\cdot)` denotes Tricomi's hypergeometric function (see ...).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_gompertz(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gompertz.m_x(t)


    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: M_X(t) = e^d \left(d \cdot E_{p(t)}(d) + \frac{\lambda}{b} E_{1+p(t)}(d)  \right), \quad \text{where } p(t) = \frac{\lambda-t}{b} \text{and } d=\frac{a}{b}.


    Here `E_p(z)` denotes the exponential integral, defined as `E_p(z) = z^{p-1} \Gamma(1-p,z) = z^{p-1} e^{-z} U(p,p,z)`. `\Gamma(\cdot)` denotes the incomplete gamma function (see ...), and `U(\cdot)` denotes Tricomi's hypergeometric function (see ...).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_gompertz(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_gompertz.k_x(t, k = 0)


    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Gompertz-Makeham distribution:

    .. math:: K_X(t) = \log(M_X(t))


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_gompertz(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_gompertz.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Gompertz-Makeham distribution. The moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_gompertz(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_gompertz.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an Gompertz-Makeham distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_gompertz(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







