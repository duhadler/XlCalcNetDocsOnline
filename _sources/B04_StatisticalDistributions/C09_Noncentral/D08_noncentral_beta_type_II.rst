

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

.. _rst_dist_logrv_beta_nc_type_II: 

Distribution of the logarithm of a noncentral Beta Type II variable
-------------------------------------------------------------------------------


.. py:class:: ctx.dist_logrv_beta_nc_type_II(a, b, lambda1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The noncentral Beta Type II distribution is a continuous probability distribution with shape parameters `a` and `b`, noncentrality parameter `\lambda_1` and the support interval `(0, 1)`.
    See also Wikipedia :cite:p:`WikipediaDis04`, MathWorld :cite:p:`WolframDis04`, BoostMath :cite:p:`BoostDis04`, :cite:t:`Wang1993`, :cite:t:`CharfunDis04`, :cite:t:`Kerns2018`, R (Statistical System) :cite:p:`RDis04`.


    A random variable `X` follows a Type I noncentral beta distribution with shape parameters `a` and `b` and noncentrality parameter `\lambda`,  if it is defined as `X = U_1/(U_1 + U_2)` where `U_1` and `U_2` are independent with `U_1 \sim \chi^2(n_1,\lambda)`, and `U_2 \sim \chi^2(n_2)`  `n_1 = 2a` and `n_2 = 2b` are the degrees of freedom, and `\lambda` is the noncentrality parameter of the noncentral `\chi^2` distribution. The random variable `Y = 1- X` is said to follow a Type II noncentral beta distribution with shape parameters `a` and `b` and noncentrality parameter `\lambda`.





|cr|

.. method:: dist_logrv_beta_nc_type_II.pdf(x)

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following 
    a Type I noncentral beta distribution:

    .. math:: \text{pdf}_X(x) = f_{\text{Beta}'}(x;a,b,\lambda) = e^{-\lambda/2} f_{\text{Beta}}(x;a,b) \times  {}_1F_1 \left((a+b), b, \tfrac{n x \lambda}{2(m+n x)}\right)

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively,  of the central Beta-distribution, and `{}_1F_1(\cdot)` is the confluent hypergeometric function. There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("pdf: ", beta_nc_type_II(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20



|cr|


.. method:: dist_logrv_beta_nc_type_II.cdf(x)

    Returns `\text{cdf}_X(x)`, the cumulative distribution function (cdf) of a random variable `X`, following a Type I noncentral beta distribution:
	
    .. math:: \text{cdf}_X(x) = F_{\text{Beta}'}(x;a,b,\lambda) =  \int_{0}^{x} f_{\text{Beta}'}(x;a,b,\lambda) \mathrm{d} t =  e^{-\lambda/2} \sum_{j=0}^{\infty}{\frac{(\lambda/2)^j}{j!} F_{\text{Beta}}(x;a+j,b) }

    and `f_{\text{Beta}}(\cdot)` and  `F_{\text{Beta}}(\cdot)`  denote the PDF and CDF, respectively,  of the central Beta-distribution, and `{}_1F_1(\cdot)` is the confluent hypergeometric function. There is no known explicit form for the quantile function `\text{cdf}^{-1}_X(x)`: It is computed using Newton iterations with starting values from a central `F` approximation.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print ("cdf: ", beta_nc_type_II(mu, sigma).pdf(x))
        6.3563523462564525615615615614561356E-20




|cr|

.. method:: dist_logrv_beta_nc_type_II.sf(x)

    Returns `\text{sf}_X(x)`, the survival function (sf) of a random variable `X`, following a Type I noncentral beta distribution:

    .. math:: \text{sf}_X(x) = 1 - \text{cdf}_X(x) = \int_{x}^{1} \text{pdf}_X(x) \mathrm{d} t.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; x = 3; 
        >>> print (" sf: ", beta_nc_type_II(mu, sigma).pdf(x))
        sf: 6.3563523462564525615615615614561356E-20



|cr|

.. method:: dist_logrv_beta_nc_type_II.qtf(q)

    Returns `\text{qtf}_X(x)`, the quantile function (qtf) of a random variable `X`, following a Type I noncentral beta distribution:

    There is no known closed form for the quantile function `\text{cdf}^{-1}_X(q)`: It is computed with Newton iterations
    where the starting values are from a approximation by Winterbottom.



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("qtf: ", beta_nc_type_II(mu, sigma).qtf(q))
        qtf: 6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta_nc_type_II.isf(q)

    Returns `\text{isf}_X(q)`, the inverse survival function (isf) of a random variable `X`, following a Type I noncentral beta distribution:

    .. math:: \text{isf}_X(q) = \text{qtf}_X(1-q) = \text{cdf}^{-1}_X(1-q).


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; q = 0.3; 
        >>> print ("isf: ", beta_nc_type_II(mu, sigma).isf(q))
        6.3563523462564525615615615614561356E+00



It is more convenient to work with `Y` rather than `X` to obtain generating functions and moments: the characteristic function, 
`C_Y(t)`, moment generating function, `M_Y(t)`, cumulant generating function and its `j^{\text{th}}` derivative, `K_Y(t)` 
and `K_Y^{(j)}(t)`, and the `r^{\text{th}}` raw moment, `\mu'_Y(r)`, of `Y` are given below:




|cr|

.. method:: dist_logrv_beta_nc_type_II.c_y(t)

    Returns `C_{Y}(s)`, the characteristic function of a random variable `Y`, as defined above:

    .. math:: C_Y(t) = \frac{\Gamma(n/2  -it)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2  -it)}  \times {}_1F_1\left( -it ;\frac{n + m}{2}  -it ; -\frac{1}{2}\lambda\right),



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f_nc_type_II(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta_nc_type_II.m_y(t)

    Returns `M_{Y}(s)`, the moment generating function of a random variable `Y`, as defined above:

    .. math:: M_Y(t) = \frac{\Gamma(n/2 + t)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2 + t)}  \times {}_1F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\lambda\right), 


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; 
        >>> print ("c_x: ", fisher_f_nc_type_II(mu, sigma).c_x(t))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta_nc_type_II.k_y(t, k = 0)

    Returns `K_{Y}(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, 
    `K_{Y}^{(j)}(s), j = 1 \ldots k`, of a random variable `Y`, as defined above:

    .. math:: K_Y(t) =  \log \left[ \frac{\Gamma(n/2 + t)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2 + t)}  \times {}_1F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\lambda\right) \right],

    .. math::
        :nowrap:

        \begin{eqnarray}
        K_Y^{(j)}(t) & = &  \psi^{(j-1)} \left( \tfrac{1}{2}n+t - \tfrac{1}{2}(i-1)\right) - \psi^{(j-1)} \left( \tfrac{1}{2}(n+m)+t - \tfrac{1}{2}(i-1)\right)  \\
        & + & \frac{\partial}{\partial t} \log \left[ {}_1F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\lambda\right)\right], 
        \end{eqnarray}


    where `\psi^{(j-1)}(\cdot)` denotes the polygamma function and `{}_1F_1(\cdot)` is the confluent 
    hypergeometric function. 



    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; t = 0.3; k = 6;
        >>> print ("c_x: ", fisher_f_nc_type_II(mu, sigma).k_x(t, k))
        6.3563523462564525615615615614561356E+00




|cr|

.. method:: dist_logrv_beta_nc_type_II.moments(k)

    Returns the first `j` raw moments, `\mu_j, j = 1 \ldots k`, of a random variable `X`, following the distribution of the square of the multiple correlation coefficient: 
    the moments are calculated from their definition: 

    .. math:: \mu'_X(r) = E(X^r) = \int_{0}^{1} x^r \text{pdf}_X(x) \mathrm{d} x

    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_r_square_type_II(mu, sigma).moments(k))
        6.3563523462564525615615615614561356E+00



|cr|

.. method:: dist_logrv_beta_nc_type_II.cumulants(k)

    Returns the first `j` cumulants, `\kappa_j, j = 1 \ldots k`, of a random variable `X`, 
    following the distribution of the square of the multiple correlation coefficient. The cumulants are calculated from the moments.


    .. code-block:: python

        >>> from mpfunlab import *
        >>> mp.dps = 30
        >>> mu = 0; sigma = 1; k = 6;
        >>> print ("saddlepoint: ", fisher_r_square_type_II(mu, sigma).cumulants(k))
        6.3563523462564525615615615614561356E+00




**Approximations**


.. method:: ctx.log1mbeta_nc_gp(t, n, m, lambda1)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Calculates the pdf, cdf and sf from the characteristic function using the procedure of Gil-Pelaez (see  :ref:`gil_pelaez_pdf() <rst_gil_pelaez_pdf>` and  :ref:`gil_pelaez_cdf() <rst_gil_pelaez_cdf>`).

    This uses `\log(1-X)`, `X` noncentral beta




.. method:: ctx.beta_nc_spa(x, n, results='c')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the Luggannini-Rice saddlepoint approximation of the pdf, cdf and sf.


    This uses `2\log (1-X)` of the non-central beta `X`


    Returns `K_{Y}(s)`, the cumulant generating function, and its `j^{\text{th}}` derivatives, 
    `K_{Y}^{(j)}(s), j = 1 \ldots k`, of a random variable `Y`, as defined above:

    .. math:: K_Y(t) =  \log \left[ \frac{\Gamma(n/2 + t)\Gamma((n + m)/2)}{\Gamma(n/2)\Gamma((n + m)/2 + t)}  \times {}_1F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\lambda\right) \right],

    .. math::
	    :nowrap:

	    \begin{eqnarray}
	    K_Y^{(j)}(t) & = &  \psi^{(j-1)} \left( \tfrac{1}{2}n+t - \tfrac{1}{2}(i-1)\right) - \psi^{(j-1)} \left( \tfrac{1}{2}(n+m)+t - \tfrac{1}{2}(i-1)\right)  \\
	    & + & \frac{\partial}{\partial t} \log \left[ {}_1F_1 \left(t,\tfrac{1}{2}(n+m)+t,-\tfrac{1}{2}\lambda\right)\right], 
	    \end{eqnarray}


    where `\psi^{(j-1)}(\cdot)` denotes the polygamma function and `{}_1F_1(\cdot)` is the confluent 
    hypergeometric function. 



.. method:: ctx.beta_nc_spa_inv(x, n, results='qtf')

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Calculates the inverse Jensen saddlepoint approximation of the qtf and isf.


    This uses `2\log (1-X)` of the non-central beta `X`





