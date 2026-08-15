




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

Nonparametric statistical tests, 1 or 2 samples
============================================================================




Sign test: p-value and confidence interval
-------------------------------------------------------------------------------

.. method:: ctx.sign_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Sign test, under `H_0`. See also: Wikipedia :cite:p:`WikipediaStat130`, Wikipedia :cite:p:`WikipediaStat131`.






Sign test: power and sample size
-------------------------------------------------------------------------------

.. method:: ctx.sign_test_power(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Sign test, under general alternatives. See also: Wikipedia :cite:p:`WikipediaStat130`, Wikipedia :cite:p:`WikipediaStat131`.





Brown-Mood median test for 2 independent samples: p-value and confidence interval
--------------------------------------------------------------------------------------------

.. method:: ctx.brown_mood_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Brown-Mood median test for 2 independent samples, under `H_0`. See also: Wikipedia :cite:p:`WikipediaStat140`.





Brown-Mood median test for 2 independent samples: power and sample size
-------------------------------------------------------------------------------

.. method:: ctx.brown_mood_power(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Brown-Mood median test for 2 independent samples, under general alternatives. See also: Wikipedia :cite:p:`WikipediaStat140`.







Wilcoxon's signed rank `T` test: p-value and confidence interval, continuous data
------------------------------------------------------------------------------------------

.. method:: ctx.signed_rank_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Wilcoxon's signed rank `T` test, under `H_0`. See also: Wikipedia :cite:p:`WikipediaStat150`.


    We consider `N` continuously distributed random variables `D_i,i=1\ldots N`, with common pdf `h_0`. In a sample `(d_1,\ldots,d_N)` of size `N` let `r_i` be the rank of `d_i` in the ordered sample.

    The test criterion of Wilcoxon's Signed Rank is `T_N=\sum_{i=1}^N S(d_i)r_i`, where `S(d_i)=1` for `x>0` and `S(d_i)=0` for `x<0`.
    `T_N` can assume values between 0 and `\tfrac{1}{2}N(N+1)` in steps of 1.











Wilcoxon's signed rank test `T` (Bennett alternatives): power and sample size
-------------------------------------------------------------------------------

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

.. method:: ctx.signed_rank_power(x, k, n, method='default')

    Returns the results of the Wilcoxon's signed rank test `T`, under Bennett alternatives. See also: Wikipedia :cite:p:`WikipediaStat150`.







Mann-Whitney `U` test (stratified): p-value and confidence interval, continuous data
---------------------------------------------------------------------------------------------

.. method:: ctx.mannwhitney_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Mann-Whitney `U` test, under `H_0`. See also: Wikipedia :cite:p:`WikipediaStat160`.

    See also: Mehrotra (2006): Rank-Based Analyses of Stratified Experiments: Alternatives to the van Elteren Test



    Let `x1,\ldots,x_m` and `y1,\ldots,y_n` be two sets of measurements, which we denote by `X` and `Y`. The test criterion `U` of the Mann-Whitney test is then

    .. math:: U = \sum_{i=1}^m \sum_{j=1}^n \text{sgn}(x_i - y_j)











Mann-Whitney `U` test:  (Lehmann alternatives): power and sample size
-------------------------------------------------------------------------------

.. method:: ctx.mannwhitney_power_lehmann(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Mann-Whitney `U` test, under Lehmann alternatives. See also: Wikipedia :cite:p:`WikipediaStat160`.






Mann-Whitney `U` test:  (Milton alternatives): power and sample size
-------------------------------------------------------------------------------

.. method:: ctx.mannwhitney_power_milton(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Mann-Whitney `U` test, under Milton alternatives. See also: Wikipedia :cite:p:`WikipediaStat160`.





Siegel-Tukey test: p-value and confidence interval
-------------------------------------------------------------------------------

.. method:: ctx.siegel_tukey_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Siegel-Tukey test, under `H_0`. See also: Wikipedia :cite:p:`WikipediaStat170`.

    See also: (Lowenstein 2017)







Kendall test for 2 correlated samples: p-value
-------------------------------------------------------------------------------

.. method:: ctx.kendall_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Kendall test for 2 correlated samples, under under `H_0`. See also Wikipedia :cite:p:`WikipediaStat180`.


    Let `(X_1, Y_1),...,(X_N, Y_N)` be independent random variables, the `X_i` with a continuous distribution `F_0`, the `Y_i` with df `G_0`. Let `R_i` and `S_i` be the ranks of `X_i` and `Y_i`, respectively.
    The Kendall rank correlation coefficient `\tau` is defined as

    .. math::    \tau = \frac{1}{N(N-1)} \sum_{i=1}^N \sum_{j=1}^N \text{sgn}(R_i - R_j)  \text{sgn}(S_i - S_j)

    and its transformation `T_N` is defined by `T_N = \tfrac{1}{4} (\tau+1)N(N-1)`. `T_N` can assume values between 0 and `N(N-1)/2`.














Theill test for 2 correlated samples: p-value and confidence interals
-------------------------------------------------------------------------------

.. method:: ctx.theill_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Theill test for 2 correlated samples, under under `H_0`.

    See also: https://en.wikipedia.org/wiki/Theil%E2%80%93Sen_estimator





