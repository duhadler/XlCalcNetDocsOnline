

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_hypergeo_nc_fisher: 

Noncentral hypergeometric distribution, Fisher alternatives
===============================================================================



.. py:class:: ctx.dist_hypergeo_nc_fisher(n1, m1, N, theta)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The noncentral hypergeometric distribution (Fisher alternatives) is the conditional distribution of one of two binomial random variables `X_1` and `X_2`, given that their sum is fixed.
    The distribution arises as the power function for Fisher's (1934) exact test of independence in a `2 \times 2` contingency table. 

    If `X_i` has parameters `n_i`, `p_i = 1 - q_i`, and `N = n_1 + n_2`, `\theta = p_1 q_2 /(q_1p_2)` then

    .. math:: Pr[X_1 = x|X_1 + X_2 = m_1] = \text{h}(x; n_1, m_1, N, \theta), 

    where `\text{h}(x; n_1, m_1, N, \theta)` is given below. There are other noncentral hypergeometric distributions as well.

    See also: Wikipedia :cite:p:`WikipediaDis102`, :cite:t:`Johnson2005` page 293.



|cr|

.. method:: dist_hypergeo_nc_fisher.pmf(x)

    Returns `\text{pmf}_X(x)`, the probability mass function (pmf) of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math:: \text{pmf}_X(x) = \text{h}(x; n_1, m_1, N, \theta) = \frac{\binom{n_1}{x} \binom{n_2}{m_1-x}\theta^x}{\binom{n_2}{m_1} {}_2F_1(-n_1, -m_1;n_2+1-m_1; \theta)}, 

    where `\theta = p_1 q_2 /(q_1p_2)` and `\text{max}(0, m_1-n_2 )\le x \le \text{min}(n_1,m_1)`. 

    The following recursions are used for the PMF (see Wikipedia):

    .. math:: \text{h}(x; n_1, m_1, N, \theta)= \frac{(m_1-x+1)(n_1-x+1) \theta}{x(m_2-n_1+x)} \text{h}(x-1; n_1, m_1, N, \theta)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pmf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_hypergeo_nc_fisher.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math:: \text{cdf}_X(x) = \sum_{j=\max(0,n+K-N)}^{k} \text{pmf}_X(j).



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", hypergeometric(mu, sigma).pmf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_hypergeo_nc_fisher.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math:: \text{sf}_X(x) = \sum_{j=k+1}^{\min(K,n)} \text{pmf}_X(j).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", hypergeometric(mu, sigma).pmf(x))
        sf: 6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_hypergeo_nc_fisher.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives).

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", hypergeometric(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeo_nc_fisher.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q).

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", hypergeometric(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_hypergeo_nc_fisher.g_x(t)

    Returns `G_X(t)`, the probability generating function of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math::  G(t) = \frac{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta t)}{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeo_nc_fisher.c_x(t)

    Returns `C_X(t)`, the characteristic function of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math::  G(z) = \frac{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta z)}{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta)}  

    .. math::  C_X(t) = G(e^{it})  .


    .. math::  C_X(t) = \frac{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta e^{it})}{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeo_nc_fisher.m_x(t)

    Returns `M_X(t)`, the moment generating function of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math:: M_X(t) =  G(e^{t}). 


    .. math::  M_X(t) = \frac{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta e^{t})}{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta)}  

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("m_x: ", hypergeometric(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_hypergeo_nc_fisher.k_x(t, k = 0)

    Returns `K_X(t)`, the cumulant generating function of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives):

    .. math:: K_X(t) = \log  \left[  G(e^{t})  \right].

    .. math:: K_X(t) = \log  \left[  \frac{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta e^{t})}{{}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta)}  \right].

    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", hypergeometric(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00









|cr|

.. method:: dist_hypergeo_nc_fisher.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following an noncentral hypergeometric distribution (Fisher alternatives) (Wikipedia). The raw moments are calculated from the factorial moments:

    .. math::  \mu'_{[r]} = \frac{n_1! m_1! (n_2-m_1)! \cdot {}_2F_1(r-n_1, r-m_1; r+n_2+1-m_1; \theta)}{(n_1-r)! (m_1-r)! (n_2-m_1+r)! \cdot {}_2F_1(-n_1, -m_1; n_2+1-m_1; \theta)}  


    where `{}_2F_1(\cdot)` is the Gauss hypergeometric function (see  :ref:`hyp2f1() <rst_mpm_hyp2f1>`.)


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00





|cr|

.. method:: dist_hypergeo_nc_fisher.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following an noncentral hypergeometric distribution (Fisher alternatives). The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", hypergeometric(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00







