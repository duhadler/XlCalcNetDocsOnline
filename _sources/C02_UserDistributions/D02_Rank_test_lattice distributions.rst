

.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |br| raw:: html

   <br />




|newpage|


Discrete (lattice) distribution functions related to (stratified) rank tests
========================================================================================




Kendall `S` (or \tau) distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.KendallTauPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Kendall  `S` (or \tau)  distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. See also  Wikipedia :cite:p:`WikipediaDis27`, :cite:t:`Noether1967`, :cite:t:`vandeWiel2000`.

Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Kendall tau distribution.

The null distribution can be calculated as follows: Let `p_N(t) = \text{Pr}[T_N=t]`. Then the following recurrence relation holds:

.. math::    p_N(t) = p_N(t-1) + [p_{N-1}(t) - p_{N-1}(t-N)] /N,

where `p_N(t) = 0` for `t<0` or `t>N(N-1)/2`, and `p_N(0)=1/N!`.





Mann-Whitney `U` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.MannWhitneyUPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Mann-Whitney `U` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

See also  Wikipedia :cite:p:`WikipediaDis28`, :cite:t:`Murakami2009`, :cite:t:`Robillard1972`, [vandeWiel2000`  and :cite:t:`Zimmermann1985b`.


Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Mann-Whitney U distribution. The null distribution of the MW test can be calculated as follows: Let `p_{n,m}(u)` denote the probability that `U=u` in samples of size `n` and `m`. Then (see :cite:t:`Zimmermann1985b`)

.. math::    (m+n) p_{n,m}(u) = n p_{n-1,m}(u-m) + m p_{n,m-1}(u) = n p_{n-1,m}(u) + m p_{n,m-1}(u-n)




Jonckheere-Terpsta `S` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.JTerpstaSPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Jonckheere-Terpsta `S` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


See also  Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`Murakami2009`, :cite:t:`Robillard1972`, [vandeWiel2000`  and :cite:t:`Skillings1980`.


Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

.. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

where the sum is over all `x` with positive `p(\cdot)`.





Spearman `\rho` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.SpearmanRhoPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Page `L` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


See also  Wikipedia :cite:p:`WikipediaDis29`, [vandeWiel2000`  and :cite:t:`Skillings1980` .


Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

.. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

where the sum is over all `x` with positive `p(\cdot)`.






Sign test distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.SigntestPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Sign test distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

See also  Wikipedia :cite:p:`WikipediaDis26`, [vandeWiel2000`, :cite:t:`Bennett1972` and :cite:t:`Zimmermann1985a`.

Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Wilcoxon signed rank T distribution. The null distribution can be calculated as follows: Let `p_N(w)` denote the probability `\text{Pr}[W_N=w]` in a sample of size `N`. Then the following recurrence relation holds (see :cite:t:`Zimmermann1985a`) :

.. math:: p_N(w) = \tfrac{1}{2} \left( p_{N-1}(w) + p_{N-1}(w-N)\right).




Wilcoxon `T` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.WilcoxonPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Wilcoxon distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

See also  Wikipedia :cite:p:`WikipediaDis26`, :cite:t:`Fellingham1964`, [vandeWiel2000`, :cite:t:`Bennett1972` and :cite:t:`Zimmermann1985a`.

Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Wilcoxon signed rank T distribution. The null distribution can be calculated as follows: Let `p_N(w)` denote the probability `\text{Pr}[W_N=w]` in a sample of size `N`. Then the following recurrence relation holds (see :cite:t:`Zimmermann1985a`) :

.. math:: p_N(w) = \tfrac{1}{2} \left( p_{N-1}(w) + p_{N-1}(w-N)\right).







Page `L` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.PageLPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Page `L` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


See also  Wikipedia :cite:p:`WikipediaDis29`, [vandeWiel2000`  and :cite:t:`Skillings1980`.


Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`:

.. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

where the sum is over all `x` with positive `p(\cdot)`.




Quade `L` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: math53lib.QuadeLPmfVector(x, n, lambda)

Returns the vector of all pmf values of the Quade `L` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


See also  Wikipedia :cite:p:`WikipediaDis29`, [vandeWiel2000`  and :cite:t:`Skillings1980`.


Returns `\text{pmf}(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`:

.. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

where the sum is over all `x` with positive `p(\cdot)`.




