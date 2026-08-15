

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_landau: 


Boost: Landau Distribution
-------------------------------------------------------------------------------




The Landau distribution is a stable distribution (see Wikipedia :cite:p:`WikipediaDis94`) with the shape parameters `\alpha = 1, \beta = 1`. For simplicity of numerical computation, this paper evaluates as follows assuming location parameter `\mu = 0`, scale parameter `c = 1 / \pi/2`, i.e. `p(x) = p(x; \alpha = 1, \beta = 1, \mu = 0, c = \pi/2)`. For other choices of the location parameter `\mu` and scale parameter `c` there is the relationship

.. math:: p(x_1; \mu_1, c_1) = p \left(x :=  \frac{x_1 - \mu_1}{c_1} - \frac{2}{\pi} \log(c); \mu:=0, c := 1  \right) \cdot \frac{1}{c_1}.

The support interval is `(-\infty,+\infty)`.


!!! The following references need to be updated: !!!



See also: https://www.boost.org/doc/libs/1_89_0/libs/math/doc/html/math_toolkit/dist_ref/dists/landau_dist.html

See also: https://en.wikipedia.org/wiki/Landau_distribution




|cr|

.. _Ctx_Landau_Pdf:

.. method:: Ctx.landau_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Landau distribution, with `\mu \in \mathbb{R}`, `c>0`:

    .. math:: \text{pdf}_X(x) = \frac{1}{\pi c} \int_{0}^{\infty} e^{-t} \cos \left ( t \left( \frac{x-\mu}{c} \right) + \frac{2t}{\pi} \log \left( \frac{t}{c} \right)  \right ) \mathrm{d}t.

    For `\mu = 0, c = \pi/2` this simplifies to:

    .. math:: \text{pdf}_X(x) = \frac{1}{\pi} \int_{0}^{\infty} \frac{\exp(-xt) \sin(\pi t)}{t^t} \mathrm{d}t.


|cr|

.. _Ctx_Landau_Cdf:

.. method:: Ctx.landau_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Landau distribution.



    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTCdf(x, a, b): ", StudentTCdf(x, a, b))
        >>> print ("dist_student_t(a, b).cdf(x): ", dist_student_t(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_Landau_Qtf:

.. method:: Ctx.landau_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the  Landau distribution.


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("StudentTQtf(q, a, b): ", StudentTQtf(q, a, b))
        >>> print ("dist_student_t(a, b).qtf(q): ", dist_student_t(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00






.. py:class:: ctx.dist_landau(n1, n2, lambda, **kwargs)

    In probability theory, the Landau distribution is a probability distribution named after Lev Landau. Because of the distribution's "fat" tail, the moments of the distribution, like mean or variance, are undefined. The distribution is a particular case of stable distribution.


    These functions return PDF, CDF, and ICDF of the Landau distribution with location `a`, scale `b > 0`, and the support interval `(-\infty,+\infty)` :

    See also: Wikipedia :cite:p:`WikipediaDis95`.




|cr|

.. method:: dist_landau.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Landau distribution:

    .. math::
        :nowrap:

        \begin{eqnarray}
        \text{pdf}_X(x)  & = & \frac{1}{\pi} \int_{0}^{\infty} \Re \left ( e^{-itx} C_X(t) \right ) \mathrm{d} t.  \\
        & = & \frac{1}{\pi c} \int_{0}^{\infty} e^{-t} \cos \left ( t \left( \frac{x-\mu}{c} \right) + \frac{2t}{\pi} \log \left( \frac{t}{c} \right)  \right ) \mathrm{d} t., 
        \end{eqnarray}

    where `\Re (z)` denotes the real part of `z`.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", dist_landau(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_landau.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Landau distribution:

    .. math:: \text{cdf}_X(x) =\frac{1}{2} -  \frac{1}{\pi} \int_{0}^{\infty} \Im \left (    \frac{  e^{-itx} C_X(t)}{t}  \right ) \mathrm{d} t,

    where `\Im (z)` denotes the imaginary part of `z`.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", dist_landau(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_landau.sf(x)

    Returns `\text{sf}_X(x)`, the survival function function (sf) of a random variable `X`, following an Landau distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", dist_landau(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_landau.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function function (qtf) of a random variable `X`, following an Landau distribution:

    .. math:: \text{qtf}_X(q) =  \text{no closed form}.



    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", dist_landau(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_landau.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function function (isf) of a random variable `X`, following an Landau distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", dist_landau(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_landau.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an Landau distribution:

    .. math::  C_X(t) = \exp\left( i t \mu - \frac{2 i c t}{\pi} \log|t| - c|t|  \right).


    .. code-block:: python

        >>> from mpdistrib import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", dist_landau(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_landau.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_landau.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.






|cr|

.. method:: dist_landau.moments(k)

    Returns ``NaN``, since moments do not exist.



|cr|

.. method:: dist_landau.cumulants(k)

    Returns ``NaN``, since cumulants do not exist.





