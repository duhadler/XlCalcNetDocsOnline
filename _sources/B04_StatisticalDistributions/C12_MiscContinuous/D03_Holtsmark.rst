

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|





Boost: Holtsmark distribution
-------------------------------------------------------------------------------


The Holtsmark distribution is a stable distribution (see Wikipedia :cite:p:`WikipediaDis94`) with the shape parameters `\alpha=3/2, \beta=0`. The Holtsmark distribution is linear with respect to the location parameter `\mu` and scale parameter `c`.

.. math:: p(x_1; \mu_1, c_1) = p \left(x :=  \frac{x_1 - \mu_1}{c_1}; \mu:=0, c := 1  \right) \cdot \frac{1}{c_1}.

The support interval is `(-\infty,+\infty)`.


!!! The following references need to be updated: !!!



See also: https://www.boost.org/doc/libs/1_89_0/libs/math/doc/html/math_toolkit/dist_ref/dists/holtsmark_dist.html

See also: https://en.wikipedia.org/wiki/Holtsmark_distribution




|cr|

.. _Ctx_Holtsmark_Pdf:

.. method:: Ctx.holtsmark_pdf(x, m, n)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following an Holtsmark distribution

    .. math:: \text{pdf}_X(x) =\frac{1}{2\pi} \int_{-\infty}^{\infty} \exp \left ( i t \mu - |c t|^{3/2}  \right ) e^{i x t} \mathrm{d}t,



    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("FisherFPdf(x, a, b): ", FisherFPdf(x, a, b))
        >>> print ("dist_fisher_f(a, b).pdf(x): ", dist_fisher_f(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_Holtsmark_Cdf:

.. method:: Ctx.holtsmark_cdf(x, m, n)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.


    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an Holtsmark distribution.




    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("FisherFCdf(x, a, b): ", FisherFCdf(x, a, b))
        >>> print ("dist_fisher_f(a, b).cdf(x): ", dist_fisher_f(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_Holtsmark_Qtf:

.. method:: Ctx.holtsmark_qtf(q, m, n)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Holtsmark distribution.


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("FisherFQtf(q, a, b): ", FisherFQtf(q, a, b))
        >>> print ("dist_fisher_f(a, b).qtf(q): ", dist_fisher_f(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: CtxBoost.dist_holtsmark(m, n)

    Returns an ``dist_holtsmark`` object, which gives access to the functions descibed below:

    .. code-block:: pycon

        >>> from mpfebnet import SReal, FReal, XReal, QReal, CReal, OReal
        >>> a = 0; b = 1; 
        >>> Ctx = SReal
        >>> dist_fisher_f = Ctx.dist_fisher_f(a, b)
        >>> print ("Dist.qtf(q=0.5): ", Dist.qtf(q=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_holtsmark.pdf(x)

    Returns `\text{pdf}(x)`, the value of the probability density function of the Holtsmark distribution. See :ref:`Ctx.holtsmark_pdf <Ctx_Holtsmark_Pdf>` for formulas and examples.



.. method:: dist_holtsmark.cdf(x)

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function of the Holtsmark distribution.  See :ref:`Ctx.holtsmark_cdf <Ctx_Holtsmark_Cdf>` for formulas and examples.



.. method:: dist_holtsmark.qtf(q)

    Returns `\text{qtf}(q)`, the value of the quantile function of the Holtsmark distribution.  See :ref:`Ctx.holtsmark_qtf <Ctx_Holtsmark_Qtf>` for formulas and examples.




|cr|

.. method:: dist_holtsmark.sf(x)

    Returns `\text{sf}(x)`, the value of the survival function (:ref:`Sf <Dist_Sf>`) of the Holtsmark distribution. 

    .. math:: 
        \text{sf}(x) =\begin{cases}
        \text{ibeta}(n/2, m/2, n/(n+mx)), & mx > n,\\
        \text{ibetac}(m/2, n/2, mx/(n+mx)) & mx \le n.
        \end{cases}

    Here `\text{ibeta}(\cdot)` denotes the real normalised incomplete beta function (:ref:`RealIBeta <rst_mpm_ibeta>`), and `\text{ibetac}(\cdot)` denotes the real normalised complementary incomplete beta function (:ref:`RealIBetac <rst_mpm_ibetac>`).


    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.sf(x=0.5): ", Dist.qtf(x=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_holtsmark.isf(q)

    Returns `\text{isf}(q)`, the value of the inverse survival function (:ref:`Isf <Dist_Isf>`) of the Holtsmark distribution. 

    .. math:: \text{isf}(q) = \frac{nx}{m(1-x)}, \quad \text{where } x = \mathrm{ibetac\_inv}(m/2, n/2, q).

    Here `\mathrm{ibetac\_inv}(\cdot)` denotes the inverse of the real normalised complementary incomplete beta function (:ref:`RealIBetacInv <rst_mpm_real_ibetac_inv>`).

    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.isf(x=0.5): ", Dist.isf(x=0.5))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.hf(x)

    Returns `\text{hazard}(x)`, the value of the hazard function (:ref:`Hf <Dist_Hf>`) of the Holtsmark distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_holtsmark.chf(x)

    Returns `\text{chf}(x)`, the value of the cumulative hazard function (:ref:`Chf <Dist_Chf>`) of the Holtsmark distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.mode()

    Returns the :ref:`mode <Dist_Mode>` of the Holtsmark distribution. Since there is not one unique mode, ``Nan`` is returned.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.median()

    Returns the :ref:`median <Dist_Median>`  of the Holtsmark distribution. Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.


    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_holtsmark.mean()

    Returns the  :ref:`mean <Dist_Mean>` (expected value) of the Holtsmark distribution. Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_holtsmark.variance()

    Returns the :ref:`variance <Dist_Variance>` of the Holtsmark distribution. Calculated as `\displaystyle \tfrac{1}{8}(b-a)^2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.stdev()

    Returns the :ref:`standard deviation <Dist_Stdev>` of the Holtsmark distribution. Calculated as `\displaystyle \sqrt{ \tfrac{1}{8}(b-a)^2}`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.skewness()

    Returns the :ref:`skewness <Dist_Skewness>` of the Holtsmark distribution. Calculated as `\displaystyle 0`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.kurtosis()

    Returns the 'proper' :ref:`kurtosis <Dist_Kurtosis>` (normalized fourth moment) of the Holtsmark distribution. Calculated as `\displaystyle 3/2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.kurtosis_excess()

    Returns the :ref:`kurtosis excess <Dist_KurtosisExcess>` of the Holtsmark distribution. Calculated as `\displaystyle -3/2`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.support_lower_endpoint()

    Returns the :ref:`support <Dist_Support_Lower_Endpoint>` of the Holtsmark distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.support_upper_endpoint()

    Returns the :ref:`support <Dist_Support_Upper_Endpoint>` of the Holtsmark distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_holtsmark.range_lower_endpoint()

    Returns the valid :ref:`range <Dist_Range_Lower_Endpoint>` of the Holtsmark distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_holtsmark.range_upper_endpoint()

    Returns the valid :ref:`range <Dist_Range_Upper_Endpoint>` of the Holtsmark distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00
























