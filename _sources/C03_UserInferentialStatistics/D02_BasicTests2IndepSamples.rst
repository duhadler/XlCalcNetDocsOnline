




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



Basic classical statistical tests for 2 independent samples (stratified)
===================================================================================



Student t-test for 2 independent samples: tests (p-values)
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2isamples_test(mean, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results for Student's t-test for for 2 independent samples. 

    See also: https://en.wikipedia.org/wiki/Student%27s_t-test#Independent_(unpaired)_samples


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
        >>> ereal.StudentT1Test(means:=[5.24, 4.05], sd:=1.5, n:=22)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5

        Student's t-test for 2 samples
        Parameter Result
        df 42
        Difference of means 1.19
        t-value (=delta) 1.465798594
        t1 - alpha(1 - sided) 1.681952357
        t1 - alpha(2 - sided) 2.018081703
        test. p-value (H01: µ1 >= µ2) 0.924924828
        test. p-value (H02: µ1 <= µ2) 0.075075172
        test. p-value (H03: µ1 = µ2) 0.150150344





|newpage|



Student t-test for 2 independent samples:  confidence intervals
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2isamples_ci(mean, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results for Student's t-test for for 2 independent samples. 





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
        >>> ereal.StudentT1CI(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, alpha=0.05, resultstring)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05

        Student's t-test for 2 samples
        Parameter Result
        df 42
        Difference of means 1.19
        t-value (=delta) 1.465798594
        t1 - alpha(1 - sided) 1.681952357
        t1 - alpha(2 - sided) 2.018081703
        µ1 - µ2. CI - Length (2 - sided) 3.276735613
        µ1 - µ2. CI Upper Limit (2-sided) 2.828367806
        µ1 - µ2. CI Lower Limit (2-sided) -0.448367806










|newpage|




Student t-test for 2 independent samples: power 
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2isamples_power(mean, sd, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of Student's t-test for 2 independent samples: power and sample size.





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
        >>> ereal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, n:=22, alpha:=0.05)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05

        Student's t-test for 2 samples
        Parameter Result
        df 42
        Difference of means 1.19
        t-value (=delta) 1.465798594
        t1 - alpha(1 - sided) 1.681952357
        t1 - alpha(2 - sided) 2.018081703
        1-sided test. power (HA1: µ1 < µ2) 0.001009403
        1-sided test. power (HA2: µ1 > µ2) 0.419683559
        2-sided test. power (HA1: µ1 < µ2) 0.000345576
        2-sided test. power (HA2: µ1 > µ2) 0.298885242
        2-sided test. power (HA3: µ1 <> µ2) 0.299230817
        test. Pr[Mean 1 < Mean 2] 0.071351582
        test. Pr[Mean 1 > Mean 2] 0.928648418







|newpage|


Student t-test for 2 independent samples: sample size calculation
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2isamples_samplesize(mu, sd, alpha=0.05, beta=0.1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of sample size calculations for Student's t-test for 2 independent samples




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
        >>> ereal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, alpha:=0.05, beta:=0.1)
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



Student t-test for 2 independent samples: power and sample size: failure to stratify
-----------------------------------------------------------------------------------------------

.. method:: ctx.studentt_2isamples_power2(mean, sd, n, alpha=0.05)

    Returns the results of the F-Test with `\delta>0` and `\eta>0`

    See "Butler Paolella 1999 Doubly noncentral F Draft.pdf" in "References B" for an example.






|newpage|



Student t-test for 2 independent samples: equivalence and non-inferiority
-------------------------------------------------------------------------------

.. method:: ctx.studentt_2isamples_equivalence(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Sign test, under `H_0`.

    Refer to Schuirman procedure.

    See Shieh 2019

    See also: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5012670/













|newpage|







F-test for the variances of 2 independent samples: tests (p-values)
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2isamples_test(s2, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results for the F-test for the variances of 2 independent samples. 

    See also: https://en.wikipedia.org/wiki/F-test_of_equality_of_variances





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
        >>> ereal.StudentT1Test(means:=[5.24, 4.05], sd:=1.5, n:=22)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5

        F-test for 2 variances
        Parameter Result
        df1 21
        df2 21
        Variance-Ratio 0.183673469
        F. 1 - alpha(1 - sided) 2.084188623
        F . 1 - alpha(2 - sided) 2.408589482
        F-test. p-value (H01: s1 >= s2) 0.999864065
        F-test. p-value (H02: s1 <= s2) 0.000135935
        F-test. p-value (H03: s1 = s2) 1.999728131






|newpage|


F-test for the variances of 2 independent samples: confidence intervals
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2isamples_ci(s2, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results of the confidence intervals for the F-test for the variances of 2 independent samples.





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
        >>> ereal.StudentT1CI(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, alpha=0.05, resultstring)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05

        F-test for 2 variances
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



F-test for the variances of 2 independent samples: power
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2isamples_power(s2, n, alpha=0.05)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results of the power calculation for the F-test for the variances of 2 independent samples.





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
        >>> ereal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, n:=22, alpha:=0.05)

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05

        F-test for 2 variances
        Parameter Result
        df1 21
        df2 21
        Variance-Ratio 0.183673469
        F. 1 - alpha(1 - sided) 2.084188623
        F . 1 - alpha(2 - sided) 2.408589482
        1-sided test. power (HA1: s1 < s2) 0.999864065
        1-sided test. power (HA2: s1 > s2) 0.999864065
        2-sided test. power (HA1: s1 < s2) 0.999864065
        2-sided test. power (HA2: s1 > s2) 0.999864065
        2-sided test. power (HA3: s1 <> s2) 0.999864065






|newpage|




F-test for the variances of 2 independent samples: sample size
----------------------------------------------------------------------------------------

.. method:: ctx.fratio_variance_2isamples_samplesize(s2, alpha=0.05, beta=0.1)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns results  of sample size calculations  for the variances of 2 independent samples.






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
        >>> ereal.StudentT1CI(mu1:=5.24, mu0:=4.05, sd:=1.5, alpha:=0.05, beta:=0.1)
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


































