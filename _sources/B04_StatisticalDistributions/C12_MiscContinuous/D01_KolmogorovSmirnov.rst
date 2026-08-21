

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}








Boost: Kolmogorov-Smirnov distribution (limiting form)
-------------------------------------------------------------------------------


Returns the pdf, cdf, qtf or boost class of a random variable `X`, following the limiting form of the Kolmogorov distribution with parameters `n > 0` and the support interval  `[0, \infty)`. 


!!! The following references need to be updated: !!!


See also  Wikipedia :cite:p:`WikipediaDis08`, MathWorld :cite:p:`WolframDis08`,  BoostMath :cite:p:`BoostDis08`, :cite:t:`Ehrhardt2018` (3.9.2).



|cr|

.. _Ctx_KolmogorovSmirnov_Pdf:

.. method:: Ctx.kolmogorov_smirnov_pdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.


    Returns the pdf of the limiting form of the Kolmogorov distribution, for `x \in [0, \infty)`. 

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BetaPdf(x, a, b): ", BetaPdf(x, a, b))
        >>> print ("dist_beta(a, b).pdf(x): ", dist_beta(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_KolmogorovSmirnov_Cdf:

.. method:: Ctx.kolmogorov_smirnov_cdf(x, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\displaystyle \mathrm{KF}(x) = 1-2\sum_{k=1}^{\infty}(-1)^k e^{-2k^2x^2}`, the CDF of the limiting form of the Kolmogorov distribution, for `x \in [0, \infty)`. 

    See also  :cite:t:`Ehrhardt2018` (3.9.14).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BetaCdf(x, a, b): ", BetaCdf(x, a, b))
        >>> print ("dist_beta(a, b).cdf(x): ", dist_beta(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_KolmogorovSmirnov_Qtf:

.. method:: Ctx.kolmogorov_smirnov_qtf(q, a=0, b=1)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.


    Returns `\mathrm{KF}^{-1}(x)`, the functional inverse of the CDF of the Kolmogorov distribution (limiting form), ie `\mathrm{KF}(\mathrm{KF}^{-1}(x)) = x`.


    See also  :cite:t:`Ehrhardt2018` (3.9.14).


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("BetaQtf(q, a, b): ", BetaQtf(q, a, b))
        >>> print ("dist_beta(a, b).qtf(q): ", dist_beta(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: CtxBoost.dist_kolmogorov_smirnov(a=0, b=1)

    Returns an ``dist_kolmogorov_smirnov`` object, which gives access to the functions descibed below:

    .. code-block:: pycon

        >>> from xlcalcnet import SReal, FReal, ereal, QReal, CReal, OReal
        >>> a = 0; b = 1; 
        >>> Ctx = SReal
        >>> dist_beta = Ctx.dist_beta(a, b)
        >>> print ("Dist.qtf(q=0.5): ", Dist.qtf(q=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_kolmogorov_smirnov.pdf(x)

    Returns `\text{pdf}(x)`, the value of the probability density function of the Kolmogorov distribution (limiting form). See :ref:`Ctx.kolmogorov_smirnov_pdf <Ctx_KolmogorovSmirnov_Pdf>` for formulas and examples.



.. method:: dist_kolmogorov_smirnov.cdf(x)

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function of the Kolmogorov distribution (limiting form).  See :ref:`Ctx.kolmogorov_smirnov_cdf <Ctx_KolmogorovSmirnov_Cdf>` for formulas and examples.



.. method:: dist_kolmogorov_smirnov.qtf(q)

    Returns `\text{qtf}(q)`, the value of the quantile function of the Kolmogorov distribution (limiting form).  See :ref:`Ctx.kolmogorov_smirnov_qtf <Ctx_KolmogorovSmirnov_Qtf>` for formulas and examples.




|cr|

.. method:: dist_kolmogorov_smirnov.sf(x)

    Returns `\text{sf}(x)`, the value of the survival function (:ref:`Sf <Dist_Sf>`) of the Kolmogorov distribution (limiting form). 


    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.sf(x=0.5): ", Dist.qtf(x=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_kolmogorov_smirnov.isf(q)

    Returns `\text{isf}(q)`, the value of the inverse survival function (:ref:`Isf <Dist_Isf>`) of the Kolmogorov distribution (limiting form). 



    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.isf(x=0.5): ", Dist.isf(x=0.5))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.hf(x)

    Returns `\text{hazard}(x)`, the value of the hazard function (:ref:`Hf <Dist_Hf>`) of the Kolmogorov distribution (limiting form). 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_kolmogorov_smirnov.chf(x)

    Returns `\text{chf}(x)`, the value of the cumulative hazard function (:ref:`Chf <Dist_Chf>`) of the Kolmogorov distribution (limiting form). 

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.mode()

    Returns the :ref:`mode <Dist_Mode>` of the Kolmogorov distribution (limiting form). Since there is not one unique mode, ``Nan`` is returned.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.median()

    Returns the :ref:`median <Dist_Median>`  of the Kolmogorov distribution (limiting form). Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.


    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_kolmogorov_smirnov.mean()

    Returns the  :ref:`mean <Dist_Mean>` (expected value) of the Kolmogorov distribution (limiting form). Calculated as `\displaystyle \tfrac{1}{2}(a+b)`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_kolmogorov_smirnov.variance()

    Returns the :ref:`variance <Dist_Variance>` of the Kolmogorov distribution (limiting form). Calculated as `\displaystyle \tfrac{1}{8}(b-a)^2`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.stdev()

    Returns the :ref:`standard deviation <Dist_Stdev>` of the Kolmogorov distribution (limiting form). Calculated as `\displaystyle \sqrt{ \tfrac{1}{8}(b-a)^2}`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.skewness()

    Returns the :ref:`skewness <Dist_Skewness>` of the Kolmogorov distribution (limiting form). Calculated as `\displaystyle 0`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.kurtosis()

    Returns the 'proper' :ref:`kurtosis <Dist_Kurtosis>` (normalized fourth moment) of the Kolmogorov distribution (limiting form). Calculated as `\displaystyle 3/2`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.kurtosis_excess()

    Returns the :ref:`kurtosis excess <Dist_KurtosisExcess>` of the Kolmogorov distribution (limiting form). Calculated as `\displaystyle -3/2`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.support_lower_endpoint()

    Returns the :ref:`support <Dist_Support_Lower_Endpoint>` of the Kolmogorov distribution (limiting form) as a tuple (left, right).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.support_upper_endpoint()

    Returns the :ref:`support <Dist_Support_Upper_Endpoint>` of the Kolmogorov distribution (limiting form) as a tuple (left, right).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.range_lower_endpoint()

    Returns the valid :ref:`range <Dist_Range_Lower_Endpoint>` of the Kolmogorov distribution (limiting form) as a tuple (left, right).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_kolmogorov_smirnov.range_upper_endpoint()

    Returns the valid :ref:`range <Dist_Range_Upper_Endpoint>` of the Kolmogorov distribution (limiting form) as a tuple (left, right).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00
















