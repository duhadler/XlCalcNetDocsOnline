

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_fisher_f_nc: 

Boost: Noncentral Fisher `F` distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the non-central Fisher F distribution with `m>0` and `n>0` degrees of freedom, noncentrality parameter `\lambda_1` , and the support interval `(0, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis02`, MathWorld :cite:p:`WolframDis02`,  BoostMath :cite:p:`BoostDis02`, :cite:t:`Benton2003`, :cite:t:`Butler2002`, :cite:t:`Chou1985`, :cite:t:`Chattamvelli1995`, :cite:t:`Wang1993`, :cite:t:`Kerns2018`.




|cr|

.. _Ctx_FisherFNcPdf:

.. method:: Ctx.fisher_f_nc_pdf(x, m, n, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the non-central Fisher F distribution:


    .. math:: \text{pdf}(x) = f_{\text{FisherF}}(x;m, n;\lambda_1) = \frac{m}{n} \int_{0}^{\infty} y  \cdot  f_{\chi^2} \left(x \cdot y  \cdot m/n, m, \lambda_1\right) \cdot f_{\chi^2}(y, n) \: \mathrm{d}y
       :label: fisher_f_nc_pdf_chou

    Here `f_{\chi^2}(\cdot, m, \lambda_1)` denotes the pdf of the noncentral `\chi^2` distribution with `m` degrees of freedom and noncentrality parameter `\lambda_1` (see :ref:`chi2_nc_pdf() <rst_mpm_chi2_nc_pdf>`), and `f_{\chi^2}(\cdot, n)` denotes the pdf of the central `\chi^2` distribution with `n` degrees of freedom  (see :ref:`chi_squared_pdf() <rst_mpm_chi_squared_pdf>`).

    Alternatively, the pdf can be written in a form which shows the relationship to the central distribution more clearly:

    .. math:: \text{pdf}(x) = f_{F'}(x;n_1,n_2,\lambda_1) = e^{-\lambda_1/2} f_{F}(x;n_1,n_2) {}_1F_1 \left(\tfrac{1}{2}(m+n), \tfrac{1}{2}n, \tfrac{n x \lambda_1}{2(m+n x)}\right), 
       :label: fisher_f_nc_pdf_hyper

    Here `f_{F}(\cdot)`  denotes the pdf of the central `F`-distribution, and `{}_1F_1(\cdot)` is the confluent hypergeometric function. 


    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("FisherFNcPdf(x, a, b): ", FisherFNcPdf(x, a, b))
        >>> print ("dist_fisher_f_nc(a, b).pdf(x): ", dist_fisher_f_nc(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_FisherFNcCdf:

.. method:: Ctx.fisher_f_nc_cdf(x, m, n, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the non-central Fisher F distribution:



    .. math:: \text{cdf}(x) =  F_{\text{FisherF}}(x;m, n;\lambda_1) = \frac{m x}{n}\int_{0}^{\infty} f_{\chi^2} \left(x \cdot y  \cdot m/n, m; \lambda_1\right) \cdot  [1-F_{\chi^2}(y, n)] \: \mathrm{d}y
       :label: fisher_f_nc_cdf_chou

    Here `f_{\chi^2}(\cdot, m, \lambda_1)` denotes the pdf of the noncentral `\chi^2` distribution with `m` degrees of freedom and noncentrality parameter `\lambda_1` (see :ref:`chi2_nc_pdf() <rst_mpm_chi2_nc_pdf>`), and `F_{\chi^2}(\cdot, n)` denotes the cdf of the central `\chi^2` distribution with `n` degrees of freedom  (see :ref:`chi_squared_cdf() <rst_mpm_chi_squared_cdf>`).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("FisherFNcCdf(x, a, b): ", FisherFNcCdf(x, a, b))
        >>> print ("dist_fisher_f_nc(a, b).cdf(x): ", dist_fisher_f_nc(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_FisherFNcQtf:

.. method:: Ctx.fisher_f_nc_qtf(q, m, n, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the non-central Fisher F distribution:

    There is no known closed exact form for `\text{qtf}(q)`. For ``fpm.`` the default method is to call the function provided by Boost. 

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("FisherFNcQtf(q, a, b): ", FisherFNcQtf(q, a, b))
        >>> print ("dist_fisher_f_nc(a, b).qtf(q): ", dist_fisher_f_nc(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_fisher_f_nc(m, n, lambda1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The non-central Fisher F  distribution is a continuous probability distribution with `m>0` and `n>0` degrees of freedom, noncentrality parameter `\lambda_1` , and the support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis02`, MathWorld :cite:p:`WolframDis02`, BoostMath :cite:p:`BoostDis02`, :cite:t:`Benton2003`, :cite:t:`Butler2002`, :cite:t:`Chou1985`, :cite:t:`Chattamvelli1995`, :cite:t:`Wang1993`, :cite:t:`CharfunDis02`, :cite:t:`Kerns2018`, R (Statistical System) :cite:p:`RDis02`. Also doubly-noncentral: :cite:t:`Yin2010`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ncfdtr.html#scipy.special.ncfdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ncfdtridfd.html#scipy.special.ncfdtridfd

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ncfdtridfn.html#scipy.special.ncfdtridfn

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ncfdtri.html#scipy.special.ncfdtri

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.ncfdtrinc.html#scipy.special.ncfdtrinc





|cr|

.. method:: dist_fisher_f_nc.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a non-central Fisher F distribution:

    .. math:: \text{pdf}_X(x) = f_{F'}(x;n_1,n_2,\lambda) = e^{-\lambda/2} f_{F}(x;n_1,n_2) {}_1F_1 \left(\tfrac{1}{2}(m+n), \tfrac{1}{2}n, \tfrac{n x \lambda}{2(m+n x)}\right), 


    Here `f_{F}(\cdot)`  denotes the pdf of the central `F`-distribution, and `{}_1F_1(\cdot)` is the confluent hypergeometric function. 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", fisher_f_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_fisher_f_nc.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a non-central Fisher F distribution:
	
    .. math:: \text{cdf}_X(x) = F_{F'}(x;m,n,\lambda) = e^{-\lambda} \sum_{j=0}^{\infty}{\frac{(\lambda/2)^j}{j!}F_F(x; m+2j,n)}


    Here `F_{F}(\cdot)` denotes the cdf of the central `F`-distribution.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", fisher_f_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_fisher_f_nc.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a non-central Fisher F distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", fisher_f_nc(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_fisher_f_nc.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a non-central Fisher F distribution:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: 
    It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", fisher_f_nc(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f_nc.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a non-central Fisher F distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", fisher_f_nc(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f_nc.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a non-central Fisher F distribution:

    .. math:: C_X(t) = \int_{0}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x



    .. math:: \phi(t) = e^{-\lambda/2} \sum_{k=0}^{\infty} \frac{(\lambda/2)^k}{k!} {}_1F_1 \left(\frac{\nu_1}{2}+k, -\frac{\nu_2}{2}, -\frac{\nu_2}{\nu_1}  it  \right).


    CRC: page 122: arcsin, page 146 half-normal


    See also: http://www.stat.uchicago.edu/~yibi/teaching/stat222/2017/Lectures/C05.pdf



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_fisher_f_nc.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_fisher_f_nc.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.





|cr|

.. method:: dist_fisher_f_nc.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a non-central Fisher F distribution. The rth moment only exists for `n_2 > 2r` and is given by

    .. math:: \mu'_X(r) = \left(\frac{n_2}{n_1}\right)^{r} \frac{\Gamma( \tfrac{1}{2}n_1+r) \Gamma( \tfrac{1}{2}n_2-r)}{\Gamma( \tfrac{1}{2}n_2)} {}_1\widetilde{F}_1(-r; \tfrac{1}{2}n_1; -\tfrac{1}{2}\lambda_1), 

    where `{}_1\widetilde{F}_1(a,b;z)` denotes Kummer's regularized confluent hypergeometric function.

    See also: https://mathworld.wolfram.com/NoncentralF-Distribution.html

    See also: Paoella 2, page 358-360


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f_nc(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_fisher_f_nc.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a non-central Fisher F distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_f_nc(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00






|cr|


**Additional methods: Confidence intervals and sample size estimates**


.. method:: dist_fisher_f_nc.nc_ci(alpha, beta)

    Returns a confidence interval for the noncentrality parameter *lambda*



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", fisher_f_nc(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






**Recurrences: Non-central Fisher F, recurrence pdf**

.. method:: ctx.fisher_f_nc_pdf_recurrence(x, lambda, start_n1, start_n2, target_n1, target_n2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The following recurrence relations hold for the pdf:


    Let the density `g_{m,n}` be that of `m/n` times an `F_{m,n}` random variable. Let `G_{m,n}(y)` be its 
    distribution function, and let `g_{m,n}^{\lambda}` and `G_{m,n}^{\lambda}(y)` be the density and distribution 
    function of its (singly) noncentral version (the distribution of `\chi_m^2(\lambda)/\chi_n^2(0)`). 
    Then the following recurrence relations hold (see :cite:t:`Chattamvelli1995`)

    Applies a recurrence relation to calculate the cdf for different degrees of freedom for a given value of *x*. This is mostly useful when using asymptotic methods.


    .. math:: n\left[G_{m,n+2}^{\lambda}(y)-G_{m-2,n+2}^{\lambda}(y)\right] =  -2g_{m,n}^{\lambda}(y)



    .. math:: \lambda(1+y) g_{m+4,n}^{\lambda}(y) = [\lambda y - m(1+y)]g_{m+2,n}^{\lambda}(y) + y(m+n)g_{m,n}^{\lambda}(y).

    .. math:: n(1+y) g_{m,n+2}^{\lambda}(y) = (m+n)g_{m,n}^{\lambda}(y) + \lambda g_{m+2,n}^{\lambda}(y).

    .. math:: \lambda g_{m+4,n-2}^{\lambda}(y) + m g_{m+2,n-2}^{\lambda}(y) = (n-2) y  g_{m,n}^{\lambda}(y).






**Recurrences: Non-central Fisher F, recurrence cdf**

.. method:: ctx.fisher_f_nc_cdf_recurrence(x, lambda, start_n1, start_n2, target_n1, target_n2)

where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


Applies a recurrence relation to calculate the cdf for different degrees of freedom for a given value of *x*. This is mostly useful when using asymptotic methods.


From these equations  we obtain


.. math::
    :nowrap:

    \begin{eqnarray}
        \lambda(1+y) G_{m+6,n}^{\lambda}(y) & = & [\lambda y - (m+2-\lambda )(1+y)]G_{m+4,n}^{\lambda}(y) \\
        & +  & [(m+2)(1+y)+y(m+n-\lambda)]G_{m+2,n}^{\lambda}(y) \nonumber \\ 
        & - & y(m+n)G_{m,n}^{\lambda}(y)  \nonumber
    \end{eqnarray}

.. math::
    :nowrap:

    \begin{eqnarray}
        n(1+y) :cite:t:`G_{m,n+2}^{\lambda}(y)-G_{m+2,n+2}^{\lambda}(y)]  & = & (m+n)G_{m,n}^{\lambda}(y) \\
        & +  & (\lambda-m-n)G_{m+2,n}^{\lambda}(y) \nonumber \\
        & - &  \lambda G_{m+4,n}^{\lambda}(y) \nonumber
    \end{eqnarray}

.. math::
    :nowrap:

    \begin{eqnarray}
        (n-2)y :cite:t:`G_{m,n}^{\lambda}(y)-G_{m+2,n}^{\lambda}(y)]  & = & (m+2)G_{m+2,n-2}^{\lambda}(y) \\
        & +  & (\lambda-m-2)G_{m+4,n-2}^{\lambda}(y) \nonumber \\
        & - &  \lambda G_{m+6,n-2}^{\lambda}(y) \nonumber
    \end{eqnarray}










**Approximations**


.. method:: ctx.fisher_f_nc_ecf(x, m, n, lambda1, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf. See also: MathWorld :cite:p:`WolframDis02`, :cite:t:`Paolella2007`, page 358-360.



.. method:: ctx.fisher_f_nc_ecf_inv(q, m, n, lambda1 results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.






