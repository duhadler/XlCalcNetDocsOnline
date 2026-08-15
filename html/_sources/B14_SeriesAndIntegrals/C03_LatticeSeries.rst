








.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />




|newpage|


Finite series for lattice distributions, based on factorial moments
======================================================================================





Fréchet's formula for calculating the pmf from the factorial moments
-------------------------------------------------------------------------------

.. method:: ctx.frechet_pmf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    For lattice distributions, the pmf can be calculated from the factorial moments as follows (see Fréchet 1940, 1943):


    .. math:: \text{pmf}_X(x) =  \sum_{j=x}^{M} (-1)^{x+j} \binom{j}{x} \frac{\mu'_{[j]}}{j!},
       :label: frechet_pmf

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 



    An example (pmf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; k = '34'; n = '100'; p = '0.5'; 
        >>> dx = dec.binomial_pmf(k, n, p); mx = mpm.binomial_pmf(k, n, p)
        >>> ix = ipm.binomial_pmf(k, n, p); fx = fpm.binomial_pmf(k, n, p)
        >>> gx = gmp.binomial_pmf(k, n, p); ax = apm.binomial_pmf(k, n, p)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  4.581052772872401245494881411350031838140E-4
        mpm:  4.581052772872401245494881411350031838141e-4
        ipm:  4.581052772872401245494881411350031838141e-4 (4.894e-39%)
        fpm:  4.58105277287240E-04
        gmp:  4.581052772872401245494881411350031838141E-04
        ipm:  4.581052772872401245494881411350031838141e-4 (4.894e-39%)





Laurent's formula for calculating the cdf from the factorial moments
-------------------------------------------------------------------------------

.. method:: ctx.laurent_cdf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    For lattice distributions, the cdf can be calculated from the factorial moments as follows (see Laurent 1965):

    .. math:: \text{cdf}_X(x) =  \sum_{j=x}^{M} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 
       :label: laurent_cdf

    .. math:: \text{sf}_X(x) =  1-\sum_{j=x}^{M} (-1)^{x+j} \binom{j-1}{x-1} \frac{\mu'_{[j]}}{j!}, 
       :label: laurent_sf

    where `\mu'_{[j]}` is the `j^{\text{th}}` factorial moment. 



    An example (cdf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; k = '34'; n = '100'; p = '0.5'; 
        >>> dx = dec.binomial_cdf(k, n, p); mx = mpm.binomial_cdf(k, n, p)
        >>> ix = ipm.binomial_cdf(k, n, p); fx = fpm.binomial_cdf(k, n, p)
        >>> gx = gmp.binomial_cdf(k, n, p); ax = apm.binomial_cdf(k, n, p)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  8.949651957434262965349913219213965127993E-4
        mpm:  8.949651957434262965349913219213965127993e-4
        ipm:  8.949651957434262965349913219213965127993e-4 (6.263e-40%)
        fpm:  8.94965195743426E-04
        gmp:  8.949651957434262965349913219213965127993E-04
        ipm:  8.949651957434262965349913219213965127993e-4 (6.263e-40%)




Binomial distribution, pmf, cdf
-------------------------------------------------------------------------------

.. method:: ctx.binomial_fm_pmf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The pmf and cdf are calculated using equations  :eq:`frechet_pmf` and  :eq:`laurent_cdf`, respectively.

    If a random variable `X` has a binomial distribution with success probability `p \in [0,1]` and number of trials `n`, then the factorial moments of `X` are

    .. math:: \operatorname{E} \bigl [(X)_{r}\bigr ] = \binom {n}{r} p^{r}r! = (n)_{r} p^{r} = \frac{n!}{(n-r)!} p^{r},
       :label: binomial_fm_fm

    where by convention, `\binom {n}{r}` is understood to be zero if `r > n`.





    An example (pmf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; k = '34'; n = '100'; p = '0.5'; 
        >>> dx = dec.binomial_pmf(k, n, p); mx = mpm.binomial_pmf(k, n, p)
        >>> ix = ipm.binomial_pmf(k, n, p); fx = fpm.binomial_pmf(k, n, p)
        >>> gx = gmp.binomial_pmf(k, n, p); ax = apm.binomial_pmf(k, n, p)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  4.581052772872401245494881411350031838140E-4
        mpm:  4.581052772872401245494881411350031838141e-4
        ipm:  4.581052772872401245494881411350031838141e-4 (4.894e-39%)
        fpm:  4.58105277287240E-04
        gmp:  4.581052772872401245494881411350031838141E-04
        ipm:  4.581052772872401245494881411350031838141e-4 (4.894e-39%)



    An example (cdf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; k = '34'; n = '100'; p = '0.5'; 
        >>> dx = dec.binomial_cdf(k, n, p); mx = mpm.binomial_cdf(k, n, p)
        >>> ix = ipm.binomial_cdf(k, n, p); fx = fpm.binomial_cdf(k, n, p)
        >>> gx = gmp.binomial_cdf(k, n, p); ax = apm.binomial_cdf(k, n, p)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  8.949651957434262965349913219213965127993E-4
        mpm:  8.949651957434262965349913219213965127993e-4
        ipm:  8.949651957434262965349913219213965127993e-4 (6.263e-40%)
        fpm:  8.94965195743426E-04
        gmp:  8.949651957434262965349913219213965127993E-04
        ipm:  8.949651957434262965349913219213965127993e-4 (6.263e-40%)




Classical hypergeometric distribution, pmf, cdf
-------------------------------------------------------------------------------

.. method:: ctx.hypergeo_fm_pmf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The pmf and cdf are calculated using equations  :eq:`frechet_pmf` and  :eq:`laurent_cdf`, respectively.

    If a random variable `X` has a hypergeometric distribution with population size `N`, number of success states `K \in \{0,...,N\}` in the population, and draws `n \in \{0,...,N\}`, then the factorial moments of `X` are

    .. math::  \operatorname {E} \bigl [(X)_{r}\bigr ] = \frac {{\binom {K}{r}}{\binom {n}{r}}r!} {\binom {N}{r}} = \frac {(K)_{r}(n)_{r}}{(N)_{r}}.
       :label: hypergeo_fm_fm



    An example (pmf):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; k = 2; n = 3; K = 10; N = 30
        >>> dx = dec.hypergeo_pmf(k, n, K, N); mx = mpm.hypergeo_pmf(k, n, K, N)
        >>> ix = ipm.hypergeo_pmf(k, n, K, N); fx = fpm.hypergeo_pmf(k, n, K, N)
        >>> gx = gmp.hypergeo_pmf(k, n, K, N); ax = apm.hypergeo_pmf(k, n, K, N)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  1.889036358989624579176488249803987683086E-2
        mpm:  1.889036358989624579176488249803987683086e-2
        ipm:  1.889036358989624579176488249803987683087e-2 (1.785e-37%)
        fpm:  1.88903635898961E-02
        gmp:  1.889036358989624579176488249803987683086E-02
        ipm:  1.889036358989624579176488249803987683087e-2 (1.785e-37%)



    An example (cdf):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; k = 2; n = 3; K = 10; N = 30
        >>> dx = dec.hypergeo_cdf(k, n, K, N); mx = mpm.hypergeo_cdf(k, n, K, N)
        >>> ix = ipm.hypergeo_cdf(k, n, K, N); fx = fpm.hypergeo_cdf(k, n, K, N)
        >>> gx = gmp.hypergeo_cdf(k, n, K, N); ax = apm.hypergeo_cdf(k, n, K, N)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  9.484909869856324992497161107476089538277E-1
        mpm:  9.484909869856324992497161107476089538277e-1
        ipm:  9.484909869856324992497161107476089538276e-1 (6.051e-40%)
        fpm:  9.48490986985633E-01
        gmp:  9.484909869856324992497161107476089538277E-01
        ipm:  9.484909869856324992497161107476089538276e-1 (6.051e-40%)






Wilcoxon distribution, pmf, cdf
-------------------------------------------------------------------------------

.. method:: ctx.wilcoxon_fm_pmf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The pmf and cdf are calculated using equations  :eq:`frechet_pmf` and  :eq:`laurent_cdf`, respectively.

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`), and the cumulants are given by

    .. math:: \kappa_{2j} = \frac{2^{2j} (2^{2j}-1) B_{2j}}{2j} \sum_{i=1}^N r_i^{2j} = \frac{2^{2j} (2^{2j}-1) B_{2j}}{2j} \frac{B_{2j+1}(N+1)-B_{2j+1}}{2j+1}, 
       :label: wilcoxon_kappa_fm

    where `\kappa_{1} = N(N+1)/4)`, `\kappa_{2j+1} = 0` for `j \geq 1`, and `B_{2j}` and `B_{2j}(x)` are the Bernoulli numbers and polynomials, respectively, of degree `2j`.



    An example (pmf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; N = '30';
        >>> dx = dec.wilcoxon_pmf(x, N); mx = mpm.wilcoxon_pmf(x, N)
        >>> ix = ipm.wilcoxon_pmf(x, N); fx = fpm.wilcoxon_pmf(x, N)
        >>> gx = gmp.wilcoxon_pmf(x, N); ax = apm.wilcoxon_pmf(x, N)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)


    An example (cdf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; N = '30';
        >>> dx = dec.wilcoxon_cdf(x, N); mx = mpm.wilcoxon_cdf(x, N)
        >>> ix = ipm.wilcoxon_cdf(x, N); fx = fpm.wilcoxon_cdf(x, N)
        >>> gx = gmp.wilcoxon_cdf(x, N); ax = apm.wilcoxon_cdf(x, N)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)





Mann-Whitney distribution, pmf, cdf
-------------------------------------------------------------------------------

.. method:: ctx.mannwhitney_fm_pmf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The pmf and cdf are calculated using equations  :eq:`frechet_pmf` and  :eq:`laurent_cdf`, respectively.

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`), and the cumulants are given by

    .. math:: \kappa_{2j} = \frac{B_{2j}}{2j(2j+1)} \left[ B_{2j+1}(N_2+N_1+1) +  B_{2j+1} -  B_{2j+1}(N_1+1) -  B_{2j+1}(N_2+1) \right]
       :label: mannwhitney_kappa_fm

    and `\kappa_{2j+1}=0`, `j \geq 1`, and `B_{2j}` and  `B_{2j}(x)` are the Bernoulli numbers and polynomials, respectively, of degree `2j`.




    An example (pmf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; m = '20'; n = '20';
        >>> dx = dec.mannwhitney_pmf(x, m, n); mx = mpm.mannwhitney_pmf(x, m, n)
        >>> ix = ipm.mannwhitney_pmf(x, m, n); fx = fpm.mannwhitney_pmf(x, m, n)
        >>> gx = gmp.mannwhitney_pmf(x, m, n); ax = apm.mannwhitney_pmf(x, m, n)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; m = '20'; n = '20';
        >>> dx = dec.mannwhitney_cdf(x, m, n); mx = mpm.mannwhitney_cdf(x, m, n)
        >>> ix = ipm.mannwhitney_cdf(x, m, n); fx = fpm.mannwhitney_cdf(x, m, n)
        >>> gx = gmp.mannwhitney_cdf(x, m, n); ax = apm.mannwhitney_cdf(x, m, n)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)





Kendall distribution, pmf, cdf
-------------------------------------------------------------------------------

.. method:: ctx.kendall_fm_pmf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The pmf is calculated using equation  :eq:`frechet_pmf`.

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`), and the cumulants are given by

    .. math:: \kappa_{2j}(T_N) = \frac{B_{2j}}{2j} \sum_{s=1}^N s^{2j} = \frac{B_{2j}}{2j} \left[ \frac{B_{2j+1}(N+1)-B_{2j+1}}{2j+1} - N \right], \quad \text{and}
       :label: kendall_kappa_fm

    .. math:: \kappa_{2j+1}(W_N) = 0, \quad \text{for } j \geq 1.

    `B_{2j}` and  `B_{2j}(x)` are the Bernoulli numbers and polynomials, respectively, of degree `2j`.



    An example (pmf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; N = '30';
        >>> dx = dec.kendall_tau_pmf(x, N); mx = mpm.kendall_tau_pmf(x, N)
        >>> ix = ipm.kendall_tau_pmf(x, N); fx = fpm.kendall_tau_pmf(x, N)
        >>> gx = gmp.kendall_tau_pmf(x, N); ax = apm.kendall_tau_pmf(x, N)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)



    An example (cdf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; N = '30';
        >>> dx = dec.kendall_tau_cdf(x, N); mx = mpm.kendall_tau_cdf(x, N)
        >>> ix = ipm.kendall_tau_cdf(x, N); fx = fpm.kendall_tau_cdf(x, N)
        >>> gx = gmp.kendall_tau_cdf(x, N); ax = apm.kendall_tau_cdf(x, N)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)





Jonckheere-Terpsta `T` distribution, pmf, cdf
-------------------------------------------------------------------------------

.. method:: ctx.jterpsta_fm_pmf(x, N)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    The pmf and cdf are calculated using equations  :eq:`frechet_pmf` and  :eq:`laurent_cdf`, respectively.

    The factorial moments are calculated from the cumulants (see :ref:`factorial_moments_from_cumulants() <rst_factorial_moments_from_cumulants>`), and the cumulants are given by

    .. math:: \kappa_{2j} = \frac{B_{2j}}{2j(2j+1)} \left[ B_{2j+1}(N+1) + (k-1) B_{2j+1} - \sum_{i=1}^{k} B_{2j+1}(n_i+1)  \right]
       :label: jterpsta_kappa_fm

    where `\kappa_{1} = M/2`, `\kappa_{2j+1} = 0` for `j \geq 1`, and `B_{2j}` and `B_{2j}(x)` are the Bernoulli numbers and polynomials, respectively, of degree `2j`.





    An example (pmf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; k = '4'; n = '10';
        >>> dx = dec.jterpsta_s_pmf(x, k, n); mx = mpm.jterpsta_s_pmf(x, k, n)
        >>> ix = ipm.jterpsta_s_pmf(x, k, n); fx = fpm.jterpsta_s_pmf(x, k, n)
        >>> gx = gmp.jterpsta_s_pmf(x, k, n); ax = apm.jterpsta_s_pmf(x, k, n)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)


    An example (cdf):

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10'; k = '4'; n = '10';
        >>> dx = dec.jterpsta_s_cdf(x, k, n); mx = mpm.jterpsta_s_cdf(x, k, n)
        >>> ix = ipm.jterpsta_s_cdf(x, k, n); fx = fpm.jterpsta_s_cdf(x, k, n)
        >>> gx = gmp.jterpsta_s_cdf(x, k, n); ax = apm.jterpsta_s_cdf(x, k, n)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  2.503894462302860479794674544578743383256E-2
        mpm:  2.503894462302860479794674544578743383257e-2
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)
        fpm:  2.50389446230288E-02
        gmp:  2.503894462302860479794674544578743383257E-02
        ipm:  2.503894462302860479794674544578743383257e-2 (3.582e-39%)

