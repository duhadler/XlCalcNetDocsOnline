

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}



Base class for univariate distributions
===============================================================================



.. py:class:: rv_base(rv_base)

    This is the base class, from which ``rv_continuous`` and ``rv_discrete`` inherit. There are no parameters and the  support interval is `(-\infty, \infty)`.


    The constructor has the following form:	   

    .. code-block:: python

        class rv_continuous(rv_base):
            __a = -mp.inf
            __b = +mp.inf

            def __init__(self, df):
                pass




.. _dist_cdf: 

Boost: Cumulative distribution function
-------------------------------------------------------------------------------


.. method:: rv_base.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`:

    See also Wikipedia :cite:p:`WikipediaDef05`.

    There are various ways to calculate a cdf. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_cdf_method(cdf_method)

    Sets the method to be used for the calculation of the cdf. ``cdf_method`` can take the following values:


    1.	"direct": this is the default if a closed form of the cdf exists, otherwise returns ``not implemented``.

    2.	"from_pdf": only for continuous functions for which the pdf is available in closed form, otherwise returns ``not implemented``.

    3.	"from_pmf": only for discrete functions, for which the pmf vector is available, otherwise returns ``not implemented``.

    4.	"from_charfunc": only for functions for which the characteristic is available in closed form, otherwise returns ``not implemented``.

    5.	"from_edgeworth": only if at least the first 2 cumulants exist, otherwise returns ``not implemented``.

    6.	"from_lug_rice": only if the cumulant generating function exists, otherwise returns ``not implemented``.

    There may be additional options for any particular function, which are documented in the decription of the function.




.. _dist_sf: 

Boost: Survival function
-------------------------------------------------------------------------------


.. method:: rv_base.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef08`.


    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _dist_hf: 

Hazard function
-------------------------------------------------------------------------------

.. method:: rv_continuous.hazard(x)

    Returns `\text{hazard}_X(x)`, the hazard function of a random variable `X`, defined as the ratio of the probability density function to the survival function.

    See also Wikipedia :cite:p:`WikipediaDef25`, BoostMath :cite:p:`BoostDef25`.


    .. math:: \text{hazard}_X(x) = \frac{\text{pdf}_X(x)}{\text{sf}_X(x)} = \frac{\text{pdf}_X(x)}{1-\text{cdf}_X(x)}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00







.. _dist_chf: 

Cumulative Hazard Function
-------------------------------------------------------------------------------


.. method:: rv_continuous.chf(x)

    Returns `\text{chf}_X(x)`, the cumulative function of a random variable `X`, defined as the ratio of the probability density function to the survival function.

    See also Wikipedia :cite:p:`WikipediaDef25`, BoostMath :cite:p:`BoostDef26`.


    .. math:: \text{chf}_X(x) =  = \int_{-\infty}^{x} \text{hazard}_X(x) \mathrm{d} t = -\log(1-\text{cdf}_X(x)).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _dist_qtf: 

Boost: Quantile function
-------------------------------------------------------------------------------

.. method:: rv_base.qtf(x)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`.

    .. math:: \text{qtf}_X(q) = \text{cdf}^{-1}_X(q).


    See also Wikipedia :cite:p:`WikipediaDef09`.


    There are various ways to calculate the quantile function. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_qtf_method(qtf_method)

    Sets the method to be used for the calculation of the cdf. ``qtf_method`` can take the following values:

    1.	"direct": this is the default if a closed form of the quantile function exists.

    2.	"from_cdf": this is the default if a closed form of the qtf does not exist.

    3.	"from_cornish_fisher": only if at least the first 2 cumulants exist, otherwise returns ``not implemented``.

    4.	"from_jensen": only if the cumulant generating function exists, otherwise returns ``not implemented``.

    There may be additional options for any particular function, which are documented in the decription of the function.



    .. code-block:: python

	    >>> from mpfunlab import *
	    >>> mp.dps = 30
	    >>> mu = 0; sigma = 1; t = 0.3; 
	    >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
	    6.3563523462564525615615615614561356E+00






.. _dist_isf: 

Boost: Inverse survival function
-------------------------------------------------------------------------------

.. method:: rv_base.isf(x)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef09`


    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00









.. _dist_mode: 

Boost: Mode
-------------------------------------------------------------------------------

.. method:: rv_base.mode()

    Returns the mode of the function.

    See also Wikipedia :cite:p:`WikipediaDef15`


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _dist_mean: 

Boost: Expected value (mean)
-------------------------------------------------------------------------------

.. method:: rv_base.mean()

    Returns the expected value (mean) of the function.

    See also Wikipedia :cite:p:`WikipediaDef07`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00







.. _dist_median: 

Boost: Median
-------------------------------------------------------------------------------

.. method:: rv_base.median()

    Returns the median of the function.

    See also Wikipedia :cite:p:`WikipediaDef16`


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00








.. _dist_variance: 

Boost: Variance
-------------------------------------------------------------------------------

.. method:: rv_base.variance()

    Returns the variance of the function.

    See also Wikipedia :cite:p:`WikipediaDef17`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _dist_stdev: 

Boost: Standard deviation
-------------------------------------------------------------------------------

.. method:: rv_base.stdev()

    Returns the Standard deviation of the function.

    See also Wikipedia :cite:p:`WikipediaDef18`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _dist_skewness: 

Boost: Skewness
-------------------------------------------------------------------------------

.. method:: rv_base.skewness()

    Returns the skewness of the function.

    See also Wikipedia :cite:p:`WikipediaDef19`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _dist_kurtosis: 

Boost: Kurtosis
-------------------------------------------------------------------------------

.. method:: rv_base.kurtosis()

    Returns the 'proper' kurtosis (normalized fourth moment) of the distribution dist.kurtosis `\mu_4 / \mu_2^2`, where `\mu_i` is the i'th central moment of the distribution, and in particular `\mu_2` is the variance of the distribution.

    See also  Wikipedia :cite:p:`WikipediaDef20`.


    The kurtosis is a measure of the "peakedness" of a distribution.

    Note that the literature definition of kurtosis is confusing. The definition used here is that used by for example Wolfram MathWorld (that includes a table of formulae for kurtosis excess for various distributions) but NOT the definition of kurtosis used by Wikipedia which treats "kurtosis" and "kurtosis excess" as the same quantity. 



    .. code-block:: pycon

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




.. _dist_kurtosisexcess: 

Boost: Kurtosis excess
-------------------------------------------------------------------------------

.. method:: rv_base.excess_kurtosis()


    Returns the kurtosis excess of the distribution dist. kurtosis excess = kurtosis - 3.

    See also  Wikipedia :cite:p:`WikipediaDef21`.


    The kurtosis excess is a measure of the "peakedness" of a distribution, and is more widely used than the "kurtosis proper". It is defined so that the kurtosis excess of a normal distribution is zero.

    This function may return a domain_error if the distribution does not have a defined kurtosis excess.

    Kurtosis excess can have a value from -2 to + infinity. 


    .. code-block:: pycon

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _Dist_Support_Lower_Endpoint:

Boost: Support, lower endpoint
-------------------------------------------------------------------------------

.. method:: Dist.support_lower_endpoint()

    Returns the lower endpoint of the support of the function.

    See also  Wikipedia :cite:p:`WikipediaDef14`.

    See also  https://en.wikipedia.org/wiki/Interval_(mathematics)


    The distribution is said to be 'supported' over a range that is "the smallest closed set whose complement has probability zero". Non-mathematicians might say it means the 'interesting' smallest range of random variate x that has the cdf going from zero to unity. Outside are uninteresting zones where the pdf is zero, and the cdf zero or unity. 


    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



.. _Dist_Support_Upper_Endpoint:

Boost: Support, upper endpoint
-------------------------------------------------------------------------------

.. method:: Dist.support_upper_endpoint()

    Returns the upper endpoint of the support of the function.

    See also  Wikipedia :cite:p:`WikipediaDef14`.

    See also  https://en.wikipedia.org/wiki/Interval_(mathematics)


    The distribution is said to be 'supported' over a range that is "the smallest closed set whose complement has probability zero". Non-mathematicians might say it means the 'interesting' smallest range of random variate x that has the cdf going from zero to unity. Outside are uninteresting zones where the pdf is zero, and the cdf zero or unity. 


    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





.. _Dist_Range_Lower_Endpoint:

Boost: Range, lower endpoint
-------------------------------------------------------------------------------

.. method:: Dist.range_lower_endpoint()

    Returns the lower endpoint of the valid range of the random variable.

    See also  Wikipedia :cite:p:`WikipediaDef14`.

    See also  https://en.wikipedia.org/wiki/Interval_(mathematics)

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






.. _Dist_Range_Upper_Endpoint:

Boost: Range, upper endpoint
-------------------------------------------------------------------------------

.. method:: Dist.range_upper_endpoint()

    Returns the upper endpoint of the valid range of the random variable.

    See also  Wikipedia :cite:p:`WikipediaDef14`.

    See also  https://en.wikipedia.org/wiki/Interval_(mathematics)

    .. code-block:: pycon

        >>> from mpfebnet import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






Characteristic function
-------------------------------------------------------------------------------

.. method:: rv_base.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`. 

    See also Wikipedia :cite:p:`WikipediaDef06`, Wikipedia :cite:p:`WikipediaDef07`.


    For a scalar random variable `X` the characteristic function is defined as the expected value of `e^{itX}`, where `i` is the imaginary unit, and `t \in \mathbb{R}` is the argument of the characteristic function:

    .. math:: C_X(t) = \operatorname{E} \left[ e^{itX} \right] =  \int_{-\infty}^{\infty} e^{itx} d \: \text{cdf}_X(x) =  \int_{-\infty}^{\infty} e^{itx} \text{pdf}_X(x) \mathrm{d} x =  \int_{0}^{1} e^{it \: \text{qtf}_X(p)} dp = M_X(it).

    Here `\text{cdf}_X(x)` is the cumulative distribution function of `X`, and the integral is of the Riemann–Stieltjes kind. If a random variable `X` has a probability density function `\text{pdf}_X(x)`, then the characteristic function is its Fourier transform with sign reversal in the complex exponential. `\text{qtf}_X(p)` is the quantile function of `X`, also known as the  inverse cumulative distribution function of `X` or the quantile function of `X`. `M_X(t)` is the moment generating function of `X`. Note that the characteristic function of a distribution always exists, even when the probability density function or moment-generating function do not.



    There are various ways to calculate the characteristic function. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_cf_method(qtf_method)

    Sets the method to be used for the calculation of the cdf. ``qtf_method`` can take the following values:



    1.	"direct": this is the default if a closed form of the characteristic function exists.

    2.	"from_pdf": only if the pdf is available in closed form, otherwise  returns ``not implemented``.

    3.	"from_qtf": only if the qtf  is available in closed form, otherwise  returns ``not implemented``.

    4.	"from_moments": only if the raw moments are available in closed form, otherwise  returns ``not implemented``.


    There may be additional options for any particular function, which are documented in the decription of the function.



    .. code-block:: python

	    >>> from mpfunlab import *
	    >>> mp.dps = 30
	    >>> mu = 0; sigma = 1; t = 0.3; 
	    >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
	    6.3563523462564525615615615614561356E+00





Moment generating function
-------------------------------------------------------------------------------


.. method:: rv_base.m_x(x)

    Returns `M_X(t)`, the moment generating function of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef10`.

    There are various ways to calculate the moment generating function. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_mgf_method(mgf_method)

    Sets the method to be used for the calculation of the mgf. ``mgf_method`` can take the following values:



    1.	"direct": this is the default if a closed form of the moment generating function exists.

    2.	"from_charfunc": only if the characteristic is available in closed form, otherwise  returns ``not implemented``.

    3.	"from_cgf": only if the moment generating function is available in closed form, otherwise  returns ``not implemented``.

    4.	"from_pgf": only for discrete distributions and only if the probability generating function  is available in closed form, otherwise  returns ``not implemented``.

    5.	"from_moments": only if the raw moments are available in closed form, otherwise  returns ``not implemented``.


    There may be additional options for any particular function, which are documented in the decription of the function.



    Related to the moment-generating function are a number of other transforms that are common in probability theory: 





Cumulant generating function
-------------------------------------------------------------------------------

.. method:: rv_base.k_x(x)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef11`.


    There are various ways to calculate the cumulant generating function. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_cgf_method(cgf_method)

    Sets the method to be used for the calculation of the cgf. ``cgf_method`` can take the following values:



    1.	"direct": this is the default if a closed form of the moment generating function exists.

    2.	"from_charfunc": only if the characteristic function is available in closed form, otherwise  returns ``not implemented``.

    3.	"from_mgf": only if the moment generating function is available in closed form, otherwise  returns ``not implemented``.

    4.	"from_pgf": only for discrete distributions and only if the probability generating function  is available in closed form, otherwise  returns ``not implemented``.

    5.	"from_cumulants": only if the cumulants are available in closed form, otherwise  returns ``not implemented``.


    There may be additional options for any particular function, which are documented in the decription of the function.












Raw Moments
-------------------------------------------------------------------------------

.. method:: rv_base.raw_moments(k)


    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef13`


    There are various ways to calculate the raw moments. Ideally, they are available in closed from and can be calculated directly, or there is are dedicated functions to calculate them. If this is not the case, then one of the options given below can be used. There is no method which is always best.


.. method:: rv_base.set_moments_method(moments_method)

    Sets the method to be used for the calculation of the  raw moments. ``moments_method`` can take the following values:


    1.	"direct": this is the default if a closed form of the cdf exists, otherwise returns ``not implemented``.

    2.	"from_pdf": only for continuous functions for which the pdf is available in closed form, otherwise returns ``not implemented``.

    3.	"from_pmf": only for discrete functions, for which the pmf vector is available, otherwise returns ``not implemented``.


    4.	"from_cumulants": only if the cumulants are available in closed form, otherwise  returns ``not implemented``.


    5.	"from_mgf": only for functions for which the moment generating function is available in closed form, otherwise returns ``not implemented``.


    6.	"from_charfunc": only for functions for which the characteristic function is available in closed form, otherwise returns ``not implemented``.


    7.	"from_pgf": only for discrete distributions and only for functions for which the moment generating function is available in closed form, otherwise returns ``not implemented``.

    There may be additional options for any particular function, which are documented in the decription of the function.







Central Moments
-------------------------------------------------------------------------------

.. method:: rv_base.central_moments(k)

    Returns the first `j` central moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef11`


    There are various ways to calculate the central moments. Ideally, they are available in closed from and can be calculated directly, or there is are dedicated functions to calculate them. If this is not the case, then one of the options given below can be used. There is no method which is always best.


.. method:: rv_base.set_central_moments_method(central_moments_method)

    Sets the method to be used for the calculation of the central_moments_method. ``central_moments_method`` can take the following values:


    1.	"direct": this is the default if a closed form of the cdf exists, otherwise returns ``not implemented``.

    2.	"from_raw_moments": only if the raw moments are available in closed form, otherwise  returns ``not implemented``.

    3.	"from_cumulants": only if the cumulants are available in closed form, otherwise  returns ``not implemented``.

    4.	"from_pdf": calculates the raw moments from the pdf, the converts the raw moments to the central moments.


    There may be additional options for any particular function, which are documented in the decription of the function.








Cumulants
-------------------------------------------------------------------------------

.. method:: rv_base.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef11`


    There are various ways to calculate the cumulants. Ideally, they are available in closed from and can be calculated directly, or there is are dedicated functions to calculate them. If this is not the case, then one of the options given below can be used. There is no method which is always best.


.. method:: rv_base.set_cumulants_method(cumulants_method)

    Sets the method to be used for the calculation of the cumulants. ``cumulants_method`` can take the following values:


    1.	"direct": this is the default if a closed form of the cdf exists, otherwise returns ``not implemented``.

    2.	"from_moments": only if the moments are available in closed form, otherwise  returns ``not implemented``.

    3.	"from_cgf": only for functions for which the moment generating function is available in closed form, otherwise returns ``not implemented``.


    There may be additional options for any particular function, which are documented in the decription of the function.







