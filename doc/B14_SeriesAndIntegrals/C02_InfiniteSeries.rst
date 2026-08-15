








.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />






|newpage|



Infinite series algorithms for selected functions and distributions
========================================================================================

This section provides additional finite sums algorithms.


.. _rst_gamma_peizer_cdf_sf_pdf: 

Incomplete gamma function, continued fractions (Peizer)
-------------------------------------------------------------------------------

.. method:: ctx.gamma_peizer_cdf_sf_pdf(a, x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    See also :cite:t:`Peizer1968`.


    The integral can be calculated using continued fractions. This method provides rigorous error bounds for for ``ipm.`` and ``apm.``.

    If `a - \frac{1}{2} > x` let `P` be a left tail. Then

    .. math:: P = \frac{M^b}{\Gamma(b+1)} e^{-M}  \frac{1}{\left(1+u_1/(v_1 + u_2 / (v_2 + u_3 / (v_3 + \ldots ))) \right)}

    where `M = x`, `b = a`, `u_1 = -M`,  `u_{2j} = jM`, `u_{2j+1}=-(b+j)M`, `v_{j}=b+j`, `j=1,2,\ldots` 

    The approximants obtained by terminating at `u_k/v_k` for `k=1,2,5,6,9,10,\ldots` decrease monotonically toward `P` and those for `k=0,3,4,7,8,11,12,\ldots` increase monotonically toward `P` as long as `k \le 2B-1`, where `B` is the integer part of `b`; for `k \ge 2B-2`, the even approximants approach `P` monotonically from above and the odd ones from below if `B` is even, vice versa if `B` is odd. The monotonicity is strict throughout except that, if `b` is an integer, the fraction terminates at `k=2b-2`.


    If `a - \frac{1}{2} \le x` let `Q` be a right tail. Then


    .. math::  Q = \frac{M^{b-1}}{\Gamma(b)} e^{-M}  \frac{1}{\left(1+u_1/(v_1 + u_2 / (v_2 + u_3 / (v_3 + \ldots ))) \right)}

    where `M = x`, `b = a`, `u_{2j-1} = j-b`, `v_{2j-1} = M`, `u_{2j}=j`, `v_{2j}=1`, `j=1,2,\ldots` 

    The approximants obtained by terminating at `u_k/v_k` approach `Q` strictly monotonically from above for 

    `k=1,2,5,6,9,10,\ldots` and from below for `k=0,3,4,7,8,11,12,\ldots`





    .. note::
       While the algorithm given above seems to offer an easy way to calculate the function in interval arithmetic, one needs to remember that forward recurrence of continuous fractions is entirely unstable in interval arithmetic (see :cite:t:`Cuyt2008`, pages 154 - 159). Therefore one first needs to evaluate the algorithm using forward recurrence in floating point arithmetic to determine the index of the (likely) highest required approximant, and then again using backward recurrence to actually evaluate it in interval arithmetic.



    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = 10.4; x = 8.7
        >>> dx = dec.gamma_peizer_cdf_sf_pdf(a, x); mx = mpm.gamma_peizer_cdf_sf_pdf(a, x); 
        >>> ix = ipm.gamma_peizer_cdf_sf_pdf(a, x); fx = fpm.gamma_peizer_cdf_sf_pdf(a, x); 
        >>> gx = gmp.gamma_peizer_cdf_sf_pdf(a, x); ax = apm.gamma_peizer_cdf_sf_pdf(a, x)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)








.. _rst_gamma_paris_cdf_sf: 

Incomplete gamma function, asymptotic expansion (Paris)
-------------------------------------------------------------------------------

.. method:: ctx.gamma_paris_cdf_sf(a, x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    This method does not provide rigorous error bounds for for ``ipm.`` and ``apm.``.

    [Paris2016` gives the following expansion (for source code, see Sub demoParis() in DistXArb):


    Let `m = 0,1,2...` and `\chi = (z-a)/\sqrt{z}`. Then, when `\Re(z-a) \ge 0`, we have the expansion


    .. math:: \Gamma(a,z) = z^{a-\tfrac{1}{2}} e^{-z} \left(  d_0(\chi) \sum_{k=0}^{m} \frac{A_k(\chi)}{z^{k/2}}  -  \sum_{k=1}^{m} \frac{B_k(\chi)}{z^{k/2}} + O \left(z^{-(m+1)/2} \right) \right)

    as `z \rightarrow \infty` in the sector `|\arg z| < \tfrac{1}{2}\pi`.


    Let `m = 0,1,2...` and `\chi = (z-a)/\sqrt{z}`. Then, when `\Re(z-a) \le 0`, we have the expansion


    .. math:: \gamma(a,z) = z^{a-\tfrac{1}{2}} e^{-z} \left(  d_0(-\chi) \sum_{k=0}^{m} \frac{A_k(\chi)}{z^{k/2}}  +  \sum_{k=1}^{m} \frac{B_k(\chi)}{z^{k/2}} + O \left(z^{-(m+1)/2} \right) \right)

    as `z \rightarrow \infty` in the sector `|\arg z| < \tfrac{1}{2}\pi`.


    .. math:: A_k(\chi) = \sum_{j=0}^{k}(-1)^j S_3(k+2j, j) p_{k+2j}(\chi), \quad B_k(\chi) = \sum_{j=0}^{k}(-1)^j S_3(k+2j, j) q_{k+2j}(\chi).

    .. math:: d_0(\chi) = \sqrt{\pi/2} \: e^{\chi^2/2} \: \text{erfc}(\chi/\sqrt{2})

    .. math:: p_0(\chi) = 1, \quad p_1(\chi) = -\chi, \quad  p_{k+1}(\chi) = \frac{1}{k+1} \left( p_{k-1}(\chi) - \chi p_k(\chi)\right), \quad k\ge 1

    .. math:: q_0(\chi) = 0, \quad q_1(\chi) = -1, \quad  q_{k+1}(\chi) = \frac{1}{k+1} \left( q_{k-1}(\chi) - \chi q_k(\chi)\right), \quad k\ge 1

    The coefficients `S_3(k,j)` are the 3-associated Stirling numbers of the second kind. They are determined recursively:

    .. math::  S_3(n+1, k)=k\ S_3(n, k)+\binom{n}{2}S_3(n-2, k-1)



    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = 1.0E5; x = 1.001E5
        >>> dx = dec.gamma_paris_cdf_sf(a, x); mx = mpm.gamma_paris_cdf_sf(a, x)
        >>> ix = ipm.gamma_paris_cdf_sf(a, x); fx = fpm.gamma_paris_cdf_sf(a, x)
        >>> gx = gmp.gamma_paris_cdf_sf(a, x); ax = apm.gamma_paris_cdf_sf(a, x)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_beta_peizer_cdf_sf_pdf: 

Incomplete beta function, continued fractions (Peizer)
-------------------------------------------------------------------------------

.. method:: ctx.beta_peizer_cdf_sf_pdf(a, b, q, p)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    The integral can be calculated using continued fractions (see :cite:t:`Peizer1968`). This method provides rigorous error bounds for for ``ipm.`` and ``apm.``. By transforming the problem if necessary (using the equation `I_x(a,b) = 1-I_{1-x}(b,a)`), let P be a lefttail probability with `b-\tfrac{1}{2} \le  (a+b-1) (1-x)`. Then

    .. math::  P = I_x(a,b)= \binom{n}{a} p^{b-1} q^a \frac{1}{(1+u_1/(v_1+u_2/(v2+u3/(v_3+ \cdots))))}, \quad \text{where } 

    .. math::  p=(1-x), \quad q=x, \quad n=a+b-1, \quad u_1= \frac{-(b-1)q}{p}, \quad u_{2j}= \frac{j(n+j)q}{p},

    .. math::  u_{2j+1}= \frac{-(a+j)(b-j-1)q}{p}, \quad v_j=a+j, \quad j=1,2,\ldots


    The approximants obtained by terminating at `u_k/v_k` for `k=1,2,5,6,9,10,\ldots` decrease monotonically toward `P` 
    and those for `k=0,3,4,7,8,11,12,\ldots` increase monotonically toward `P` as long as `k \le 2B-1`, where `B` is 
    the integer part of `b`; for `k \ge 2B-2`, the even approximants approach `P` monotonically from above and the 
    odd ones from below if `B` is even, vice versa if `B` is odd. The monotonicity is strict throughout except that, 
    if `b` is an integer, the fraction terminates at `k=2b-2`.


    For a combined fraction see :cite:t:`Tretter1979`.


    .. note::
       While the algorithm given above seems to offer an easy way to calculate the function in interval arithmetic, one needs to remember that forward recurrence of continuous fractions is entirely unstable in interval arithmetic (see :cite:t:`Cuyt2008`, pages 154 - 159). Therefore one first needs to evaluate the algorithm using forward recurrence in floating point arithmetic to determine the index of the (likely) highest required approximant, and then again using backward recurrence to actually evaluate it in interval arithmetic.


    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = 8.3; b = 10.4; x = 0.7
        >>> dx = dec.beta_peizer_cdf_sf_pdf(a, b, x); mx = mpm.beta_peizer_cdf_sf_pdf(a, b, x)
        >>> ix = ipm.beta_peizer_cdf_sf_pdf(a, b, x); fx = fpm.beta_peizer_cdf_sf_pdf(a, b, x)
        >>> gx = gmp.beta_peizer_cdf_sf_pdf(a, b, x); ax = apm.beta_peizer_cdf_sf_pdf(a, b, x)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_chi2_nc_benton_cdf_sf: 

Noncentral `\chi^2` distribution, pdf, cdf and sf (Boost)
-------------------------------------------------------------------------------

.. method:: ctx.chi2_nc_benton_cdf_sf(x, n, lambda1, cdf=True, **options)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns `\text{cdf}_X(x)`, the cumulative distribution function, for ``cdf=True``, or `\text{sf}_X(x)`, the survival function, for ``cdf=False``, of a random variable `X`, noncentral chi-squared distribution with degrees of freedom `n>0`, noncentrality parameter `\lambda_1`, and support interval `(0, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis01`, MathWorld :cite:p:`WolframDis01`, :cite:t:`Patnaik1949`, :cite:t:`Penev2000`, :cite:t:`Wang1993`, :cite:t:`Winterbottom1979`, BoostMath :cite:p:`BoostDis01`, :cite:t:`CharfunDis01`, :cite:t:`Kerns2018`.


    Noncentral CDF: Infinite series in terms of the central cdf:

    The cdf of a noncentral chi-square variable with `n` degrees of freedom and `\lambda` is given by

    .. math:: F_{\chi^2}\left(n, x; \lambda\right) = e^{-\lambda/2} \sum_{j=0}^\infty {\frac{(\lambda /2)^j}{j!} F_{\chi^2}\left(n+2+j, x\right) }

    where `F_{\chi^2}(n, \cdot)` is the cdf of the (central) `\chi^2` distribution.



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 12; nu = 10; l1 = 30
        >>> dx = dec.chi2_nc_benton_cdf_sf(x, nu, l1); mx = mpm.chi2_nc_benton_cdf_sf(x, nu, l1)
        >>> ix = ipm.chi2_nc_benton_cdf_sf(x, nu, l1); fx = fpm.chi2_nc_benton_cdf_sf(x, nu, l1)
        >>> gx = gmp.chi2_nc_benton_cdf_sf(x, nu, l1); ax = apm.chi2_nc_benton_cdf_sf(x, nu, l1)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_student_t_nc_benton_cdf_sf: 

Noncentral Student `t` distribution, pdf, cdf and sf (Boost)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_nc_benton_cdf_sf(x, nu, delta, cdf=True, **options)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns `\text{cdf}_X(x)`, the cumulative distribution function, for ``cdf=True``, or `\text{sf}_X(x)`, the survival function, for ``cdf=False``, of a random variable `X`, following a noncentral t-distribution with `n>0` degrees of freedom, noncentrality parameter `\delta`, and support interval `(-\infty, +\infty)`.
    See also Wikipedia :cite:p:`WikipediaDis03`, MathWorld :cite:p:`WolframDis03`, BoostMath :cite:p:`BoostDis03`, :cite:t:`Benton2003`, :cite:t:`Broda2007`, :cite:t:`Owen1968`, :cite:t:`Wang1993`, :cite:t:`Witkovsky2013`, :cite:t:`Kerns2018`.



    The pdf of a variable following a noncentral  t-distribution with `n` degrees of freedom and noncentrality parameter `\delta` is given by (boost_math)

    .. math:: f_{t'}\left(n,x, \delta\right) = \frac{nt}{n^2+2nt^2+t^4} + \frac{1}{2} \sum_{i=0}^{\infty} P_i I'_x\left(i+ \frac{1}{2} , \frac{n}{2}\right) + \frac{\delta}{\sqrt{2}} Q_i I'_x\left(i+1, \frac{n}{2}\right), \quad \text{and}

    `I'_x(\cdot,\cdot)` denotes the density of the beta distribution (see section \ref{BetaDistributionDensity}), and `P_i` and `Q_i` are defined in equation (eq:NonCentralTSeriesCoeff).


    The cdf of a variable following a noncentral  t-distribution with `n` degrees of freedom and noncentrality parameter `\delta` is given by (Benton, 2003)

    .. math:: F_{t'}\left(n,x, \delta\right) = \Phi(-\delta) + \frac{1}{2} \sum_{i=0}^{\infty} P_i I_x\left(i+ \frac{1}{2} , \frac{n}{2}\right) + \frac{\delta}{\sqrt{2}} Q_i I_x\left(i+1, \frac{n}{2}\right), \quad \text{and}

    .. math:: 1-F_{t'}\left(n,x, \delta\right) = \frac{1}{2} \sum_{i=0}^{\infty} P_i I_y\left( \frac{n}{2}, i+ \frac{1}{2} \right) + \frac{\delta}{\sqrt{2}} Q_i I_y\left(\frac{n}{2},i+1\right), \quad \text{where}

    .. math:: \lambda = \tfrac{1}{2}\delta^2; \quad P_i =  \frac{e^{-\lambda} \lambda^i}{i!} ; \quad Q_i = \frac{e^{-\lambda} \lambda^i}{\Gamma(i+3/2)};  \quad x=\frac{t^2}{n+t^2};  \quad y=1-x,

    `I_x(\cdot,\cdot)` denotes the (normalized) incomplete beta function, and `\Phi(\cdot)` denotes the cdf of the normal distribution.



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 20.2; nu = 10; d = 30
        >>> dx = dec.student_t_nc_benton_cdf_sf(x, n, d); mx = mpm.student_t_nc_benton_cdf_sf(x, n, d)
        >>> ix = ipm.student_t_nc_benton_cdf_sf(x, n, d); fx = fpm.student_t_nc_benton_cdf_sf(x, n, d)
        >>> gx = gmp.student_t_nc_benton_cdf_sf(x, n, d); ax = apm.student_t_nc_benton_cdf_sf(x, n, d)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_beta_nc_benton_cdf_sf: 

Noncentral Beta distribution, pdf, cdf and sf (Boost)
-------------------------------------------------------------------------------

.. method:: ctx.beta_nc_benton_cdf_sf(x, a, b, lambda1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns simulataneously `\text{pdf}_X(x)`, the probability density function, `\text{cdf}_X(x)`, the cumulative distribution function, and `\text{sf}_X(x)`, the survival function, of a random variable `X`, following a noncentral Beta distribution with shape parameters `a` and `b`, noncentrality parameter `\lambda_1` and the support interval `(0, 1)`.
    See also Wikipedia :cite:p:`WikipediaDis04`, BoostMath :cite:p:`BoostDis04`, :cite:t:`Wang1993`, :cite:t:`CharfunDis04`, :cite:t:`Kerns2018`.



    CDF: Infinite Series:

    The cdf of a variable following a (singly) noncentral F-distribution with `n` and `m` degrees of freedom and noncentrality parameter `\lambda_1` and is given by

    .. math:: \text{Pr}(F \leq x) = F_{F'}(x;m,n,\lambda) = e^{-\lambda} \sum_{j=0}^{\infty}{\frac{(\lambda/2)^j}{j!}F(m+2j,n,x)}

    where `F_{F}(\cdot)` denotes the cdf of the central F-distribution.




    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; a = '10'; b = '20'; l1 = '30'
        >>> dx = dec.beta_nc_benton_cdf_sf(x, a, b, l1); mx = mpm.beta_nc_benton_cdf_sf(x, a, b, l1)
        >>> ix = ipm.beta_nc_benton_cdf_sf(x, a, b, l1); fx = fpm.beta_nc_benton_cdf_sf(x, a, b, l1)
        >>> gx = gmp.beta_nc_benton_cdf_sf(x, a, b, l1); ax = apm.beta_nc_benton_cdf_sf(x, a, b, l1)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_fisher_f_nc_benton_cdf_sf: 

Noncentral `F` distribution, pdf, cdf and sf (Benton)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_f_nc_benton_cdf_sf(x, m, n, lambda1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns simulataneously `\text{pdf}_X(x)`, the probability density function, `\text{cdf}_X(x)`, the cumulative distribution function, and `\text{sf}_X(x)`, the survival function, of a random variable `X`, following a noncentral `F` distribution with degrees of freedom `m` and `n`, noncentrality parameter `\lambda_1` and the support interval `(0, \infty)`.
    See also Wikipedia :cite:p:`WikipediaDis04`, BoostMath :cite:p:`BoostDis04`, :cite:t:`Wang1993`, :cite:t:`CharfunDis04`, :cite:t:`Kerns2018`.



    CDF: Infinite Series:

    The cdf of a variable following a (singly) noncentral F-distribution with `n` and `m` degrees of freedom and noncentrality parameter `\lambda_1` and is given by

    .. math:: \text{Pr}(F \leq x) = F_{F'}(x;m,n,\lambda) = e^{-\lambda} \sum_{j=0}^{\infty}{\frac{(\lambda/2)^j}{j!}F(m+2j,n,x)}

    where `F_{F}(\cdot)` denotes the cdf of the central F-distribution.




    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; m = '10'; n = '20'; l1 = '30'
        >>> dx = dec.fisher_f_nc_benton_cdf_sf(x,m,n,l1); mx = mpm.fisher_f_nc_benton_cdf_sf(x,m,n,l1)
        >>> ix = ipm.fisher_f_nc_benton_cdf_sf(x,m,n,l1); fx = fpm.fisher_f_nc_benton_cdf_sf(x,m,n,l1)
        >>> gx = gmp.fisher_f_nc_benton_cdf_sf(x,m,n,l1); ax = apm.fisher_f_nc_benton_cdf_sf(x,m,n,l1)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_pearson_rho_nc_ht_cdf: 

Pearson's `\rho` distribution, cdf and sf (Hotelling's series)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_nc_ht_cdf(r, N, rho)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns simulaneously `\text{cdf}_X(r)`, the cumulative distribution function, and `\text{sf}_X(r)`, the survival function, of a random variable `X`, following the distribution of Pearson's rho (the distribution of the sample correlation coefficient),  with sample size `N \ge 3`, noncentrality parameter `\rho \in (-1,+1)` and support interval `(-1,+1)`.
    See also Wikipedia :cite:p:`WikipediaDis05`, MathWorld :cite:p:`WolframDis05`, :cite:t:`Hotelling1953`, :cite:t:`Guenther1977`, :cite:t:`Winterbottom1979`, :cite:t:`Winterbottom1980`, :cite:t:`Odeh1986`, :cite:t:`Ruben1966`, :cite:t:`Subrahmaniam1983`.



    Hotelling (1953)  defines `Q_N(r;\rho) = \text{Pr}(\rho<R<r)` and develops  `Q_N(r;\rho)` in the following uniformly convergent series for `-1<\rho<r<1`. 

    .. math:: 	Q_N(r,\rho) = K_1 \sum_{j=0}^{\infty}{\frac{(1 \cdot 3 \cdots (2j-1))^2 S_j}{j! 2^{2j} \cdot (2N+1) \cdots (2N+2j-1)}},

    where `K_1` and `S_j` are defined in equations (\ref{eq:PearsonRho_K1}) and (\ref{eq:PearsonRho_Hotelling_Sj}), respectively. From the relationships

    .. math:: 	P_N(r, \rho) = 1-F_R(r, N; \rho) = Q_N(1,\rho)-Q_N(r,\rho)

    .. math:: 	P_N(-1, \rho) = 1

    .. math:: 	F_R(r, N; \rho) = 1 -P_N(r, \rho)

    .. math:: 	F_R(-r, N; -\rho) = 1 -F_R(r, N; \rho)

    we can compute `F_N(r;\rho)` for any value of r and `\rho` with `-1 \leq r \leq 1`, `-1<\rho<1`.
    Hotelling shows that the error committed by truncating the series at any point is less than `\frac{2}{1-|\rho|}` times the last term used. However, it is important to note that the series converges very slowly for small values of `N`, and in this case a large number of terms must be computed.

    .. math:: 	S_j = \sum_{k=0}^{j} \binom{j}{k}(-1)^k \: \tfrac{1}{2} (1-\rho^2)^k \: 2^{j-k}  N_k

    .. math:: 	N_k = \sum_{s=0}^{\infty} \frac{\Gamma\left(\tfrac{3}{2}-k\right)}{\Gamma\left(\tfrac{3}{2}-k-s\right) s!} \cdot I \left(\tfrac{1}{2}(s+1), \tfrac{1}{2}(n-1),\frac{(r-\rho)^2}{(1-\rho r)^2}\right),

    where `I(a,b;x)` denotes the Incomplete Beta Function (see section \ref{sec:IncompleteBetaFunction}). Hotelling shows that in the evaluation of `N_k` for large `s` the absolute value of the ratio of the term of order `(s+1)` to the term of order `s` is bounded by `|\rho (r-\rho)/(1-\rho r)|`, so that the series converges rapidly.




    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; r = '0.3'; N = '10'; rho = '0.1'
        >>> dx = dec.pearson_rho_nc_ht_cdf(r, N, rho); mx = mpm.pearson_rho_nc_ht_cdf(r, N, rho)
        >>> ix = ipm.pearson_rho_nc_ht_cdf(r, N, rho); fx = fpm.pearson_rho_nc_ht_cdf(r, N, rho)
        >>> gx = gmp.pearson_rho_nc_ht_cdf(r, N, rho); ax = apm.pearson_rho_nc_ht_cdf(r, N, rho)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)



.. _rst_pearson_rho_nc_gt_cdf: 

Pearson's `\rho` distribution, cdf and sf (Guenther's series)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_nc_gt_cdf(r, N, rho)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns simulaneously `\text{cdf}_X(r)`, the cumulative distribution function, and `\text{sf}_X(r)`, the survival function, of a random variable `X`, following the distribution of Pearson's rho (the distribution of the sample correlation coefficient),  with sample size `N \ge 3`, noncentrality parameter `\rho \in (-1,+1)` and support interval `(-1,+1)`.
    See also Wikipedia :cite:p:`WikipediaDis05`, MathWorld :cite:p:`WolframDis05`, :cite:t:`Hotelling1953`, :cite:t:`Guenther1977`, :cite:t:`Winterbottom1979`, :cite:t:`Winterbottom1980`, :cite:t:`Odeh1986`, :cite:t:`Ruben1966`, :cite:t:`Subrahmaniam1983`.



    The functions uses an algorithm by :cite:t:`Guenther1977`, :

    Guenther writes `P_N(r;\rho) = \text{Pr}(R>0) -  \text{Pr}(0<R<r)` and develops `\text{Pr}(0<R<r)` in an infinite series involving the Incomplete Beta Function denoted by `I(a,b;x)`. The result is

    .. math:: 	\text{Pr}(R>0) = \tfrac{1}{2} \left(1+\text{sgn}(\rho) \cdot I\left(\tfrac{1}{2}(N-1), \tfrac{1}{2}; \rho^2\right) \right)


    .. math::
       :nowrap:

       \begin{eqnarray}
	    \text{Pr}(0 < R <r) & = \sum_{j=0}^{\infty} K_1(j) \cdot I\left(\tfrac{1}{2}(N-2), \tfrac{1}{2}(2j+1); r^2 \right) \\
	    & + \sum_{j=0}^{\infty} K_2(j) \cdot I\left(\tfrac{1}{2}(N-2), j+1; r^2 \right)  \nonumber
       \end{eqnarray}


    where  `K_1(j), K_2(j)` are defined recursively by

    .. math:: 	K_1(0) = \tfrac{1}{2} \left(1-\rho^2 \right)^{\tfrac{1}{2}(N-1)}, \quad K_1(j)=\frac{2j+N-3}{2j} \rho^2 K_1(j-1)

    .. math:: 	K_2(0) = \frac{\Gamma \left(\tfrac{1}{2}N\right)}{\sqrt{\pi}\Gamma\left(\tfrac{1}{2}(N-1)\right)} \rho \left(1-\rho^2 \right)^{\tfrac{1}{2}(N-1)}, \quad K_2(j)=\frac{2j+N-2}{2j+1} \rho^2 K_2(j-1)

    These equations are used together to give `P_N(r;\rho)`. Guenther also obtains error bounds for truncating the infinite series.



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; r = '0.3'; N = '10'; rho = '0.1'
        >>> dx = dec.pearson_rho_nc_gt_cdf(r, N, rho); mx = mpm.pearson_rho_nc_gt_cdf(r, N, rho)
        >>> ix = ipm.pearson_rho_nc_gt_cdf(r, N, rho); fx = fpm.pearson_rho_nc_gt_cdf(r, N, rho)
        >>> gx = gmp.pearson_rho_nc_gt_cdf(r, N, rho); ax = apm.pearson_rho_nc_gt_cdf(r, N, rho)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_fisher_r2_gd2_cdf: 

Fisher's `R^2` distribution, cdf and sf (Boost, Benton)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_r2_gd2_cdf(x, p, N, rho2, **options)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns `\text{pdf}_X(x)`, the probability density function (pdf) of a random variable `X`, following 
    the distribution of Fisher's `R^2` (the distribution of the square of the sample multiple correlation coefficient), with `p \ge 1` predictor variables, sample size `N \ge p+2`, noncentrality parameter `\rho^2 \in (0,1)` and the support interval `(0,1)`.
    See also :cite:t:`Lee1971`, :cite:t:`Lee1972`, :cite:t:`Gurland1968`, :cite:t:`Gurland1970`, :cite:t:`Gurland1991`, :cite:t:`Muirhead1982`, :cite:t:`Benton2003`, :cite:t:`Fisher1928`, :cite:t:`Gatsonis1989`.




    Density: Infinite series:

    The density function of the multiple sample correlation coefficient is given by \citep{Ding_1996,Benton_2003}

    .. math:: f_{R^2}(x;p,N,\rho^2) = \sum_{i=0}^\infty f_{\text{NegBin}}\left((N-1)/2, i; 1-\rho^2\right) \times f_{\text{Beta}}\left(x; \tfrac{1}{2}(p-1) + i, \tfrac{1}{2}(N-p)\right)

    where `f_{\text{NegBin}}(\cdot)` denotes the pmf of the negative binomial distribution and `f_{\text{Beta}}(\cdot)` denotes the pdf of the Beta distribution 



    CDF: Infinite series:

    The CDF of the multiple sample correlation coefficient is given by \citep{Ding_1996,Benton_2003}

    .. math:: F_{R^2}(x;p,N,\rho^2) = \sum_{i=0}^\infty f_{\text{NegBin}}\left((N-1)/2, i; 1-\rho^2\right) \times  F_{\text{Beta}}\left(x; \tfrac{1}{2}(p-1) + i, \tfrac{1}{2}(N-p)\right)

    where `f_{\text{NegBin}}(\cdot)` denotes the pmf of the negative binomial distribution and `F_{\text{Beta}}(\cdot)` denotes the CDF of the Beta distribution



    CDF: Series of Gurland:


    .. math:: \text{Pr}[F \leq x` = F_{R^2}(x;a,b,\rho^2) = \frac{b^m}{a^{n/2}}  \sum_{j=0}^{\infty}{c_j I(m+j,k,y)} \quad \text{where}

    .. math:: z=F(p-1), \quad y=\frac{z}{z+(N-p)}, \quad a=\frac{1}{1-\rho^2}, \quad n=(N-p)/2, \quad m=(p-1)/2

    .. math:: c_0=1, \quad c_j=\frac{c_{j-1}(-n/2-j+1)\rho^2}{j}



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; p = '3'; N = '20'; rho2 = '0.6'
        >>> dx = dec.fisher_r2_gd2_cdf(x, p, N, rho2); mx = mpm.fisher_r2_gd2_cdf(x, p, N, rho2)
        >>> ix = ipm.fisher_r2_gd2_cdf(x, p, N, rho2); fx = fpm.fisher_r2_gd2_cdf(x, p, N, rho2)
        >>> gx = gmp.fisher_r2_gd2_cdf(x, p, N, rho2); ax = apm.fisher_r2_gd2_cdf(x, p, N, rho2)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




