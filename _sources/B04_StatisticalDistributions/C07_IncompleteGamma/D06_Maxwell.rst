

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_maxwell: 

!!!Boost: Maxwell Distribution
===============================================================================


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following a Maxwell distribution with scale `b > 0`, and the support interval `(0,+\infty)`.


See also  Wikipedia :cite:p:`WikipediaDis47`, MathWorld :cite:p:`WolframDis47`, :cite:t:`Ehrhardt2018` (3.9.20).



|cr|

.. _Ctx_MaxwellPdf:

.. method:: Ctx.maxwell_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Maxwell distribution:

    .. math:: \text{pdf}(x) = \sqrt{\frac{2}{\pi}} \frac{x^2}{b^3} \exp\left( -\frac{x^2}{2b^2} \right).

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("MaxwellPdf(x, a, b): ", MaxwellPdf(x, a, b))
        >>> print ("dist_maxwell(a, b).pdf(x): ", dist_maxwell(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_MaxwellCdf:

.. method:: Ctx.maxwell_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Maxwell distribution:

    .. math:: \text{cdf}(x) = P\left( \frac{3}{2}, \frac{x^2}{2b^2} \right).

    Here `P(\cdot)` denotes the lower regularized incomplete gamma function (:ref:`RealGammaP <rst_mpm_gamma_p>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("MaxwellCdf(x, a, b): ", MaxwellCdf(x, a, b))
        >>> print ("dist_maxwell(a, b).cdf(x): ", dist_maxwell(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_MaxwellQtf:

.. method:: Ctx.maxwell_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Maxwell distribution:

    .. math:: \text{qtf}(q) =  b \sqrt{2 P^{-1}\left(\frac{3}{2}, q\right)}.

    Here `P^{-1}(\cdot)` denotes the inverse of the lower regularized incomplete gamma function (:ref:`RealGammaPInv <rst_mpm_real_gamma_p_inv>`).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("MaxwellQtf(q, a, b): ", MaxwellQtf(q, a, b))
        >>> print ("dist_maxwell(a, b).qtf(q): ", dist_maxwell(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|


.. py:class:: ctx.dist_maxwell(b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Maxwell distribution is a continuous probability distribution with scale `b > 0`, and the support interval `(0,+\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis47`, MathWorld :cite:p:`WolframDis47`, :cite:t:`CharfunDis47`.





|cr|

.. method:: dist_maxwell.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Maxwell distribution:

    .. math:: \text{pdf}_X(x) = \sqrt{\frac{2}{\pi}} \frac{x^2}{b^3} \exp\left( -\frac{x^2}{2b^2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", maxwell(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_maxwell.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Maxwell distribution:

    .. math:: \text{cdf}_X(x) = P\left( \frac{3}{2}, \frac{x^2}{2b^2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", maxwell(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_maxwell.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an Maxwell distribution:

    .. math:: \text{sf}_X(x)  = Q\left( \frac{3}{2}, \frac{x^2}{2b^2} \right).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", maxwell(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_maxwell.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an Maxwell distribution:

    .. math:: \text{qtf}_X(q) =  b \sqrt{2 P^{-1}\left(\frac{3}{2}, q\right)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", maxwell(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_maxwell.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an Maxwell distribution:

    .. math:: \text{isf}_X(q) =  b \sqrt{2 Q^{-1}\left(\frac{3}{2}, q\right)}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", maxwell(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_maxwell.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Maxwell distribution:

    .. math::  C_X(t) = M\left( \frac{3}{2},  \frac{1}{2} \frac{-t^2}{2} \right) +  \frac{2 \sqrt{2} \, i t  }{\sqrt{\pi}}   M\left(2,  \frac{3}{2}, \frac{-t^2}{2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", maxwell(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_maxwell.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Maxwell distribution:

    .. math:: M_X(t) =  M\left( \frac{3}{2},  \frac{1}{2} \frac{t^2}{2} \right) +  \frac{2 \sqrt{2} \, t }{\sqrt{\pi}}  M\left( 2,  \frac{3}{2}, \frac{t^2}{2} \right).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", maxwell(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_maxwell.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Maxwell distribution:

    .. math:: K_X(t) = \log \left[  M\left( \frac{3}{2},  \frac{1}{2} \frac{t^2}{2} \right) + \frac{2 \sqrt{2} \, t }{\sqrt{\pi}}  M\left(2,  \frac{3}{2}, \frac{t^2}{2} \right) \right].



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", maxwell(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00








|cr|

.. method:: dist_maxwell.moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Maxwell distribution (Wikipedia). The raw moments are calculated from the central moments.


    .. math::  

        \mu_{X}(r) = \begin{cases}
        \sqrt{\frac{2}{\pi}} k! \alpha^{2k-1} & \text{for } n=2k-1,\\
        (n+1)!! \alpha^n &  \text{for } n \text{ even},
        \end{cases} 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", maxwell(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_maxwell.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Maxwell distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", maxwell(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00





