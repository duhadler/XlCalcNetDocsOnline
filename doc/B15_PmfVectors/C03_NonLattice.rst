






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />









|newpage|


Discrete (non-lattice) distribution functions related to rank tests
========================================================================================







Cochran `S` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.cochran_s_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Cochran `S` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`vandeWiel2000`, and :cite:t:`Skillings1980`.


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.




Friedman `S` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.friedman_s_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Friedman `S` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

    See also: https://www.statsdirect.com/help/nonparametric_methods/friedman.htm

    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`vandeWiel2000` and :cite:t:`Skillings1980`.


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.



Quade `S` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.quade_s_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Quade `S` distribution distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`vandeWiel2000`, and :cite:t:`Skillings1980` .


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.




Kruskal-Wallis `H` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.kruskal_wallis_h_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Kruskal-Wallis `H` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`Murakami2009`, :cite:t:`Robillard1972`, :cite:t:`vandeWiel2000`,  and :cite:t:`Skillings1980` .


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.


