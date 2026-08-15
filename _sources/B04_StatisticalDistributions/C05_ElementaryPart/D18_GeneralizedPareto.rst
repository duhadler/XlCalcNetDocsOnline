

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_genpareto: 

Generalized Pareto distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_genpareto(n1, n2, lambda, **kwargs)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    These functions return PDF, CDF, and ICDF of the Generalized Pareto distribution with parameters \mu \in \mathbb R, \sigma >0`, and `c \in \mathbb R`, where the support of `x\ge \mu`  when `c \ge 0`, and `\mu \le x \le \mu -\sigma /c`  when `c <0`.


    See also: Wikipedia :cite:p:`WikipediaDis65`, :cite:t:`Pires2018`,  :cite:t:`Kleiber2003`, 



|cr|

.. method:: dist_genpareto.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Generalized Pareto distribution:

    .. math:: \text{pdf}_X(x) =  f_{c }(z)={\begin{cases}(1+c z)^{-{\frac {c +1}{c }}}&{\text{for }}c \neq 0,\\e^{-z}&{\text{for }}c =0.\end{cases}}, \quad \text{where } z = \frac{x-\mu}{\sigma}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_genpareto(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_genpareto.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Generalized Pareto distribution:


    .. math:: \text{cdf}_X(x)={\begin{cases}
            1-\left(1 + c z\right)^{-1/c } & \text{for }c \neq 0,\\
            1-\exp \left(-z\right) & \text{for }c =0,
            \end{cases}}, \quad \text{where } z = \frac{x-\mu}{\sigma}


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_genpareto(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_genpareto.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following a Generalized Pareto distribution:

    .. math:: \text{sf}_X(x)={\begin{cases}
            \left(1 + c z\right)^{-1/c } & \text{for }c \neq 0,\\
            \exp \left(-z\right) & \text{for }c =0,
            \end{cases}}, \quad \text{where } z = \frac{x-\mu}{\sigma}

    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_genpareto(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_genpareto.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following a Generalized Pareto distribution:

    .. math:: \text{qtf}_X(q) = \mu + \sigma \times {\begin{cases}
            \dfrac{(1-q)^{-c}-1}{c} & \text{for }c \neq 0,\\
            -\log(1-q) & \text{for }c =0,
            \end{cases}}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_genpareto(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genpareto.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following a Generalized Pareto distribution:

    .. math:: \text{isf}_X(q) = \mu + \sigma \times {\begin{cases}
            \dfrac{(q)^{-c}-1}{c} & \text{for }c \neq 0,\\
            -\log(q) & \text{for }c =0,
            \end{cases}}



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_genpareto(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genpareto.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Generalized Pareto distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_genpareto(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_genpareto.m_x(t)

    Returns None, since the moment generating function does not exist.




|cr|

.. method:: dist_genpareto.k_x(t, k = 0)

    Returns None, since the cumulant generating function does not exist.







|cr|

.. method:: dist_genpareto.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Generalized Pareto distribution (see Kleiber_2007_Dagum_moments). The rth moment exists for `c < 1/r` and equals


    .. math:: \mu_k = \frac{r! \sigma!}{\prod_{i=1}^r (1 - i c)}.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_genpareto(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_genpareto.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Generalized Pareto distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", dist_genpareto(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







