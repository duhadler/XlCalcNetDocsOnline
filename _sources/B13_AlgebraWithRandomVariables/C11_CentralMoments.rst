

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />





|newpage|

Central Moments
========================================================

See also Wikipedia :cite:p:`WikipediaDef11`



Calculating the central moments from the factorial moments
----------------------------------------------------------------------------------------


.. method:: ctx.centralmoments_from_factorialmoments(self, mfac)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.



    Calculates the central moments `\mu_r`  from the factorial moments.




Calculating the central moments from the raw moments
----------------------------------------------------------------------------------------

.. method:: ctx.centralmoments_from_rawmoments(central, raw)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the central moments `\mu_r` from raw the moments `\mu_r'`  (see :cite:t:`Lee1992`, :cite:t:`Rinne2008`, p. 36): 

    .. math:: \mu_r = \sum_{j=0}^r \binom{r}{j} \mu'_{r-j} (-\mu'_1)^{j}

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpr, ivr, ivc
        >>> ivr.dps = 25; ivr.pretty = True
        >>> ivr.exp([-inf,0])
        [0.0, 1.0]
        >>> ivr.exp([0,1])
        [1.0, 2.71828182845904523536028749558]






Calculating the central moments from the cumulants
----------------------------------------------------------------------------------------


.. method:: ctx.centralmoments_from_cumulants()

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the central moments `\mu_r` from the cumulants `\kappa_r`  (see :cite:t:`Lee1992`, :cite:t:`Rinne2008`, p. 36): 

    .. math:: \mu_r = \kappa_r + \sum_{j=1}^{r-1} \binom{r-1}{j-1} \mu_{r-j} \kappa_j

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpr, ivr, ivc
        >>> ivr.dps = 25; ivr.pretty = True
        >>> ivr.exp([-inf,0])
        [0.0, 1.0]
        >>> ivr.exp([0,1])
        [1.0, 2.71828182845904523536028749558]






