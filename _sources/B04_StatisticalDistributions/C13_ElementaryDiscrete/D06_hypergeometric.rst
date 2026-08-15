

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_hypergeometric: 

Boost: Classical hypergeometric distribution 
===============================================================================


The following functions return pmf, cdf, qtf or boost class of the hypergeometric distribution, with `k` successes (random draws for which the object drawn has a specified feature) in `n \in \{0, 1 ,2, \ldots, N \}` draws, without replacement, from a finite population of size `N \in \{0, 1 ,2, \ldots \}`` that contains exactly `K \in \{0, 1 ,2, \ldots, N \}` objects with that feature, wherein each draw is either a success or a failure, and the support interval `(\max(0,n+K-N), \min(K,n))`, and `0 \le q \le 1`.


See also   Wikipedia :cite:p:`WikipediaDis35`, MathWorld :cite:p:`WolframDis35`,  BoostMath :cite:p:`BoostDis35`, :cite:t:`RDis35`, :cite:t:`Berkopec2007`, :cite:t:`Johnson2005` page 251,  :cite:t:`Ehrhardt2018` (3.9.11).





|cr|

.. _Ctx_HypergeoPmf:

.. method:: Ctx.hypergeometric_pmf(k, n, K, N)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pmf}(k)`, the value of the probability mass function (:ref:`Pmf <Dist_Pmf>`) of the hypergeometric distribution. 

    .. math:: \text{pmf}_X(k) = \frac{\displaystyle\binom{K}{k} \binom{N-K}{n-k}}{\displaystyle\binom{N}{n}}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("HypergeoPdf(x, a, b): ", HypergeoPdf(x, a, b))
        >>> print ("dist_hypergeometric(a, b).pdf(x): ", dist_hypergeometric(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_HypergeoCdf:

.. method:: Ctx.hypergeometric_cdf(k, n, K, N)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the hypergeometric distribution:

    .. math:: \text{cdf}_X(k) = \sum_{j=\max(0,n+K-N)}^{k} \text{pmf}_X(j).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("HypergeoCdf(x, a, b): ", HypergeoCdf(x, a, b))
        >>> print ("dist_hypergeometric(a, b).cdf(x): ", dist_hypergeometric(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_HypergeoQtf:

.. method:: Ctx.hypergeometric_qtf(q, n, K, N)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the hypergeometric distribution:

    There is no known closed exact form for `\text{qtf}(q)` or `\text{isf}(q)`.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("HypergeoQtf(q, a, b): ", HypergeoQtf(q, a, b))
        >>> print ("dist_hypergeometric(a, b).qtf(q): ", dist_hypergeometric(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_hypergeometric(n, K, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The hypergeometric distribution is a discrete (lattice) probability distribution  with `k` successes (random draws for which the object drawn has a specified feature) in `n \in \{0, 1 ,2, \ldots, N \}` draws, without replacement, from a finite population of size `N \in \{0, 1 ,2, \ldots \}`` that contains exactly `K \in \{0, 1 ,2, \ldots, N \}` objects with that feature, wherein each draw is either a success or a failure, and the support interval `(\max(0,n+K-N), \min(K,n))`.
    See also  Wikipedia :cite:p:`WikipediaDis35`, MathWorld :cite:p:`WolframDis35`, BoostMath :cite:p:`BoostDis35`, R (Statistical System) :cite:p:`RDis35`, :cite:t:`Berkopec2007`, :cite:t:`Johnson2005` page 251.




|cr|

.. method:: dist_hypergeometric.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an hypergeometric distribution:


    .. math:: \text{pmf}_X(x) =   \binom{K}{k}  \binom{N-K}{n-k}  \bigg/  \binom{N}{n} .



    The following recursions are used for the PMF:

    .. math:: f(k+1)= \frac{(n_1 - k)(n-k)}{(k+1)(n_2 - n+k+1} f(k)

    .. math:: f(k-1)= \frac{k(n_2 - n + k)}{(n_1 - k+1)(n-k+1} f(k)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|


.. method:: dist_hypergeometric.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an hypergeometric distribution:

    .. math:: \text{cdf}_X(k) = \sum_{j=\max(0,n+K-N)}^{k} \text{pmf}_X(j) = 1 - \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_hypergeometric.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an hypergeometric distribution:

    .. math:: \text{sf}_X(k) = \sum_{j=k+1}^{\min(K,n)} \text{pmf}_X(j) = \text{pmf}_X(k+1) \times {}_3F_2(1,k+1-K,k+1-n;k+2,N+k+2-K-n;1),

    where `{}_3F_2(\cdot)` is a generalized hypergeometric function (see  :ref:`hyp3f2() <rst_mpm_hyp3f2>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hypergeometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_hypergeometric.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an hypergeometric distribution.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", hypergeometric(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeometric.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an hypergeometric distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hypergeometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeometric.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following an hypergeometric distribution:

    .. math::  G_X(t) = {}_2F_1(-n, -K; N-K-n+1; t) \binom{N-K}{n}  \bigg/  \binom{N}{n} .

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_hypergeometric.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an hypergeometric distribution:

    .. math::  C_X(t) = {}_2F_1(-n, -K; N-K-n+1; e^{it}) \binom{N-K}{n}  \bigg/  \binom{N}{n} .

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeometric.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an hypergeometric distribution:

    .. math:: M_X(t) =  {}_2F_1(-n, -K; N-K-n+1; e^t) \binom{N-K}{n}  \bigg/  \binom{N}{n}.

    .. math:: L_X(t) = {}_2F_1(-n, -K; N-K-n+1; e^{-t}) \binom{N-K}{n}  \bigg/  \binom{N}{n}.

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeometric.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an hypergeometric distribution:

    .. math:: K_X(t) = \log  \left[(  {}_2F_1(-n, -K; N-K-n+1; e^t) \binom{N-K}{n}  \bigg/  \binom{N}{n}  \right].

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a hypergeometric distribution, are defined as


    .. math::  K_X(t) = \log \left(T \cdot {}_2F_1(a, b; c; e^t)\right), \quad \text{where } a=-n, b=-K, c=N-K-n+1,  T = \binom{N-K}{n}  \bigg/  \binom{N}{n}.

    .. math::  K_X^{(1)}(t) = \frac{a \cdot b \cdot e^x \cdot G_1(x)}{c \cdot G_0(x)}, \quad \text{where } G_i(x)={}_2F_1(a+i, b+i; c+i; e^t),

    .. math::  K_X^{(2)}(t) = -\frac{a^2 \cdot b^2 \cdot e^{2x} \cdot (G_1(x))^2}{c^2 \cdot (G_0(x))^2} + \frac{a \cdot b \cdot e^x \cdot G_1(x)}{c \cdot G_0(x)} + \frac{a(a+1) \cdot b(b+1) \cdot e^{2x} \cdot G_2(x)}{c(c+1) \cdot G_0(x)}, 


    .. math::  K_X^{(3)}(t) = \frac{2 a^3 \cdot b^3 \cdot e^{3x} \cdot (G_1(x))^3}{c^3 \cdot (G_0(x))^3} - \frac{3 a^2 \cdot b^2 \cdot e^{2x} \cdot (G_1(x))^2}{c^2 \cdot (G_0(x))^2}  - \frac{3 a^2(a+1) \cdot b^2(b+1) \cdot e^{3x} \cdot G_2(x)\cdot G_1(x)}{c(c+1) \cdot G_0(x)}  \\
        + \frac{a \cdot b \cdot e^x \cdot G_1(x)}{c \cdot G_0(x)} + \frac{3 a(a+1) \cdot b(b+1) \cdot e^{2x} \cdot G_2(x)}{c(c+1) \cdot G_0(x)}   + \frac{a(a+1)(a+2) \cdot b(b+1)(b+2) \cdot e^{3x} \cdot G_3(x)}{c(c+1)(c+2) \cdot G_0(x)}


    and for `j \ge 4` the derivatives are calculated by numerically differentiating `K_X^{(3)}(t)`. We also have

    .. math::  \frac{\mathrm{d}}{\mathrm{d}z} \biggl({}_2F_1(a,b,c;z)\biggr) = \frac{ab}{c} \cdot {}_2F_1(a+1,b+1,c+1;z), \quad \text{and }

    .. math::  z(1-z) \cdot \frac{\mathrm{d}^2}{\mathrm{d}z^2} \biggl({}_2F_1(a,b,c;z)\biggr) + (c-(a+b+1)z) \cdot \frac{\mathrm{d}}{\mathrm{d}z} \biggl({}_2F_1(a,b,c;z)\biggr) - ab \cdot{}_2F_1(a,b,c;z) = 0.







    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", hypergeometric(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_hypergeometric.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an hypergeometric distribution (Wikipedia). 

    .. math::  \mu'^{}_X(r) = \sum_{j=1}^{j_{\text{max}}} S_{r,j} T_j, \quad \text{where } j_{\text{max}} = \text{min}(r, n, M, N), 

    .. math::  S_{r,1} = S_{r,r} = 1, \quad S_{r+1,j} = j S_{r,j} + S_{r,j-1},  \quad \text{and} 

    .. math::  T_1 = nM/N,  \quad  T_{j+1} = T_j (n-j) (M-j) / (N-j).



    .. math::  \mu'_{[r]} = \frac{n! K! (K+(N-K)-r)! }{(n-r)! (K-r)! (K+(N-K))!}  

    .. math::  \mu'_{[r]} = \frac{n! K! (N-r)! }{(n-r)! (K-r)! N!}  




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_hypergeometric.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an hypergeometric distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








**Approximations**


.. method:: ctx.hypergeo_ecf(k, n, K, N, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the  pdf, cdf and sf.



.. method:: ctx.hypergeo_ecf_inv(q, n, K, N, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.



.. method:: ctx.hypergeo_spa(k, n, K, N, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.



.. method:: ctx.hypergeo_spa_inv(q, n, K, N,  results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.





