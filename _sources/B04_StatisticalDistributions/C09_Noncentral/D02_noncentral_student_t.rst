

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_student_t_nc: 

Boost: Noncentral Student `t` distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the non-central Student t distribution with `n>0` degrees of freedom, noncentrality parameter `\delta`, and support interval `(-\infty, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis03`, MathWorld :cite:p:`WolframDis03`,  BoostMath :cite:p:`BoostDis03`, :cite:t:`Benton2003`, :cite:t:`Broda2007`, :cite:t:`Owen1968`, :cite:t:`Wang1993`, :cite:t:`Witkovsky2013`, :cite:t:`Kerns2018`.




|cr|

.. _Ctx_StudentTNcPdf:

.. method:: Ctx.student_t_nc_pdf(x, n, delta)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the non-central Student t distribution:


    .. math::  \text{pdf}(x) = f_{\text{StudentT}}\left(n,x, \delta\right) = \int_{0}^{\infty} \phi \left(x \sqrt{\frac{y}{n}} -\delta\right) f_{\chi^2}(y, n) \sqrt{\frac{y}{n}} \: \mathrm{d}y,
       :label: student_t_nc_pdf_witkovsky

    where `\phi(\cdot)` denotes the pdf of the standard normal distribution and `f_{\chi^2}(\cdot, n)` denotes the pdf of the `\chi^2` distribution with `n` degrees of freedom (see :ref:`chi_squared_pdf() <rst_mpm_chi_squared_pdf>`).

    Alternatively, the pdf can be written in a form which shows the relationship to the central distribution more clearly:

    .. math:: \text{pdf}(x) = f_{t'}(x; n, \delta) = \frac{n^m \Gamma(n+1) \exp(-\tfrac{1}{2}\delta^2)}{2^n a^m\Gamma(m)} \left[ \frac{\sqrt{2} \delta x \cdot {}_1F_1(m+1;\tfrac{3}{2};y^2)}{a \Gamma(m+\tfrac{1}{2})}  -   \frac{ {}_1F_1(m+\tfrac{1}{2}; \tfrac{1}{2};y^2)}{\sqrt{a} \Gamma(m+1)} \right], 
       :label: student_t_nc_pdf_hyper

    .. math::   m = \frac{n}{2},\quad a = n+x^2, \quad y^2 = \frac{\delta^2x^2}{2a},

    and `{}_1F_1(\cdot)` is the confluent hypergeometric function.



    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTNcPdf(x, a, b): ", StudentTNcPdf(x, a, b))
        >>> print ("dist_student_t_nc(a, b).pdf(x): ", dist_student_t_nc(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_StudentTNcCdf:

.. method:: Ctx.student_t_nc_cdf(x, n, delta)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the non-central Student t distribution:


    .. math:: \text{cdf}(x) =  F_{\text{StudentT}}\left(x, n, \delta\right) = \int_{0}^{\infty} \Phi \left(x \sqrt{\frac{y}{n}} -\delta\right) f_{\chi^2}(y, n) \: \mathrm{d}y,
       :label: student_t_nc_cdf_witkovsky


    for `x<0` by `F_{\text{StudentT}}\left(n,x, \delta\right) = 1-F_{\text{StudentT}}\left(n,-x, -\delta\right)`, and for `x=0` by `F_{\text{StudentT}}\left(n,x, \delta\right) = \Phi(-\delta)`.

    Here `\Phi(\cdot)` denotes the cdf of the standard normal distribution and `f_{\chi^2}(\cdot, n)` denotes the pdf of the `\chi^2` distribution with `n` degrees of freedom.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTNcCdf(x, a, b): ", StudentTNcCdf(x, a, b))
        >>> print ("dist_student_t_nc(a, b).cdf(x): ", dist_student_t_nc(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00




|cr|

.. _Ctx_StudentTNcQtf:

.. method:: Ctx.student_t_nc_qtf(q, n, delta)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the non-central Student t distribution:

    There is no known closed exact form for `\text{qtf}(q)`. For ``fpm.`` the default method is to call the function provided by Boost. 

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("StudentTNcQtf(q, a, b): ", StudentTNcQtf(q, a, b))
        >>> print ("dist_student_t_nc(a, b).qtf(q): ", dist_student_t_nc(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_student_t_nc(n, lambda1)

    The noncentral `t` distribution is a continuous probability distribution with degrees of freedom `n>0`, 
    noncentrality parameter `\delta`, and support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis03`, MathWorld :cite:p:`WolframDis03`, BoostMath :cite:p:`BoostDis03`, :cite:t:`Benton2003`, :cite:t:`Broda2007`, :cite:t:`Owen1968`, :cite:t:`Wang1993`, :cite:t:`Witkovsky2013`, :cite:t:`Kerns2018`, R (Statistical System) :cite:p:`RDis03`.


    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nctdtr.html#scipy.special.nctdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nctdtridf.html#scipy.special.nctdtridf

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nctdtrit.html#scipy.special.nctdtrit

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.nctdtrinc.html#scipy.special.nctdtrinc






    Ref: Kim (2007), CI noncentrality parameters

    Application: Scholz.

    Young, R package tolerance intervals






|cr|

.. method:: dist_student_t_nc.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a 
    non-central Student t distribution:

    .. math:: \text{pdf}_X(x) = f_{t'}(x; n, \delta) = \frac{n^m \Gamma(n+1) \exp(-\tfrac{1}{2}\delta^2)}{2^n a^m\Gamma(m)} \left[ \frac{\sqrt{2} \delta x \cdot {}_1F_1(m+1;\tfrac{3}{2};y^2)}{a \Gamma(m+\tfrac{1}{2})}  -   \frac{ {}_1F_1(m+\tfrac{1}{2}; \tfrac{1}{2};y^2)}{\sqrt{a} \Gamma(m+1)} \right], 

    .. math::   m = \frac{n}{2},\quad a = n+x^2, \quad y^2 = \frac{\delta^2x^2}{2a},

    and `{}_1F_1(\cdot)` is the confluent hypergeometric function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", student_t_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_student_t_nc.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a non-central Student t distribution:

    .. math:: \text{cdf}_X(x) = F_{t'}(x; n, \delta) =  \int_{0}^{x} f_t(x; n, \delta) \mathrm{d} t =  \Phi(-\delta) + \frac{1}{2} \sum_{i=0}^{\infty} P_i I_z\left(i+ \tfrac{1}{2} , m\right) + \frac{\delta}{\sqrt{2}} Q_i I_z\left(i+1, m\right),

    .. math::  \quad P_i =  \frac{e^{-\lambda} \lambda^i}{i!}, \quad Q_i = \frac{e^{-\lambda} \lambda^i}{\Gamma(i+3/2)};  \quad z=\frac{t^2}{n+t^2},

    and `I_x(\cdot,\cdot)` denotes the (normalized) incomplete beta function , and `\Phi(\cdot)` denotes the CDF of the normal distribution.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", student_t_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_student_t_nc.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a non-central Student t distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", student_t_nc(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_student_t_nc.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a non-central Student t distribution:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: 
    It is computed using Newton iterations with starting values from a normal approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", student_t_nc(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t_nc.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a non-central Student t distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", student_t_nc(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t_nc.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a non-central Student t distribution:

    .. math:: C_X(t) = \int_{-\infty}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", student_t_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t_nc.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_student_t_nc.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.





|cr|

.. method:: dist_student_t_nc.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a non-central Student t distribution. The rth moment only exists for `n > r`. and is given by


    .. math:: \mu'_X(r) = \left({\tfrac{1}{2}n}\right)^{r/2} \frac{\Gamma\left(\tfrac{1}{2}(n-r)\right)}{\Gamma\left(\tfrac{1}{2}n\right)} \times \sum_{i=0}^{\lfloor r/2 \rfloor} { \binom{r}{2i} \frac{(2i)!} {2^i i!}} \delta^{r-2i}, 

    See also: Paoella 2, page 381-382


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", student_t_nc(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_student_t_nc.cumulants(k)

Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
following a non-central Student t distribution. The cumulants are calculated from the moments.


.. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; k = 6;
    >>> print ("saddlepoint: ", student_t_nc(mu, sigma).cumulants(k))
    6.3563523462564525615615615614561356E+00









**Approximations**




.. method:: ctx.student_t_nc_ecf(x, n, delta, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf. See also: :cite:t:`Paolella2007`, page 381-382.




.. method:: ctx.student_t_nc_ecf_inv(q, n, delta, theta, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.








