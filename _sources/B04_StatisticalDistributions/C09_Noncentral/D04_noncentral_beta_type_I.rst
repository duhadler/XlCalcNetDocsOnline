

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_beta_nc_type_I: 

Boost: Noncentral Beta Type I distribution 
-------------------------------------------------------------------------------


The following functions return pdf, cdf, qtf or boost class of the noncentral beta distribution  with shape parameters `a` and `b`, noncentrality parameter `\lambda_1` and the support interval `(0, 1)`.


See also  Wikipedia :cite:p:`WikipediaDis04`,  BoostMath :cite:p:`BoostDis04`, :cite:t:`Wang1993`, :cite:t:`Kerns2018`.




|cr|

.. _Ctx_BetaNcPdf:

.. method:: Ctx.beta_nc_pdf(x, a, b, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the noncentral beta distribution:



    .. math:: \text{pdf}(x) = f_{\text{Beta}}(x;a, b;\lambda_1) = \frac{a}{b} \int_{0}^{\infty} y  \cdot  f_{\chi^2} \left(x \cdot y  \cdot a/b, 2a, \lambda_1\right) \cdot f_{\chi^2}(y, n) \: \mathrm{d}y
       :label: beta_nc_pdf_chou

    Here `f_{\chi^2}(\cdot, m, \lambda_1)` denotes the pdf of the noncentral `\chi^2` distribution with `m` degrees of freedom and noncentrality parameter `\lambda_1` (see :ref:`chi2_nc_pdf() <rst_mpm_chi2_nc_pdf>`), and `f_{\chi^2}(\cdot, n)` denotes the pdf of the central `\chi^2` distribution with `n` degrees of freedom  (see :ref:`chi_squared_pdf() <rst_mpm_chi_squared_pdf>`).

    Alternatively, the pdf can be written in a form which shows the relationship to the central distribution more clearly:

    .. math:: \text{pdf}(x) = f_{\text{Beta}'}(x;a,b,\lambda_1) = e^{-\lambda_1/2} f_{\text{Beta}}(x;a,b) \times  {}_1F_1 \left((a+b), b, \tfrac{n x \lambda_1}{2(m+n x)}\right)
       :label: beta_nc_pdf_hyper

    and `f_{\text{Beta}}(\cdot)` denotes the PDF of the central Beta-distribution, and `{}_1F_1(\cdot)` is the confluent hypergeometric function.


    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BetaNcPdf(x, a, b): ", BetaNcPdf(x, a, b))
        >>> print ("dist_beta_nc(a, b).pdf(x): ", dist_beta_nc(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BetaNcCdf:

.. method:: Ctx.beta_nc_cdf(x, a, b, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the noncentral beta distribution:



    .. math:: \text{cdf}(x) =  F_{\text{Beta}}(x;a, b;\lambda_1) = \frac{a z}{b}\int_{0}^{\infty} f_{\chi^2} \left(z \cdot y  \cdot a/b, 2a; \lambda_1\right) \cdot  [1-F_{\chi^2}(y, 2b)] \: \mathrm{d}y, \quad z = \frac{bx}{a(1-x)}
       :label: beta_nc_cdf_chou

    Here `f_{\chi^2}(\cdot, m, \lambda_1)` denotes the pdf of the noncentral `\chi^2` distribution with `m` degrees of freedom and noncentrality parameter `\lambda_1` (see :ref:`chi2_nc_pdf() <rst_mpm_chi2_nc_pdf>`).



    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BetaNcCdf(x, a, b): ", BetaNcCdf(x, a, b))
        >>> print ("dist_beta_nc(a, b).cdf(x): ", dist_beta_nc(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BetaNcQtf:

.. method:: Ctx.beta_nc_qtf(q, a, b, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the noncentral beta distribution:

    There is no known closed exact form for `\text{qtf}(q)`. For ``fpm.`` the default method is to call the function provided by Boost. 

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("BetaNcQtf(q, a, b): ", BetaNcQtf(q, a, b))
        >>> print ("dist_beta_nc(a, b).qtf(q): ", dist_beta_nc(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_beta_nc_type_I(a, b, lambda1)

where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

The noncentral Beta Type I distribution is a continuous probability distribution with shape parameters `a` and `b`, noncentrality parameter `\lambda_1` and the support interval `(0, 1)`.
See also Wikipedia :cite:p:`WikipediaDis04`, MathWorld :cite:p:`WolframDis04`, BoostMath :cite:p:`BoostDis04`, :cite:t:`Wang1993`, :cite:t:`CharfunDis04`, :cite:t:`Kerns2018`, R (Statistical System) :cite:p:`RDis04`.


A random variable `X` follows a Type I noncentral beta distribution with shape parameters `a` and `b` and noncentrality parameter `\lambda`,  if it is defined as `X = U_1/(U_1 + U_2)` where `U_1` and `U_2` are independent with `U_1 \sim \chi^2(n_1,\lambda)`, and `U_2 \sim \chi^2(n_2)`  `n_1 = 2a` and `n_2 = 2b` are the degrees of freedom, and `\lambda` is the noncentrality parameter of the noncentral `\chi^2` distribution. The random variable `Y = 1- X` is said to follow a Type II noncentral beta distribution with shape parameters `a` and `b` and noncentrality parameter `\lambda`.





|cr|

.. method:: dist_beta_nc_type_I.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following 
    a Type I noncentral beta distribution:

    .. math:: \text{pdf}_X(x) = f_{\text{Beta}'}(x;a,b,\lambda) = e^{-\lambda/2} f_{\text{Beta}}(x;a,b) \times  {}_1F_1 \left((a+b), b, \tfrac{n x \lambda}{2(m+n x)}\right)

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively,  of the central Beta-distribution, and `{}_1F_1(\cdot)` is the confluent hypergeometric function. There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", beta_nc_type_I(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_beta_nc_type_I.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Type I noncentral beta distribution:

    .. math:: \text{cdf}_X(x) = F_{\text{Beta}'}(x;a,b,\lambda) =  \int_{0}^{x} f_{\text{Beta}'}(x;a,b,\lambda) \mathrm{d} t =  e^{-\lambda/2} \sum_{j=0}^{\infty}{\frac{(\lambda/2)^j}{j!} F_{\text{Beta}}(x;a+j,b) }

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively,  of the central Beta-distribution, and `{}_1F_1(\cdot)` is the confluent hypergeometric function. There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", beta_nc_type_I(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_beta_nc_type_I.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Type I noncentral beta distribution:
    
    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{1} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", beta_nc_type_I(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_beta_nc_type_I.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Type I noncentral beta distribution:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a approximation by Winterbottom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", beta_nc_type_I(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_nc_type_I.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Type I noncentral beta distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", beta_nc_type_I(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_nc_type_I.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a Type I noncentral beta distribution:

    .. math:: C_X(t) = \int_{0}^{1} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", beta_nc_type_I(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_nc_type_I.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a Type I noncentral beta distribution:

    .. math:: M_X(t) = \int_{0}^{1} e^{tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", beta_nc_type_I(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_beta_nc_type_I.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function:

    .. math:: K_X(t) = \log (M_X(t))


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", beta_nc_type_I(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_beta_nc_type_I.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a Type I noncentral beta distribution: 
    the moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x


    Returns the raw moments of non-central beta function. See Walk for details.

    Algebraic moments of the non-central Beta-distribution are given  as (see \cite{walck_2007}, p. 109)

    .. math :: \operatorname{E}(x^k) = e^{-\lambda/2} \sum_{r=0}^{\infty} \frac{(\lambda/2)^r}{r!} \frac{B(p+r+k,q)}{B(p+r,q)}

    .. math :: \operatorname{E}(x^k) = \frac{\Gamma(p+k) \Gamma(p+q)}{\Gamma(p) \Gamma(p+q+k)} \times e^{-\lambda/2}  {}_2F_21(p+q,p+k;p,p+q+k;\lambda/2)

    Lower order moments are given by

    .. math :: \operatorname{E}(Y) = \frac{a}{a+b} \times e^{-\lambda/2}  {}_2F_2(a+1,a+b;a,a+b+1;\lambda/2)

    .. math :: \operatorname{E}(Y^2) = \frac{a(a+1)}{a+b(a+b+1)} \times e^{-\lambda/2}  {}_2F_2(a+1,a+b;a,a+b+1;\lambda/2)


    The moments of `Y=1-X` are given by:


    .. math:: \mu'_Y(r) =  \frac{\Gamma(n/2 + r)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2 + r)}  \times {}_1F_1\left(r ;\frac{n + m}{2}+ r ; -\frac{1}{2}\lambda\right),




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", beta_nc_type_I(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_beta_nc_type_I.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a Type I noncentral beta distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", beta_nc_type_I(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







