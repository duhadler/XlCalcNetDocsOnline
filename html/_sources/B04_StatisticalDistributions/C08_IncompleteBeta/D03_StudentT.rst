

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_student_t: 

Boost: Student `t` (Pearson Type VII) distribution 
===============================================================================


The following functions return the pdf, cdf, qtf or boost class of the Student t distribution with `n > 0` degrees of freedom and the support interval `(-\infty, +\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis07`, MathWorld :cite:p:`WolframDis07`,  BoostMath :cite:p:`BoostDis07`, :cite:t:`Ehrhardt2018` (3.9.29).




|cr|

.. _Ctx_StudentTPdf:

.. method:: Ctx.student_t_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Student t distribution:

    .. math:: \text{pdf}(x) = \frac{\Gamma((n+1)/2)}{\sqrt{n\pi}\Gamma(n/2)} \left(\frac{n}{n+t^2}\right)^{(n+1)/2}.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTPdf(x, a, b): ", StudentTPdf(x, a, b))
        >>> print ("dist_student_t(a, b).pdf(x): ", dist_student_t(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_StudentTCdf:

.. method:: Ctx.student_t_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Student t distribution:

    .. math:: 
        \text{cdf}(x) =\begin{cases}
        1-p, & x > 0,\\
        p & x \le 0.
        \end{cases},   
        \quad \text{where }
        p =\begin{cases}
        \text{ibeta}(n/2, 1/2, n/(n+x^2))/2, & n < 2x^2,\\
        \text{ibetac}(1/2, n/2, x^2/(n+x^2))/2, & n \ge 2x^2.
        \end{cases}   

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function (:ref:`RealIBeta <rst_mpm_ibeta>`), and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function (:ref:`RealIBetac <rst_mpm_ibetac>`).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTCdf(x, a, b): ", StudentTCdf(x, a, b))
        >>> print ("dist_student_t(a, b).cdf(x): ", dist_student_t(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_StudentTQtf:

.. method:: Ctx.student_t_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Student t distribution:

    .. math:: \text{qtf}(q) = t_{\nu, \alpha} =  \text{sign}(q-0.5) \sqrt{n (1-x)/x}, \quad \text{where } x = \mathrm{ibeta\_inv}\left(\tfrac{1}{2} n, \tfrac{1}{2}, 2 \cdot \text{min}(q, 1-q)\right).

    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function (:ref:`RealIBetaInv <rst_mpm_real_ibeta_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("StudentTQtf(q, a, b): ", StudentTQtf(q, a, b))
        >>> print ("dist_student_t(a, b).qtf(q): ", dist_student_t(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


    .. py:class:: ctx.dist_student_t(n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Student `t` distribution is a continuous probability distribution with `n > 0` degrees of freedom and the support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis07`, MathWorld :cite:p:`WolframDis07`, BoostMath :cite:p:`BoostDis07`, :cite:t:`Broda2007`, :cite:t:`Witkovsky2001`, :cite:t:`CharfunDis07`, R (Statistical System) :cite:p:`RDis07`.


    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html#scipy.stats.t

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.stdtr.html#scipy.special.stdtr

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.stdtridf.html#scipy.special.stdtridf

    See also: https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.stdtrit.html#scipy.special.stdtrit



|cr|

.. method:: dist_student_t.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a central Student t distribution:

    .. math:: \text{pdf}_X(x) = \frac{\Gamma((n+1)/2)}{\sqrt{n\pi}\Gamma(n/2)} \left(\frac{n}{n+t^2}\right)^{(n+1)/2}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", student_t(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_student_t.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a central Student t distribution:

    .. math:: 
        \text{cdf}_X(x) =\begin{cases}
        1-p, & x > 0,\\
        p & x \le 0.
        \end{cases},   
        \quad \text{where }
        p =\begin{cases}
        \text{ibeta}(n/2, 1/2, n/(n+x^2))/2, & n < 2x^2,\\
        \text{ibetac}(1/2, n/2, x^2/(n+x^2))/2, & n \ge 2x^2.
        \end{cases}   


    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function, and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", student_t(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_student_t.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a central Student t distribution:


    .. math:: \text{sf}_X(x)  = \text{cdf}_X(-x)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", student_t(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_student_t.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a central Student t distribution:


    .. math:: \text{qtf}_X(q) = \text{sign}(q-0.5) \sqrt{n (1-x)/x}, \quad \text{where } x = \mathrm{ibeta\_inv}\left(\tfrac{1}{2} n, \tfrac{1}{2}, 2 \cdot \text{min}(q, 1-q)\right).



    Here `\mathrm{ibeta\_inv}(\cdot)` denotes the inverse of the real normalised incomplete beta function.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", student_t(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a central Student t distribution:

    .. math:: \text{isf}_X(q) = -\text{qtf}_X(q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", student_t(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following a central Student t distribution:

    .. math:: C_X(t) = \frac{K_{n/2}(\sqrt{n}|t|)^{n/2}}{\Gamma(n/2) 2^{n/2-1}},

    where `K_n(\cdot)` denotes the modified Bessel function of the second kind.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", student_t(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_student_t.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.





|cr|

.. method:: dist_student_t.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following a central Student t distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_X(r) = \mu'_{t}(r)= \left({\tfrac{1}{2}n}\right)^{r/2} \frac{\Gamma\left(\tfrac{1}{2}(n-r)\right)}{\Gamma\left(\tfrac{1}{2}n\right)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", student_t(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_student_t.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following a central Student t distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", student_t(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




