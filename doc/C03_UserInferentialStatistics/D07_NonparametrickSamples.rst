




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

Nonparametric statistical tests, k samples
==========================================================================




Jonckheere-Terpsta `S` test: p-value and confidence interval, continuous data
-------------------------------------------------------------------------------

.. method:: ctx.jterpsta_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Jonckheere-Terpsta `S` test, under `H_0`. See also Wikipedia :cite:p:`WikipediaStat190`.



    Consider `k` independent groups `X_i` of sizes `n_i, i=1 \ldots k`. The Jonckheere-Terpsta statistic is defined as

    .. math::  J = \sum_{i<j}^{c} U_{ij} = \sum_{i=1}^{c-1} \sum_{j=i+1}^{c} U_{ij}

    where `U_{ij}` is Mann-Whitney's `U` calculated for groups `X_i` and `X_j`.













Jonckheere-Terpsta `S` test,  Shorack alternatives: power and sample size
-------------------------------------------------------------------------------

.. method:: ctx.jterpsta_power_shorack(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Jonckheere-Terpsta `S` test, under Shorack alternatives. See also Wikipedia :cite:p:`WikipediaStat190`.





Jonckheere-Terpsta `S` test (stratified), Milton alternatives: power and sample size
---------------------------------------------------------------------------------------------

.. method:: ctx.jterpsta_power_milton(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Jonckheere-Terpsta `S` test, under Milton alternatives. See also Wikipedia :cite:p:`WikipediaStat190`.






Spearman test for 2 correlated samples: p-value
-------------------------------------------------------------------------------

.. method:: ctx.spearman_test(x, k, n, method='default')

    Returns the results of the Spearman test, under `H_0`. See also: Wikipedia :cite:p:`WikipediaStat200`.





Generalized Page `L` test: p-value 
-------------------------------------------------------------------------------

.. method:: ctx.page_l_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Page `L` test under `H_0`.  See also: Wikipedia :cite:p:`WikipediaStat210`.


    Page's test (see Page, 1963) is a test for ordered alternatives in a randomised block
    design. We consider `n` independent random vectors such that `(X_{i1}, \ldots , X_{ik})` 
    has a continuous distribution function `F_i`. 

    Within each block rank scores `1, \ldots k` are assigned to `k` treatments. Let `\beta_j`
    denote the block effect of the `j`th treatment. The null hypothesis is `\text{H}_0:  \beta_1 = \cdots = \beta_t` and the alternative hypothesis is `\text{H}_1:  \beta_1 \le \cdots \le \beta_k`
    with at least one strict inequality. 
    Let `\rho_i` be Spearman's rank correlation coefficient between  `(X_{i1}, \ldots , X_{ik})` and its own order statistic, 
    and let `D_i = (k-1)k(k+1)(1-\rho_i)/6`. The statistic `L` is defined as


    .. math:: L =  \sum_{j=1}^{n} D_i =  \sum_{j=1}^{n} jR_j,


    where `R_j` is the sum of the `n` ranks assigned to treatment `j`. The pmf of the distribution of `S_i` is obtained by enumeration of all permutations from `1, \ldots k`, followed by calculation of the `D_i`-statistic. From the pmf, the cumulants and the probability generating function are obtained.   










Generalized Page `L` test, Milton alternatives: power and sample size
---------------------------------------------------------------------------------------------

.. method:: ctx.page_l_milton_power(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Generalized Page `L` test, under Milton alternatives.









Generalized Quade `L` test: p-value
-------------------------------------------------------------------------------

.. method:: ctx.quade_l_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Quade `L` test under `H_0`. 




Friedman's S, and related linear rank statistics
-------------------------------------------------------------------------------


.. method:: ctx.friedman_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Friedman test under `H_0`. See also Wikipedia :cite:p:`WikipediaStat220`.





Kruskal-Wallis' H, and related linear rank statistics
-------------------------------------------------------------------------------


.. method:: ctx.kruskal_wallis_test(x, k, n, method='default')

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    Returns the results of the Kruskal-Wallis test under `H_0`. See also Wikipedia :cite:p:`WikipediaStat230`.






