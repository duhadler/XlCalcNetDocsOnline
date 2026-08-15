




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


Basic classical statistical tests for 2 correlated samples (stratified)
==========================================================================================================




Student t-test for 2 correlated samples: tests (p-values)
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2csamples_test(mean, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results for Student's t-test for for 2 correlated samples. 


    See also: https://en.wikipedia.org/wiki/Student%27s_t-test#Paired_samples



    **Parameters:**

    :mean:   The mean of the sample.

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals




    Let `(X_1, X_2, \ldots, X_N)` denote a random sample of size `N` from a normal distribution with mean `\mu` and variance `\sigma^2`, and let

    .. math:: \overline{x}_1 = \frac{1}{N} \sum_{i=1}^N X_i \quad \text{and } s^2 = \frac{1}{N-1} \sum_{i=1}^N (X_i - \overline{x}_1)

    be the usual sample estimates of the unkown population mean `\mu` and unkown population variance `\sigma^2`. Then Student's t-test can be used to test hypotheses concerning `\mu` with regard to a reference value `\mu_2`.

    Let `F_t\left(\cdot, \nu\right)` denote the CDF (see section \ref{tDistributionCDF}) and let `t_{\nu,\alpha}` denote the `\alpha`-quantile (see section \ref{tDistributionQuantile}) of the `t`-distribution with `\nu` degrees of freedom. Define

    .. math:: t= \frac{\overline{x}_1-\mu_2}{s}, \quad s=\sqrt{s_1^2 /N}, \quad \nu=N-1.


    Then `p`-values and rejection criteria for `H_0` can be calculated as summarized below


|spacingstart|

     =========================================================  =================================================================  =================================================================
                 Test problem                                         `p`-value                                                           Reject `H_0`                                           
     =========================================================  =================================================================  ================================================================= 
       `H_{01}: \mu_1\leq \mu_2` vs `H_{A1}: \mu_1> \mu_2`            `F_t\left(-t, \nu\right)`                                           `t > t_{\nu;1-\alpha}`                                    
       `H_{02}: \mu_1\geq \mu_2` vs `H_{A2}: \mu_1< \mu_2`            `F_t\left(t, \nu\right)`                                            `t > t_{\nu;\alpha}`                                      
       `H_{03}: \mu_1= \mu_2` vs `H_{A3}: \mu_1\neq \mu_2`            `F_t\left(t, \nu\right)-F_t\left(-t, \nu\right)`                    `t > t_{\nu;1-\alpha/2}` or `t > t_{\nu;\alpha/2}`        
     =========================================================  =================================================================  =================================================================

|spacingend|


    The test can also be expressed in terms of a correlation coefficient `r` between the combined `X` and an indicator variable, where `t` and `r` are related by

    .. math:: r=\frac{t}{\sqrt{t^2+\nu}}, \quad t= \nu \frac{r}{1-r^2}.


    An actual call to the function, requesting Student's t-test with description, the critical value for a two-sided test, the p-value for `H_{03}` (in the case of `\textsf{TTest}` this is `\mu_1 \neq \mu_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1Test(means:=[5.24, 4.05], sd:=1.5, n:=22)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Student's t-test for 2 corr. samples
        Parameter Result
        df 21
        Difference of means 1.19
        t-value (=delta) 2.087398086
        t1 - alpha(1 - sided) 1.720742903
        t1 - alpha(2 - sided) 2.079613845
        test. p-value (H01: µ1 >= µ2) 0.97538843
        test. p-value (H02: µ1 <= µ2) 0.02461157
        test. p-value (H03: µ1 = µ2) 0.04922314





|newpage|



Student t-test for 2 correlated samples:  confidence intervals
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2csamples_ci(mean, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results for Student's t-test for for 2 correlated samples. 





    **Parameters:**

    :mean:   The mean of the sample.

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals



    Let `A_1=t_{\nu,\alpha} \cdot s` and `A_2=t_{\nu,\alpha/2} \cdot s`, where `s` and `\nu` are defined in (\ref{eq:TTest1}), and `t_{\nu,\alpha}` denotes the `\alpha`-quantile of the (central) `t`-distribution with `\nu` degrees of freedom (see section \ref{tDistributionQuantile}). 


|spacingstart|

     =========================================================  ============================================================================================
       Type                                                          Confidence Interval (Difference of Means)                   
     =========================================================  ============================================================================================
       Left-sided                                                    `-\infty \leq \mu_1 - \mu_2 \leq (\overline{x}_1-\mu_2)  + A_1`                        
       Right-sided                                                  `(\overline{x}_1-\mu_2 ) - A_1 \leq \mu_1 - \mu_2 \leq +\infty`                         
       Two-sided                                                    `(\overline{x}_1-\mu_2 ) - A_2 \leq \mu_1 - \mu_2 \leq (\overline{x}_1-\mu_2 ) + A_2`   
     =========================================================  ============================================================================================

|spacingend|



    An actual call to the function, requesting Student's t-test with description, the critical value for a two-sided test, the p-value for `H_{03}` (in the case of \textsf{TTest} this is `\mu_1 \neq \mu_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, alpha=0.05, resultstring)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Student's t-test for 2 corr. samples
        Parameter Result
        df 21
        Difference of means 1.19
        t-value (=delta) 2.087398086
        t1 - alpha(1 - sided) 1.720742903
        t1 - alpha(2 - sided) 2.079613845
        µ1 - µ2. CI - Length (2 - sided) 2.371124599
        µ1 - µ2. CI Upper Limit (2-sided) 2.3755623
        µ1 - µ2. CI Lower Limit (2-sided) 0.0044377











|newpage|




Student t-test for 2 correlated samples: power 
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2csamples_power(mean, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of Student's t-test for 2 correlated samples: power and sample size.





    **Parameters:**

    :mean:   The mean of the sample.

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals



    Let `\sigma_1^2 = \sigma^2` and `\nu=N-1`. Define


    .. math:: \widetilde{\rho} = \frac{\mu_1-\mu_2}{\sigma} \text{ and } \delta = \sqrt{N} \widetilde{\rho}.


    Let `F_{t'}\left(\cdot, \nu, \delta \right)` denote the CDF of the (singly) noncentral `t`-distribution with `\nu` degrees of freedom and noncentrality parameter `\delta` and let `t_{\nu,\alpha}` denote the `\alpha`-quantile of the central `t`-distribution with `\nu` degrees of freedom. Then the power for accepting `H_A` at the confidence level `\alpha` can be calculated as summarized below:

|spacingstart|

     ==================  ====================================  ======================================  =============================================================================================================
       Test                   Null Hypothesis                        Alternative                             Power                                                                                                  
     ==================  ====================================  ======================================  =============================================================================================================
       1 sided               `H_{01}: \mu_1\leq \mu_2`              `H_{A1}: \mu_1> \mu_2`                  `F_{t'}\left(-t_{\nu;1-\alpha}, \nu, \delta \right)`                                                      
       1 sided               `H_{02}: \mu_1\geq \mu_2`              `H_{A2}: \mu_1< \mu_2`                  `F_{t'}\left(t_{\nu;1-\alpha}, \nu, \delta \right)`                                                       
       2 sided               `H_{03}: \mu_1= \mu_2`                 `H_{A1}: \mu_1> \mu_2`                  `F_{t'}\left(-t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                    
       2 sided               `H_{03}: \mu_1= \mu_2`                 `H_{A1}: \mu_1> \mu_2`                  `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                     
       2 sided               `H_{03}: \mu_1= \mu_2`                 `H_{A3}: \mu_1\neq \mu_2`               `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)-F_t\left(-t_{\nu;1-\alpha/2}, \nu\, \delta \right)`  
     ==================  ====================================  ======================================  =============================================================================================================

|spacingend|




    An actual call to the function, requesting Student's t-test with description, the critical calue for a two-sided test, the power for `H_{A3}` (in the case of \textsf{TTest} this is `\mu_1 \neq \mu_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, n:=22, alpha:=0.05)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Student's t-test for 2 corr. samples
        Parameter Result
        df 21
        Difference of means 1.19
        t-value (=delta) 2.087398086
        t1 - alpha(1 - sided) 1.720742903
        t1 - alpha(2 - sided) 2.079613845
        1-sided test. power (HA1: µ1 < µ2) 0.000122287
        1-sided test. power (HA2: µ1 > µ2) 0.646013238
        2-sided test. power (HA1: µ1 < µ2) 3.78799E-05
        2-sided test. power (HA2: µ1 > µ2) 0.512603358
        2-sided test. power (HA3: µ1 <> µ2) 0.512641238
        test. Pr[Mean 1 < Mean 2] 0.018426082
        test. Pr[Mean 1 > Mean 2] 0.981573918





|newpage|


Student t-test for 2 correlated samples: sample size calculation
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2csamples_samplesize(mu, sd, alpha=0.05, beta=0.1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of sample size calculations for Student's t-test for 2 correlated samples




    **Parameters:**

    :mean:   The mean of the sample.

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals

    :beta:     The beta-level used for power



    Let `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)` denote the sample size function of the (singly) noncentral `t`-distribution (see section \ref{NoncentralTDistributionSampleSize} ) for a given confidence level `\alpha`, power `\beta` and noncentrality parameter `\widetilde{\rho}` (as defined in equation \ref{eq:TTestPower1}. The required total sample size `N` can be calculated as summarized below



|spacingstart|

     ==================  ====================================  ======================================  =============================================================
       Test                   Null Hypothesis                        Alternative                             Minimal sample size                                    
     ==================  ====================================  ======================================  =============================================================
       1 sided               `H_{01}: \mu_1\leq \mu_2`              `H_{A1}: \mu_1> \mu_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       1 sided               `H_{02}: \mu_1\geq \mu_2`              `H_{A2}: \mu_1< \mu_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \mu_1= \mu_2`                 `H_{A1}: \mu_1> \mu_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \mu_1= \mu_2`                 `H_{A1}: \mu_1> \mu_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \mu_1= \mu_2`                 `H_{A3}: \mu_1\neq \mu_2`               `N2_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`    
     ==================  ====================================  ======================================  =============================================================

|spacingend|





    Note that the returned value of `N` will in general not be an integer, and rounding up may be required.

    An actual call to the function, requesting an upper sample size estimate (and actual power) for `\alpha = 0.95`, `\beta=0.1` , and standard deviations `\sigma_1=\sigma_2=1` , means `\mu_1=2.3` and `\mu_2=4.5`,   would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, alpha:=0.05, beta:=0.1)
                                                 df: 21
                                difference of means: 1.19
                                   t-value (=delta): 3.721063
                                t(1-alpha, 1-sided): 1.720743
                                t(1-alpha, 2-sided): 2.079614
          1-sided test, required N (HA1: mu1 < mu2): 18
        1-sided test, actual power (HA1: mu1 < mu2): 0.974564
          1-sided test, required N (HA2: mu1 > mu2): 148
        1-sided test, actual power (HA2: mu1 > mu2): 0.964564
          2-sided test, required N (HA1: mu1 < mu2): 22
        2-sided test, actual power (HA1: mu1 < mu2): 0.954564
          2-sided test, required N (HA2: mu1 > mu2): 212
        2-sided test, actual power (HA2: mu1 > mu2): 0.977456
          2-sided test, required N (HA2: mu1 <>mu2): 24
        2-sided test, actual power (HA2: mu1 <>mu2): 0.955544











|newpage|




Morgan-Pitman test for the variances of 2 correlated samples: tests (p-values)
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2csamples_test(s2, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results for the Morgan-Pitman test for the variances of 2 correlated samples. 




    **Parameters:**

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals




    Let `(X_1, X_2, \ldots, X_N)` denote a random sample of size `N` from a normal distribution with mean `\sigma` and variance `\sigma^2`, and let

    .. math:: \overline{x}_1 = \frac{1}{N} \sum_{i=1}^N X_i \quad \text{and } s^2 = \frac{1}{N-1} \sum_{i=1}^N (X_i - \overline{x}_1)

    be the usual sample estimates of the unkown population mean `\sigma` and unkown population variance `\sigma^2`. Then Student's t-test can be used to test hypotheses concerning `\sigma` with regard to a reference value `\sigma_2`.

    Let `F_t\left(\cdot, \nu\right)` denote the CDF (see section \ref{tDistributionCDF}) and let `t_{\nu,\alpha}` denote the `\alpha`-quantile (see section \ref{tDistributionQuantile}) of the `t`-distribution with `\nu` degrees of freedom. Define

    .. math:: t= \frac{\overline{x}_1-\sigma_2}{s}, \quad s=\sqrt{s_1^2 /N}, \quad \nu=N-1.


    Then `p`-values and rejection criteria for `H_0` can be calculated as summarized below


|spacingstart|

     ====================================================================  =================================================================  =================================================================
                 Test problem                                                    `p`-value                                                           Reject `H_0`                                           
     ====================================================================  =================================================================  ================================================================= 
       `H_{01}: \sigma_1\leq \sigma_2` vs `H_{A1}: \sigma_1> \sigma_2`            `F_t\left(-t, \nu\right)`                                           `t > t_{\nu;1-\alpha}`                                    
       `H_{02}: \sigma_1\geq \sigma_2` vs `H_{A2}: \sigma_1< \sigma_2`            `F_t\left(t, \nu\right)`                                            `t > t_{\nu;\alpha}`                                      
       `H_{03}: \sigma_1= \sigma_2` vs `H_{A3}: \sigma_1\neq \sigma_2`            `F_t\left(t, \nu\right)-F_t\left(-t, \nu\right)`                    `t > t_{\nu;1-\alpha/2}` or `t > t_{\nu;\alpha/2}`        
     ====================================================================  =================================================================  =================================================================

|spacingend|


    The test can also be expressed in terms of a correlation coefficient `r` between the combined `X` and an indicator variable, where `t` and `r` are related by

    .. math:: r=\frac{t}{\sqrt{t^2+\nu}}, \quad t= \nu \frac{r}{1-r^2}.


    An actual call to the function, requesting Student's t-test with description, the critical value for a two-sided test, the p-value for `H_{03}` (in the case of `\textsf{TTest}` this is `\sigma_1 \neq \sigma_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1Test(means:=[5.24, 4.05], sd:=1.5, n:=22)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Pitman-Morgan-test for 2 corr. variances
        Parameter Result
        df1 21
        df2 21
        Variance-Ratio 0.183673469
        F. 1 - alpha(1 - sided) 2.084188623
        F . 1 - alpha(2 - sided) 2.408589482
        Pitman-Morgan F-test. p-value (H01: s1 >= s2) 0.999864065
        Pitman-Morgan F-test. p-value (H02: s1 <= s2) 0.000135935
        Pitman-Morgan F-test. p-value (H03: s1 = s2) 0.999728131





|newpage|


Morgan-Pitman test for the variances of 2 correlated samples: confidence intervals
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2csamples_ci(s2, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results of the confidence intervals for the Morgan-Pitman test for the variances of 2 correlated samples. 





    **Parameters:**

    :mean:   The mean of the sample.

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals



    Let `A_1=t_{\nu,\alpha} \cdot s` and `A_2=t_{\nu,\alpha/2} \cdot s`, where `s` and `\nu` are defined in (\ref{eq:TTest1}), and `t_{\nu,\alpha}` denotes the `\alpha`-quantile of the (central) `t`-distribution with `\nu` degrees of freedom (see section \ref{tDistributionQuantile}). 


|spacingstart|

     =========================================================  =======================================================================================================
       Type                                                          Confidence Interval (Difference of Means)                   
     =========================================================  =======================================================================================================
       Left-sided                                                    `-\infty \leq \sigma_1 - \sigma_2 \leq (\overline{x}_1-\sigma_2)  + A_1`                        
       Right-sided                                                  `(\overline{x}_1-\sigma_2 ) - A_1 \leq \sigma_1 - \sigma_2 \leq +\infty`                         
       Two-sided                                                    `(\overline{x}_1-\sigma_2 ) - A_2 \leq \sigma_1 - \sigma_2 \leq (\overline{x}_1-\sigma_2 ) + A_2`   
     =========================================================  =======================================================================================================

|spacingend|



    An actual call to the function, requesting Student's t-test with description, the critical value for a two-sided test, the p-value for `H_{03}` (in the case of \textsf{TTest} this is `\sigma_1 \neq \sigma_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, alpha=0.05, resultstring)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Pitman-Morgan-test for 2 corr. variances
        Parameter Result
        df1 21
        df2 21
        Variance-Ratio 0.183673469
        F. 1 - alpha(1 - sided) 2.084188623
        F . 1 - alpha(2 - sided) 2.408589482
        s1/s2. CI - Length(2 - sided) 0.366136297
        s1/s2. CI Upper Limit (2-sided) 0.442393986
        s1/s2. CI Lower Limit (2-sided) 0.07625769











|newpage|



Morgan-Pitman test for the variances of 2 correlated samples: power
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2csamples_power(s2, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results of the power calculation for the Morgan-Pitman test for the variances of 2 correlated samples. 





    **Parameters:**

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals



    Let `\sigma_1^2 = \sigma^2` and `\nu=N-1`. Define


    .. math:: \widetilde{\rho} = \frac{\sigma_1-\sigma_2}{\sigma} \text{ and } \delta = \sqrt{N} \widetilde{\rho}.


    Let `F_{t'}\left(\cdot, \nu, \delta \right)` denote the CDF of the (singly) noncentral `t`-distribution with `\nu` degrees of freedom and noncentrality parameter `\delta` and let `t_{\nu,\alpha}` denote the `\alpha`-quantile of the central `t`-distribution with `\nu` degrees of freedom. Then the power for accepting `H_A` at the confidence level `\alpha` can be calculated as summarized below:

|spacingstart|

     ==================  ====================================  =================================================  ========================================================================================================================
       Test                   Null Hypothesis                                     Alternative                             Power                                                                                                  
     ==================  ====================================  =================================================  ========================================================================================================================
       1 sided               `H_{01}: \sigma_1\leq \sigma_2`              `H_{A1}: \sigma_1> \sigma_2`                  `F_{t'}\left(-t_{\nu;1-\alpha}, \nu, \delta \right)`                                                      
       1 sided               `H_{02}: \sigma_1\geq \sigma_2`              `H_{A2}: \sigma_1< \sigma_2`                  `F_{t'}\left(t_{\nu;1-\alpha}, \nu, \delta \right)`                                                       
       2 sided               `H_{03}: \sigma_1= \sigma_2`                 `H_{A1}: \sigma_1> \sigma_2`                  `F_{t'}\left(-t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                    
       2 sided               `H_{03}: \sigma_1= \sigma_2`                 `H_{A1}: \sigma_1> \sigma_2`                  `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                     
       2 sided               `H_{03}: \sigma_1= \sigma_2`                 `H_{A3}: \sigma_1\neq \sigma_2`               `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)-F_t\left(-t_{\nu;1-\alpha/2}, \nu\, \delta \right)`  
     ==================  ====================================  =================================================  ========================================================================================================================

|spacingend|




    An actual call to the function, requesting Student's t-test with description, the critical calue for a two-sided test, the power for `H_{A3}` (in the case of \textsf{TTest} this is `\sigma_1 \neq \sigma_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, n:=22, alpha:=0.05)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Pitman-Morgan-test for 2 corr. variances
        Parameter Result
        df1 21
        df2 21
        Variance-Ratio 0.183673469
        F. 1 - alpha(1 - sided) 2.084188623
        F . 1 - alpha(2 - sided) 2.408589482
        Pitman-Morgan 1-sided test. power (HA1: s1 < s2) 0.999864065
        Pitman-Morgan 1-sided test. power (HA2: s1 > s2) 0.999864065
        Pitman-Morgan 2-sided test. power (HA1: s1 < s2) 0.999864065
        Pitman-Morgan 2-sided test. power (HA2: s1 > s2) 0.999864065
        Pitman-Morgan 2-sided test. power (HA3: s1 <> s2) 0.999864065






|newpage|




Morgan-Pitman test for the variances of 2 correlated samples: sample size
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2csamples_samplesize(s2, alpha=0.05, beta=0.1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results  of sample size calculations  for the Morgan-Pitman test for the variances of 2 correlated samples. 






    **Parameters:**

    :sd:     The standard deviation of the sample

    :alpha:     The alpha-level used for confidence intervals

    :beta:     The beta-level used for power



    Let `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)` denote the sample size function of the (singly) noncentral `t`-distribution (see section \ref{NoncentralTDistributionSampleSize} ) for a given confidence level `\alpha`, power `\beta` and noncentrality parameter `\widetilde{\rho}` (as defined in equation \ref{eq:TTestPower1}. The required total sample size `N` can be calculated as summarized below



|spacingstart|

     ==================  ====================================  =================================================  =============================================================
       Test                   Null Hypothesis                                 Alternative                                Minimal sample size                                    
     ==================  ====================================  =================================================  =============================================================
       1 sided               `H_{01}: \sigma_1\leq \sigma_2`              `H_{A1}: \sigma_1> \sigma_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       1 sided               `H_{02}: \sigma_1\geq \sigma_2`              `H_{A2}: \sigma_1< \sigma_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \sigma_1= \sigma_2`                 `H_{A1}: \sigma_1> \sigma_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \sigma_1= \sigma_2`                 `H_{A1}: \sigma_1> \sigma_2`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \sigma_1= \sigma_2`                 `H_{A3}: \sigma_1\neq \sigma_2`               `N2_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`    
     ==================  ====================================  =================================================  =============================================================

|spacingend|





    Note that the returned value of `N` will in general not be an integer, and rounding up may be required.

    An actual call to the function, requesting an upper sample size estimate (and actual power) for `\alpha = 0.95`, `\beta=0.1` , and standard deviations `\sigma_1=\sigma_2=1` , means `\sigma_1=2.3` and `\sigma_2=4.5`,   would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, alpha:=0.05, beta:=0.1)
                                                 df: 21
                                difference of means: 1.19
                                   t-value (=delta): 3.721063
                                t(1-alpha, 1-sided): 1.720743
                                t(1-alpha, 2-sided): 2.079614
          1-sided test, required N (HA1: mu1 < mu2): 18
        1-sided test, actual power (HA1: mu1 < mu2): 0.974564
          1-sided test, required N (HA2: mu1 > mu2): 148
        1-sided test, actual power (HA2: mu1 > mu2): 0.964564
          2-sided test, required N (HA1: mu1 < mu2): 22
        2-sided test, actual power (HA1: mu1 < mu2): 0.954564
          2-sided test, required N (HA2: mu1 > mu2): 212
        2-sided test, actual power (HA2: mu1 > mu2): 0.977456
          2-sided test, required N (HA2: mu1 <>mu2): 24
        2-sided test, actual power (HA2: mu1 <>mu2): 0.955544
























|newpage|






Pearson's rho, 2 correlated samples: tests (p-values)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_test(rho, rh0, n, alpha=0.05, rtype=1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results of tests for Pearson's rho, 2 correlated samples. 




    **Parameters:**

    :mean:   The mean of the sample.

    :mean0:   The reference mean.

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals




    Let `(X_1, X_2, \ldots, X_N)` denote a random sample of size `N` from a normal distribution with mean `\rho` and variance `\sigma^2`, and let

    .. math:: \overline{x}_1 = \frac{1}{N} \sum_{i=1}^N X_i \quad \text{and } s^2 = \frac{1}{N-1} \sum_{i=1}^N (X_i - \overline{x}_1)

    be the usual sample estimates of the unkown population mean `\rho` and unkown population variance `\sigma^2`. Then Student's t-test can be used to test hypotheses concerning `\rho` with regard to a reference value `\rho_0`.

    Let `F_t\left(\cdot, \nu\right)` denote the CDF (see section \ref{tDistributionCDF}) and let `t_{\nu,\alpha}` denote the `\alpha`-quantile (see section \ref{tDistributionQuantile}) of the `t`-distribution with `\nu` degrees of freedom. Define

    .. math:: t= \frac{\overline{x}_1-\rho_0}{s}, \quad s=\sqrt{s_1^2 /N}, \quad \nu=N-1.


    Then `p`-values and rejection criteria for `H_0` can be calculated as summarized below


|spacingstart|

     =========================================================  =================================================================  =================================================================
                 Test problem                                         `p`-value                                                           Reject `H_0`                                           
     =========================================================  =================================================================  ================================================================= 
       `H_{01}: \rho \leq \rho_0` vs `H_{A1}: \rho > \rho_0`            `F_t\left(-t, \nu\right)`                                           `t > t_{\nu;1-\alpha}`                                    
       `H_{02}: \rho \geq \rho_0` vs `H_{A2}: \rho < \rho_0`            `F_t\left(t, \nu\right)`                                            `t > t_{\nu;\alpha}`                                      
       `H_{03}: \rho = \rho_0` vs `H_{A3}: \rho \neq \rho_0`            `F_t\left(t, \nu\right)-F_t\left(-t, \nu\right)`                    `t > t_{\nu;1-\alpha/2}` or `t > t_{\nu;\alpha/2}`        
     =========================================================  =================================================================  =================================================================

|spacingend|


    The test can also be expressed in terms of a correlation coefficient `r` between the combined `X` and an indicator variable, where `t` and `r` are related by

    .. math:: r=\frac{t}{\sqrt{t^2+\nu}}, \quad t= \nu \frac{r}{1-r^2}.


    An actual call to the function, requesting Student's t-test with description, the critical value for a two-sided test, the p-value for `H_{03}` (in the case of `\textsf{TTest}` this is `\rho_1 \neq \rho_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1Test(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, resultstring:='All')

        Input
        VariableVariable1
        CommonN22
        Mean.Group15.24
        Mean.Group24.05
        StDev.Group11.5
        StDev.Group23.5
        Pearson'srho0.7
        Pearson'srho0.reference0.2

        Pearson'srho
        ParameterResult
        df
        rho0.1-alpha(1-sided)
        rho0.1-alpha(2-sided)
        p-value(H01:rho>=0)
        p-value(H02:rho<=0)
        p-value(H03:rho=0)
        p-value(H01:rho>=rho0)
        p-value(H02:rho<=rho0)
        p-value(H03:rho=rho0)
        p-value(H04:rho^2=rho0^2)






|newpage|



Pearson's rho, 2 correlated samples: confidence intervals
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_ci(rho, rh0, n, alpha=0.05, rtype=1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results of confidence intervals for Pearson's rho, 2 correlated samples. 






    **Parameters:**

    :mean:   The mean of the sample.

    :mean0:   The reference mean.

    :sd:     The standard deviation of the sample

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals



    Let `A_1=t_{\nu,\alpha} \cdot s` and `A_2=t_{\nu,\alpha/2} \cdot s`, where `s` and `\nu` are defined in (\ref{eq:TTest1}), and `t_{\nu,\alpha}` denotes the `\alpha`-quantile of the (central) `t`-distribution with `\nu` degrees of freedom (see section \ref{tDistributionQuantile}). 


|spacingstart|

     =========================================================  ============================================================================================
       Type                                                          Confidence Interval (Difference of Means)                   
     =========================================================  ============================================================================================
       Left-sided                                                    `-\infty \leq \rho_1 - \rho_0 \leq (\overline{x}_1-\rho_0)  + A_1`                        
       Right-sided                                                  `(\overline{x}_1-\rho_0 ) - A_1 \leq \rho_1 - \rho_0 \leq +\infty`                         
       Two-sided                                                    `(\overline{x}_1-\rho_0 ) - A_2 \leq \rho_1 - \rho_0 \leq (\overline{x}_1-\rho_0 ) + A_2`   
     =========================================================  ============================================================================================

|spacingend|



    An actual call to the function, requesting Student's t-test with description, the critical value for a two-sided test, the p-value for `H_{03}` (in the case of \textsf{TTest} this is `\rho_1 \neq \rho_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, alpha=0.05, resultstring)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Pearson's rho
        Parameter Result
        df
        rho0. 1 - alpha(1 - sided)
        rho0 . 1 - alpha(2 - sided)
        rho. CI Upper Limit (2-sided)
        rho. estimate
        rho. CI Lower Limit (2-sided)
        rho. CI - Length(2 - sided)










|newpage|


Pearson's rho, 2 correlated samples:: power 
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_power(rho, rho0, n, alpha=0.05, rtype=1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of power calculations for Pearson's rho, 2 correlated samples.




    **Parameters:**

    :rho:   The mean of the sample.

    :rho0:   The reference mean.

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals



    Let `\sigma_1^2 = \sigma^2` and `\nu=N-1`. Define


    .. math:: \widetilde{\rho} = \frac{\rho_1-\rho_0}{\sigma} \text{ and } \delta = \sqrt{N} \widetilde{\rho}.


    Let `F_{t'}\left(\cdot, \nu, \delta \right)` denote the CDF of the (singly) noncentral `t`-distribution with `\nu` degrees of freedom and noncentrality parameter `\delta` and let `t_{\nu,\alpha}` denote the `\alpha`-quantile of the central `t`-distribution with `\nu` degrees of freedom. Then the power for accepting `H_A` at the confidence level `\alpha` can be calculated as summarized below:

|spacingstart|

     ==================  ====================================  ======================================  =============================================================================================================
       Test                   Null Hypothesis                        Alternative                             Power                                                                                                  
     ==================  ====================================  ======================================  =============================================================================================================
       1 sided               `H_{01}: \rho \leq \rho_0`              `H_{A1}: \rho > \rho_0`                  `F_{t'}\left(-t_{\nu;1-\alpha}, \nu, \delta \right)`                                                      
       1 sided               `H_{02}: \rho \geq \rho_0`              `H_{A2}: \rho < \rho_0`                  `F_{t'}\left(t_{\nu;1-\alpha}, \nu, \delta \right)`                                                       
       2 sided               `H_{03}: \rho = \rho_0`                 `H_{A1}: \rho > \rho_0`                  `F_{t'}\left(-t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                    
       2 sided               `H_{03}: \rho = \rho_0`                 `H_{A1}: \rho > \rho_0`                  `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                     
       2 sided               `H_{03}: \rho = \rho_0`                 `H_{A3}: \rho \neq \rho_0`               `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)-F_t\left(-t_{\nu;1-\alpha/2}, \nu\, \delta \right)`  
     ==================  ====================================  ======================================  =============================================================================================================

|spacingend|




    An actual call to the function, requesting Student's t-test with description, the critical calue for a two-sided test, the power for `H_{A3}` (in the case of \textsf{TTest} this is `\rho_1 \neq \rho_2`), for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, n:=22, alpha:=0.05)


        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05
        Pearson's rho 0.7
        Pearson's rho0. reference 0.2

        Pearson's rho
        Parameter Result
        df
        rho0. 1 - alpha(1 - sided)
        rho0 . 1 - alpha(2 - sided)
        Power (HA1: rho > rho0)
        Power (HA2: rho < rho0)
        Power (HA3: rho <> rho0)
        Power (HA4: rho^2 <> rho0^2)






|newpage|



Pearson's rho, 2 correlated samples:: sample size calculation 
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_samplesize(rho, rho0, n, alpha=0.05, beta=0.1, rtype=1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of power calculations for Pearson's rho, 2 correlated samples.





    **Parameters:**

    :rho:   The mean of the sample.

    :rho0:   The reference mean.

    :n:     The sample size

    :alpha:     The alpha-level used for confidence intervals

    :beta:     The beta-level used for power



    Let `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)` denote the sample size function of the (singly) noncentral `t`-distribution (see section \ref{NoncentralTDistributionSampleSize} ) for a given confidence level `\alpha`, power `\beta` and noncentrality parameter `\widetilde{\rho}` (as defined in equation \ref{eq:TTestPower1}. The required total sample size `N` can be calculated as summarized below



|spacingstart|

     ==================  ====================================  ======================================  =============================================================
       Test                   Null Hypothesis                        Alternative                             Minimal sample size                                    
     ==================  ====================================  ======================================  =============================================================
       1 sided               `H_{01}: \rho \leq \rho_0`              `H_{A1}: \rho > \rho_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       1 sided               `H_{02}: \rho \geq \rho_0`              `H_{A2}: \rho < \rho_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \rho = \rho_0`                 `H_{A1}: \rho > \rho_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \rho = \rho_0`                 `H_{A1}: \rho > \rho_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
       2 sided               `H_{03}: \rho = \rho_0`                 `H_{A3}: \rho \neq \rho_0`               `N2_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`    
     ==================  ====================================  ======================================  =============================================================

|spacingend|





    Note that the returned value of `N` will in general not be an integer, and rounding up may be required.

    An actual call to the function, requesting an upper sample size estimate (and actual power) for `\alpha = 0.95`, `\beta=0.1` , and standard deviations `\sigma_1=\sigma_2=1` , means `\rho_1=2.3` and `\rho_2=4.5`,   would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, alpha:=0.05, beta:=0.1)
                                                 df: 21
                                difference of means: 1.19
                                   t-value (=delta): 3.721063
                                t(1-alpha, 1-sided): 1.720743
                                t(1-alpha, 2-sided): 2.079614
          1-sided test, required N (HA1: mu1 < mu2): 18
        1-sided test, actual power (HA1: mu1 < mu2): 0.974564
          1-sided test, required N (HA2: mu1 > mu2): 148
        1-sided test, actual power (HA2: mu1 > mu2): 0.964564
          2-sided test, required N (HA1: mu1 < mu2): 22
        2-sided test, actual power (HA1: mu1 < mu2): 0.954564
          2-sided test, required N (HA2: mu1 > mu2): 212
        2-sided test, actual power (HA2: mu1 > mu2): 0.977456
          2-sided test, required N (HA2: mu1 <>mu2): 24
        2-sided test, actual power (HA2: mu1 <>mu2): 0.955544








