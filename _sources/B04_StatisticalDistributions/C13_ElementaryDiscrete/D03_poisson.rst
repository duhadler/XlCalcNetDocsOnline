

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|


.. _rst_dist_poisson: 

Boost: Poisson distribution 
===============================================================================


The following functions return the pmf, cdf, qtf or boost class of the Poisson distribution with mean `mu` and the support interval `(0,+\infty)`, and `0 \le q \le 1`.


See also   Wikipedia :cite:p:`WikipediaDis32`, MathWorld :cite:p:`WolframDis32`,  BoostMath :cite:p:`BoostDis32`, :cite:t:`Ehrhardt2018` (3.9.26).




|cr|

.. _Ctx_PoissonPmf:

.. method:: Ctx.poisson_pmf(k, mu)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pmf}(x)`, the value of the probability mass function (:ref:`Pmf <Dist_Pmf>`) of the Poisson distribution:

    .. math:: \text{pmf}(x) = \frac{\mu^k}{k!} e^{-\mu}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("PoissonPdf(x, a, b): ", PoissonPdf(x, a, b))
        >>> print ("dist_poisson(a, b).pdf(x): ", dist_poisson(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_PoissonCdf:

.. method:: Ctx.poisson_cdf(k, mu)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Poisson distribution:

    .. math:: \text{cdf}(x) = e^{-\mu} \sum_{i=0}^k \frac{\mu^i}{i!} = Q(1+k,\mu).

    Here `Q(\cdot)` denotes the upper regularized incomplete gamma function (:ref:`RealGammaQ <rst_mpm_gamma_q>`).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("PoissonCdf(x, a, b): ", PoissonCdf(x, a, b))
        >>> print ("dist_poisson(a, b).cdf(x): ", dist_poisson(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_PoissonQtf:

.. method:: Ctx.poisson_qtf(q, mu)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Poisson distribution:

    .. math:: \text{qtf}(q) = \mathrm{gammaq\_inva}(\mu, p) - 1.

    Here `\mathrm{gammaq\_inva}(\cdot)` denotes the inverse (on parameter `a`) of the real upper normalised incomplete gamma function (:ref:`RealGammaQInva <rst_mpm_real_gamma_q_inva>`).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("PoissonQtf(q, a, b): ", PoissonQtf(q, a, b))
        >>> print ("dist_poisson(a, b).qtf(q): ", dist_poisson(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_poisson(lambda1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Poisson distribution is a discrete (lattice) probability distribution  with mean `mu` and the support interval `(0,+\infty)`.
    See also  Wikipedia :cite:p:`WikipediaDis32`, MathWorld :cite:p:`WolframDis32`, BoostMath :cite:p:`BoostDis32`, and :cite:t:`CharfunDis32`, R (Statistical System) :cite:p:`RDis32`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.pdtr.html#scipy.special.pdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.pdtrc.html#scipy.special.pdtrc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.pdtri.html#scipy.special.pdtri

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.pdtrik.html#scipy.special.pdtrik




|cr|

.. method:: dist_poisson.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Poisson distribution:

    .. math:: \text{pmf}_X(x) = \frac{\lambda_1^k}{k!} e^{-\lambda_1}.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", poisson(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_poisson.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Poisson distribution:


    .. math:: \text{cdf}_X(x) = e^{-\lambda_1} \sum_{i=0}^k \frac{\lambda_1^i}{i!} = Q(1+k,\lambda_1).


    Here `Q(\cdot)` denotes the upper regularized incomplete gamma functions.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", poisson(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_poisson.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Poisson distribution:


    .. math:: \text{sf}_X(x)  = 1 - e^{-\lambda_1} \sum_{i=0}^k \frac{\lambda_1^i}{i!} = P(1+k,\lambda_1).


    Here `P(\cdot)` denotes the lower regularized incomplete gamma functions.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", poisson(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_poisson.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Poisson distribution. 

    .. math:: \text{qtf}_X(q) = \mathrm{gamma_q\_inva}(\lambda_1, p) - 1.

    Here `\mathrm{gamma_q\_inva}(\cdot)` denotes the inverse (on parameter `a`) of the real normalised incomplete gamma function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", poisson(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_poisson.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Poisson distribution:


    .. math:: \text{isf}_X(q) = \mathrm{gamma_p\_inva}(\lambda_1, q) - 1.


    Here `\mathrm{gamma_p\_inva}(\cdot)` denotes the inverse (on parameter `a`) of the real normalised complementary incomplete gamma function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", poisson(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_poisson.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following a Poisson distribution:

    .. math::  G_X(t) = \exp( \lambda(t -1)).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", poisson(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_poisson.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Poisson distribution:

    .. math::  C_X(t) = \exp( \lambda(e^{it} -1)).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", poisson(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_poisson.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Poisson distribution:

    .. math:: M_X(t) =  \exp( \lambda(e^{t} -1)).

    .. math::  L_X(t) = \exp( \lambda(e^{-t} -1)).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", poisson(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_poisson.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following a Poisson distribution:

    .. math:: K_X(t) = \lambda(e^t -1).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", poisson(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_poisson.moments(k)

    Returns the first `j` moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Poisson distribution (Wikipedia). The moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", poisson(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_poisson.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Poisson distribution:

    .. math::  \kappa_r = \lambda, \quad  r = 1, 2, ...


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", poisson(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







**Approximations**


.. method:: ctx.poisson_ecf(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.



.. method:: ctx.poisson_ecf_inv(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.





.. method:: ctx.poisson_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.



    The solution `\hat{s}(x)` of the saddlepoint equation `K_X^{(1)}(\hat{s}(x))=x`, of a random variable `X`, following a Poisson distribution is given by:

    .. math:: \hat{s}(x)= \log ( k / \lambda).



.. method:: ctx.poisson_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.




