

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|




Boost: Saspoint5 distribution
-------------------------------------------------------------------------------

The SaS point5 distribution is a stable distribution (see Wikipedia :cite:p:`WikipediaDis94`) with the shape parameters `\alpha=1/2, \beta=0`. The Saspoint5 distribution is linear with respect to the location parameter `\mu` and scale parameter `c`.

.. math:: p(x_1; \mu_1, c_1) = p \left(x :=  \frac{x_1 - \mu_1}{c_1}; \mu:=0, c := 1  \right) \cdot \frac{1}{c_1}.

The support interval is `(-\infty,+\infty)`.


!!! The following references need to be updated: !!!


See also: https://www.boost.org/doc/libs/1_89_0/libs/math/doc/html/math_toolkit/dist_ref/dists/saspoint5_dist.html

See also: https://en.wikipedia.org/wiki/Stable_distribution#Other_analytic_cases




|cr|

.. _Ctx_Saspoint5_Pdf:

.. method:: Ctx.saspoint5_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.


    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Saspoint5 distribution. Let  `S(x)` and  `C(x)` denote the Fresnel integrals. Then:

    .. math:: \text{pdf}_X(x) ={\frac {1}{\sqrt {2\pi |x|^{3}}}}\left(\sin \left({\tfrac {1}{4|x|}}\right)\left[{\frac {1}{2}}-S\left({\tfrac {1}{\sqrt {2\pi |x|}}}\right)\right]+\cos \left({\tfrac {1}{4|x|}}\right)\left[{\frac {1}{2}}-C\left({\tfrac {1}{\sqrt {2\pi |x|}}}\right)\right]\right).




    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTPdf(x, a, b): ", StudentTPdf(x, a, b))
        >>> print ("dist_student_t(a, b).pdf(x): ", dist_student_t(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_Saspoint5_Cdf:

.. method:: Ctx.saspoint5_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Saspoint5 distribution.




    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTCdf(x, a, b): ", StudentTCdf(x, a, b))
        >>> print ("dist_student_t(a, b).cdf(x): ", dist_student_t(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_Saspoint5_Qtf:

.. method:: Ctx.saspoint5_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Saspoint5 distribution:


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("StudentTQtf(q, a, b): ", StudentTQtf(q, a, b))
        >>> print ("dist_student_t(a, b).qtf(q): ", dist_student_t(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: CtxBoost.dist_saspoint5(a=0, b=1)

    Returns an ``dist_saspoint5`` object, which gives access to the functions descibed below:

    .. code-block:: pycon

        >>> from mpfebnet import SReal, FReal, XReal, QReal, CReal, OReal
        >>> a = 0; b = 1; 
        >>> Ctx = SReal
        >>> dist_student_t = Ctx.dist_student_t(a, b)
        >>> print ("Dist.qtf(q=0.5): ", Dist.qtf(q=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_saspoint5.pdf(x)

    Returns `\text{pdf}(x)`, the value of the probability density function of the Saspoint5 distribution. See :ref:`Ctx.saspoint5_pdf <Ctx_Saspoint5_Pdf>` for formulas and examples.



.. method:: dist_saspoint5.cdf(x)

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function of the Saspoint5 distribution.  See :ref:`Ctx.saspoint5_cdf <Ctx_Saspoint5_Cdf>` for formulas and examples.



.. method:: dist_saspoint5.qtf(q)

    Returns `\text{qtf}(q)`, the value of the quantile function of the Saspoint5 distribution.  See :ref:`Ctx.saspoint5_qtf <Ctx_Saspoint5_Qtf>` for formulas and examples.




|cr|

.. method:: dist_saspoint5.sf(x)

    Returns `\text{sf}(x)`, the value of the survival function (:ref:`Sf <Dist_Sf>`) of the Saspoint5 distribution. 

    .. math:: \text{sf}(x)  = \text{cdf}_X(-x)

    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.sf(x=0.5): ", Dist.qtf(x=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_saspoint5.isf(q)

    Returns `\text{isf}(q)`, the value of the inverse survival function (:ref:`Isf <Dist_Isf>`) of the Saspoint5 distribution. 

    .. math:: \text{isf}(q) = -\text{qtf}(q).

    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.isf(x=0.5): ", Dist.isf(x=0.5))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_saspoint5.hf(x)

    Returns `\text{hazard}(x)`, the value of the hazard function (:ref:`Hf <Dist_Hf>`) of the Saspoint5 distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_saspoint5.chf(x)

    Returns `\text{chf}(x)`, the value of the cumulative hazard function (:ref:`Chf <Dist_Chf>`) of the Saspoint5 distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.mode()

    Returns the :ref:`mode <Dist_Mode>` of the Saspoint5 distribution. Since there is not one unique mode, ``Nan`` is returned.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.median()

    Returns the :ref:`median <Dist_Median>`  of the Saspoint5 distribution. Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.


    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_saspoint5.mean()

    Returns the  :ref:`mean <Dist_Mean>` (expected value) of the Saspoint5 distribution. Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_saspoint5.variance()

    Returns the :ref:`variance <Dist_Variance>` of the Saspoint5 distribution. Calculated as `\displaystyle \tfrac{1}{8}(b-a)^2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.stdev()

    Returns the :ref:`standard deviation <Dist_Stdev>` of the Saspoint5 distribution. Calculated as `\displaystyle \sqrt{ \tfrac{1}{8}(b-a)^2}`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.skewness()

    Returns the :ref:`skewness <Dist_Skewness>` of the Saspoint5 distribution. Calculated as `\displaystyle 0`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.kurtosis()

    Returns the 'proper' :ref:`kurtosis <Dist_Kurtosis>` (normalized fourth moment) of the Saspoint5 distribution. Calculated as `\displaystyle 3/2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.kurtosis_excess()

    Returns the :ref:`kurtosis excess <Dist_KurtosisExcess>` of the Saspoint5 distribution. Calculated as `\displaystyle -3/2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.support_lower_endpoint()

    Returns the :ref:`support <Dist_Support_Lower_Endpoint>` of the Saspoint5 distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.support_upper_endpoint()

    Returns the :ref:`support <Dist_Support_Upper_Endpoint>` of the Saspoint5 distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.range_lower_endpoint()

    Returns the valid :ref:`range <Dist_Range_Lower_Endpoint>` of the Saspoint5 distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_saspoint5.range_upper_endpoint()

    Returns the valid :ref:`range <Dist_Range_Upper_Endpoint>` of the Saspoint5 distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



















