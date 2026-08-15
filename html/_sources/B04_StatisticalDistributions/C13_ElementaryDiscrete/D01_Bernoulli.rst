

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}









Boost: Bernoulli distribution
-------------------------------------------------------------------------------


The following functions return the pmf, cdf, qtf or boost class of the Bernoulli distribution 

The Bernoulli distribution is a discrete distribution of the outcome of a single trial with only two results, 0 (failure) or 1 (success), with a probability of success p.

The Bernoulli distribution is the simplest building block on which other discrete distributions of sequences of independent Bernoulli trials can be based.

The Bernoulli is the binomial distribution (k = 1, p) with only one trial.

The domain of the random variable is 0 and 1, and the useful supported range is only 0 or 1.

The support interval for `k` is `{0, 1}`, and `0 \le q \le 1`.

The Bernoulli distribution is implemented here as a strict discrete distribution. If a generalised version, allowing k to be any real, is required then the binomial distribution with a single trial should be used, for example:

binomial_distribution(1, 0.25)


!!! The following references need to be updated: !!!

See also   Wikipedia :cite:p:`WikipediaDis31`, MathWorld :cite:p:`WolframDis31`,  BoostMath :cite:p:`BoostDis31` .



|cr|

.. _Ctx_BernoulliPmf:

.. method:: Ctx.bernoulli_pmf(k, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{pmf}(x)`, the value of the probability mass function (:ref:`Pmf <Dist_Pmf>`) of the Bernoulli distribution. It is calculated using the relation `\text{pmf}(k) = 1 - p` for `k = 0`, else `p`.

    The following example shows both forms of the syntax: 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BernoulliPdf(x, a, b): ", BernoulliPdf(x, a, b))
        >>> print ("dist_bernoulli(a, b).pdf(x): ", dist_bernoulli(a, b).pdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BernoulliCdf:

.. method:: Ctx.bernoulli_cdf(k, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function (:ref:`Cdf <Dist_Cdf>`) of the Bernoulli distribution. It is calculated using the relation `\text{cdf}(k) = 1 - p` for `k = 0`, else `1`.


    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; x = 0.6;
        >>> print ("BernoulliCdf(x, a, b): ", BernoulliCdf(x, a, b))
        >>> print ("dist_bernoulli(a, b).cdf(x): ", dist_bernoulli(a, b).cdf(x))
        6.3563523462564525615615615614561356E+00



|cr|

.. _Ctx_BernoulliQtf:

.. method:: Ctx.bernoulli_qtf(q, p)

    where ``Ctx`` is ``Math53`` or ``CtxBoost``.

    Returns `\text{qtf}(q)`, the value of the quantile function (:ref:`Qtf <Dist_Qtf>`) of the Bernoulli distribution.  It is calculated using the relation `\text{qtf}(k) = 0` for `k \le (1-p)`, else `1`.

    The following example shows both forms of the syntax:

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> a = 0; b = 1; t = 0.3; q = 0.6;
        >>> print ("BernoulliQtf(q, a, b): ", BernoulliQtf(q, a, b))
        >>> print ("dist_bernoulli(a, b).qtf(q): ", dist_bernoulli(a, b).qtf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: CtxBoost.dist_bernoulli(p)

    Returns an ``dist_bernoulli`` object, which gives access to the functions descibed below:

    .. code-block:: pycon

        >>> from mpfebnet import SReal, FReal, XReal, QReal, CReal, OReal
        >>> a = 0; b = 1; 
        >>> Ctx = SReal
        >>> dist_bernoulli = Ctx.dist_bernoulli(a, b)
        >>> print ("Dist.qtf(q=0.5): ", Dist.qtf(q=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_bernoulli.pmf(x)

    Returns `\text{pdf}(x)`, the value of the probability density function of the Bernoulli distribution. See :ref:`Ctx.BernoulliPmf <Ctx_BernoulliPmf>` for formulas and examples.



.. method:: dist_bernoulli.cdf(x)

    Returns `\text{cdf}(x)`, the value of the cumulative distribution function of the Bernoulli distribution.  See :ref:`Ctx.BernoulliCdf <Ctx_BernoulliCdf>` for formulas and examples.



.. method:: dist_bernoulli.qtf(q)

    Returns `\text{qtf}(q)`, the value of the quantile function of the Bernoulli distribution.  See :ref:`Ctx.BernoulliQtf <Ctx_BernoulliQtf>` for formulas and examples.




|cr|

.. method:: dist_bernoulli.sf(x)

    Returns `\text{sf}(x)`, the value of the survival function (:ref:`Sf <Dist_Sf>`) of the Bernoulli distribution. It is calculated using the relation `\text{sf}(k) = p` for `k = 0`, else `0`.

    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.sf(x=0.5): ", Dist.qtf(x=0.5))
        6.3563523462564525615615615614561356E+00



.. method:: dist_bernoulli.isf(q)

    Returns `\text{isf}(q)`, the value of the inverse survival function (:ref:`Isf <Dist_Isf>`) of the Bernoulli distribution. It is calculated using the relation `\text{qtf}(k) = 1` for `k \le (1-p)`, else `0`.

    .. code-block:: pycon

        >>> # continued from above
        >>> print ("Dist.isf(x=0.5): ", Dist.isf(x=0.5))
        6.3563523462564525615615615614561356E+00







|cr|

.. method:: dist_bernoulli.hf(x)

    Returns `\text{hazard}(x)`, the value of the hazard function (:ref:`Hf <Dist_Hf>`) of the Bernoulli distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_bernoulli.chf(x)

    Returns `\text{chf}(x)`, the value of the cumulative hazard function (:ref:`Chf <Dist_Chf>`) of the Bernoulli distribution. 

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.mode()

    Returns the :ref:`mode <Dist_Mode>` of the Bernoulli distribution, which is `0` if `(p < 0.5)` else `1`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.median()

    Returns the :ref:`median <Dist_Median>`  of the Bernoulli distribution. Calculated as `\displaystyle tbd`.


    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_bernoulli.mean()

    Returns the  :ref:`mean <Dist_Mean>` (expected value) of the Bernoulli distribution, which is `p`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_bernoulli.variance()

    Returns the :ref:`variance <Dist_Variance>` of the Bernoulli distribution. Calculated as `\displaystyle p (1-p)`.


    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.stdev()

    Returns the :ref:`standard deviation <Dist_Stdev>` of the Bernoulli distribution. Calculated as `\displaystyle \sqrt{p (1-p)}`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.skewness()

    Returns the :ref:`skewness <Dist_Skewness>` of the Bernoulli distribution. Calculated as `\displaystyle (1-2p)/\sqrt{p(1-p)}`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.kurtosis()

    Returns the 'proper' :ref:`kurtosis <Dist_Kurtosis>` (normalized fourth moment) of the Bernoulli distribution. Calculated as `\displaystyle 3+(1-6p(1-p))/(p(1-p))`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.kurtosis_excess()

    Returns the :ref:`kurtosis excess <Dist_KurtosisExcess>` of the Bernoulli distribution. Calculated as `\displaystyle (1-6p(1-p))/(p(1-p))`.

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.support_lower_endpoint()

    Returns the :ref:`support <Dist_Support_Lower_Endpoint>` of the Bernoulli distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00


|cr|

.. method:: dist_bernoulli.support_upper_endpoint()

    Returns the :ref:`support <Dist_Support_Upper_Endpoint>` of the Bernoulli distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_bernoulli.range_lower_endpoint()

    Returns the valid :ref:`range <Dist_Range_Lower_Endpoint>` of the Bernoulli distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_bernoulli.range_upper_endpoint()

    Returns the valid :ref:`range <Dist_Range_Upper_Endpoint>` of the Bernoulli distribution as a tuple (left, right).

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





























