

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_pearson_rho_nc: 

Noncentral distribution of the sample correlation coefficient
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_pearson_rho_nc(N, rho)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The noncentral distribution of Pearson's rho (the distribution of the sample correlation coefficient), with sample size `N \ge 3`, noncentrality parameter `\rho \in (-1,+1)` is a continuous distribution with the support interval `(-1,+1)`.
    See also Wikipedia :cite:p:`WikipediaDis104`, :cite:t:`Hotelling1953`, :cite:t:`Guenther1977`, :cite:t:`Winterbottom1979`, :cite:t:`Winterbottom1980`, :cite:t:`Odeh1986`, :cite:t:`Ruben1966`, :cite:t:`Subrahmaniam1983`.


    The correlation coefficient `r` in samples of size `N>2` from a non-singular bivariate normal population with correlation coefficent `\rho` can be represented in the form 

    .. math:: \tilde{r} = (z+ \tilde{\rho} \chi_{N-1})/\chi_{N-2}

    where `\tilde{r} =r/\sqrt{1-r^2}` , `\tilde{\rho} =\rho/\sqrt{1-\rho^2}`, `z` is a standardized normal variate and  `z` , `\chi_{N-1}`, and `\chi_{N-2}` are independent.

    A random variable `X` follows the distribution of Pearson's correlation coefficient with sample size `N` and noncentrality parameter `\rho`,  if `Y=X/(1-X)`  has the representation given above.





|cr|

.. method:: dist_pearson_rho_nc.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following the noncentral distribution of Pearson's rho:

    .. math:: \text{pdf}_X(x) = f_R(r, N; \rho) = \frac{(N-2)\Gamma(N-1)}{\sqrt{2\pi}\Gamma\left(N-\tfrac{1}{2}\right)} A^{N-1} C^{N-4} (1-x)^{\tfrac{3}{2}-N}{}_2F_1\left(\tfrac{1}{2},\tfrac{1}{2}; N-\tfrac{1}{2}; \tfrac{1}{2}+\tfrac{1}{2}\rho r\right),

    where `A=\sqrt{1-\rho^2},  \quad C=\sqrt{1-r^2}`, and  `{}_2F_1(\cdot)` is the Gaussian hypergeometric function.


    In the special case when `\rho =0`, the exact density function `f(r)` can be written as: 

    .. math:: f(r)={\frac {(1-r^{2})^{\frac {n-4}{2}}}{\mathbf {B} \left({\frac {1}{2}},{\frac {n-2}{2}}\right)}}.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", pearson_rho_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_pearson_rho_nc.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following the noncentral distribution of Pearson's rho:


    .. math:: \text{cdf}_X(x) = F_{R^2}(x;p,N,\rho^2) =  \int_{-1}^{x} f_{R^2}(x;p,N,\rho^2) \mathrm{d} t

    Two additional algorithms by Hotelling(1953) are also used to cover a broader range of parameters.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", pearson_rho_nc(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_pearson_rho_nc.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following the noncentral distribution of Pearson's rho:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{1} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", pearson_rho_nc(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_pearson_rho_nc.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following the noncentral distribution of Pearson's rho:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a approximation by Winterbottom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", pearson_rho_nc(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho_nc.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following the noncentral distribution of Pearson's rho:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", pearson_rho_nc(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho_nc.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following the noncentral distribution of Pearson's rho:

    .. math:: C_X(t) = \int_{-1}^{1} e^{i tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", pearson_rho_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho_nc.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following the noncentral distribution of Pearson's rho:

    .. math:: M_X(t) = \int_{-1}^{1} e^{tx} \text{pdf}_X(x) \mathrm{d} x


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", pearson_rho_nc(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_pearson_rho_nc.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function:

    .. math:: K_X(t) = \log (M_X(t))


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", pearson_rho_nc(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00






|cr|

.. method:: dist_pearson_rho_nc.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the noncentral distribution of Pearson's rho: 
    the moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{-1}^{1} x^r \text{pdf}_X(x) \mathrm{d} x


    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of Pearson's rho: 

    :cite:t:`Johnson1995`, 2nd vol, page 555, gives the following formulas:

    .. math:: \mu_{2k+1} = \frac{B((k+1)/2), (n-2)/2}{B(1/2, (n-2)/2)} (1-\rho^2)^{(n-1)/2} \times {}_3F_2 \left( \frac{k+1}{2}, \frac{n-1}{2}, \frac{n-1}{2}, \frac{n+k-1}{2}, \frac{1}{2}; \rho^2  \right)

    .. math:: \mu_{2k} = \frac{(n-2)B((k+2)/2), (n-2)/2}{B(1/2, (n-2)/2)} (1-\rho^2)^{(n-1)/2} \times {}_3F_2 \left( \frac{k+2}{2}, \frac{n}{2}, \frac{n}{2}, \frac{n+k}{2}, \frac{3}{2}; \rho^2  \right)




    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pearson_rho_nc(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_pearson_rho_nc.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the noncentral distribution of Pearson's rho. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", pearson_rho_nc(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00










**Additional methods: Results based on Fisher's z-transformation**


The generating functions and cumulants all exist, but are complicated and not useful for numerical work. Asymptotic expansions typically rely on the Fisher `z`-transform `Z(a)= \text{atanh}(a)` and its inverse `Z^{-1}(a) = \tanh(a)`.

Let `m = N - 1` and let `u_\alpha` = `\Phi^{-1}(\alpha)` be the lower `100\alpha` percentage point of the standard normal distribution. The first 4 cumulants of `Z(X)`  are given by 

.. math:: \kappa_1= \tfrac{1}{2} \log \left(\frac{1+\rho}{1-\rho}\right) + \frac{\rho}{2m} + \frac{5+\rho^2}{4m^2} + \frac{11+2\rho^2+3\rho^4}{8m^3} + O(m^{-4}),

.. math:: \kappa_2=\frac{1}{m} + \frac{4-\rho^2}{2m^2} + \frac{22-6\rho^2-3\rho^4}{6m^3} + O(m^{-4}), \quad \kappa_3=\frac{\rho^3}{m^3} + O(m^{-4}), \quad  \kappa_4=\frac{2}{m^3} + O(m^{-4}).



