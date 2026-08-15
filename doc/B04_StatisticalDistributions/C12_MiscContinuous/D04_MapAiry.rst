

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|




Boost: Map-Airy distribution
-------------------------------------------------------------------------------


The Map-Airy distribution (or Airy distribution of the ’Map’-type) is a stable distribution (see Wikipedia :cite:p:`WikipediaDis94`) with the shape parameters `\alpha = 3/2, \beta = 1`, which describes the probability distribution of the area under a Brownian excursion over a unit interval. For simplicity of numerical computation, this paper evaluates as follows assuming location parameter `\mu = 0`, scale parameter `c = 1 / \sqrt[3]{18}`, i.e. `p(x) = p(x; \alpha = 3/2, \beta = 1, \mu = 0, c = 1 / \sqrt[3]{18})`. The Map-Airy distribution is linear with respect to the location parameter `\mu` and scale parameter `c`.

.. math:: p(x_1; \mu_1, c_1) = p \left(x :=  \frac{x_1 - \mu_1}{c_1}; \mu:=0, c := 1  \right) \cdot \frac{1}{c_1}.

The support interval is `(-\infty,+\infty)` :


!!! The following references need to be updated: !!!



See also: https://www.boost.org/doc/libs/1_89_0/libs/math/doc/html/math_toolkit/dist_ref/dists/mapairy_dist.html

See also: https://mathworld.wolfram.com/Map-AiryDistribution.html




|cr|

.. _Ctx_MapAiry_Pdf:

.. method:: Ctx.mapairy_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}(x)`, the value of the probability density function (:ref:`Pdf <Dist_Pdf>`) of the MapAiry distribution:

    Boost:

    .. math:: \text{pdf}(x) = 2 e^{-2x^3 / 3}  \left( x \text{Ai}(x^2) - \text{Ai}'(x^2)\right).

    Wolfram:

    .. math:: \text{pdf}(x) = 2 e^{2x^3 / 3}  \left( -x \text{Ai}(x^2) - \text{Ai}'(x^2)\right).


    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTPdf(x, a, b): ", StudentTPdf(x, a, b))
        >>> print ("dist_student_t(a, b).pdf(x): ", dist_student_t(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_MapAiry_Cdf:

.. method:: Ctx.mapairy_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the MapAiry distribution:



    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("StudentTCdf(x, a, b): ", StudentTCdf(x, a, b))
        >>> print ("dist_student_t(a, b).cdf(x): ", dist_student_t(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_MapAiry_Qtf:

.. method:: Ctx.mapairy_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the MapAiry distribution:


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("StudentTQtf(q, a, b): ", StudentTQtf(q, a, b))
        >>> print ("dist_student_t(a, b).qtf(q): ", dist_student_t(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: CtxBoost.dist_mapairy(a=0, b=1)

    Returns an ``dist_mapairy`` object, which gives access to the functions descibed below:

    .. code-block:: pycon

        >>> from mpfebnet import SReal, FReal, XReal, QReal, CReal, OReal
        >>> a = 0; b = 1; 
        >>> Ctx = SReal
        >>> dist_student_t = Ctx.dist_student_t(a, b)
        >>> print ("Dist.qtf(q=0.5): ", Dist.qtf(q=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_mapairy.pdf(x)

    Returns `\text{pdf}(x)`, the value of the probability density function of the Map-Airy distribution. See :ref:`Ctx.mapairy_pdf <Ctx_MapAiry_Pdf>` for formulas and examples.



.. method:: dist_mapairy.cdf(x)

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function of the Map-Airy distribution.  See :ref:`Ctx.mapairy_cdf <Ctx_MapAiry_Cdf>` for formulas and examples.



.. method:: dist_mapairy.qtf(q)

    Returns `\text{qtf}(q)`, the value of the quantile function of the Map-Airy distribution.  See :ref:`Ctx.mapairy_qtf <Ctx_MapAiry_Qtf>` for formulas and examples.




|cr|

.. method:: dist_mapairy.sf(x)

    Returns `\text{sf}(x)`, the value of the survival function (:ref:`Sf <Dist_Sf>`) of the Map-Airy distribution. 

    .. math:: \text{sf}(x)  = \text{cdf}_X(-x)

    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.sf(x=0.5): ", Dist.qtf(x=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_mapairy.isf(q)

    Returns `\text{isf}(q)`, the value of the inverse survival function (:ref:`Isf <Dist_Isf>`) of the Map-Airy distribution. 

    .. math:: \text{isf}(q) = -\text{qtf}(q).

    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.isf(x=0.5): ", Dist.isf(x=0.5))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_mapairy.hf(x)

    Returns `\text{hazard}(x)`, the value of the hazard function (:ref:`Hf <Dist_Hf>`) of the Map-Airy distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_mapairy.chf(x)

    Returns `\text{chf}(x)`, the value of the cumulative hazard function (:ref:`Chf <Dist_Chf>`) of the Map-Airy distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.mode()

    Returns the :ref:`mode <Dist_Mode>` of the Map-Airy distribution. Since there is not one unique mode, ``Nan`` is returned.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.median()

    Returns the :ref:`median <Dist_Median>`  of the Map-Airy distribution. Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.


    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_mapairy.mean()

    Returns the  :ref:`mean <Dist_Mean>` (expected value) of the Map-Airy distribution. Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_mapairy.variance()

    Returns the :ref:`variance <Dist_Variance>` of the Map-Airy distribution. Calculated as `\displaystyle \tfrac{1}{8}(b-a)^2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.stdev()

    Returns the :ref:`standard deviation <Dist_Stdev>` of the Map-Airy distribution. Calculated as `\displaystyle \sqrt{ \tfrac{1}{8}(b-a)^2}`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.skewness()

    Returns the :ref:`skewness <Dist_Skewness>` of the Map-Airy distribution. Calculated as `\displaystyle 0`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.kurtosis()

    Returns the 'proper' :ref:`kurtosis <Dist_Kurtosis>` (normalized fourth moment) of the Map-Airy distribution. Calculated as `\displaystyle 3/2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.kurtosis_excess()

    Returns the :ref:`kurtosis excess <Dist_KurtosisExcess>` of the Map-Airy distribution. Calculated as `\displaystyle -3/2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.support_lower_endpoint()

    Returns the :ref:`support <Dist_Support_Lower_Endpoint>` of the Map-Airy distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.support_upper_endpoint()

    Returns the :ref:`support <Dist_Support_Upper_Endpoint>` of the Map-Airy distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.range_lower_endpoint()

    Returns the valid :ref:`range <Dist_Range_Lower_Endpoint>` of the Map-Airy distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_mapairy.range_upper_endpoint()

    Returns the valid :ref:`range <Dist_Range_Upper_Endpoint>` of the Map-Airy distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



















