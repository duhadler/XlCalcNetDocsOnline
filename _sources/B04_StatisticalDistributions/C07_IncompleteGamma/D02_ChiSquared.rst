

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_chi_squared: 

.. _rst_mpm_chi_squared_pdf: 

.. _rst_mpm_chi_squared_cdf: 


Boost: Chi-Squared distribution 
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the chi-squared distribution with `n > 0` degrees of freedom and the support interval `(0,+\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis06`, MathWorld :cite:p:`WolframDis06`,  BoostMath :cite:p:`BoostDis06`, :cite:t:`Ehrhardt2018` (3.9.6)



|cr|

.. _Ctx_ChiSquaredPdf:

.. method:: Ctx.chi_squared_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the chi-squared distribution:

    .. math:: \text{pdf}(x) = f_{\chi^2}\left(x, n\right) = \frac{1}{2^{n/2} \Gamma(n/2)} x^{(n-2)/2}e^{-x/2}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ChiSquaredPdf(x, a, b): ", ChiSquaredPdf(x, a, b))
        >>> print ("dist_chi_squared(a, b).pdf(x): ", dist_chi_squared(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ChiSquaredCdf:

.. method:: Ctx.chi_squared_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the chi-squared distribution:

    .. math:: \text{cdf}(x) =  F_{\chi^2}\left(x, n\right) = P(n/2, x/2).

    Here `P(\cdot)` denotes the lower regularized incomplete gamma function (:ref:`RealGammaP <rst_mpm_gamma_p>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ChiSquaredCdf(x, a, b): ", ChiSquaredCdf(x, a, b))
        >>> print ("dist_chi_squared(a, b).cdf(x): ", dist_chi_squared(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ChiSquaredQtf:

.. method:: Ctx.chi_squared_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the chi-squared distribution:

    .. math:: \text{qtf}(q) = 2 P^{-1}(n/2, q).

    Here `P^{-1}(\cdot)` denotes the inverse of the lower regularized incomplete gamma function (:ref:`RealGammaPInv <rst_mpm_real_gamma_p_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("ChiSquaredQtf(q, a, b): ", ChiSquaredQtf(q, a, b))
        >>> print ("dist_chi_squared(a, b).qtf(q): ", dist_chi_squared(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_chi_squared(n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The chi-squared distribution is a continuous probability distribution with `n > 0` degrees of freedom and the support interval `(0,+\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis06`, MathWorld :cite:p:`WolframDis06`, BoostMath :cite:p:`BoostDis06`, :cite:t:`CharfunDis06`, R (Statistical System) :cite:p:`RDis06`.


    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chdtr.html#scipy.special.chdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chdtrc.html#scipy.special.chdtrc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chdtri.html#scipy.special.chdtri

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chdtriv.html#scipy.special.chdtriv





|cr|

.. method:: dist_chi_squared.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a chi-squared distribution:

    .. math:: \text{pdf}_X(x) = f_{\chi^2}\left(n, x\right) = \frac{1}{2^{n/2} \Gamma(n/2)} x^{(n-2)/2}e^{-x/2}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", chi_squared(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_chi_squared.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a chi-squared distribution:

    .. math:: \text{cdf}_X(x) =  F_{\chi^2}\left(x, n\right) = P(n/2, x/2).

    Here `P(\cdot)` and `P^{-1}(\cdot)` are the regularized gamma function and its functional inverse, respectively.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", chi_squared(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_chi_squared.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a chi-squared distribution:

    .. math:: \text{sf}_X(x)  =  1-F_{\chi^2}\left(x, n\right) = Q(n/2, x/2).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", chi_squared(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_chi_squared.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a chi-squared distribution:

    .. math:: \text{qtf}_X(q) = 2 P^{-1}(n/2, q).

    Here `P(\cdot)` and `P^{-1}(\cdot)` are the regularized gamma function and its functional inverse, respectively.

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", chi_squared(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a chi-squared distribution:

    .. math:: \text{isf}_X(q) = 2 Q^{-1}(n/2, q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", chi_squared(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a chi-squared distribution:

    .. math:: C_X(t) = (1-2it)^{-n/2}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a chi-squared distribution:

    .. math:: M_X(t) = (1-2t)^{-n/2}, \quad t \in \left(-\infty, \tfrac{1}{2}\right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, of a random variable `X`, following a chi-squared distribution:

    .. math:: K_X(t) = - \frac{n}{2} \log(1-2t), \quad t \in \left(-\infty, \tfrac{1}{2}\right),

    .. math:: K_X^{(j)}(t) = \frac{2^{j-1}(j-1)!}{(1-2t)^j} n .


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", chi_squared(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_chi_squared.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a chi-squared distribution: the moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", chi_squared(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_chi_squared.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a chi-squared distribution:

    .. math:: \kappa_{r+1} = 2^r r! n.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", chi_squared(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




**Recurrences: Central Chi-square**

.. method:: ctx.chi_squared_recurrence(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The following recurrence relations hold for the pdf and CDF:

    .. math:: f_{\chi^2}(n+2, x) = \frac{x}{n} f_{\chi^2}(n, x)

    .. math:: F_{\chi^2}(n, x)  - F_{\chi^2}(n+2, x) = 2f_{\chi^2}(n+2, x)






**Approximations**




.. method:: ctx.chi_squared_gp(x, n, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).





.. method:: ctx.chi_squared_ecf(x, f, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Edgeworth approximation to the pdf, cdf and sf.






.. method:: ctx.chi_squared_ecf_inv(q, f, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Cornish-Fisher approximation to the qtf and isf.




.. method:: ctx.chi_squared_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.



    The solution `\hat{s}(x)` of the saddlepoint equation `K_X^{(1)}(\hat{s}(x))=x`, of a random variable `X`, following a non-central chi-squared distribution is given by:

    .. math:: \hat{s}(x) = -\frac{1}{4x} \left[n-2x+n \right], \quad x>0




.. method:: ctx.chi_squared_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.




