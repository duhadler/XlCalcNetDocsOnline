

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_pareto: 

Boost: Pareto distribution 
-------------------------------------------------------------------------------


The following functions return pdf, cdf, qtf or boost class of the Pareto distribution with minimum (real) value `k > 0`, shape `a > 0`, and the support interval `(k, +\infty)`.

See also  Wikipedia :cite:p:`WikipediaDis21`, MathWorld :cite:p:`WolframDis21`,  BoostMath :cite:p:`BoostDis21`, :cite:t:`Ehrhardt2018` (3.9.25).



|cr|

.. _Ctx_ParetoPdf:

.. method:: Ctx.pareto_pdf(x, k, a)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the Pareto distribution:

    .. math:: \text{pdf}(x) = \frac{a}{x} \left(\frac{k}{x}\right)^a.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ParetoPdf(x, a, b): ", ParetoPdf(x, a, b))
        >>> print ("dist_pareto(a, b).pdf(x): ", dist_pareto(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ParetoCdf:

.. method:: Ctx.pareto_cdf(x, k, a)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Pareto distribution:

    .. math:: \text{cdf}(x) = 1 - \left(\frac{k}{x}\right)^a = - \text{powm1}(k/x,a).

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("ParetoCdf(x, a, b): ", ParetoCdf(x, a, b))
        >>> print ("dist_pareto(a, b).cdf(x): ", dist_pareto(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_ParetoQtf:

.. method:: Ctx.pareto_qtf(q, k, a)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Pareto distribution:

    .. math:: \text{qtf}(q) = \frac{k}{(1-q)^{1/a}}.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("ParetoQtf(q, a, b): ", ParetoQtf(q, a, b))
        >>> print ("dist_pareto(a, b).qtf(q): ", dist_pareto(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00



|cr|


.. py:class:: ctx.dist_pareto(k, a)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The Pareto distribution is a continuous probability distribution  with minimum (real) value `k > 0`, shape `a > 0`, and the support interval `(k, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis21`, MathWorld :cite:p:`WolframDis21`, BoostMath :cite:p:`BoostDis21`, :cite:t:`CharfunDis21`.





|cr|

.. method:: dist_pareto.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Pareto distribution:

    .. math:: \text{pdf}_X(x) = \frac{a}{x} \left(\frac{k}{x}\right)^a.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", pareto(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_pareto.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Pareto distribution:

    .. math:: \text{cdf}_X(x) = 1 - \left(\frac{k}{x}\right)^a = - \text{powm1}(k/x,a).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", pareto(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_pareto.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an Pareto distribution:

    .. math:: \text{sf}_X(x) = \left(\frac{k}{x}\right)^a = \text{pow}(k/x,a).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", pareto(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_pareto.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an Pareto distribution:

    .. math:: \text{qtf}_X(q) = \frac{k}{(1-q)^{1/a}}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", pareto(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pareto.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an Pareto distribution:

    .. math:: \text{isf}_X(q) = \frac{k}{q^{1/a}}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", pareto(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pareto.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Pareto distribution:

    .. math:: C_X(t) = a(-ikt)^a \Gamma(-a, -ikt).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", pareto(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pareto.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an Pareto distribution:

    .. math:: M_X(t) = a(-kt)^a \Gamma(-a, -kt), \quad \text{for } t<0.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", pareto(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pareto.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an Pareto distribution:

    .. math:: K_X(t) = K_X(t) = \log(M_X(t)), \quad \text{for } t<0.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", pareto(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_pareto.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an Pareto distribution. The rth moments only exists for `n_2 > 2r`.

    .. math:: \mu'_{X}(r) = \frac{a k}{a - n} \quad \text{for } a>n.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pareto(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_pareto.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, following an Pareto distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pareto(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







