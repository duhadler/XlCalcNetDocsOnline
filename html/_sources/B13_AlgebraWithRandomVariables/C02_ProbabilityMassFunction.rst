

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />





|newpage|



Probability mass function (pmf)
========================================================



Calculating the pmf from the cdf
-------------------------------------------------------------------------------

.. method:: ctx.pmf_from_cdf(x, cdf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Returns `\text{pmf}_X(x)`, the probability mass function,  calculated from the cumulative distribution function (cdf) of a random variable `X`:

    .. math:: \text{pmf}_X(x) = (\text{cdf}_X(x+d) - \text{cdf}_X(x))/d.


    Using this method can be a viable option when the cdf, but not the pmf, is available in closed form.




.. _rst_pmf_from_cf_lattice: 

Calculating the pmf from the characteristic function
-------------------------------------------------------------------------------

.. method:: ctx.pmf_from_cf_lattice(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Returns `\text{pmf}_X(x)`, the probability mass function, calculated from  the characteristic function `C_X(t)` of a random variable `X`:

    .. math::  \text{pmf}(x) = \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{-itx} C_X(t) \mathrm{d} t.


    Using this method can be a viable option when the characteristic function, but not the pmf, is available in closed form.




Calculating the pmf from the factorial moments
-------------------------------------------------------------------------------

.. method:: ctx.pmf_from_factorialmoments(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns `\text{pmf}_X(x)`, the probability mass function,  of a random variable `X`, calculated from the factorial moments `\mu_[r]`:

    .. math::  \text{Pr}[X=x] = \sum_{j \ge x} (-1)^{x+j} \binom{j}{x} \frac{\mu'_{[j]}}{j!}  = \sum_{r \ge 0} (-1)^{r} \frac{\mu'_{[x+r]}}{x!r!}


    and

    .. math::  \sum_{i \ge x} \text{Pr}[X=i] = \sum_{j \ge x} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!} 


    Using this method can be a viable option when the factorial moments, but not the pmf, are available in closed form.




Approximating the pmf with asymptotic expansions
-------------------------------------------------------------------------------


This call Edgeworth, Cornish-Fisher, or Lugganinni-Rice.



