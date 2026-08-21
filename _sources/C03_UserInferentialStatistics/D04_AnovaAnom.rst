




.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}







.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />







|newpage|

Analysis of variance (ANOVA), orthogonal polynomials, and  analysis of means (AOM)
===========================================================================================


Literature
-------------------------------------------------------------------------------



See also: Howell, 2010


ANOM: Hothorn_AnalysisOfMeans, Elamir_2016

Nonparametric: Govindarajulu_2007

Genz_Bretz_2003

General: CRC - standard probability and statistic tables

Kirk, page 415

Lübschen

Power of Ancova: https://cran.r-project.org/web/packages/Superpower/vignettes/ANCOVAs.html (Shieh, 2020)

See also: https://en.wikipedia.org/wiki/Multiple_comparisons_problem

See also: https://en.wikipedia.org/wiki/Omnibus_test







|newpage|

.. _rst_anova_models: 

Anova: overview
-------------------------------------------------------------------------------

See also: https://en.wikipedia.org/wiki/One-way_analysis_of_variance

See also: https://en.wikipedia.org/wiki/Repeated_measures_design#Repeated_measures_ANOVA



We consider two different models:

The completely randomized model (CR): `k` independent samples of size `n_i` with mean `\bar{x}_{i}` and standard deviation `s_i`. We define `\displaystyle N = \sum_{i=1}^k n_i` and `\displaystyle \bar{\bar{x}} = \frac{1}{N} \sum_{i=1}^k n_i \bar{x}_{i}`. For `k=2` this is equivalent to a two-sided t-test for 2 independent samples.

The randomized blocks model (RB): `k` correlated samples of common size `n_i=n` and common correlation `\rho`, with `\bar{x}_{i}`, `s_i`, `N` and `\bar{\bar{x}}` as above. For `k=2` this is equivalent to a two-sided t-test for 2 correlated samples.

TODO: Generalized randomized block design (Kirk, page 293).

We assume normally distributed data, homogeneity of variances for CR and the validity of the circularity assumption for RB. When referring to populations, we will use `\bar{\mu}`, `\mu_{i}` and `\sigma_i` for means and standard deviations instead of `\bar{\bar{x}}`, `\bar{x}_{i}` and `s_i`.  In the following sections, we will refer to the following definitions:



.. math:: \mathit{SS}_{\text{WG}} = \sum_{i=1}^k(n_i-1)s_i^2; \quad \mathit{df}_{\text{\!WG}} = N-k; \quad \mathit{MS}_{\text{WG}} = \frac{\mathit{SS}_{\text{WG}}}{\mathit{df}_{\text{\!WG}}}


.. math:: \mathit{SS}_{\text{Treat}} = \sum_{i=1}^k  \left(\bar{x}_{i} - \bar{\bar{x}} \right)^2; \quad \mathit{df}_{\text{\!Treat}} = k-1; \quad \mathit{MS}_{\text{Treat}} = \frac{\mathit{SS}_{\text{Treat}}}{\mathit{df}_{\text{\!Treat}}}


.. math:: \mathit{MS}_{\text{Err}} =\begin{cases}
    \text{CR: } & \mathit{MS}_{\text{WG}},\\
    \text{RB: } & \mathit{MS}_{\text{WG}} \cdot (1-\rho).
    \end{cases} \quad  
    \mathit{df}_{\text{\!Err}} =\begin{cases}
    \text{CR: } & \mathit{df}_{\text{\!WG}},\\
    \text{RB: } & \mathit{df}_{\text{\!WG}} \cdot (k-1)/k.
    \end{cases}








|newpage|

Anova (completely randomized and randomized blocks): p-value
-------------------------------------------------------------------------------

.. method:: ctx.anova_test(mean, sd, n, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of tests for a CR or RB Anova. 

    We consider two different models:


    With this definition of `\mathit{MS}_{\text{Err}}` and `\mathit{df}_{\text{Err}}`, we can state that the test-criterion `\displaystyle F = \frac{\mathit{MS}_{\text{Treat}}}{\mathit{MS}_{\text{Err}}}` follows (under `H_0`) a central F-distribution with `\mathit{df}_{\!1} = \mathit{df}_{\text{\!Treat}}` and `\mathit{df}_{\!2} = \mathit{df}_{\text{\!Err}}` degrees of freedom, for both models.



    A call to the function, requesting a CR Anova with the critical value for a two-sided test, the p-value for `H_{03}` , for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> ereal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5

        Anova. k independent groups
        Parameter Result
        SSTreatment 15.5771
        SSError 304.5
        SSTotal 320.0771
        dfTreatment 1
        dfError 42
        dfTotal 43
        MSTreatment 15.5771
        MSError 7.25
        F-Value 2.148565517
        p-value 0.150150344
        F1-alpha 4.072653759



    A call to the function, requesting a RB Anova with common correlation 0.5, the critical value for a two-sided test, the p-value for `H_{03}`, for 3 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> ereal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=22, rho=0.5)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5

        Anova. k independent groups
        Parameter Result
        SSTreatment 15.5771
        SSError 304.5
        SSTotal 320.0771
        dfTreatment 1
        dfError 42
        dfTotal 43
        MSTreatment 15.5771
        MSError 7.25
        F-Value 2.148565517
        p-value 0.150150344
        F1-alpha 4.072653759







|newpage|

Anova (completely randomized and randomized blocks): power
-------------------------------------------------------------------------------

.. method:: ctx.anova_power(mean, sd, alpha=0.05, beta=0.1, rho=none, eta=0)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of power calculations for a CR or RB Anova. 

    See also: https://tjmurphy.github.io/jabstb/posthoc.html



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> ereal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05

        Anova. k independent groups
        Parameter Result
        SSTreatment 15.5771
        SSError 304.5
        SSTotal 320.0771
        dfTreatment 1
        dfError 42
        dfTotal 43
        MSTreatment 15.5771
        MSError 7.25
        F-Value 2.148565517
        F1-alpha 4.072653759
        NC parameter 2.148565517
        Power 0.299230817







|newpage|

Anova (completely randomized and randomized blocks): sample size
-------------------------------------------------------------------------------

.. method:: ctx.anova_samplesize(mean, sd, alpha=0.05, beta=0.1, rho=none, eta=0)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of sample size calculations for a CR or RB Anova. 






|newpage|



Anova, trend tests using orthogonal polynomials: p-value
--------------------------------------------------------------------------------------------------------

.. method:: ctx.orthogonal_poly_test(mean, sd, n, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of orthogonal polynomials for a CR or RB Anova. 

    See Kirk, page 152 and page 773.


    `\mathit{SS}_{\text{Treat}}` can be partitioned into `i = 1, \ldots, p-1` sums of squares `\displaystyle SS_{\psi_i} = \left(\sum_{j=1}^k n_j c_{ij} \bar{x}_{i} \right)^2 \bigg/ \sum_{j=1}^k c_{ij}^2`, reflecting orthogonal trend (linear, quadratic, cubic etc.) contrasts, such that 
    `\mathit{SS}_{\text{Treat}} = SS_{\psi_1} + SS_{\psi_2} + \ldots SS_{\psi_{k-1}}`, where the coefficients `c_{ij}` can be computed according to the procedure given in Narula.


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> ereal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        StDev. Group 3 3.5

        Anova. k independent groups. orthogonale polynomials
        Parameter Polynomial 1 Polynomial 2 Treatment Error Total
        Variable Variable Variable Variable Variable Variable
        df 2 2 2 63 65
        SSl 15.5771 5.192366667 20.76946667 561.75 582.5194667
        MS 15.5771 5.192366667 10.38473333 8.916666667
        F-Value 1.746964486 0.582321495 1.164642991
        p-value. 2-sided (without adjustment) 0.19103836 0.448251923 0.318660397
        p-value. 1-sided (SMM) 0.181523004 0.397610496
        p-value. 2-sided (SMM) 0.344015295 0.693938137







Anova, trend tests using orthogonal polynomials: confidence interval
--------------------------------------------------------------------------------------------------------

.. method:: ctx.orthogonal_poly_ci(mean, sd, n, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of orthogonal polynomials for a CR or RB Anova. 






Anova, trend tests using orthogonal polynomials: power
--------------------------------------------------------------------------------------------------

.. method:: ctx.orthogonal_poly_power(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of orthogonal polynomials for a CR or RB Anova. 



Anova, trend tests using orthogonal polynomials: sample size
--------------------------------------------------------------------------------------------------

.. method:: ctx.orthogonal_poly_samplesize(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of orthogonal polynomials for a CR or RB Anova. 





|newpage|


Analysis of means (ANOM): p-value
--------------------------------------------------------------------------------------------------

.. method:: ctx.anom_test(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the ANOM-test for a CR Anova. 

    See also: Hothorn_AnalysisOfMeans, Elamir_2016



|newpage|


Distribution fitting
--------------------------------------------------------------------------------------------------

.. method:: ctx.dist_fit(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Returns the results of a distribtion fit 

    See also: https://en.wikipedia.org/wiki/Probability_distribution_fitting

    See also: https://en.wikipedia.org/wiki/Method_of_moments_(statistics)

    See also: https://en.wikipedia.org/wiki/Maximum_likelihood_estimation

    See also: https://towardsdatascience.com/maximum-likelihood-estimation-in-r-b21f68f1eba4

    See also: https://stat.ethz.ch/R-manual/R-devel/library/stats4/html/mle.html







Additional info: Narula's algorithm
--------------------------------------------------------------------------------------------------

The problem of approximating the relation of a response variable to a predictor variable consists of (i) the determination of the degree of the polynomial that "best" describes any trends in the data and (ii) the evaluation of the coefficients of the approximating polynomial. One may approach the problem in one of two ways: (a) the usual polynomial regression, or (b) the orthogonal polynomial approach.


The usual polynomial regression approach gives rise to the following difficulties: (i) the tests of significance for the various parameters are not independent, (ii) the estimates of the parameters of a polynomial of degree `(k-1)` cannot be used for estimating coefficients of a polynomial of degree `k`, and (iii) for degrees of polynomial greater than 4, the estimates may be inaccurate due to round-off errors.


The orthogonal polynomial approach does not suffer from the shortcomings associated with the usual polynomial regression.


The following algorithm has been given by :cite:t:`Narula1978`: Let `x_i`  denote the `i^{\text{th}}` value `(i=1,\ldots,k)`  of the predictor variable observed `n_i`  times. Then


.. math:: P_0(x_i)=1


.. math:: P_1(x_i)=(x_i- \alpha_1)P_0(x_i)


.. math:: P_j(x_i)=(x_i- \alpha_j)P_0(x_i) - \beta_{j-2}(x_i), \quad j=2,3,\ldots,m\leq k-1


represents a set of orthogonal polynomials if

.. math:: \alpha_j = \frac{\sum_{i=1}^k n_i x_i P_{j-1}^2(x_i) }{\sum_{i=1}^k n_i P_{j-1}^2(x_i) }, \quad j=1,2,\ldots,m, \text{ and}



.. math:: \beta_j = \frac{\sum_{i=1}^k n_i x_i P_{j-2}(x_i) P_{j-1}(x_i)}{\sum_{i=1}^k n_i P_{j-1}^2(x_i) }, \quad j=2,3,\ldots,m.


The orthogonal polynomial model can  be written as

.. math:: E(Y_{ij}) = \beta_0^* P_0(x_i) + \beta_1^* P_1(x_i) + \ldots + \beta_m^* P_m(x_i), \quad i=1,\ldots,k, \text{ and } j=1,\ldots,n_i,


where  `Y_{ij}` denotes the  `j^{\text{th}}` values `(j=1,\ldots,n_i)`  of the response variable corresponding to `x_i`, the  `i^{\text{th}}` value of the predictor variable, and  `P_j` denote the orthogonal polynomials as given above.

The least quares estimators `b_j^*` of `\beta_j^*` `(j=0,1,\ldots,m)`  are given by


.. math:: \beta_j^* = \frac{\sum_{i=1}^k Y_{i\bullet} P_{j}(x_i) }{\sum_{i=1}^k n_i P_{j}^2(x_i) }, \quad j=0,1,\ldots,m, 


and the sum of squares due to the  `j^{\text{th}}` degree polynomial, `P_j` , is


.. math:: SS_j = \left(b_j^*\right)^2 \sum_{i=1}^k n_{i} P_j^2(x_i), \quad j=1,\ldots,m, \text{ where } Y_{i\bullet}=\sum_{j=1}^{n_i}Y_{ij} \text{ and } Y_{\bullet\bullet}=\sum_{i=1}^{k}Y_{i\bullet}



