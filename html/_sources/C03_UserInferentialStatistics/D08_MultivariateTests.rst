








.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />







|newpage|


Multivariate statistical tests
===============================================================



Canonical correlation: 


Canonical correlation:  See also: Wikipedia :cite:p:`WikipediaStat300`.

Linear_discriminant_analysis:  See also: Wikipedia :cite:p:`WikipediaStat310`.

Principal_component_analysis:  See also: Wikipedia :cite:p:`WikipediaStat320`.

Regression_analysis:  See also: Wikipedia :cite:p:`WikipediaStat330`.

Linear_regression:  See also: Wikipedia :cite:p:`WikipediaStat340`.

Analysis_of_variance:  See also: Wikipedia :cite:p:`WikipediaStat350`.

One-way_analysis_of_variance:  See also: Wikipedia :cite:p:`WikipediaStat360`.

Design_matrix:  See also: Wikipedia :cite:p:`WikipediaStat370`.

Analysis_of_covariance:  See also: Wikipedia :cite:p:`WikipediaStat380`.

General_linear_model:  See also: Wikipedia :cite:p:`WikipediaStat390`.

Multivariate_analysis_of_variance:  See also: Wikipedia :cite:p:`WikipediaStat400`.

Multivariate_analysis_of_covariance:  See also: Wikipedia :cite:p:`WikipediaStat410`.

Correlation_and_dependence:  See also: Wikipedia :cite:p:`WikipediaStat420`.


Standardization:  See also: Wikipedia :cite:p:`WikipediaStat430`.








Multiple linear regression: p-value and confidence interval
------------------------------------------------------------------------------------

.. method:: ctx.multlinreg_test(self, ctx, mean, mean0, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 




Multiple linear regression Type I: power and sample size
---------------------------------------------------------------------------------

.. method:: ctx.multlinreg_type1_power(self, ctx, mean, mean0, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 





Multiple linear regression Type II: power and sample size
------------------------------------------------------------------------------------

.. method:: ctx.multlinreg_type2_power(self, ctx, mean, mean0, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 


    Ref:

    Kelley (2008): Sample size, confidence interval





|newpage|

Hotelling's `T^2` test for 1 sample:  p-value and confidence interval
-----------------------------------------------------------------------------------

.. method:: ctx.hotelling_1sample_test(self, ctx, mean, mean0, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 




Hotelling's `T^2` test for 1 sample: power and sample size
----------------------------------------------------------------------------------

.. method:: ctx.hotelling_1sample_power(self, ctx, mean, mean0, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 





Hotelling's `T^2` test for 2 independent samples:  p-value and confidence interval
------------------------------------------------------------------------------------------

.. method:: ctx.hotelling_2isamples_test(self, ctx, mean, mean0, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 




Hotelling's `T^2` test for 2 independent samples: power and sample size
----------------------------------------------------------------------------------------

.. method:: ctx.hotelling_2isamples_power(self, ctx, mean, mean0, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 







|newpage|

Overview: 4 test criteria for 3 hypotheses
-------------------------------------------------------------------------------

    Test explaining, based on Tretter and Bortz.





.. _rst_mpm_manova: 

MANOVA: Wilks `\Lambda`, Pillai's `V`, Hotelling's `T^2`, Roy's largest root `\theta`
------------------------------------------------------------------------------------------

.. method:: ctx.four_tests_glm_test(x, p, m, n, cdf=True, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.



    The Lawley-Hotelling generalized `T_0^2` and Pillai's `V` statistic, defined respectively by

    .. math:: T_0^2 = n \text{tr} (AB^{-1}), \quad V = n \text{tr} (A(A+B)^{-1}),

    have been suggested as alternatives to Wilk's criterion for testing multivariate linear hypotheses. 
    Here `A` and `B` are independent `p \times p` Wishart matrices on `q` and `n` degrees of freedom respectively. 




.. _rst_mpm_cancorr: 

Canonical correlation: Wilks `\Lambda`, Pillai's `V`, Hotelling's `T^2`, Roy's largest root `\theta`
-------------------------------------------------------------------------------------------------------

.. method:: ctx.four_tests_ind_test(x, p, m, n, cdf=True, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Some Text



Power estimates of 4 tests in MANOVA
-------------------------------------------------------------------------------

.. method:: ctx.four_tests_glm_power(x, p, m, n, Omega, cdf=True, method='default')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns `\text{cdf}_X(x)`, the cumulative distribution function, for ``cdf=True``, or `\text{sf}_X(x)`, the survival function, for ``cdf=False``, of a random variable `X`, following a noncentral Wilks’ `\Lambda` distribution under the GLM alternative,, with `p \ge 1` predictor variables, error degress of freedom `m \ge 1` and `n \ge 1`, noncentrality parameter `\Omega` with diagonal entries `\omega_{jj} \in (0,\infty)` and the support interval `(0,1)`.


    This approach is discussed in detail in chapter ...



    There are other ways of calculating  `\text{pdf}_X(x)` as well. If ``method`` is not specified, the algorithm is chosen automatically.

    For ``fpm.`` the default method is to call the function provided by Boost. Otherwise, the default is verified integration.



    ``method='finite_series'``: the finite series described in ... is used.

    ``method='infinite_series'``: the infinite series described in ... is used.

    ``method='edgeworth'``: the edgeworth expansion described in ... is used.

    ``method='lugannini_rice'``: the Lugannini-Rice saddlepoint approximation described in ... is used.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; p = '3'; m = '4'; n = '20'; O = [3.6, 1.2, 0.5]
        >>> dx = dec.four_tests_glm_cdf(x,p,m,n,O); mx = mpm.four_tests_glm_cdf(x,p,m,n,O)
        >>> ix = ipm.four_tests_glm_cdf(x,p,m,n,O); fx = fpm.four_tests_glm_cdf(x,p,m,n,O)
        >>> gx = gmp.four_tests_glm_cdf(x,p,m,n,O); ax = apm.four_tests_glm_cdf(x,p,m,n,O)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  9.727307040581953720491613246746146674676E-1
        mpm:  9.727307040581953720491613246746146674676e-1
        ipm:  9.727307040581953720491613246746146674676e-1 (5.901e-40%)
        fpm:  9.72730704058195E-01
        gmp:  9.727307040581953720491613246746146674676E-01
        ipm:  9.727307040581953720491613246746146674676e-1 (5.901e-40%)






Power estimates of 4 tests in canonical correlation (Type I)
-------------------------------------------------------------------------------

.. method:: ctx.four_tests_ind_power(x, p1, p2, n, Rho2, cdf=True, method='default')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns `\text{cdf}_X(x)`, the cumulative distribution function, for ``cdf=True``, or `\text{sf}_X(x)`, the survival function, for ``cdf=False``, of a random variable `X`, following a noncentral Wilks’ `\Lambda` distribution under the independence alternative, with `p_1 \ge 1` and  `p_2 \ge 1` groups of variables, error degress of freedom `n \ge 1`, noncentrality parameter `P^2` with diagonal entries `\rho^2_{jj} \in (0,1)` and the support interval `(0,1)`.



    This approach is discussed in detail in chapter ...



    There are other ways of calculating  `\text{pdf}_X(x)` as well. If ``method`` is not specified, the algorithm is chosen automatically.

    For ``fpm.`` the default method is to call the function provided by Boost. Otherwise, the default is verified integration.



    ``method='finite_series'``: the finite series described in ... is used.

    ``method='infinite_series'``: the infinite series described in ... is used.

    ``method='edgeworth'``: the edgeworth expansion described in ... is used.

    ``method='lugannini_rice'``: the Lugannini-Rice saddlepoint approximation described in ... is used.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; p1 = '3'; p2 = '4'; n = '20'; P = [3.6, 1.2, 0.5]
        >>> dx = dec.four_tests_ind_cdf(x,p1,p2,n,P); mx = mpm.four_tests_ind_cdf(x,p1,p2,n,P)
        >>> ix = ipm.four_tests_ind_cdf(x,p1,p2,n,P); fx = fpm.four_tests_ind_cdf(x,p1,p2,n,P)
        >>> gx = gmp.four_tests_ind_cdf(x,p1,p2,n,P); ax = apm.four_tests_ind_cdf(x,p1,p2,n,P)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  9.727307040581953720491613246746146674676E-1
        mpm:  9.727307040581953720491613246746146674676e-1
        ipm:  9.727307040581953720491613246746146674676e-1 (5.901e-40%)
        fpm:  9.72730704058195E-01
        gmp:  9.727307040581953720491613246746146674676E-01
        ipm:  9.727307040581953720491613246746146674676e-1 (5.901e-40%)



