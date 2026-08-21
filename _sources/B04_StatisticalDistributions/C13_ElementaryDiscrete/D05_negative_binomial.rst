

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_negative_binomial: 

Boost: Negative binomial distribution 
===============================================================================


The following functions return the pmf, cdf, qtf or boost class of the negative binomial distribution with target for number of successful trials `r > 0` and success probability `0 \le p \le 1`, and `0 \le q \le 1`.


See also   Wikipedia :cite:p:`WikipediaDis34`, MathWorld :cite:p:`WolframDis34`,  BoostMath :cite:p:`BoostDis34`, :cite:t:`Ehrhardt2018` (3.9.23).




|cr|

.. _Ctx_NegbinomPmf:

.. method:: Ctx.negbinomial_pmf(k, r, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pmf}(x)`, the value of the probability mass function (:ref:`Pmf <Dist_Pmf>`) of the negative binomial distribution:

    .. math:: \text{pmf}(x) = \frac{\Gamma(k+r)}{k! \Gamma(r)} p^r (1-p)^k.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("NegbinomPdf(x, a, b): ", NegbinomPdf(x, a, b))
        >>> print ("dist_negbinomial(a, b).pdf(x): ", dist_negbinomial(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_NegbinomCdf:

.. method:: Ctx.negbinomial_cdf(k, r, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the negative binomial distribution:

    .. math:: \text{cdf}(x) = \sum_{j=0}^{k} \text{pmf}_X(j) = \text{ibeta}(r, k+1, p).

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function (:ref:`RealIBeta <rst_mpm_ibeta>`).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("NegbinomCdf(x, a, b): ", NegbinomCdf(x, a, b))
        >>> print ("dist_negbinomial(a, b).cdf(x): ", dist_negbinomial(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_NegbinomQtf:

.. method:: Ctx.negbinomial_qtf(q, r, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the negative binomial distribution:

    .. math:: \text{qtf}(q) = \mathrm{ibeta\_invb}(r, p, q) - 1.

    Here `\mathrm{ibeta\_invb}(\cdot)` denotes the inverse (on parameter b) of the real normalised incomplete beta function (:ref:`RealIBetaInvb <rst_mpm_real_ibeta_invb>`).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("NegbinomQtf(q, a, b): ", NegbinomQtf(q, a, b))
        >>> print ("dist_negbinomial(a, b).qtf(q): ", dist_negbinomial(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_negbinom(r, p)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The negative binomial distribution is a discrete (lattice) probability distribution with target for number of successful trials `r > 0` and success probability `0 \le p \le 1`.
    See also  Wikipedia :cite:p:`WikipediaDis34`, MathWorld :cite:p:`WolframDis34`, BoostMath :cite:p:`BoostDis34` , and :cite:t:`CharfunDis34`, R (Statistical System) :cite:p:`RDis34`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nbdtr.html#scipy.special.nbdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nbdtrc.html#scipy.special.nbdtrc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nbdtri.html#scipy.special.nbdtri

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nbdtrik.html#scipy.special.nbdtrik

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nbdtrin.html#scipy.special.nbdtrin




|cr|

.. method:: dist_negbinom.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an negative binomial distribution:

    .. math:: \text{pmf}_X(x) = \frac{\Gamma(n+k)}{K! \Gamma(n)} P^n (1-P)^k.

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively, of the central beta distribution. The following recursions are used for the PMF:

    .. math:: \text{Pr}(X=k+1 |n) = \frac{(n+k) (1-P)}{(k+1) } \text{Pr}(X=k |n)

    .. math:: \text{Pr}(X=k-1 |n) = \frac{k}{(n-k+1)(1-P)} \text{Pr}(X=k |n)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", negative_binomial(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_negbinom.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an negative binomial distribution:

    .. math:: \text{cdf}_X(x) = \sum_{j=0}^{k} \text{pmf}_X(j) = F_{\text{Beta}}(1-p; r,k+1).

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively, of the central beta distribution.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", negative_binomial(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_negbinom.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an negative binomial distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", negative_binomial(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_negbinom.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an negative binomial distribution:

    .. math:: \text{qtf}_X(q) =  a-b \: \text{ln}\left((1-y)/y\right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", negative_binomial(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_negbinom.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an negative binomial distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", negative_binomial(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_negbinom.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following an negative binomial distribution:

    .. math::  G_X(t) = \left(\frac{1}{P} - \frac{1-P}{P} t \right)^{-n}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", negative_binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_negbinom.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an negative binomial distribution:

    .. math::  C_X(t) = \left(\frac{1}{P} - \frac{1-P}{P} e^{it} \right)^{-n}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", negative_binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_negbinom.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an negative binomial distribution:

    .. math:: M_X(t) =  \left(\frac{1}{P} - \frac{1-P}{P} e^{t} \right)^{-n}.

    .. math:: L_X(t) = \left(\frac{1}{P} - \frac{1-P}{P} e^{t} \right)^{-n}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", negative_binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_negbinom.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an negative binomial distribution:

    .. math:: K_X(t) = -n \log \left(\frac{1}{P} - \frac{1-P}{P} e^t \right).


    `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a negative binomial distribution, are defined as

    .. math:: K_X(t) = r \log \left(\frac{1-p}{1-p \cdot e^t} \right), \quad \text{for } t < -\log(p)


    .. math::  K_X^{(1)}(t) = \frac{p \cdot r \cdot e^x}{1-p \cdot e^x},

    .. math::  K_X^{(2)}(t) = \frac{p \cdot r \cdot e^x}{(1-p \cdot e^x)^2},

    .. math::  K_X^{(3)}(t) = \frac{p \cdot r \cdot e^x (p \cdot e^x +1)}{(1-p \cdot e^x)^3},


    and for `j \ge 4` the derivatives are calculated by numerically differentiating `K_X^{(3)}(t)`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", negative_binomial(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_negbinom.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an negative binomial distribution (Wikipedia). The raw moments are calculated from the central moments.

    .. math::  \mu^{}_X(r) = \mu_2 \sum_{i=0}^{r-2} \binom{r-1}{i} \mu_i - \frac{1-P}{P} \sum_{i=0}^{r-2}  \binom{r-1}{i} \mu_{i+1},  \quad  r>2; \quad \mu_1 = n \frac{1-P}{P},  \quad  \mu_2 = \frac{\mu_1}{P}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", negative_binomial(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_negbinom.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an negative binomial distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", negative_binomial(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







**Approximations**



.. method:: ctx.negbinom_ecf(k, r, p, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf



.. method:: ctx.negbinom_ecf_inv(q, r, p, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.



.. method:: ctx.negbinom_spa(k, r, p, results='c')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.


    The saddlepoint is given by:

    .. math:: \hat{s}(x)= \log \left( \frac{k (1-P)}{(n-k) P} \right).





.. method:: ctx.negbinom_spa_inv(q, r, p, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.





