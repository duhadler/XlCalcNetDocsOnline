






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />










|newpage|


Discrete (lattice) distribution functions related to (stratified) rank tests
========================================================================================





Sign test distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.signtest_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Sign test distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

    See also Wikipedia :cite:p:`WikipediaDis26`, :cite:t:`vandeWiel2000`, :cite:t:`Bennett1972` and :cite:t:`Zimmermann1985a`, and  :ref:`dist_wilcoxon() <rst_dist_wilcoxon_continuous>`.

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Wilcoxon signed rank T distribution. The null distribution can be calculated as follows: Let `p_N(w)` denote the probability `\text{Pr}[W_N=w]` in a sample of size `N`. Then the following recurrence relation holds (see :cite:t:`Zimmermann1985a`) :

    .. math:: p_N(w) = \tfrac{1}{2} \left( p_{N-1}(w) + p_{N-1}(w-N)\right).




Wilcoxon `T` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.wilcoxon_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Wilcoxon distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

    See also Wikipedia :cite:p:`WikipediaDis26`, :cite:t:`Fellingham1964`, :cite:t:`vandeWiel2000`, :cite:t:`Bennett1972` and :cite:t:`Zimmermann1985a`, and  :ref:`dist_wilcoxon() <rst_dist_wilcoxon_continuous>`.

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Wilcoxon signed rank T distribution. The null distribution can be calculated as follows: Let `p_N(w)` denote the probability `\text{Pr}[W_N=w]` in a sample of size `N`. Then the following recurrence relation holds (see :cite:t:`Zimmermann1985a`) :

    .. math:: p_N(w) = \tfrac{1}{2} \left( p_{N-1}(w) + p_{N-1}(w-N)\right).



Wilcoxon `T` distribution (under Bennett alternatives), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.wilcoxon_bennett_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Wilcoxon `T` distribution under Bennett alternatives. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

    See also Wikipedia :cite:p:`WikipediaDis26`, :cite:t:`Fellingham1964`,  :cite:t:`vandeWiel2000`, :cite:t:`Bennett1972` and :cite:t:`Zimmermann1985a`, and  :ref:`dist_wilcoxon() <rst_dist_wilcoxon_continuous>`.

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Wilcoxon signed rank T distribution. The null distribution can be calculated as follows: Let `p_N(w)` denote the probability `\text{Pr}[W_N=w]` in a sample of size `N`. Then the following recurrence relation holds (see :cite:t:`Zimmermann1985a`) :

    .. math:: p_N(w) = \tfrac{1}{2} \left( p_{N-1}(w) + p_{N-1}(w-N)\right).






Kendall `S` (or \tau) distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.kendall_tau_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Kendall  `S` (or \tau)  distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. See also Wikipedia :cite:p:`WikipediaDis27`, :cite:t:`Noether1967`,  :cite:t:`vandeWiel2000`, and :ref:`dist_kendall() <rst_dist_kendall_continuous>`.

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Kendall tau distribution.

    The null distribution can be calculated as follows: Let `p_N(t) = \text{Pr}[T_N=t]`. Then the following recurrence relation holds:

    .. math::	p_N(t) = p_N(t-1) + [p_{N-1}(t) - p_{N-1}(t-N)] /N,

    where `p_N(t) = 0` for `t<0` or `t>N(N-1)/2`, and `p_N(0)=1/N!`.





Mann-Whitney `U` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.mannwhitney_u_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Mann-Whitney `U` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

    See also Wikipedia :cite:p:`WikipediaDis28`, :cite:t:`Murakami2009`, :cite:t:`Robillard1972`, :cite:t:`vandeWiel2000` and :cite:t:`Zimmermann1985b`, and  :ref:`dist_mann_whitney() <rst_dist_mann_whitney_continuous>`.


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Mann-Whitney U distribution. The null distribution of the MW test can be calculated as follows: Let `p_{n,m}(u)` denote the probability that `U=u` in samples of size `n` and `m`. Then (see :cite:t:`Zimmermann1985b`)

    .. math::	(m+n) p_{n,m}(u) = n p_{n-1,m}(u-m) + m p_{n,m-1}(u) = n p_{n-1,m}(u) + m p_{n,m-1}(u-n)




Jonckheere-Terpsta `S` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.jterpsta_s_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Jonckheere-Terpsta `S` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`Murakami2009`, :cite:t:`Robillard1972`,  :cite:t:`vandeWiel2000`, and :cite:t:`Skillings1980` and  :ref:`dist_jterpsta() <rst_dist_jterpsta_continuous>`.


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.




Spearman `\rho` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.spearman_rho_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Page `L` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`vandeWiel2000` and :cite:t:`Skillings1980` .


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.





Page `L` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.page_l_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Page `L` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


    See also Wikipedia :cite:p:`WikipediaDis29`, :cite:t:`vandeWiel2000`, and :cite:t:`Skillings1980`.


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.




Quade `L` distribution (under `H_0`), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.quade_l_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Quade `L` distribution under `H_0`. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 


    See also Wikipedia :cite:p:`WikipediaDis29`,  :cite:t:`vandeWiel2000`,  and :cite:t:`Skillings1980`.


    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following a Jonckheere-Terpsta S distribution. Let `p(n_1,\ldots,n_k; t) = \text{Pr}[J_N=t]`. If `J_N` is based on `k` independent samples of sizes `n_1,\ldots,n_k`,  then (Skillings 1980):

    .. math:: p(n_1,\ldots,n_k; t) = \sum_{x} p(n_1,\ldots,n_k; x) \times p(n_1,\ldots,n_k; t-x)

    where the sum is over all `x` with positive `p(\cdot)`.





Mann-Whitney `U` distribution (under Lehmann alternatives), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.mannwhitney_u_lehmann_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Lehmann alternatives are of the form `F_1(x) = :cite:t:`F_0(x)]^k` or `F_1(x) = 1-[1-F_0(x)]^k`.

    See also: :cite:t:`Shorack1966`, :cite:t:`Shorack1967`.

    Under Lehmann alternatives, rank order probabilities can be expressed in closed form for `F_1 = (F_0)^k`: 
    let `S_1,\ldots,S_n` denote the ranks of `Y` in the combined sample, 
    e.g. `\text{Pr}[S_1=3,S_2=5)] = P_{3,2}(0,0,1,0,1)`. Then

    .. math::	\text{Pr}[S_1=s_1,\ldots,,S_n=s_n) = k^n \frac{n! m!}{\Gamma(n+m+1+n(k-1))} \prod_{j=1}^n \frac{\Gamma(s_j + j(k-1))}{\Gamma(s_j + (j-1)(k-1))}.

    The exact distribution under this alternative can also be calculated using recurrence relations, similar to the 
    null-distribution (Shorack_1966): 

    Let `p_{n,m}(u)` denote the probability that `U=u` in samples of size `n` and `m`. Then

    .. math:: (km+n) p_{n,m}(u) = n p_{n-1,m}(u-m) + km p_{n,m-1}(u) \quad \text{for } F_1 = (F_0)^k 

    .. math:: (km+n) p_{n,m}(u) = n p_{n-1,m}(u) + km p_{n,m-1}(u-n) \quad \text{for } F_1 = 1-(1-F_0)^k

    This recursive procedure allows the calculation of the exact noncentral distribution also for larger samples.








Mann-Whitney `U` distribution (under Milton alternatives), pmf vector
-------------------------------------------------------------------------------

.. method:: ctx.mannwhitney_u_milton_pmf_vector(x, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the vector of all pmf values of the Mann-Whitney `U` distribution under Milton alternatives. The vector is returned as a nested list of Decimals or as a mp.matrix or as a iv.matrix. 

    See also: :cite:t:`Milton1970`

    We consider `k` continuous random variables `X_i` with density functions `f_i` and sample sizes `n_i`, `i=1 \ldots k`, and `N=n_1+ \ldots +n_k`.

    Let `\textbf{U} = (U_1,\ldots,U_{N}), U_1 < \cdots < U_{N}`, denote the order statistics of the random variables `(X_{1,1},\ldots,X_{1,n_1}, \dots, X_{k,1},\ldots,X_{k,n_k})`,
    and let `\textbf{Z} = (Z_1,\ldots,Z_{N})` denote a random vector of integers `1,2,\dots,k`, where the `i^{\text{th}}` component `\textbf{Z}_i` is `i`  if `U_i` is an `X_i`.

    If  `\textbf{z} = (z_1,\ldots,z_{N})` is a fixed vector of integers `1,2,\dots,k` (with each `i` occurring `n_i` times), the probability of the rank 
    order `z`, Pr `[\textbf{Z}=\textbf{z}]`, is given by

 
    .. math:: P_{n_1,\ldots,n_k}(\textbf{z} \vert d) = n_1! \ldots n_k! \idotsint\limits_R \prod_{i=1}^{N} f_i(t_i) dt_i,

    where the region of integration `R` is `-\infty < t_1 \leq t_2  \leq \cdots  \leq t_{N} < \infty` 

    The original algorithm by  :cite:t:`Milton1970` has been developed for the normal distribution, but it has been found to also work well for the logistic distribution and for Lehmann alternatives, if the reference distribution is normal.




