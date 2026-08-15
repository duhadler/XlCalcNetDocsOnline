

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_hypoexponential: 

Hypoexponential (Generalized Erlang) Distribution
===============================================================================


.. py:class:: ctx.dist_hypoexponential(n, lambdaj)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The hypoexponential distribution is a continuous probability distribution with `n` rate parameters `\lambda_j > 0, j=1 \ldots n`, and the support interval `(0, +\infty)`. It is the distribution of the sum of `n` independent exponential variables with parameters `\lambda_j`. It is called the hypoexponential distribution as it has a coefficient of variation less than one, compared to the hyperexponential distribution which has coefficient of variation greater than one and the exponential distribution which has coefficient of variation of one. If all parameters are equal (`\lambda_j = \lambda`), the hypoexponential distribution is identical with the Erlang distribution (which is a special case of the gamma distribution wherein the shape parameter of the distribution is an integer).


    See also: Wikipedia :cite:p:`WikipediaDis74`, Wikipedia :cite:p:`WikipediaDis75`, MathWorld :cite:p:`WolframDis74`, :cite:t:`Chesneau2018`, :cite:t:`Smaili2013`.




|cr|

.. method:: dist_hypoexponential.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a hypoexponential distribution:


    .. math:: \text{pdf}_X(x) = \begin{cases}
            \dfrac{\lambda^n x^{n-1} e^{-\lambda x}}{(n-1)!} & \text{for all parameters equal: } \lambda_j = \lambda, \\
            \displaystyle\sum_{j=1}^n  \dfrac{\lambda_j}{d_j}  e^{-\lambda_j x} & \text{for all parameters distinct: } \lambda_j \ne \lambda_k \text{ for } j \ne k, \\
            -\boldsymbol{\alpha}e^{x\Theta}\Theta\boldsymbol{1} & \text{for general parameters: }\lambda_j > 0,
        \end{cases}


    where `\boldsymbol{\alpha}=(1,0,\dots,0)`, `\boldsymbol{1}` is a column vector of ones of the size `n`, `e^{A}` is the matrix exponential of `A`, and 

    .. math:: 
        d_j = \prod_{k=1, k \ne j}^n \left(1 - \frac{\lambda_j}{\lambda_k} \right), \quad \Theta = \left[\begin{matrix}-\lambda_{1}&\lambda_{1}&0&\dots&0&0\\
            0&-\lambda_{2}&\lambda_{2}&\ddots&0&0\\
            \vdots&\ddots&\ddots&\ddots&\ddots&\vdots\\
            0&0&\ddots&-\lambda_{n-2}&\lambda_{n-2}&0\\
            0&0&\dots&0&-\lambda_{n-1}&\lambda_{n-1}\\
            0&0&\dots&0&0&-\lambda_{n}
        \end{matrix}\right]\; .
        :label: hypoexp_matrix




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", mp_hypoexponential(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_hypoexponential.cdf(x)

Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a hypoexponential distribution:


.. math:: \text{cdf}_X(x) = \begin{cases}
        P(n, \lambda x) & \text{for all parameters equal: } \lambda_j = \lambda, \\
        1 - \displaystyle\sum_{j=1}^n  \dfrac{1}{d_j}  e^{-\lambda_j x} & \text{for all parameters distinct: } \lambda_j \ne \lambda_k \text{ for } j \ne k, \\
        1-\boldsymbol{\alpha}e^{x\Theta}\boldsymbol{1} & \text{for general parameters: }\lambda_j > 0,
    \end{cases}


where `P(\cdot)` is the lower regularized gamma function, `d_j` and `\Theta` are defined in equation :eq:`hypoexp_matrix`, `\boldsymbol{\alpha}=(1,0,\dots,0)`, `\boldsymbol{1}` is a column vector of ones of the size `n`, and `e^{A}` is the matrix exponential of `A`.



.. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; x = 3; 
    >>> print ("cdf: ", mp_hypoexponential(mu, sigma).pdf(x))
    6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_hypoexponential.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a hypoexponential distribution:


    .. math:: \text{sf}_X(x) = \begin{cases}
            Q(n, \lambda x) & \text{for all parameters equal: } \lambda_j = \lambda, \\
            \displaystyle\sum_{j=1}^n  \dfrac{1}{d_j}  e^{-\lambda_j x} & \text{for all parameters distinct: } \lambda_j \ne \lambda_k \text{ for } j \ne k, \\
            \boldsymbol{\alpha}e^{x\Theta}\boldsymbol{1} & \text{for general parameters: }\lambda_j > 0,
        \end{cases}



    where `Q(\cdot)` is the upper regularized gamma function, `d_j` and `\Theta` are defined in equation :eq:`hypoexp_matrix`, `\boldsymbol{\alpha}=(1,0,\dots,0)`, `\boldsymbol{1}` is a column vector of ones of the size `n`, and `e^{A}` is the matrix exponential of `A`.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", mp_hypoexponential(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_hypoexponential.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a hypoexponential distribution.

    There is no known closed form for `\text{qtf}_X(q)` or `\text{isf}_X(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", mp_hypoexponential(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypoexponential.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a hypoexponential distribution.

    There is no known closed form for `\text{qtf}_X(q)` or `\text{isf}_X(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", mp_hypoexponential(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypoexponential.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a hypoexponential distribution:

    .. math:: C_X(t) = \prod_{j=1}^n \frac{\lambda_j}{\lambda_j-it}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_hypoexponential(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypoexponential.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a hypoexponential distribution:

    .. math:: M_X(t) =  \prod_{j=1}^n \frac{\lambda_j}{\lambda_j-t}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", mp_hypoexponential(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypoexponential.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a hypoexponential distribution:

    .. math:: K_X(t) = \sum_{j=1}^n \log \left( \frac{\lambda_j}{\lambda_j-t} \right)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", mp_hypoexponential(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_hypoexponential.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a hypoexponential distribution. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_hypoexponential(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_hypoexponential.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a hypoexponential distribution. The cumulants are given by 


    .. math::  \kappa_{X}(r) = (r-1)! \sum_{j=1}^n \frac{1}{\lambda_j^r}



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", mp_hypoexponential(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




