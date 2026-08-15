

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Base class for discrete univariate distributions
===============================================================================


.. py:class:: rv_discrete(rv_base)

    The base discrete probability distribution class, which inherits from ``rv_base``. There are no parameters and the  support interval is `(-\infty, \infty)`.


    The constructor has the following form:	   

    .. code-block:: python

        class rv_continuous(rv_base):
            __a = -mp.inf
            __b = +mp.inf

            def __init__(self, df):
                pass


.. _dist_pmf: 

Probability mass function
-------------------------------------------------------------------------------

.. method:: rv_discrete.pmf(x)


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef29`.


    There are various ways to calculate a pmf. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_pmf_method(pmf_method)

    Sets the method to be used for the calculation of the pmf. ``pmf_method`` can take the following values:


    1.	"direct": this is the default if a closed form of the cdf exists, otherwise returns ``not implemented``.

    2.	"from_pmf_vector": only for discrete functions for which the pmf vector is available in polynomial time, otherwise returns ``not implemented``.

    3.	"from_charfunc": only for functions for which the characteristic is available in closed form, otherwise returns ``not implemented``.

    4.	"from_edgeworth": only if at least the first 2 cumulants exist, otherwise returns ``not implemented``.

    5.	"from_lug_rice": only if the cumulant generating function exists, otherwise returns ``not implemented``.

    There may be additional options for any particular function, which are documented in the decription of the function.









Probability generating function
-------------------------------------------------------------------------------

See also Wikipedia :cite:p:`WikipediaDef30`.

.. method:: rv_discrete.pgf(x)

    Returns `\text{pgf}_X(x)`, the probability generating function (pgf) of a discrete random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef30`.


    It is a power series representation (the generating function) of the probability mass function of the random variable.

    If `X` is a discrete random variable taking values in the non-negative integers `\{0,1, ...\}`, then the probability generating function of X is defined as 

    .. math:: G(z)=\operatorname {E} (z^{X})=\sum _{x=0}^{\infty }p(x)z^{x},

    where `p` is the probability mass function of X. Note that the subscripted notations `G_X` and `p_X` are often used to emphasize that these pertain to a particular random variable `X`, and to its distribution. The power series converges absolutely at least for all complex numbers `z` with `|z| \le 1`; in many examples the radius of convergence is larger. 

    The probability-generating function is related to the moment-generating function by

    .. math::  G_{X}(e^{t}) =  M_{X}(t); \quad  G(t) =  M_{X}(\log(t)).


    There are various ways to calculate a pgf. Ideally, it is available in closed from and can be calculated directly, or there is are dedicated functions to calculate it. If this is not the case, then one of the options given below can be used. There is no method which is always best, and the choice depends not only on the function, but also on the values of the argument and the parameters.


.. method:: rv_base.set_pgf_method(pgf_method)

    Sets the method to be used for the calculation of the pgf. ``pgf_method`` can take the following values:


    1.	"direct": this is the default if a closed form of the cdf exists, otherwise returns ``not implemented``.

    2.	"from_pmf_vector": only for discrete functions for which the pmf vector is available in polynomial time, otherwise returns ``not implemented``.

    3.	"from_charfunc": only for functions for which the characteristic function is available in closed form, otherwise returns ``not implemented``.

    4.	"from_mgf": only for functions for which the moment generating function is available in closed form, otherwise returns ``not implemented``.

    5.	"from_mgf": only for functions for which the moment generating function is available in closed form, otherwise returns ``not implemented``.


    There may be additional options for any particular function, which are documented in the decription of the function.





Vector containing all values of the pmf
-------------------------------------------------------------------------------

.. method:: rv_discrete.pmfvec(x)

    Returns a vector containing all values of the pmf. This is useful is such a vector is cheap to compute, and further operations (like convolutions) are required.

    See also Wikipedia :cite:p:`WikipediaDef29`.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00








Entropy
-------------------------------------------------------------------------------

.. method:: rv_discrete.entropy(x)

    Returns `\text{entropy}_X(x)`, the entropy of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef27`.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00







Logarithm of the probability mass function
-------------------------------------------------------------------------------

.. method:: rv_discrete.logpmf(x)


    Returns `\text{logpmf}_X(x)`, the logarithm of the probability mass function (pmf) of a random variable `X`.

    See also Wikipedia :cite:p:`WikipediaDef29`.


    .. math:: \text{logpmf}_X(x) = \log(\text{pmf}_X(x))



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", chi_squared(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00





