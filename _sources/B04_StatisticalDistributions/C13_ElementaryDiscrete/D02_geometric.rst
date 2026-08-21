

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




   |newpage|

.. _rst_dist_geometric: 

Boost: Geometric distribution 
===============================================================================


The following functions return the pmf, cdf, qtf or boost class of the geometric distribution with parameter `p, 0 \le p \le 1` (`p` is the probability that any one trial will be successful, it is also known as "success fraction"). The function returns the probability of obtaining exactly `k` failures from `k` trials with success fraction `p`. For this implementation, the set of trials includes zero (unlike another definition where the set of trials starts at one, sometimes named shifted), so the support interval for `k` is `(0, \infty)`, and `0 \le q \le 1`.


See also   Wikipedia :cite:p:`WikipediaDis31`, MathWorld :cite:p:`WolframDis31`,  BoostMath :cite:p:`BoostDis31` .



|cr|

.. _Ctx_GeometricPmf:

.. method:: Ctx.geometric_pmf(k, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pmf}(x)`, the value of the probability mass function (:ref:`Pmf <Dist_Pmf>`) of the geometric distribution:

    .. math:: \text{pmf}_X(k) = p (1-p)^k = p \cdot \exp\left(k \text{log1p}(-p)\right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("GeometricPdf(x, a, b): ", GeometricPdf(x, a, b))
        >>> print ("dist_geometric(a, b).pdf(x): ", dist_geometric(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_GeometricCdf:

.. method:: Ctx.geometric_cdf(k, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the geometric distribution. The cumulative distribution function returns the probability of obtaining `k` failures or fewer from `k` trials with success fraction `p` and success on the last trial.

    .. math:: \text{cdf}(x) = 1 - (1-p)^{k+1} = -\text{expm1}\left(\text{log1p}(-p) (k+1)\right).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("GeometricCdf(x, a, b): ", GeometricCdf(x, a, b))
        >>> print ("dist_geometric(a, b).cdf(x): ", dist_geometric(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_GeometricQtf:

.. method:: Ctx.geometric_qtf(q, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the geometric distribution. The quantile function returns the greatest number of failures `k` expected to be observed from `k` trials with success fraction `p`, at probability `q`. Note that the value returned is a real-number, and not an integer. Depending on the use case you may want to take either the floor or ceiling of the real result.

    .. math:: \text{qtf}(q) = \frac{\text{log1p}(-q)}{\text{log1p}(-p)} -1.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("GeometricQtf(q, a, b): ", GeometricQtf(q, a, b))
        >>> print ("dist_geometric(a, b).qtf(q): ", dist_geometric(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_geometric(p)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The geometric distribution is a (discrete or continuous) probability distribution with parameter `p, 0 \le p \le 1` (`p` is the probability that any one trial will be successful, it is also known as "success fraction"). The function returns the probability of obtaining exactly `k` failures from `k` trials with success fraction `p`. For this implementation, the set of trials includes zero (unlike another definition where the set of trials starts at one, sometimes named shifted), so the support interval for `k` is `(0, \infty)`. 
    See also  Wikipedia :cite:p:`WikipediaDis31`, MathWorld :cite:p:`WolframDis31`, BoostMath :cite:p:`BoostDis31` , and :cite:t:`CharfunDis31`, R (Statistical System) :cite:p:`RDis31`.




|cr|

.. method:: dist_geometric.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an geometric distribution:

    .. math:: \text{pmf}_X(k) = p (1-p)^k = p \cdot \exp\left(k \text{log1p}(-p)\right)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", geometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_geometric.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an geometric distribution:

    .. math:: \text{cdf}_X(x) = 1 - (1-p)^{k+1} = -\text{expm1}\left(\text{log1p}(-p) (k+1)\right)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", geometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_geometric.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an geometric distribution:

    .. math:: \text{sf}_X(x) = (1-p)^{k+1} =  \exp\left(\text{log1p}(-p) (k+1)\right)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", geometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_geometric.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an geometric distribution:

    .. math:: \text{qtf}_X(q) = \frac{\text{log1p}(-q)}{\text{log1p}(-p)} -1



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", geometric(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_geometric.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an geometric distribution:

    .. math:: \text{isf}_X(q) = \frac{\log(q)}{\text{log1p}(-p)} -1


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", geometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_geometric.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an geometric distribution:

    .. math::  C_X(t) = ??.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", geometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_geometric.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an geometric distribution:

    .. math:: M_X(t) =  ??.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", geometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_geometric.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an geometric distribution:

    .. math:: K_X(t) = ??.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", geometric(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_geometric.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an geometric distribution (Wikipedia). The raw moments are calculated from the central moments.

    .. math::  \mu_{X}(n) = ??


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", geometric(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_geometric.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an geometric distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", geometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00










The geometric distribution is used when there are exactly two mutually exclusive outcomes of a Bernoulli trial: these outcomes are labelled "success" and "failure". For Bernoulli trials each with success fraction `p`, the geometric distribution gives the probability of observing `k` trials (failures, events, occurrences, or arrivals) before the first success.

The pmf of a variable following a geometric distribution with parameter `p` is given by

.. math::  f(k;p)= p (1-p)^k 

The CDF of a variable following a geometric distribution with parameter `p` is given by

.. math::  F(k;p)= 1- (1-p)^{k+1} 

The ICDF of a variable following a geometric distribution with parameter `p` is given by

.. math::  F^{-1}(x;p)= \frac{\text{log1p}(-x)}{\text{log1p}(-p)} -1






