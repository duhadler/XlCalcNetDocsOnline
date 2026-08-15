

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}


|newpage|

Base class for continuous univariate distributions
===============================================================================



.. py:class:: rv_continuous(rv_base)

    The base continuous probability distribution class, which inherits from ``rv_base``. There are no parameters and the  support interval is `(-\infty, \infty)`.


    The constructor has the following form:	   

    .. code-block:: python

        class rv_continuous(rv_base):
            __a = -mp.inf
            __b = +mp.inf

            def __init__(self, df):
                pass




.. _dist_pdf: 

Probability density function
-------------------------------------------------------------------------------

.. method:: rv_continuous.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`:

    See also Wikipedia :cite:p:`WikipediaDef23`.

    There are various ways to calculate a pdf. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_pdf_method(pdf_method)

    Sets the method to be used for the calculation of the pdf. ``pdf_method`` can take the following values:


    1.	"direct": this is the default if a closed form of the cdf exists, otherwise returns ``not implemented``.

    2.	"from_cdf": only for continuous functions for which the pdf is available in closed form, otherwise returns ``not implemented``.

    3.	"from_charfunc": only for functions for which the characteristic is available in closed form, otherwise returns ``not implemented``.

    4.	"from_edgeworth": only if at least the first 2 cumulants exist, otherwise returns ``not implemented``.

    5.	"from_lug_rice": only if the cumulant generating function exists, otherwise returns ``not implemented``.

    There may be additional options for any particular function, which are documented in the decription of the function.










Probability sparsity function
-------------------------------------------------------------------------------

.. method:: rv_continuous.psf(x)

    Returns `\text{psf}_X(x)`, the probability sparsity function (psf), which is the derivative of the quantile function (qtf).

    See also Wikipedia :cite:p:`WikipediaDef09`, Wikipedia :cite:p:`WikipediaDef24`.


    The probability sparsity function can be calculated using the probability density function (pdf) and the qtf:

    .. math :: \text{psf}_X(q) = \frac{\mathrm{d}}{\mathrm{d}q} \text{qtf}_X(q) = \frac{1}{\text{pdf}_X(\text{qtf}_X(q))}


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00











Differerential entropy
-------------------------------------------------------------------------------

.. method:: rv_continuous.entropy(x)

    Returns `\text{entropy}_X(x)`, the differential entropy of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef27`




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00









Negative loglikelihood function
-------------------------------------------------------------------------------

See also Wikipedia :cite:p:`WikipediaDef28`

.. method:: rv_continuous.nnlf(x)

    Returns `\text{nnlf}_X(x)`, the negative loglikelihood function of a random variable `X`:

    .. math:: \text{nnlf}_X(x) = -\sum(\log \text{pdf}_X(x, \theta), axis=0),

    where theta are the parameters (including loc and scale).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00






Logarithm of the probability density function
-------------------------------------------------------------------------------

.. method:: rv_continuous.logpdf(x)

    Returns `\text{logpdf}_X(x)`, the logarithm of the probability density function (pdf) of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef23`


    .. math:: \text{logpdf}_X(x) = \log(\text{pdf}_X(x))


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00



