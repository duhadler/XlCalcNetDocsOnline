

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





Basic classical statistical tests (stratified)
=========================================================================






Student t-test for 1 sample: tests (p-values) and confidence intervals
-------------------------------------------------------------------------------

.. method:: ctx.student_t_1sample_test(n, mu0, mean, stdev, alpha, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns tests and/or confidence intervals for Student's t-test for 1 sample with sample size *N* (`N`), reference mean *mu0* (`\mu_0`), sample mean *mean* (`\overline{x}_1`),  sample standard deviation *stdev* (`s`) and type I error *alpha* (`\alpha`). See also: Wikipedia :cite:p:`WikipediaStat001`.

    The following boolean keyword arguments determine the output:

    **I**: if ``True``, the input parameters are shown.

    **D**: if ``True``, the descriptive statistics is shown.

    **T**: if ``True``, the tests are shown.

    **C**: if ``True``, the confidence intervals are shown.

    **Onesided**: if ``True``, onesided tests and/or confidence intervals are shown.

    **Twosided**: if ``True``, onesided tests and/or confidence intervals are shown.



    **Examples**



    *   Skellam: poisson with same rate back to back


    *   Laplace: exponential with same rate back to back


    *   Asymmetric Laplace: exponential with different rates back to back


    *   Hyperexponential distribution





    **Examples**



    1.   Skellam: poisson with same rate back to back


    2.   Laplace: exponential with same rate back to back


    3.   Asymmetric Laplace: exponential with different rates back to back


    4.   Hyperexponential distribution




    Let `(X_1, X_2, \ldots, X_N)` denote a random sample of size `N` from a normal distribution with mean `\mu` and variance `\sigma^2`, and let

    .. math:: \overline{x}_1 = \frac{1}{N} \sum_{i=1}^N X_i \quad \text{and } s^2 = \frac{1}{N-1} \sum_{i=1}^N (X_i - \overline{x}_1)^2

    be the usual sample estimates of the unkown population mean `\mu` and unkown population variance `\sigma^2`. Then Student's t-test can be used to test hypotheses concerning `\mu` with regard to a reference value `\mu_0`.

    Let `F_t\left(\cdot, \nu\right)` denote the CDF and let `t_{\nu,\alpha}` denote the `\alpha`-quantile of the `t`-distribution with `\nu` degrees of freedom. Define

    .. math:: t= \frac{\overline{x}_1-\mu_0}{s}, \quad s=\sqrt{s_1^2 /N}, \quad \nu=N-1.


    The test can also be expressed in terms of a correlation coefficient `r` between the combined `X` and an indicator variable, where `t` and `r` are related by

    .. math:: r=\frac{t}{\sqrt{t^2+\nu}}, \quad t= \nu \frac{r}{1-r^2}.


    Then `p`-values and rejection criteria for `H_0` can be calculated as summarized below: |spacingstart|

    =========================================================  =================================================================  =================================================================
                Test problem                                         `p`-value                                                           Reject `H_0`                                           
    =========================================================  =================================================================  ================================================================= 
        `H_{01}: \mu \leq \mu_0` vs `H_{A1}: \mu > \mu_0`            `F_t\left(-t, \nu\right)`                                           `t > t_{\nu;1-\alpha}`                                    
        `H_{02}: \mu \geq \mu_0` vs `H_{A2}: \mu < \mu_0`            `F_t\left(t, \nu\right)`                                            `t > t_{\nu;\alpha}`                                      
        `H_{03}: \mu = \mu_0` vs `H_{A3}: \mu \neq \mu_0`            `F_t\left(t, \nu\right)-F_t\left(-t, \nu\right)`                    `t > t_{\nu;1-\alpha/2}` or `t > t_{\nu;\alpha/2}`        
    =========================================================  =================================================================  =================================================================

    Let `A_1=t_{\nu,\alpha} \cdot s` and `A_2=t_{\nu,\alpha/2} \cdot s`. Then the confidence intervals at confidence level `1-\alpha` can be calculated as follows: 

    =========================================================  ============================================================================================
        Type                                                          Confidence Interval (Difference of Means)                   
    =========================================================  ============================================================================================
        Left-sided                                                    `-\infty \leq \mu_1 - \mu_0 \leq (\overline{x}_1-\mu_0)  + A_1`                        
        Right-sided                                                  `(\overline{x}_1-\mu_0 ) - A_1 \leq \mu_1 - \mu_0 \leq +\infty`                         
        Two-sided                                                    `(\overline{x}_1-\mu_0 ) - A_2 \leq \mu_1 - \mu_0 \leq (\overline{x}_1-\mu_0 ) + A_2`   
    =========================================================  ============================================================================================

    **Examples** |spacingend|

    An actual call to the function, requesting Student's t-test for 1 independent sample of size 10 and standard deviation 1 each, with means 2.3 and reference mean = 1.0, and a type I error `\alpha=0.05` would be



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> n = 16; mu0 = 4.05; mean = 5.24; stdev = 1.5; alpha=0.05
        >>> mpm.student_t_1sample_test(n, mu0, mean, stdev, alpha, \
          I=True, D=True, T=True, C=True, Onesided=True, Twosided = True)
        Student t-test for 1 sample: tests and confidence intervals
                                  Parameter  Variable1
                                          n: [16.0]
                                       mean: [5.24]
                                        mu0: [4.05]
                                      stdev: [1.5]
                                      alpha: [0.05]
                         degrees of freedom: [15.0]
                        difference of means: [1.19]
               rho-tilde = (mean-mu0)/stdev: [0.7933333]
                           t-value (=delta): [3.173333]
                        t(1-alpha, 1-sided): [1.75305]
                        t(1-alpha, 2-sided): [2.13145]
            test, p-value (H01: mu1 >= mu0): [0.9968508]
            test, p-value (H02: mu1 <= mu0): [0.003149208]
             test, p-value (H03: mu1 = mu2): [0.006298416]
        mu1 - mu0, CI upper limit (1-sided): [1.847394]
        mu1 - mu0, CI lower limit (1-sided): [0.5326061]
        mu1 - mu0, CI upper limit (2-sided): [1.989294]
        mu1 - mu0, CI lower limit (2-sided): [0.3907064]
             mu1 - mu0, CI-length (2-sided): [1.598587]


    An actual call to the function, requesting Student's t-test with description, the critical value for a two-sided test, the p-value for `H_{03}` for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> n = [10, 20, 30]; mu0 = 1.0; mean = [4.5,4.6]; stdev = [1,2,3,4]; alpha=0.015
        >>> mpm.student_t_1sample_test(n, mu0, mean, stdev, alpha, \
          I=True, D=True, T=True, C=True, Onesided=True, Twosided = True)
        Student t-test for 1 sample: tests and confidence intervals
                                  Parameter  Variable1
                                          n: [10.0 20.0 30.0 30.0]
                                       mean: [4.5 4.6 4.6 4.6]
                                        mu0: [1.0 1.0 1.0 1.0]
                                      stdev: [1.0 2.0 3.0 4.0]
                                      alpha: [0.015 0.015 0.015 0.015]
                         degrees of freedom: [9.0, 19.0, 29.0, 29.0]
                        difference of means: [3.5, 3.6, 3.6, 3.6]
               rho-tilde = (mean-mu0)/stdev: [3.5, 1.8, 1.2, 0.9]
                           t-value (=delta): [11.06797, 8.049845, 6.572671, 4.929503]
                        t(1-alpha, 1-sided): [2.573804, 2.345648, 2.282175, 2.282175]
                        t(1-alpha, 2-sided): [2.998203, 2.674209, 2.585992, 2.585992]
            test, p-value (H01: mu1 >= mu0): [0.9999992, 0.9999999, 0.9999998, 0.9999846]
            test, p-value (H02: mu1 <= mu0): [7.642012e-7, 7.64034e-8, 1.67689e-7, 1.542853e-5]
             test, p-value (H03: mu1 = mu2): [1.528402e-6, 1.528068e-7, 3.35378e-7, 3.085705e-5]
        mu1 - mu0, CI upper limit (1-sided): [4.313908, 4.649005, 4.849998, 5.266665]
        mu1 - mu0, CI lower limit (1-sided): [2.686092, 2.550995, 2.350002, 1.933335]
        mu1 - mu0, CI upper limit (2-sided): [4.448115, 4.795942, 5.016406, 5.488542]
        mu1 - mu0, CI lower limit (2-sided): [2.551885, 2.404058, 2.183594, 1.711458]
             mu1 - mu0, CI-length (2-sided): [1.89623, 2.391885, 2.832812, 3.777083]








|newpage|


Student t-test for 1 sample: power calculations
-------------------------------------------------------------------------------

.. method:: ctx.student_t_1sample_power(n, mu0, mu1, sigma, alpha,**kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns power calculations for Student's t-test for 1 sample with sample size *N* (`N`), reference mean *mu0* (`\mu_0`), population mean *mu1* (`\mu_1`),  population standard deviation *sigma* (`\sigma`) and type I error *alpha*  (`\alpha`). See also: Wikipedia :cite:p:`WikipediaStat001`.


    The following boolean keyword arguments determine the output:

    **I**: if ``True``, the input parameters are shown.

    **D**: if ``True``, the descriptive statistics is shown.

    **P**: if ``True``, the power calculations are shown.

    **E**: if ``True``, some extra calculations are shown.

    **Onesided**: if ``True``, onesided tests are shown.

    **Twosided**: if ``True``, twosided tests are shown.



    Let `\sigma_1^2 = \sigma^2` and `\nu=N-1` and define `\displaystyle  \widetilde{\rho} = \frac{\mu_1-\mu_0}{\sigma} \text{ and } \delta = \sqrt{N} \widetilde{\rho}`.
    Let `F_{t'}\left(\cdot, \nu, \delta \right)` denote the CDF of the noncentral `t`-distribution with `\nu` degrees of freedom and noncentrality parameter `\delta` and let `t_{\nu,\alpha}` denote the `\alpha`-quantile of the central `t`-distribution with `\nu` degrees of freedom. Then the power for accepting `H_A` at the confidence level `\alpha` can be calculated as summarized below: |spacingstart|

    ==================  ====================================  ======================================  =============================================================================================================
        Test                   Null Hypothesis                        Alternative                             Power                                                                                                
    ==================  ====================================  ======================================  =============================================================================================================
        onesided               `H_{01}: \mu \leq \mu_0`              `H_{A1}: \mu > \mu_0`               `F_{t'}\left(-t_{\nu;1-\alpha}, \nu, \delta \right)`                                                      
        onesided               `H_{02}: \mu \geq \mu_0`              `H_{A2}: \mu < \mu_0`               `F_{t'}\left(t_{\nu;1-\alpha}, \nu, \delta \right)`                                                       
        twosided               `H_{03}: \mu = \mu_0`                 `H_{A1}: \mu > \mu_0`               `F_{t'}\left(-t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                    
        twosided               `H_{03}: \mu = \mu_0`                 `H_{A2}: \mu < \mu_0`               `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                     
        twosided               `H_{03}: \mu = \mu_0`                 `H_{A3}: \mu \neq \mu_0`            `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)-F_t\left(-t_{\nu;1-\alpha/2}, \nu\, \delta \right)`  
    ==================  ====================================  ======================================  =============================================================================================================

    **Examples** |spacingend|


    An actual call to the function, requesting Student's t-test with description, the critical calue for a two-sided test, the power for `H_{A3}`  for 2 independent samples of size 10 and standard deviation 1 each, with means 2.3 and 4.5, and a type I error `\alpha=0.05` would be




    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> n = 56; mu0 = 4.05; mu1 = 5.24; sigma = 1.5; alpha=0.05
        >>> mpm.student_t_1sample_power(n, mu0, mu1, sigma, alpha, \
          I=True, D=True, T=True, C=True, Onesided=True, Twosided = True)
        Student t-test for 1 sample: power
                                    Parameter  variable1
                                            n: [56.0]
                                          mu0: [4.05]
                                          mu1: [5.24]
                                        sigma: [1.5]
                                        alpha: [0.05]
                           degrees of freedom: [55.0]
                                    mu1 - mu0: [1.19]
                                          rho: [0.6249392]
                                        delta: [5.936763]
                          t(1-alpha, 1-sided): [1.673034]
                          t(1-alpha, 2-sided): [2.004045]
         1-sided test, power (HA1: mu1 < mu2): 7.46e-08
         1-sided test, power (HA2: mu1 > mu2): 0.974564
         2-sided test, power (HA1: mu1 < mu2): 1.65e-08
         2-sided test, power (HA2: mu1 > mu2): 0.943648
        2-sided test, power (HA1: mu1 <> mu2): 0.943648
                            Pr(Mean1 < Mean2): 9.92e-05
                            Pr(Mean1 > Mean2): 0.999901

    Another example



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> n = [10, 20, 30]; mu0 = 1.0; mu1 = [4.5,4.6]; sigma = [1,2,3,4]; alpha=0.015
        >>> mpm.student_t_1sample_power(n, mu0, mu1, sigma, alpha, \
          I=True, D=True, T=True, C=True, Onesided=True, Twosided = True)
        Student t-test for 1 sample: power
                                    Parameter  variable1
                                            n: [10.0 20.0 30.0 30.0]
                                          mu0: [1.0 1.0 1.0 1.0]
                                          mu1: [4.5 4.6 4.6 4.6]
                                        sigma: [1.0 2.0 3.0 4.0]
                                        alpha: [0.015 0.015 0.015 0.015]
                           degrees of freedom: [9.0, 19.0, 29.0, 29.0]
                                    mu1 - mu0: [3.5, 3.6, 3.6, 3.6]
                                          rho: [0.965173, 0.8793576, 0.7735231, 0.675211]
                                        delta: [11.06797, 8.049845, 6.572671, 4.929503]
                          t(1-alpha, 1-sided): [2.573804, 2.345648, 2.282175, 2.282175]
                          t(1-alpha, 2-sided): [2.998203, 2.674209, 2.585992, 2.585992]
         1-sided test, power (HA1: mu1 < mu2): 7.46e-08
         1-sided test, power (HA2: mu1 > mu2): 0.974564
         2-sided test, power (HA1: mu1 < mu2): 1.65e-08
         2-sided test, power (HA2: mu1 > mu2): 0.943648
        2-sided test, power (HA1: mu1 <> mu2): 0.943648
                            Pr(Mean1 < Mean2): 9.92e-05
                            Pr(Mean1 > Mean2): 0.999901




|newpage|


Student t-test for 1 sample: sample size calculation
-------------------------------------------------------------------------------

.. method:: ctx.student_t_1sample_samplesize(mu0, mu1, sigma, alpha, beta, **kwargs)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns sample size calculations for Student's t-test for 1 sample with reference mean *mu0* (`\mu_0`), population mean *mu1* (`\mu_1`), population standard deviation *sigma* (`\sigma`), type I error *alpha*  (`\alpha`), and type II error *beta*  (`\beta`). See also: Wikipedia :cite:p:`WikipediaStat001`.


    The following boolean keyword arguments determine the output:

    **I**: if ``True``, the input parameters are shown.

    **D**: if ``True``, the descriptive statistics is shown.

    **N**: if ``True``, the sample size calculations are shown.

    **P**: if ``True``, the actual power (for the calculated sample size) is shown.

    **Onesided**: if ``True``, onesided tests are shown.

    **Twosided**: if ``True``, twosided tests are shown.



    Let `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)` denote the sample size function of the (singly) noncentral `t`-distribution  for a given type I error `\alpha`, type II error `\beta` and noncentrality parameter  `\displaystyle \widetilde{\rho} = \frac{\mu_1-\mu_0}{\sigma}`. The required total sample size `N` can be calculated as summarized below. Note that the returned value of `N` will in general not be an integer, and rounding up may be required. |spacingstart|

    ==================  ====================================  ======================================  =============================================================
        Test                   Null Hypothesis                        Alternative                             Minimal sample size                                    
    ==================  ====================================  ======================================  =============================================================
        onesided               `H_{01}: \mu \leq \mu_0`              `H_{A1}: \mu > \mu_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
        onesided               `H_{02}: \mu \geq \mu_0`              `H_{A2}: \mu < \mu_0`                  `N_{t'}\left(\alpha, \beta, -\widetilde{\rho} \right)`     
        twosided               `H_{03}: \mu = \mu_0`                 `H_{A1}: \mu > \mu_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
        twosided               `H_{03}: \mu = \mu_0`                 `H_{A2}: \mu < \mu_0`                  `N_{t'}\left(\alpha, \beta, -\widetilde{\rho} \right)`     
        twosided               `H_{03}: \mu = \mu_0`                 `H_{A3}: \mu \neq \mu_0`               `N^{(2)}_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`    
    ==================  ====================================  ======================================  =============================================================

    **Examples** |spacingend|


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



Chi-squared-test for the variance of 1 sample: tests (p-values)
-------------------------------------------------------------------------------------

.. method:: ctx.chi2_variance_1sample_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Text


    Then `p`-values and rejection criteria for `H_0` can be calculated as summarized below


|spacingstart|

    ==========================================================================  =================================================================  =================================================================
                Test problem                                                               `p`-value                                                           Reject `H_0`                                           
    ==========================================================================  =================================================================  ================================================================= 
      `H_{01}: \sigma\leq \sigma_0` vs `H_{A1}: \sigma> \sigma_0`                     `F_t\left(-t, \nu\right)`                                           `t > t_{\nu;1-\alpha}`                                    
      `H_{02}: \sigma\geq \sigma_0` vs `H_{A2}: \sigma< \sigma_0`                     `F_t\left(t, \nu\right)`                                            `t > t_{\nu;\alpha}`                                      
      `H_{03}: \sigma= \sigma_0` vs `H_{A3}: \sigma\neq \sigma_0`                     `F_t\left(t, \nu\right)-F_t\left(-t, \nu\right)`                    `t > t_{\nu;1-\alpha/2}` or `t > t_{\nu;\alpha/2}`        
    ==========================================================================  =================================================================  =================================================================

|spacingend|


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1Test(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, resultstring:='All')

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5

        Chi2-test for the variance of 1 sample
        Parameter Result
        df 21
        Variance-Ratio 0.183673469
        Chi2-value 3.857142857
        Chi2. 1 - alpha(1 - sided) 10.28289778
        Chi2 . 1 - alpha(2 - sided) 35.47887591
        Chi2-test. p-value (H01: s1 >= s0) 1.44636E-05
        Chi2-test. p-value (H02: s1 <= s0) 0.999985536
        Chi2-test. p-value (H03: s1 = s0) 2.89273E-05






|newpage|


Chi-squared-test for the variance of 1 sample: confidence intervals
-------------------------------------------------------------------------------------

.. method:: ctx.chi2_variance_1sample_ci(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Text


    Then confidence intervals can be calculated as summarized below

|spacingstart|

    =========================================================  =============================================================================================================
      Type                                                          Confidence Interval (Difference of Means)                   
    =========================================================  =============================================================================================================
      Left-sided                                                    `-\infty \leq \sigma_1 - \sigma_0 \leq (\overline{x}_1-\sigma_0)  + A_1`                        
      Right-sided                                                  `(\overline{x}_1-\sigma_0 ) - A_1 \leq \sigma_1 - \sigma_0 \leq +\infty`                         
      Two-sided                                                    `(\overline{x}_1-\sigma_0 ) - A_2 \leq \sigma_1 - \sigma_0 \leq (\overline{x}_1-\sigma_0 ) + A_2`   
    =========================================================  =============================================================================================================

|spacingend|

    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1Test(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, resultstring:='All')

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        Type 1 Error 0.05

        Chi2-test for the variance of 1 sample. CI
        Parameter Result
        df 21
        Variance-Ratio 0.183673469
        Chi2-value 3.857142857
        Chi2. 1 - alpha(1 - sided) 10.28289778
        Chi2 . 1 - alpha(2 - sided) 35.47887591
        s1. CI - Length(2 - sided) 3.263229852
        s1. CI Upper Limit (2-sided) 4.595008236
        s1. CI Lower Limit (2-sided) 1.331778383









|newpage|

Chi-squared-test for the variance of 1 sample: power
-------------------------------------------------------------------------------------

.. method:: ctx.chi2_variance_1sample_power(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Chi-squared-test for the variance of 1 sample, under `H_0`.

    Then the power for accepting `H_A` at the confidence level `\alpha` can be calculated as summarized below:

|spacingstart|

    ==================  ====================================  ======================================  ==============================================================================================================================
      Test                   Null Hypothesis                        Alternative                             Power                                                                                                  
    ==================  ====================================  ======================================  ==============================================================================================================================
      1 sided               `H_{01}: \sigma\leq \sigma_0`              `H_{A1}: \sigma> \sigma_0`                  `F_{t'}\left(-t_{\nu;1-\alpha}, \nu, \delta \right)`                                                      
      1 sided               `H_{02}: \sigma\geq \sigma_0`              `H_{A2}: \sigma< \sigma_0`                  `F_{t'}\left(t_{\nu;1-\alpha}, \nu, \delta \right)`                                                       
      2 sided               `H_{03}: \sigma= \sigma_0`                 `H_{A1}: \sigma> \sigma_0`                  `F_{t'}\left(-t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                    
      2 sided               `H_{03}: \sigma= \sigma_0`                 `H_{A1}: \sigma> \sigma_0`                  `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)`                                                     
      2 sided               `H_{03}: \sigma= \sigma_0`                 `H_{A3}: \sigma\neq \sigma_0`               `F_{t'}\left(t_{\nu;1-\alpha/2}, \nu, \delta \right)-F_t\left(-t_{\nu;1-\alpha/2}, \nu\, \delta \right)`  
    ==================  ====================================  ======================================  ==============================================================================================================================

|spacingend|



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.StudentT1Test(mean:=5.24, mean0:=4.05, sd:=1.5, n:=22, resultstring:='All')

        Input
        Variable Variable 1
        Common N 22
        Mean, Group 1 5,24
        Mean, Group 2 4,05
        StDev, Group 1 1,5
        StDev, Group 2 3,5
        Type 1 Error 0,05

        Chi2-test for the variance of 1 sample , power
        Parameter Result
        df 21
        Variance-Ratio 0,183673469
        Chi2-value 3,857142857
        Chi2, 1 - alpha(1 - sided) 10,28289778
        Chi2 , 1 - alpha(2 - sided) 35,47887591
        1-sided test, power (HA1: s1 < s0) 1,44636E-05
        1-sided test, power (HA2: s1 > s0) 1,44636E-05
        2-sided test, power (HA1: s1 < s0) 1,44636E-05
        2-sided test, power (HA2: s1 > s0) 1,44636E-05
        2-sided test, power (HA3: s1 <> s0) 1,44636E-05




|newpage|

Chi-squared-test for the variance of 1 sample: sample size
-------------------------------------------------------------------------------------

.. method:: ctx.chi2_variance_1sample_samplesize(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Chi-squared-test for the variance of 1 sampl, under `H_0`.


    The required total sample size `N` can be calculated as summarized below

|spacingstart|

    ==================  ====================================  ======================================  ==============================================================================
      Test                   Null Hypothesis                        Alternative                             Minimal sample size                                    
    ==================  ====================================  ======================================  ==============================================================================
      1 sided               `H_{01}: \sigma\leq \sigma_0`              `H_{A1}: \sigma> \sigma_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
      1 sided               `H_{02}: \sigma\geq \sigma_0`              `H_{A2}: \sigma< \sigma_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
      2 sided               `H_{03}: \sigma= \sigma_0`                 `H_{A1}: \sigma> \sigma_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
      2 sided               `H_{03}: \sigma= \sigma_0`                 `H_{A1}: \sigma> \sigma_0`                  `N_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`     
      2 sided               `H_{03}: \sigma= \sigma_0`                 `H_{A3}: \sigma\neq \sigma_0`               `N2_{t'}\left(\alpha, \beta, \widetilde{\rho} \right)`    
    ==================  ====================================  ======================================  ==============================================================================

|spacingend|


    Note that the returned value of `N` will in general not be an integer, and rounding up may be required.








