

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}






.. _rst_dist_chi_squared_nc: 

.. _rst_mpm_chi2_nc_pdf: 

.. _rst_mpm_chi2_nc_cdf: 


Boost: Noncentral `\chi^2` distribution 
-------------------------------------------------------------------------------


The following functions return the pdf, cdf, qtf or boost class of the noncentral chi-squared distribution with degrees of freedom `n>0`, noncentrality parameter `\lambda_1`, and support interval `(0, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis01`, MathWorld :cite:p:`WolframDis01`, :cite:t:`Patnaik1949`, :cite:t:`Penev2000`, :cite:t:`Wang1993`, :cite:t:`Winterbottom1979`,  BoostMath :cite:p:`BoostDis01`, :cite:t:`Kerns2018`.




|cr|

.. _Ctx_Chi2NcPdf:

.. method:: Ctx.chi_squared_nc_pdf(x, n, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the noncentral chi-squared distribution:


    .. math:: \text{pdf}(x) = f_{\chi^2}\left(n, x; \lambda_1\right)  =\frac {1}{2}e^{-(x+\lambda )/2} \left(\frac {x}{\lambda } \right)^{k/4-1/2} I_{k/2-1}({\sqrt {\lambda x}})
       :label: chi2_nc_pdf_bessel

    where `I_{k}(y)` is a modified Bessel function of the first kind of order `k`. 


    Alternatively, the pdf can be written in a form which shows the relationship to the central distribution more clearly:

    .. math:: \text{pdf}(x) = f_{\chi^2}\left(n, x; \lambda_1\right) = f_{\chi^2}(x, n) \times e^{-\lambda_1/2}  \times  {}_0F_1 \left(-; \frac{n}{2}; \frac{x \lambda_1}{4}\right).
       :label: chi2_nc_pdf_hyper

    Here `f_{\chi^2}(\cdot)` is the PDF of the central chi-square distribution, and `{}_0F_1(\cdot)` is the  confluent hypergeometric limit function. 


    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("Chi2NcPdf(x, a, b): ", Chi2NcPdf(x, a, b))
        >>> print ("dist_chi_squared_nc(a, b).pdf(x): ", dist_chi_squared_nc(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_Chi2NcCdf:

.. method:: Ctx.chi_squared_nc_cdf(x, n, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the noncentral chi-squared distribution:

    .. math:: \text{cdf}(x) = F_{\chi^2}\left(n, x; \lambda\right) =  \int_{0}^{x} f_{\chi^2}\left(n, x; \lambda_1\right)  \mathrm{d}t.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("Chi2NcCdf(x, a, b): ", Chi2NcCdf(x, a, b))
        >>> print ("dist_chi_squared_nc(a, b).cdf(x): ", dist_chi_squared_nc(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_Chi2NcQtf:

.. method:: Ctx.chi_squared_nc_qtf(q, n, lambda1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the noncentral chi-squared distribution:

    There is no known closed exact form for `\text{qtf}(q)`. The default method is to call the function provided by Boost. 

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("Chi2NcQtf(q, a, b): ", Chi2NcQtf(q, a, b))
        >>> print ("dist_chi_squared_nc(a, b).qtf(q): ", dist_chi_squared_nc(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|



.. py:class:: ctx.dist_chi_squared_nc(n, lambda1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The noncentral chi-square distribution is a continuous probability distribution with degrees of freedom `n>0`, 
    noncentrality parameter `\lambda_1`, and support interval `(0, \infty)`.
    See also Wikipedia :cite:p:`WikipediaDis01`, MathWorld :cite:p:`WolframDis01`, :cite:t:`Patnaik1949`, :cite:t:`Penev2000`, :cite:t:`Wang1993`, :cite:t:`Winterbottom1979`, BoostMath :cite:p:`BoostDis01`, :cite:t:`CharfunDis01`, :cite:t:`Kerns2018`, R (Statistical System) :cite:p:`RDis01`, :cite:t:`Yu2011`.

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chndtr.html#scipy.special.chndtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chndtridf.html#scipy.special.chndtridf

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chndtrinc.html#scipy.special.chndtrinc

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.chndtrix.html#scipy.special.chndtrix





|cr|

.. method:: dist_chi_squared_nc.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a non-central chi-squared distribution:

    .. math:: \text{pdf}_X(x) = f_{\chi^2}\left(n, x; \lambda\right) = e^{-\lambda/2} f_{\chi^2}(n, x)  {}_0F_1 \left(-; \frac{n}{2}; \frac{x \lambda}{4}\right),

    Here `f_{\chi^2}(\cdot)` and `F_{\chi^2}(\cdot)` are the PDF and CDF, respectively, of the central chi-square distribution, and   `{}_0F_1(\cdot)` is the  confluent hypergeometric limit function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", chi_squared_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_chi_squared_nc.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a non-central chi-squared distribution:
	
    .. math:: \text{cdf}_X(x) = \int_{0}^{x} \text{pdf}_X(x) \mathrm{d} t = F_{\chi^2}\left(n, x; \lambda\right) =  e^{-\lambda/2} \sum_{j=0}^\infty {\frac{(\lambda /2)^j}{j!} F_{\chi^2}\left(n+2+j, x\right) },

    Here `f_{\chi^2}(\cdot)` and `F_{\chi^2}(\cdot)` are the PDF and CDF, respectively, of the central chi-square distribution, and   `{}_0F_1(\cdot)` is the  confluent hypergeometric limit function.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", chi_squared_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_chi_squared_nc.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a non-central chi-squared distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", chi_squared_nc(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_chi_squared_nc.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a non-central chi-squared distribution:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a central chi-square approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", chi_squared_nc(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared_nc.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a non-central chi-squared distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", chi_squared_nc(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared_nc.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a non-central chi-squared distribution:

    .. math:: C_X(t) = \exp \left(\frac{i \lambda t}{1-2it}\right)  (1-2it)^{-n/2}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared_nc.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following a non-central chi-squared distribution:

    .. math:: M_X(t) = \exp \left(\frac{\lambda t}{1-2t}\right)  (1-2t)^{-n/2}, \quad t \in \left(-\infty, \tfrac{1}{2}\right),


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_chi_squared_nc.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, `K_X^{(j)}(t), j = 1 \ldots k`, 
    of a random variable `X`, following a non-central chi-squared distribution:

    .. math:: K_X(t) = -\frac{n}{2} \log(1-2t) + \frac{\lambda t}{1-2t}, \quad t \in \left(-\infty, \tfrac{1}{2}\right),

    .. math:: K_X^{(j)}(t) = \frac{2^{j-1}(j-1)!}{(1-2t)^j} \left[n + \frac{\lambda j}{1-2t}   \right].  


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", chi_squared_nc(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_chi_squared_nc.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a non-central chi-squared distribution: the moments are calculated from the cumulants.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", chi_squared_nc(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_chi_squared_nc.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a non-central chi-squared distribution:

    .. math:: \kappa_{r} = 2^{r-1} (r-1)! (n+r\lambda)


    .. code-block:: python

        def MakeNoncentralChiSquaredCumulants(self):
            df = iv.mpf(2000)
            lambda_ = 33
            k = 10
            kappa = iv.matrix(k+1, 1)
            kappa[0] = 1
            kappa[1] = df + lambda_
            for i in range(2, k+1):
                kappa[i] = kappa[i - 1] * 2 * (i - 1) * (1 + lambda_ / (df + (i - 1) * lambda_))
            return kappa





**Recurrences: Non-central Chi-square**

.. method:: ctx.chi_squared_nc_recurrence(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The following recurrence relations hold for the pdf and CDF (see :cite:t:`Cohen1988`):

    .. math:: f_{\chi^2}\left(n+4,x;\lambda\right)  = \frac{x \cdot f_{\chi^2}\left(n,x;\lambda\right) - n \cdot f_{\chi^2}\left(n+2,x;\lambda\right) }{\lambda} 

    .. math:: F_{\chi^2}\left(n,x;\lambda\right)  - F_{\chi^2}\left(n+2,x;\lambda\right) = 2f_{\chi^2}\left(n+2,x;\lambda\right)

    .. math:: F_{\chi^2}\left(n,x;\lambda\right)  - F_{\chi^2}\left(n-2,x;\lambda\right) = 2 \frac{\partial}{\partial \lambda} F_{\chi^2}\left(n-2,x;\lambda\right)





    Ref:

    Pav 2015: Moments of log noncentral chisquare

    Yu 2011: mode of noncentral chi-square







**Approximations**


.. method:: ctx.chi_squared_nc_gp(x, n, lambda, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).




.. method:: ctx.chi_squared_nc_ecf(x, f, lambda1, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf.




.. method:: ctx.chi_squared_nc_ecf_inv(q, f, lambda1, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.





.. method:: ctx.chi_squared_nc_spa(x, n, lambda, results='cdf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf.


    The solution `\hat{s}(x)` of the saddlepoint equation `K_X^{(1)}(\hat{s}(x))=x`, of a random variable `X`, following a non-central chi-squared distribution is given by:

    .. math:: \hat{s}(x) = -\frac{1}{4x} \left[n-2x+\sqrt{n^2+4x\lambda} \right], \quad x>0



    .. code-block:: python
        
        def NonCentralChi2_SPA2(self, n0, x0, lambda0_):
            n = iv.mpf(n0)
            x = iv.mpf(x0)
            lambda_ = iv.mpf(lambda0_)
            s = -(1 / (4 * x)) * (n - 2 * x + iv.sqrt(n * n + 4 * x * lambda_))
            Order = 18
            kderiv = iv.matrix(Order+2, 1)
            for j in range(0, Order+1):     
                kderiv[j] = self.NonCentralChi2_CGF_Derivative(s, n, lambda_, j)

            LeftTail, RightTail = self.LugannaniRice(Order, kderiv, s)
            return LeftTail, RightTail
        
    The following code tests the procedure

    
    .. code-block:: python

        def LugannaniRiceDemo(self):
            nu = 40.0
            x = 61.0
            nc = 70.0
            LeftTail, RightTail = self.NonCentralChi2_SPA2(nu, x, nc)
            print("LeftTail:  ", LeftTail)
            print("RightTail: ", RightTail)





.. method:: ctx.chi_squared_nc_spa_inv(x, n, lambda, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.


