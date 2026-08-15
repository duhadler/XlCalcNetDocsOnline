

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />







|newpage|

Cumulants
========================================================

See also Wikipedia :cite:p:`WikipediaDef11`



Calculating the cumulants from the pmf vector
----------------------------------------------------------------------------------------


.. method:: cumulants_from_pmfvector(self, x, nl, order, show=False)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.



    Calculates the cumulants `\kappa_r` from the pmf vector.




Calculating the cumulants from the factorial moments
----------------------------------------------------------------------------------------


.. method:: ctx.cumulants_from_factorialmoments(self, mfac)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.



    Calculates the cumulants `\kappa_r` from the factorial moments.




Calculating the cumulants from the raw moments
----------------------------------------------------------------------------------------


.. method:: ctx.cumulants_from_rawmoments(raw_moments)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.



    Calculates the cumulants `\kappa_r` from the raw moments `\mu_r'`   (see :cite:t:`Lee1992`, :cite:t:`Rinne2008`, p. 36): 

    .. math:: \kappa_r = \mu_r' - \sum_{j=1}^{r-1} \binom{r-1}{j-1} \mu_{r-j}' \kappa_j






Calculating the cumulants from the central moments
----------------------------------------------------------------------------------------


.. method:: ctx.cumulants_from_centralmoments(cumulants, central)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the cumulants  `\kappa_r` from the central moments `\mu_r` : 

    .. math:: \kappa_r = \mu_r - \sum_{j=2}^{r-1} \binom{r-1}{j-1} \mu_{r-j} \kappa_j, \quad r>1, \quad \kappa_1=\mu_1.

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpr, ivr, ivc
        >>> ivr.dps = 25; ivr.pretty = True
        >>> ivr.exp([-inf,0])
        [0.0, 1.0]
        >>> ivr.exp([0,1])
        [1.0, 2.71828182845904523536028749558]





Calculating the cumulants from the cumulant-generating function 
----------------------------------------------------------------------------------------

.. method:: ctx.cumulants_from_cdf(k, cgf)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    The cumulants `\kappa _{n}` are obtained from a power series expansion of the cumulant generating function: 

    .. math::  K(t)=\sum _{n=1}^{\infty }\kappa _{n}{\frac {t^{n}}{n!}}=\mu t+\sigma ^{2}{\frac {t^{2}}{2}}+\cdots .

    This expansion is a Maclaurin series, so the n-th cumulant can be obtained by differentiating the above expansion n times and evaluating the result at zero:

    .. math::  \kappa _{n}=K^{(n)}(0).





