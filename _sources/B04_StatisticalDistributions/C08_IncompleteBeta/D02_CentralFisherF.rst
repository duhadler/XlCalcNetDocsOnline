

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_fisher_f: 

Boost: Central Fisher F distribution 
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the Fisher F distribution with `m > 0` and  `n > 0` degrees of freedom, and the support interval `(0, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis09`, MathWorld :cite:p:`WolframDis09`, BoostMath :cite:p:`BoostDis09`, :cite:t:`Ehrhardt2018` (3.9.9).




|cr|

.. _Ctx_FisherFPdf:

.. method:: Ctx.fisher_f_pdf(x, m, n)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Fisher F distribution:

    .. math:: \text{pdf}(x) = \frac{m^{m/2} n^{n/2}}{B(m/2,n/2)} x^{(m-2)/2} (n+mx)^{-(m+n)/2}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("FisherFPdf(x, a, b): ", FisherFPdf(x, a, b))
        >>> print ("dist_fisher_f(a, b).pdf(x): ", dist_fisher_f(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_FisherFCdf:

.. method:: Ctx.fisher_f_cdf(x, m, n)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Fisher F distribution:

    .. math:: 
        \text{cdf}(x) =\begin{cases}
        \text{ibetac}(n/2, m/2, n/(n+mx)), & mx > n,\\
        \text{ibeta}(m/2, n/2, mx/(n+mx)) & mx \le n.
        \end{cases}

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function (:ref:`RealIBeta <rst_mpm_ibeta>`), and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function (:ref:`RealIBetac <rst_mpm_ibetac>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("FisherFCdf(x, a, b): ", FisherFCdf(x, a, b))
        >>> print ("dist_fisher_f(a, b).cdf(x): ", dist_fisher_f(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_FisherFQtf:

.. method:: Ctx.fisher_f_qtf(q, m, n)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Fisher F distribution:

    .. math:: \text{qtf}(q) = \frac{nx}{m(1-x)}, \quad \text{where } x = \mathrm{ibeta\_inv}(m/2, n/2, q).

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function (:ref:`RealIBetaInv <rst_mpm_real_ibeta_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("FisherFQtf(q, a, b): ", FisherFQtf(q, a, b))
        >>> print ("dist_fisher_f(a, b).qtf(q): ", dist_fisher_f(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_fisher_f(m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Fisher `F`-distribution is a continuous probability distribution with `m > 0` and  `n > 0` degrees of freedom, and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis09`, MathWorld :cite:p:`WolframDis09`, BoostMath :cite:p:`BoostDis09`, :cite:t:`CharfunDis09`, R (Statistical System) :cite:p:`RDis09`, :cite:t:`AbramowitzDis09`, :cite:t:`Butler2002`, :cite:t:`Chattamvelli1995`, :cite:t:`Witkovsky2001`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.fdtr.html#scipy.special.fdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.fdtrc.html#scipy.special.fdtrc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.fdtri.html#scipy.special.fdtri

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.fdtridfd.html#scipy.special.fdtridfd



|cr|

.. method:: dist_fisher_f.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a central Fisher F distribution:

    .. math:: \text{pdf}_X(x) = \frac{m^{m/2} n^{n/2}}{B(m/2,n/2)} x^{(m-2)/2} (n+mx)^{-(m+n)/2},



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_fisher_f.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a central Fisher F distribution:


    .. math:: 
        \text{cdf}_X(x) =\begin{cases}
        \text{ibetac}(n/2, m/2, n/(n+mx)), & mx > n,\\
        \text{ibeta}(m/2, n/2, mx/(n+mx)) & mx \le n.
        \end{cases}

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_fisher_f.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a central Fisher F distribution:


    .. math:: 
        \text{sf}_X(x) =\begin{cases}
        \text{ibeta}(n/2, m/2, n/(n+mx)), & mx > n,\\
        \text{ibetac}(m/2, n/2, mx/(n+mx)) & mx \le n.
        \end{cases}


    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_fisher_f.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a central Fisher F distribution:

    .. math:: \text{qtf}_X(q) = \frac{nx}{m(1-x)}, \quad \text{where } x = \mathrm{ibeta\_inv}(m/2, n/2, q).

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a central Fisher F distribution:

    .. math:: \text{isf}_X(q) = \frac{nx}{m(1-x)}, \quad \text{where } x = \mathrm{ibetac\_inv}(m/2, n/2, q).

    Here `\mathrm{ibetac\_inv}(\cdot)` denotes the inverse of the real normalised complementary incomplete beta function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a central Fisher F distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x = \frac{\Gamma(m/2+n/2)}{\Gamma(n/2)}  U \left( \frac{m}{2}, 1-\frac{n}{2}, -\frac{n}{m} it \right)

    where `U(\cdot)` denotes the confluent hypergeometric function of the second kind.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_fisher_f.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_fisher_f.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a central Fisher F distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = \mu'_{F}(r)= \frac{\Gamma( \tfrac{1}{2}n_1+r)-\Gamma( \tfrac{1}{2}n_2-r)}{\Gamma( \tfrac{1}{2}n_2)}, \quad \text{for } n_2 > 2r.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_fisher_f.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a central Fisher F distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




**Additional methods: Recurrence relations**

Let the density `g_{m,n}` be that of `m/n` times an `F_{m,n}` random variable. 
Let `G_{m,n}(y)` be its distribution function.

Then the following recurrence relations hold (see Chattamvelli, 1995)




.. method:: dist_fisher_f.recurrence_pdf(x, lambda, start_n1, start_n2, target_n1, target_n2)

    Applies a recurrence relation to calculate the cdf for different degrees of freedom for a given value of *x*. This is mostly useful when using asymptotic methods.


    .. math:: n\left[G_{m,n+2}(y)-G_{m-2,n+2}(y)\right] =  -2g_{m,n}(y)

    .. math:: m(1+y)]g_{m+2,n}(y) + y(m+n)g_{m,n}(y).

    .. math:: n(1+y) g_{m,n+2}(y) = (m+n)g_{m,n}(y).

    .. math:: m g_{m+2,n-2}(y) = (n-2) y  g_{m,n}(y).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", fisher_f(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_fisher_f.recurrence_cdf(x, lambda, start_n1, start_n2, target_n1, target_n2)

    Applies a recurrence relation to calculate the cdf for different degrees of freedom for a given value of *x*. This is mostly useful when using asymptotic methods.

    From these equations  we obtain

    .. math::
        :nowrap:

        \begin{eqnarray}
            [(m+2)(1+y)]G_{m+4,n}(y) & = & [(m+2)(1+y)+y(m+n]G_{m+2,n}(y)  \\
            & - & y(m+n)G_{m,n}(y)  \nonumber
        \end{eqnarray}

    .. math:: n(1+y) :cite:t:`G_{m,n+2}(y)-G_{m+2,n+2}(y)]   =  (m+n) :cite:t:`G_{m,n}(y) - G_{m+2,n}(y)]

    .. math:: (m+2) :cite:t:`G_{m+2,n}(y)-G_{m+4,n-2}(y)]   =  (n-2) :cite:t:`G_{m,n}(y) - G_{m+2,n}(y)]


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", fisher_f(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






