




Statistical Distributions
**************************************************************************************************



For a general introduction to probability distributions, see: Wikipedia :cite:p:`WikipediaDef01`, Wikipedia :cite:p:`WikipediaDef02`, Wikipedia :cite:p:`WikipediaDef03`, Wikipedia :cite:p:`WikipediaDef04`.




The design of this library has been influenced by :cite:t:`Bristow2013`, :cite:t:`Witkovsky2017`.



See also Wikipedia :cite:p:`WikipediaDef05` and :cite:t:`Abramowitz1970` (from which the following introductory text has been taken, with small edits).

A real-valued function `F(x)` is termed a (univariate) cumulative distribution function (cdf) or simply distribution function if

1. `F(x)` is non-decreasing, i.e. `F(x_1) \le F(x_2)` for `x_1 \le x_2`.

2. `F(x)` is everywhere continuous from the right, i.e. `F(x) = \lim \limits_{\epsilon \to 0+} F(x+\epsilon)`

3. `F(-\infty) = 0, F(\infty) = 1`.

The function `F(x)` signifies the probability of the event "`X \le x`", i.e. Pr `\{X \le x \} = F(x),` where `X` is a random variable, and thus describes the cdf of `X.` The two principle types of distribution functions are termed *discrete* and *continuous*.

*Discrete distributions*: Discrete distributions are characterized by the random variable `X` taking on an enumerable number of values `\ldots x_{-1}, x_0, x_1, \ldots` with point probabilities `p_n = \text{Pr} \{X = x_n \} \ge 0,` which only need to be subject to the restriction `\sum_n p_n =1.` The corresponding distribution function can then be written as

.. math:: F(x) = \text{Pr} \{X \le x \} = \sum_{x_n \le x} p_n,

where the summation is over all values of x for which `x_n \le x`. The set `\{ x_n \}` of values for which `p_n > 0` is termed the domain of he random variable `X.` A discrete distribution of a random variable is called a *lattice distribution* if there exists numbers `a` and `b \ne 0` such that every possible value of `X` can be represented in the form `a+bn` where `n` takes only integral values.

*Continuous distributions*: Continuous distributions are characterized by `F(x)` being continuous. If  `F(x)` is absolutely continuous then `F(x)` possesses a derivative `F'(x) = f(x)` and the cdf can be written as

.. math:: F(x) = \text{Pr} \{X \le x \} = \int_{-\infty}^x f(t) \mathrm{d} t.

The derivative `f(x)` is termed the probability density function (pdf), and the values of `x` for which `f(x) > 0` make up the domain of the variable `X`.






.. toctree ::
    :caption: Statistical Distributions
    :maxdepth: 5


    C01_Intro.rst

    C02_BaseClass.rst

    C03_BaseClassCont.rst

    C04_BaseClassDiscrete.rst




    C05_ElementaryPart/index.rst


    C06_ErrorFunction/index.rst


    C07_IncompleteGamma/index.rst


    C08_IncompleteBeta/index.rst


    C09_Noncentral/index.rst


    C10_MCP/index.rst


    C11_Multivariate/index.rst



    C12_MiscContinuous/index.rst


    C13_ElementaryDiscrete/index.rst


    C14_LattticeRank/index.rst


    C15_NonLatticeRank/index.rst







