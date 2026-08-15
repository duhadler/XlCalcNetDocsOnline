

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_student_t_2nc: 

Doubly non-central Student `t` distribution
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_student_t_2nc(n, delta, theta)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The doubly non-central Student `t` distribution is a continuous probability distribution with `n>0` degrees of freedom, noncentrality parameters `\delta` and `\theta`, and support interval `(-\infty, +\infty)`.
    See also :cite:t:`Broda2007`, :cite:t:`Kocherlakota1991`, :cite:t:`Paolella2006`, :cite:t:`Paolella2007`, :cite:t:`Gessner2014`,





|cr|

.. method:: dist_student_t_2nc.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following a 
    doubly non-central Student t distribution:

    .. math:: \text{pdf}_X(x) = f_{t''}(t;n;\mu,\theta) = \sum_{i=0}^{\infty} \omega_{i,\theta} s_{i,n} f_{t'}(s_{i,n} x;n+2i,\mu), 

    where `f_{t'}(\cdot)` denotes the PDF of the singly noncentral `t`-distribution, and

    .. math:: \omega_{i,\theta} = \frac{\exp(-\theta/2)(\theta/2)^i}{i!}  \quad \text{and}  \quad s_{i,n}=\sqrt{\frac{n+2i}{n}}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", student_t_2nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_student_t_2nc.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a doubly non-central Student t distribution:

    .. math:: \text{cdf}_X(x) = F_{t''}(x;n;\mu,\theta) =  \int_{0}^{x} f_{t''}(x;n;\mu,\theta) \mathrm{d} t = \sum_{i=0}^{\infty} \omega_{i,\theta} s_{i,n} F_{t'}(s_{i,n} x;n+2i,\mu),

    where `F_{t'}(\cdot)` denotes the CDF of the singly noncentral `t`-distribution, and

    .. math:: \omega_{i,\theta} = \frac{\exp(-\theta/2)(\theta/2)^i}{i!}  \quad \text{and}  \quad s_{i,n}=\sqrt{\frac{n+2i}{n}}.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", student_t_2nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_student_t_2nc.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a doubly non-central Student t distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{\infty} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", student_t_2nc(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_student_t_2nc.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a doubly non-central Student t distribution:

    There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: 
    It is computed using Newton iterations with starting values from a singly noncentral `t` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", student_t_2nc(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t_2nc.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a doubly non-central Student t distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", student_t_2nc(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t_2nc.c_x(t)

Returns `C_X(t)`, the characteristic function of a random variable `X`, following a doubly non-central Student t distribution:

.. math:: C_X(t) = \int_{-\infty}^{\infty} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


.. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; t = 0.3; 
    >>> print ("c_x: ", student_t_2nc(mu, sigma).c_x(t))
    6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_student_t_2nc.m_x(t)

    Returns ``NaN``, since the moment generating function does not exist.




|cr|

.. method:: dist_student_t_2nc.k_x(t, k = 0)

    Returns ``NaN``, since the cumulant generating function does not exist.





|cr|

.. method:: dist_student_t_2nc.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, 
    following a doubly non-central Student t distribution. The rth moment only exists for `n > r` and is given by


    .. math:: \mu'_X(r) = \left({\tfrac{1}{2}n}\right)^{r/2} \frac{\Gamma\left(\tfrac{1}{2}(n-r)\right)}{\Gamma\left(\tfrac{1}{2}n\right)} \times {}_1F_1(\tfrac{1}{2}r, \tfrac{1}{2}n, -\tfrac{1}{2}\theta)  \times \sum_{i=0}^{\lfloor r/2 \rfloor} { \binom{r}{2i} \frac{(2i)!} {2^i i!}} \delta^{r-2i}, 

    where `{}_1F_1(\cdot)` denotes Kummer's confluent hypergeometric function.

    See also: Paoella 2, page 381-382



    .. code-block:: python

    >>> from mpfunlab import *
    >>> mp.dps = 30
    >>> mu = 0; sigma = 1; k = 6;
    >>> print ("saddlepoint: ", student_t_2nc(mu, sigma).moments(k))
    6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_student_t_2nc.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following a doubly non-central Student t distribution. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", student_t_2nc(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00








**Approximations**


.. method:: ctx.student_t_nc2_ecf(x, n, delta, theta, results='cdf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Edgeworth approximation to the pdf, cdf and sf. See also: :cite:t:`Paolella2007`, page 381-382.



.. method:: ctx.student_t_nc2_ecf_inv(q, n, delta, theta, results='qtf')

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation to the qtf and isf.





