






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />



|newpage|

Approximations based on the noncentral F or beta distribution
===============================================================================



.. _rst_mpm_fisher_r2_lee_mu3_cdf: 

Multiple correlation coefficient (Lee and Gurland)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_r2_lee_mu3_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    :cite:t:`Lee1971` suggests the following approximation, based on the noncentral `F` distribution:

    .. math:: F_{R^2}(x;n_1,n_2,\rho^2) \thickapprox F_{F'}\left(y; \nu, n_2, \lambda\right),

    where `\gamma=1/(1-\rho^2), \quad  A_j=(n_1+n_2) (\gamma^{\:j}-1) + n_1, \quad j=1,2,3`, 

    `G = (A_2 - \sqrt{A_2^2  -A_1 A_3})/A_1, \quad \lambda=\rho^2 \gamma \sqrt{\gamma (n_1+n_2) n_2}/G^2 , \quad  \nu= (A_2/G^2)- 2\lambda, \quad  y= x/(1-x) \times n_2/(\nu \cdot G)`, 
    
    and `F_{F'}\left(\cdot; \nu, n_2, \lambda\right)` denotes the CDF of the noncentral `F` distribution with `\nu` and `n_2` degrees of freedom and noncentrality parameter `\lambda` 




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hotelling_t2_ind_chi2_cdf(x, nu, nc); mx = mpm.hotelling_t2_ind_chi2_cdf(x, nu, nc)
        >>> ix = ipm.hotelling_t2_ind_chi2_cdf(x, nu, nc); fx = fpm.hotelling_t2_ind_chi2_cdf(x, nu, nc)
        >>> gx = gmp.hotelling_t2_ind_chi2_cdf(x, nu, nc); ax = apm.hotelling_t2_ind_chi2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_wilks_lambda_glm_mu2_cdf: 

Noncentral Wilks' Lambda under the GLM alternative
-------------------------------------------------------------------------------

.. method:: ctx.wilks_lambda_glm_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    See also: :cite:t:`OBrien1992`,  :cite:t:`Kulp1984`


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.wilks_lambda_glm_mu2_cdf(x, nu, nc); mx = mpm.wilks_lambda_glm_mu2_cdf(x, nu, nc)
        >>> ix = ipm.wilks_lambda_glm_mu2_cdf(x, nu, nc); fx = fpm.wilks_lambda_glm_mu2_cdf(x, nu, nc)
        >>> gx = gmp.wilks_lambda_glm_mu2_cdf(x, nu, nc); ax = apm.wilks_lambda_glm_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_wilks_lambda_ind_mu2_cdf: 

Noncentral Wilks' Lambda under the independence alternative
-------------------------------------------------------------------------------

.. method:: ctx.wilks_lambda_ind_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    See also: :cite:t:`OBrien1992`,  :cite:t:`Kulp1984`


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.wilks_lambda_ind_mu2_cdf(x, nu, nc); mx = mpm.wilks_lambda_ind_mu2_cdf(x, nu, nc)
        >>> ix = ipm.wilks_lambda_ind_mu2_cdf(x, nu, nc); fx = fpm.wilks_lambda_ind_mu2_cdf(x, nu, nc)
        >>> gx = gmp.wilks_lambda_ind_mu2_cdf(x, nu, nc); ax = apm.wilks_lambda_ind_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_mpm_hotelling_t2_glm_mu2_cdf: 

Noncentral Hotelling's T under the GLM alternative
-------------------------------------------------------------------------------

.. method:: ctx.hotelling_t2_glm_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    See also: :cite:t:`OBrien1992`

    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hotelling_t2_glm_mu2_cdf(x, nu, nc); mx = mpm.hotelling_t2_glm_mu2_cdf(x, nu, nc)
        >>> ix = ipm.hotelling_t2_glm_mu2_cdf(x, nu, nc); fx = fpm.hotelling_t2_glm_mu2_cdf(x, nu, nc)
        >>> gx = gmp.hotelling_t2_glm_mu2_cdf(x, nu, nc); ax = apm.hotelling_t2_glm_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)



.. _rst_mpm_hotelling_t2_ind_mu2_cdf: 

Noncentral Hotelling's T under the independence alternative
-------------------------------------------------------------------------------

.. method:: ctx.hotelling_t2_ind_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    See also: :cite:t:`OBrien1992`

    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hotelling_t2_ind_mu2_cdf(x, nu, nc); mx = mpm.hotelling_t2_ind_mu2_cdf(x, nu, nc)
        >>> ix = ipm.hotelling_t2_ind_mu2_cdf(x, nu, nc); fx = fpm.hotelling_t2_ind_mu2_cdf(x, nu, nc)
        >>> gx = gmp.hotelling_t2_ind_mu2_cdf(x, nu, nc); ax = apm.hotelling_t2_ind_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)







.. _rst_mpm_pillai_v_glm_mu2_cdf: 

Noncentral Pillai's V under the GLM alternative
-------------------------------------------------------------------------------

.. method:: ctx.pillai_v_glm_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    See also: :cite:t:`OBrien1992`

    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pillai_v_glm_mu2_cdf(x, nu, nc); mx = mpm.pillai_v_glm_mu2_cdf(x, nu, nc)
        >>> ix = ipm.pillai_v_glm_mu2_cdf(x, nu, nc); fx = fpm.pillai_v_glm_mu2_cdf(x, nu, nc)
        >>> gx = gmp.pillai_v_glm_mu2_cdf(x, nu, nc); ax = apm.pillai_v_glm_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_pillai_v_ind_mu2_cdf: 

Noncentral Pillai's V under the independence alternative
-------------------------------------------------------------------------------

.. method:: ctx.pillai_v_ind_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.



    See also: :cite:t:`OBrien1992`

    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pillai_v_ind_mu2_cdf(x, nu, nc); mx = mpm.pillai_v_ind_mu2_cdf(x, nu, nc)
        >>> ix = ipm.pillai_v_ind_mu2_cdf(x, nu, nc); fx = fpm.pillai_v_ind_mu2_cdf(x, nu, nc)
        >>> gx = gmp.pillai_v_ind_mu2_cdf(x, nu, nc); ax = apm.pillai_v_ind_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)








.. _rst_mpm_roy_glm_mu2_cdf: 

Noncentral Roy's largest root under the GLM alternative
-------------------------------------------------------------------------------

.. method:: ctx.roy_glm_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    See :cite:t:`Muirhead1975`.


    Let `l_1 \ge l_2 \ge \cdots  \ge l_m > 0` be the latent roots of `S_1S_2^{-1}.
    Let `\Omega = \Sigma^{-1} M' M`, and `\omega_i` are the latent roots of `\Omega`.
    An upper bound for the distribution function of `l_1` is given by

    .. math:: P(l_1 \le x) \le \prod_{i=1}^m (F_{n1,n2}(\omega_i) \le x)

    and a lower bound for the distribution function of `l_m` is given by


    .. math:: P(l_m \le x) \ge \prod_{i=1}^m (F_{n1,n2}(\omega_i) \ge x)


    where  `F_{n1,n2}(\omega_i)`  denotes a random variable having the noncentral F distribution on n1 and n2 degrees of freedom and noncentrality parameter `\omega_i`.


    Muirhead,R.J.; Chikuse,Y. (1975): Approximations for the distributions of the extreme latent roots of three matrices. Ann. Inst. Statist. Math., 27, 473-478


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.roy_glm_mu2_cdf(x, nu, nc); mx = mpm.roy_glm_mu2_cdf(x, nu, nc)
        >>> ix = ipm.roy_glm_mu2_cdf(x, nu, nc); fx = fpm.roy_glm_mu2_cdf(x, nu, nc)
        >>> gx = gmp.roy_glm_mu2_cdf(x, nu, nc); ax = apm.roy_glm_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_roy_ind_mu2_cdf: 

Noncentral Roy's largest root under the independence alternative
-------------------------------------------------------------------------------

.. method:: ctx.roy_ind_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.



    See :cite:t:`Muirhead1975`.


    Let `l_1 \ge l_2 \ge \cdots  \ge l_m > 0` be the latent roots of `S_1S_2^{-1}.
    Let `\Omega = \Sigma^{-1} M' M`, and `\omega_i` are the latent roots of `\Omega`.
    An upper bound for the distribution function of `l_1` is given by

    .. math:: P(l_1 \le x) \le \prod_{i=1}^m (F_{n1,n2}(\omega_i) \le x)

    and a lower bound for the distribution function of `l_m` is given by


    .. math:: P(l_m \le x) \ge \prod_{i=1}^m (F_{n1,n2}(\omega_i) \ge x)


    where  `F_{n1,n2}(\omega_i)`  denotes a random variable having the noncentral F distribution on n1 and n2 degrees of freedom and noncentrality parameter `\omega_i`.


    Muirhead,R.J.; Chikuse,Y. (1975): Approximations for the distributions of the extreme latent roots of three matrices. Ann. Inst. Statist. Math., 27, 473-478


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.roy_ind_mu2_cdf(x, nu, nc); mx = mpm.roy_ind_mu2_cdf(x, nu, nc)
        >>> ix = ipm.roy_ind_mu2_cdf(x, nu, nc); fx = fpm.roy_ind_mu2_cdf(x, nu, nc)
        >>> gx = gmp.roy_ind_mu2_cdf(x, nu, nc); ax = apm.roy_ind_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





