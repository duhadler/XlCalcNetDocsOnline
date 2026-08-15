




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

Multiple comparisons of means
================================================================================



|newpage|


Scheffé F-test: p-value
--------------------------------------------------------------------------

.. method:: ctx.scheffe_test(mean, sd, n, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Scheffé F-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Scheff%C3%A9%27s_method

    See also: Kirk, p.121; Röhr p. 270


    .. math:: \psi(S) = \sqrt{(p-1) F_{\alpha; \nu_1, \nu_2}} \sqrt{MS_{Err} \sum_{j=1}^p \frac{c_j^2}{n_j}}

    .. math:: \frac{\sum_{j=1}^p c_j \bar{x}_{i}}{MS_{Err} \sum_{j=1}^p \frac{c_j^2}{n_j}} \sim (p-1) F_{\alpha; \nu_1, \nu_2}


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        StDev. Group 3 3.5

        Scheffe Test
        Parameter A vs Rest B vs Rest C vs Rest
        Variable Variable Variable Variable
        df 63 63 63
        Difference of means 1.19 -0.595 -0.595
        t-value (=delta) 1.52619985 -0.763099925 -0.763099925
        t . 1 - alpha(1 - sided) 1.669402222 1.669402222 1.669402222
        t . 1 - alpha(2 - sided) 1.998340543 1.998340543 1.998340543
        test. p-value (H01: µ1 >= µ2) 0.131965171 0.448251923 0.448251923
        test. p-value (H02: µ1 <= µ2) 0.395895513 1.344755769 1.344755769
        test. p-value (H03: µ1 = µ2) 0.318660397 0.748395757 0.748395757




    Scheffé F-test: confidence interval
    --------------------------------------------------------------------------------------------------------

    .. method:: ctx.scheffe_ci(mean, sd, n, rho=none)

        where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Scheffé F-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Scheff%C3%A9%27s_method


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        StDev. Group 3 3.5
        Type 1 Error 0.05

        Scheffe Test. CI
        Parameter A vs Rest B vs Rest C vs Rest
        Variable Variable Variable Variable
        df 63 63 63
        Difference of means 1.19 -0.595 -0.595
        t-value (=delta) 1.52619985 -0.763099925 -0.763099925
        t . 1 - alpha(1 - sided) 1.669402222 1.669402222 1.669402222
        t . 1 - alpha(2 - sided) 1.998340543 1.998340543 1.998340543
        µ1 -µ2. CI - Length(2 - sided) 2.748134897 0.963134897 0.963134897
        µ1 - µ2. CI Upper Limit (2-sided) -0.368134897 -2.153134897 -2.153134897
        µ1 - µ2. CI Lower Limit (2-sided) 3.116269794 3.116269794 3.116269794






Scheffé F-test: power
--------------------------------------------------------------------------------------------------

.. method:: ctx.scheffe_power(mean, sd, n, alpha=0.05, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Scheffé F-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Scheff%C3%A9%27s_method


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 4.05
        StDev. Group 1 1.5
        StDev. Group 2 3.5
        StDev. Group 3 3.5
        Type 1 Error 0.05

        Scheffe Test. Power
        Parameter A vs Rest B vs Rest C vs Rest
        Variable Variable Variable Variable
        df 63 63 63
        Difference of means 1.19 -0.595 -0.595
        t-value (=delta) 1.52619985 -0.763099925 -0.763099925
        t . 1 - alpha(1 - sided) 1.669402222 1.669402222 1.669402222
        t . 1 - alpha(2 - sided) 1.998340543 1.998340543 1.998340543
        1-sided test. power (HA1: µ1 < µ2) 0.000802878 0.186751203 0.186751203
        1-sided test. power (HA2: µ1 > µ2) 0.446280461 0.008201358 0.008201358
        2-sided test. power (HA1: µ1 < µ2) 0.000266811 0.113439166 0.113439166
        2-sided test. power (HA2: µ1 > µ2) 0.32383362 0.003348175 0.003348175
        2-sided test. power (HA3: µ1 <> µ2) 0.324100432 0.116787342 0.116787342
        test. Pr[Mean1 < Mean 2] 0.06348005 0.777298098 0.777298098
        test. Pr[Mean1 > Mean 2] 0.93651995 0.222701902 0.222701902






Scheffé F-test: sample size
--------------------------------------------------------------------------------------------------

.. method:: ctx.scheffe_samplesize(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Scheffé F-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Scheff%C3%A9%27s_method






|newpage|



Tukey-Kramer q-test: p-value
--------------------------------------------------------------------------------------------------------

.. method:: ctx.tukey_kramer_test(mean, sd, n, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Tukey-Kramer q-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Tukey%27s_range_test


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 3.05
        StDev. Group 1 1.5
        StDev. Group 2 1.5
        StDev. Group 3 1.5

        Tukey. test
        Parameter A - B A - C B - C
        Variable Variable Variable Variable
        df 63 63 63
        Difference of means 1.19 2.19 1
        t-value (=delta) 2.631189 4.842272194 2.211083194
        t . 1 - alpha(2 - sided). t-test 1.998340543 1.998340543 1.998340543
        t . 1 - alpha(2 - sided) HSD test 2.400325653 2.400325653 2.400325653
        t-test. p-value (H01: µ1 >= µ2) 0.01068454 8.68857E-06 0.030667389
        Bonferroni t-test. p-value (H02: µ1 <= µ2) 0.032053621 2.60657E-05 0.092002166
        Tukey HSD-test. p-value (H03: µ1 = µ2) 0.028417641 2.5665E-05 0.077047764






|newpage|


Tukey-Kramer q-test: confidence interval
--------------------------------------------------------------------------------------------------------

.. method:: ctx.tukey_kramer_ci(mean, sd, n, alpha=0.05, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Tukey-Kramer q-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Tukey%27s_range_test

    .. math:: L \pm T \cdot \sqrt{MQR } \tfrac{1}{2} \left(\sum_{i=1}^p |c_i| \right), \quad T = \frac{1}{\sqrt{N}} \cdot q_{\alpha: p; n-p}

    See also: Röhr page 272-3,  Hochberg page 83.

    .. math:: \psi(TK) = q_{\alpha: p; \ nu} \sqrt{\tfrac{1}{2} MS_Err \left({1}{n_j} + {1}{n_j}  \right)}

    See also: Kirk, page 120, Hochberg, page 92.


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 3.05
        StDev. Group 1 1.5
        StDev. Group 2 1.5
        StDev. Group 3 1.5
        Type 1 Error 0.05

        Tukey. CI
        Parameter A - B A - C B - C
        Variable Variable Variable Variable
        df 63 63 63
        Difference of means 1.19 2.19 1
        t-value (=delta) 2.631189 4.842272194 2.211083194
        t . 1 - alpha(2 - sided). t-test 1.998340543 1.998340543 1.998340543
        t . 1 - alpha(2 - sided) HSD test 2.400325653 2.400325653 2.400325653
        µ1 -µ2. CI - Length(2 - sided) 2.275588123 3.275588123 2.085588123
        µ1 - µ2. CI Upper Limit (2-sided) 0.104411877 1.104411877 -0.085588123
        µ1 - µ2. CI Lower Limit (2-sided) 2.171176245 2.171176245 2.171176245





Tukey-Kramer q-test: power
--------------------------------------------------------------------------------------------------

.. method:: ctx.tukey_kramer_power(mean, sd, n, alpha=0.05, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Tukey-Kramer q-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Tukey%27s_range_test

    See also: https://www.real-statistics.com/one-way-analysis-of-variance-anova/power-tukey-hsd-test/


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 3.05
        StDev. Group 1 1.5
        StDev. Group 2 1.5
        StDev. Group 3 1.5
        Type 1 Error 0.05

        Power
        Parameter A - B A - C B - C
        Variable Variable Variable Variable
        df 63 63 63
        Difference of means 1.19 2.19 1
        t-value (=delta) 2.631189 4.842272194 2.211083194
        t . 1 - alpha(2 - sided). t-test 1.998340543 1.998340543 1.998340543
        t . 1 - alpha(2 - sided) HSD test 2.400325653 2.400325653 2.400325653
        1-sided test. power (HA1: µ1 < µ2) NA NA NA
        1-sided test. power (HA2: µ1 > µ2) NA NA NA
        2-sided test. power (HA1: µ1 < µ2) 4.44894E-07 7.18173E-13 3.34712E-06
        2-sided test. power (HA2: µ1 > µ2) 0.592974974 0.991730949 0.430285937
        2-sided test. power (HA3: µ1 <> µ2) 0.592975419 0.991730949 0.430289284
        test. Pr[Mean1 < Mean 2] 0.004254335 6.41814E-07 0.013515038
        test. Pr[Mean1 > Mean 2] 0.995745665 0.999999358 0.986484962







Tukey-Kramer q-test: sample size
--------------------------------------------------------------------------------------------------

.. method:: ctx.tukey_kramer_samplesize(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Tukey-Kramer q-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Tukey%27s_range_test





|newpage|






Fisher-Hayter test: p-value
--------------------------------------------------------------------------------------------------

.. method:: ctx.fisher_hayter_test(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Fisher-Hayter test for a CR or RB Anova. 

    See also: Kirk textbook

    See also: https://imaging.mrc-cbu.cam.ac.uk/statswiki/FAQ/hfmore




REGWQ test (CR only): p-value
--------------------------------------------------------------------------------------------------

.. method:: ctx.rEGWQ_test(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Tukey-Kramer q-test for a CR or RB Anova. 
    See also: Omer 2013.

    See also: SAS documentation

    See also: https://www.real-statistics.com/one-way-analysis-of-variance-anova/unplanned-comparisons/regwq-post-hoc-test/





Newman-Keuls test (CR only): p-value
--------------------------------------------------------------------------------------------------

.. method:: ctx.newman_keuls_test(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Tukey-Kramer q-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Newman%E2%80%93Keuls_method




Duncan-test (CR only): p-value
--------------------------------------------------------------------------------------------------

.. method:: ctx.duncan_test(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Tukey-Kramer q-test for a CR or RB Anova. 

    https://en.wikipedia.org/wiki/Duncan%27s_new_multiple_range_test






|newpage|


Dunnett t-test: p-value
--------------------------------------------------------------------------------------------------------

.. method:: ctx.dunnett_test(mean, sd, n, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Dunnett t-test for a CR or RB Anova. 

    See also: https://en.wikipedia.org/wiki/Dunnett%27s_test

    We are using the same conventions as in section  :ref:`Anova: Overview <rst_anova_models>`.


    .. math:: L \pm T \cdot \sqrt{MQR } \left(\sum_{i=1}^p |c_i| \right), \quad T = |T|^{(\alpha)}_{k-1; \nu, (r_{ij})}

    See Hochberg, 147

    .. math:: tD' =  \frac{c_i \bar{x}_{i} + c_j \bar{x}_{j}}{\sqrt{MS_{Err} \left(\frac{c_i^2}{n_i} + \frac{c_j^2}{n_j}\right) }   }



    See Kirk, page 112 and Hochberg, page 147



    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 3.05
        StDev. Group 1 1.5
        StDev. Group 2 1.5
        StDev. Group 3 1.5

        Dunnett. test
        Parameter A - B A - C
        Variable Variable Variable
        df 63 63
        Difference of means 1.19 2.19
        t-value (=delta) 2.631189 4.842272194
        t . 1 - alpha(1 - sided) 1.950318085 1.950318085
        t . 1 - alpha(2 - sided) 2.262684158 2.262684158
        test. p-value (H01: µ1 >= µ2) 0.010078544 8.62178E-06
        test. p-value (H02: µ1 <= µ2) 0.999394003 0.999999933
        test. p-value (H03: µ1 = µ2) 0.020156912 1.72436E-05







|newpage|


Dunnett t-test: confidence interval
--------------------------------------------------------------------------------------------------------

.. method:: ctx.dunnett_ci(mean, sd, n, alpha=0.05, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Dunnett tests for a CR or RB Anova. 

    See also: https://en.wikipedia.org/wiki/Dunnett%27s_test


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 3.05
        StDev. Group 1 1.5
        StDev. Group 2 1.5
        StDev. Group 3 1.5
        Type 1 Error 0.05

        Dunnett. CI
        Parameter A - B A - C
        Variable Variable Variable
        df 63 63
        Difference of means 1.19 2.19
        t-value (=delta) 2.631189 4.842272194
        t . 1 - alpha(1 - sided) 1.950318085 1.950318085
        t . 1 - alpha(2 - sided) 2.262684158 2.262684158
        µ1 -µ2. CI - Length(2 - sided) 2.213337414 3.213337414
        µ1 - µ2. CI Upper Limit (2-sided) 0.166662586 1.166662586
        µ1 - µ2. CI Lower Limit (2-sided) 2.046674829 2.046674829





|newpage|



Dunnett t-test: power
--------------------------------------------------------------------------------------------------

.. method:: ctx.dunnett_power(mean, sd, n, alpha=0.05, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Dunnett tests for a CR or RB Anova. 

    See also: https://en.wikipedia.org/wiki/Dunnett%27s_test


    .. code-block:: pycon

        >>> from mpfunlab import mpm
        >>> xreal.AnovaTest(means:=[5.24, 4.05, 7.01], sd:=1.5, n:=[22,11,16])

        Input
        Variable Variable 1
        Common N 22
        Mean. Group 1 5.24
        Mean. Group 2 4.05
        Mean. Group 3 3.05
        StDev. Group 1 1.5
        StDev. Group 2 1.5
        StDev. Group 3 1.5
        Type 1 Error 0.05

        Dunnett. Power
        Parameter A - B A - C
        Variable Variable Variable
        df 63 63
        Difference of means 1.19 2.19
        t-value (=delta) 2.631189 4.842272194
        t . 1 - alpha(1 - sided) 1.950318085 1.950318085
        t . 1 - alpha(2 - sided) 2.262684158 2.262684158
        1-sided test. power (HA1: µ1 < µ2) 3.2724E-06 1.12831E-11
        1-sided test. power (HA2: µ1 > µ2) 0.751275964 0.997858356
        2-sided test. power (HA1: µ1 < µ2) 8.27724E-07 1.67643E-12
        2-sided test. power (HA2: µ1 > µ2) 0.644365029 0.99441096
        2-sided test. power (HA3: µ1 <> µ2) 0.644365856 0.99441096
        test. Pr[Mean1 < Mean 2] 0.004254335 6.41814E-07
        test. Pr[Mean1 > Mean 2] 0.995745665 0.999999358



|newpage|



Dunnett t-test: sample size
--------------------------------------------------------------------------------------------------

.. method:: ctx.dunnett_sample_size(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Dunnett tests for a CR or RB Anova. 

    See also: https://en.wikipedia.org/wiki/Dunnett%27s_test





|newpage|


Marcus test: p-value
--------------------------------------------------------------------------------------------------

.. method:: ctx.marcus_test(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Marcus-test for a CR or RB Anova. 




|newpage|


Hsu test: p-value
--------------------------------------------------------------------------------------------------

.. method:: ctx.hsu_test(mean, sd, alpha=0.05, beta=0.1, rho=none)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Hsu-test for a CR or RB Anova. 

    See also: https://www.real-statistics.com/one-way-analysis-of-variance-anova/unplanned-comparisons/hsus-mcb/




