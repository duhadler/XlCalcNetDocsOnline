

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_wald: 

Boost: Wald (or Inverse Gaussian) distribution 
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the Wald distribution with mean `\mu>0`,  scale `b > 0`, and  the support interval `(0, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis16`, MathWorld :cite:p:`WolframDis16`,  BoostMath :cite:p:`BoostDis16`, :cite:t:`Ehrhardt2018` (3.9.32).




|cr|

.. _Ctx_WaldPdf:

.. method:: Ctx.wald_pdf(x, mu, b)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Wald distribution:

    .. math:: \text{pdf}(x) = \sqrt{\frac{b}{2\pi x^3}} \exp \left( \frac{-b(x-\mu)^2}{2\mu^2 x} \right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("WaldPdf(x, a, b): ", WaldPdf(x, a, b))
        >>> print ("dist_wald(a, b).pdf(x): ", dist_wald(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_WaldCdf:

.. method:: Ctx.wald_cdf(x, mu, b)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Wald distribution:

    .. math:: \text{cdf}(x) =  \Phi\left(\sqrt{\frac{b}{x}} \left(\frac{x}{\mu}-1\right)\right) + \exp \left( \frac{2b}{\mu} \right) \Phi\left(-\sqrt{\frac{b}{x}} \left(\frac{x}{\mu}+1\right)\right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("WaldCdf(x, a, b): ", WaldCdf(x, a, b))
        >>> print ("dist_wald(a, b).cdf(x): ", dist_wald(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_WaldQtf:

.. method:: Ctx.wald_qtf(q, mu, b)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Wald distribution:

    There is no known closed form for `\text{qtf}(q)`: it is computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("WaldQtf(q, a, b): ", WaldQtf(q, a, b))
        >>> print ("dist_wald(a, b).qtf(q): ", dist_wald(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_wald(mu, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Wald (or inverse Gaussian) distribution is a continuous probability distribution with mean `\mu>0`,  scale `b > 0`, and  the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis16`, MathWorld :cite:p:`WolframDis16`, BoostMath :cite:p:`BoostDis16`, :cite:t:`CharfunDis16`.





|cr|

.. method:: dist_wald.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a Wald distribution:

    .. math:: \text{pdf}_X(x) = \sqrt{\frac{b}{2\pi x^3}} \exp \left( \frac{-b(x-\mu)^2}{2\mu^2 x} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", wald(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_wald.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Wald distribution:

    .. math:: \text{cdf}_X(x) =  \Phi\left(\sqrt{\frac{b}{x}} \left(\frac{x}{\mu}-1\right)\right) + \exp \left( \frac{2b}{\mu} \right) \Phi\left(-\sqrt{\frac{b}{x}} \left(\frac{x}{\mu}+1\right)\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", wald(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_wald.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Wald distribution:

    .. math:: \text{sf}_X(x)  =  \Phi\left(-\sqrt{\frac{b}{x}} \left(\frac{x}{\mu}-1\right)\right) - \exp \left( \frac{2b}{\mu} \right) \Phi\left(-\sqrt{\frac{b}{x}} \left(\frac{x}{\mu}+1\right)\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", wald(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_wald.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Wald distribution:

    There is no known closed form for `\text{qtf}_X(q)` or `\text{isf}_X(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", wald(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wald.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Wald distribution:

    There is no known closed form for `\text{qtf}_X(q)` or `\text{isf}_X(q)`: These functions are computed with Newton iterations where the starting values are from the corresponding Boost functions (in double precision).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", wald(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wald.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Wald distribution:

    .. math:: C_X(t) = \exp \left[  \frac{\lambda}{\mu} \left( 1 - \sqrt{1 - \frac{2 \mu^2 it}{\lambda}} \right)  \right] .



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", wald(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wald.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Wald distribution:

    .. math:: M_X(t) = \exp \left[  \frac{\lambda}{\mu} \left( 1 - \sqrt{1 - \frac{2 \mu^2 t}{\lambda}} \right)  \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", wald(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_wald.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, 
    of a random variable `X`, following a Wald distribution:

    .. math:: K_X(t) = \frac{\lambda}{\mu} \left( 1 - \sqrt{1 - \frac{2 \mu^2 t}{\lambda}} \right).

    .. math:: K_X^{(j)}(t) = tbd .


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", wald(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_wald.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a Wald distribution. The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wald(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_wald.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Wald distribution. 

    .. math:: \kappa_X(n+1) =\kappa_{X, n+1} = \frac{(2n)!}{2^n n! \mu^{2n+1} \lambda^n}

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", wald(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








