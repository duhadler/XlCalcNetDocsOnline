

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_binomial: 

Boost: Binomial distribution 
===============================================================================


The following functions return the pmf, cdf, qtf or boost class of the binomial distribution with number of trials `n \ge 0` and success probability `0 \le p \le 1`, and `0 \le q \le 1`.


See also   Wikipedia :cite:p:`WikipediaDis33`, MathWorld :cite:p:`WolframDis33`,  BoostMath :cite:p:`BoostDis33`, :cite:t:`Ehrhardt2018` (3.9.3).




|cr|

.. _Ctx_BinomialPmf:

.. method:: Ctx.binomial_pmf(k, n, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pmf}(x)`, the value of the probability density function (:ref:`Pmf <Dist_Pmf>`) of the binomial distribution:

    .. math:: \text{pmf}(x) = \binom{n}{k} p^k (1-p)^{n-k} = f_{\text{Beta}}(k+1,n-k+1,p)/(n+1).

    Here `f_{\text{Beta}}(\cdot)` denotes the PDF of the central beta distribution. 


    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BinomialPdf(x, a, b): ", BinomialPdf(x, a, b))
        >>> print ("dist_binomial(a, b).pdf(x): ", dist_binomial(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BinomialCdf:

.. method:: Ctx.binomial_cdf(k, n, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the binomial distribution:

    .. math:: \text{cdf}(x) = \sum_{j=0}^{k} \text{pmf}_X(j) = \text{ibetac}(k+1, n-k, p).

    Here `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function (:ref:`RealIBetac <rst_mpm_ibetac>`).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BinomialCdf(x, a, b): ", BinomialCdf(x, a, b))
        >>> print ("dist_binomial(a, b).cdf(x): ", dist_binomial(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BinomialQtf:

.. method:: Ctx.binomial_qtf(q, n, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the binomial distribution:


    There is no known closed form for `\text{qtf}(q)`: it is computed with Newton iterations where the starting values are from the corresponding Boost functions.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("BinomialQtf(q, a, b): ", BinomialQtf(q, a, b))
        >>> print ("dist_binomial(a, b).qtf(q): ", dist_binomial(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_binomial(n, p)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The binomial distribution is a discrete (lattice) probability distribution  with number of trials `n \ge 0` and success probability `0 \le p \le 1`.
    See also  Wikipedia :cite:p:`WikipediaDis33`, MathWorld :cite:p:`WolframDis33`, BoostMath :cite:p:`BoostDis33`, :cite:t:`CharfunDis33`, R (Statistical System) :cite:p:`RDis33`.

    A special case is the Bernoulli distribution, see  See also  Wikipedia :cite:p:`WikipediaDis30`, MathWorld :cite:p:`WolframDis30`, and BoostMath :cite:p:`BoostDis30`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.bdtr.html#scipy.special.bdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.bdtrc.html#scipy.special.bdtrc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.bdtri.html#scipy.special.bdtri

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.bdtrik.html#scipy.special.bdtrik

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.bdtrin.html#scipy.special.bdtrin





|cr|

.. method:: dist_binomial.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an binomial distribution:

    .. math:: \text{pmf}_X(x) = \binom{n}{k} p^k (1-p)^{n-k} = f_{\text{Beta}}(k+1,n-k+1,p)/(n+1).

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively, of the central beta distribution. 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", binomial(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_binomial.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an binomial distribution:

    .. math:: \text{cdf}_X(x) = \sum_{j=0}^{k} \text{pmf}_X(j) = F_{\text{Beta}}(1-p; n-k, k+1).

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively, of the central beta distribution.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", binomial(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_binomial.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an binomial distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", binomial(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_binomial.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an binomial distribution. There is no closed form for the qtf: It is computed with Newton iterations where the starting values are from Boost.

    .. math:: \text{qtf}_X(q) =  tbd.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", binomial(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_binomial.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an binomial distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", binomial(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_binomial.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following an binomial distribution:

    .. math::  G_X(t) = \left(P t + Q\right)^n.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_binomial.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an binomial distribution:

    .. math::  C_X(t) = \left(P e^{it} + Q\right)^n.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_binomial.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an binomial distribution:

    .. math:: M_X(t) = \left(P e^{t} + Q\right)^n.

    .. math:: L_X(t) =  \left(P e^{-t} + Q\right)^n.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", binomial(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_binomial.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an binomial distribution:

    .. math:: K_X(t) = K_X(t) = n \log \left(P e^t + Q\right).


    `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a binomial distribution, are defined as

    .. math::  K_X(t) = n \log \left(p \cdot e^t + 1-p\right),

    .. math::  K_X^{(1)}(t) = \frac{n \cdot p  \cdot e^x}{p(e^x-1)+1},

    .. math::  K_X^{(2)}(t) = -\frac{n (p-1) p \cdot e^x}{(p(e^x-1)+1)^2},

    .. math::  K_X^{(3)}(t) = \frac{n (p-1) p \cdot e^x ( p \cdot e^x +p-1)}{(p(e^x-1)+1)^3},


    and for `j \ge 4` the derivatives are calculated by numerically differentiating `K_X^{(3)}(t)`.




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", binomial(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_binomial.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following an binomial distribution (Wikipedia). The raw moments are calculated from the central moments.

    .. math::  \mu^{}_X(r) = n P Q \sum_{i=0}^{r-2} \binom{r-1}{i} \mu_i - P \sum_{i=0}^{r-2}  \binom{r-1}{i} \mu_{i+1},  \quad  r>2; \quad \mu_1 = nP,  \quad  \mu_2 = nPQ.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", binomial(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_binomial.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an binomial distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", binomial(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





**Approximations**


.. method:: ctx.hypergeo_ft(x, n, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function (see  :ref:`pmf_from_cf_lattice() <rst_pmf_from_cf_lattice>` and  :ref:`cdf_from_cf_lattice() <rst_cdf_from_cf_lattice>`).




.. method:: ctx.binomial_ft(x, n, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function (see  :ref:`pmf_from_cf_lattice() <rst_pmf_from_cf_lattice>` and  :ref:`cdf_from_cf_lattice() <rst_cdf_from_cf_lattice>`).


.. method:: ctx.binomial_ecf(k, n, p, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf, support `k \in \{0, \cdots n\}`.



.. method:: ctx.binomial_ecf_inv(q, n, p, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.




.. method:: ctx.binomial_spa(k, n, p, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.

    The saddlepoint is given by

    .. math:: \hat{s}(x)= \log \left( \frac{k Q}{(n-k) P} \right).



.. method:: ctx.binomial_spa_inv(q, n, p, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.


