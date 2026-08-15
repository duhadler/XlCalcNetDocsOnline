






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />






|newpage|

Approximations based on the central `t`, `F` or beta distribution
===============================================================================



.. _rst_mpm_dunn_sidak_qtf: 

Dunn-Šidák percentage points
----------------------------------------------------------------------------------------------------

.. method:: ctx.dunn_sidak_qtf(q, nu, C)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns the percentage points of Dunn-Šidák.

    See also: Kirk, Games.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.dunn_sidak_qtf(x, nu, nc); mx = mpm.dunn_sidak_qtf(x, nu, nc)
        >>> ix = ipm.dunn_sidak_qtf(x, nu, nc); fx = fpm.dunn_sidak_qtf(x, nu, nc)
        >>> gx = gmp.dunn_sidak_qtf(x, nu, nc); ax = apm.dunn_sidak_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_fisher_f_nc_mu2_cdf: 

Singly non-central Fisher F distribution: cdf, sf (Patnaik)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_f_nc_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns an approximation to the cdf of the noncentral Fisher F distribution. 

    [Patnaik1949` suggests the following approximation, see also :cite:t:`Tiku1966`:

    .. math:: F_{F'}(x;n_1,n_2,\lambda) \thickapprox  F_F\left(y; m_1, n_2\right),  \quad \text{where}


    `A_1=(n_1+\lambda)`, 
    
    `B_1=(n_1+2\lambda)`, 
    
    `m_1= A_1^2/B_1`, 
    
    `y=n_1/A_1`, 

    and `F_F\left(\cdot; m_1, n_2\right)` denotes the CDF of a central `F` distribution with `m_1` and `n_2` degrees of freedom.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_f_nc_mu2_cdf(x, nu, nc); mx = mpm.fisher_f_nc_mu2_cdf(x, nu, nc)
        >>> ix = ipm.fisher_f_nc_mu2_cdf(x, nu, nc); fx = fpm.fisher_f_nc_mu2_cdf(x, nu, nc)
        >>> gx = gmp.fisher_f_nc_mu2_cdf(x, nu, nc); ax = apm.fisher_f_nc_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_fisher_f_nc_mu2_qtf: 

Singly non-central F distribution: qtf, isf (Patnaik)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_f_nc_mu2_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to `F_{\alpha,n_1,n_2,\lambda}`, the `\alpha`-quantile of a non-central F-distribution with `n_1` and `n_2` degress of freedom and noncentrality parameter `\lambda`.

    .. math:: F_{\alpha,n_1,n_2,\lambda}  \thickapprox  c \cdot F_{\alpha,m_1,n_2,} 
    
    `A_1=(n_1+\lambda)`, 
    
    `B_1=(n_1+2\lambda)`, 
    
    `m_1= A_1^2/B_1`, 
    
    `c=A_1/n_1`, 

    and `F_{\alpha,m_1,n_2,}` denotes the `\alpha`-quantile of a central `F`-distribution with `m_1` and `n_2` degress of freedom. 


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_f_nc_mu2_qtf(x, nu, nc); mx = mpm.fisher_f_nc_mu2_qtf(x, nu, nc)
        >>> ix = ipm.fisher_f_nc_mu2_qtf(x, nu, nc); fx = fpm.fisher_f_nc_mu2_qtf(x, nu, nc)
        >>> gx = gmp.fisher_f_nc_mu2_qtf(x, nu, nc); ax = apm.fisher_f_nc_mu2_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_fisher_f_nc_mu2_cl: 

Singly non-central F: confidence interval for the noncentrality parameter `\lambda` 
-----------------------------------------------------------------------------------------

.. method:: ctx.fisher_f_nc_mu2_cl(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the confidence interval (CI) for the noncentrality parameter `\lambda` of a singly non-central F-distribution.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_f_nc_mu2_cl(x, nu, nc); mx = mpm.fisher_f_nc_mu2_cl(x, nu, nc)
        >>> ix = ipm.fisher_f_nc_mu2_cl(x, nu, nc); fx = fpm.fisher_f_nc_mu2_cl(x, nu, nc)
        >>> gx = gmp.fisher_f_nc_mu2_cl(x, nu, nc); ax = apm.fisher_f_nc_mu2_cl(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_mpm_fisher_f_nc2_mu2_cdf: 

Doubly non-central F distribution: cdf, sf (Patnaik)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_f_nc2_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the doubly noncentral Fisher F distribution. 

    Mudholkar (1976) suggests an approximation by noncentral `F`, which can be converted into an approximation by central `F` as follows:

    .. math::  F_{F''}(x;n_1,n_2,\lambda_1,\lambda_2) \thickapprox  F_F\left(y; m_1, m_2\right),  \quad \text{where}

    `A_1=(n_1+\lambda_1), A_2=(n_2+\lambda_2)`,  
    
    `B_1=(n_1+2\lambda_1), B_2=(n_2+2\lambda_2)`, 
    
    `m_1= A_1^2/B_1, m_2= A_2^2/B_2`, 
    
    `y= x (n_1 A_2)/(n_2 A_1)`, 


    and `F_F\left(\cdot; m_1, m_2\right)` denotes the CDF of a central `F` distribution with `m_1` and `m_2` degrees of freedom.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_f_nc2_mu2_cdf(x, nu, nc); mx = mpm.fisher_f_nc2_mu2_cdf(x, nu, nc)
        >>> ix = ipm.fisher_f_nc2_mu2_cdf(x, nu, nc); fx = fpm.fisher_f_nc2_mu2_cdf(x, nu, nc)
        >>> gx = gmp.fisher_f_nc2_mu2_cdf(x, nu, nc); ax = apm.fisher_f_nc2_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_mpm_fisher_f_nc2_mu2_qtf: 

Doubly non-central F distribution: qtf, isf (Patnaik)
-------------------------------------------------------------------------------


.. method:: ctx.fisher_f_nc2_mu2_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to `F_{\alpha,n_1,n_2,\lambda_1,\lambda_2}`, the `\alpha`-quantile of a doubly non-central F-distribution with `n_1` and `n_2` degress of freedom and noncentrality parameters `\lambda_1` and `\lambda_2`, is obtained as

    .. math:: F_{\alpha,n_1,n_2,\lambda_1,\lambda_2}  \thickapprox  c \cdot F_{\alpha,m_1,m_2,} 

    `A_1=(n_1+\lambda_1), A_2=(n_1+\lambda_2)`,  
    
    `B_1=(n_1+2\lambda_1), B_2=(n_1+2\lambda_2)`, 
    
    `m_1= A_1^2/B_1, m_2= A_2^2/B_2`, 
    
    `c=(n_2 A_1)/(n_1 A_2)`, 

    and denotes the `\alpha`-quantile of a central `F`-distribution with `m_1` and `m_2` degress of freedom.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_f_nc2_mu2_qtf(x, nu, nc); mx = mpm.fisher_f_nc2_mu2_qtf(x, nu, nc)
        >>> ix = ipm.fisher_f_nc2_mu2_qtf(x, nu, nc); fx = fpm.fisher_f_nc2_mu2_qtf(x, nu, nc)
        >>> gx = gmp.fisher_f_nc2_mu2_qtf(x, nu, nc); ax = apm.fisher_f_nc2_mu2_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_fisher_r2_lee_cdf: 

Multiple correlation coefficient: cdf, sf (Lee and Gurland)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_r2_lee_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the Fisher `R^2` distribution. 

    See also :cite:t:`Lee1971`, :cite:t:`Gurland1968`, :cite:t:`Gurland1970`.


    .. math:: F_{F'}(x;n_1,n_2,\rho^2)  \thickapprox  F_F\left(x/c; m_1, n_2\right), 

    where `c=A_1/n_1`, `m_1= A_1^2/A_2`, `A_1=(n_1+n_2) (\gamma-1)+n_1`, `A_2=(n_1+n_2) (\gamma^2-1)+n_1`, `\gamma=1/(1-\rho^2)`, and `F_F\left(\cdot; m_1, n_2\right)` denotes the CDF of a central `F` distribution with `m_1` and `n_2` degrees of freedom.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_r2_lee_cdf(x, nu, nc); mx = mpm.fisher_r2_lee_cdf(x, nu, nc)
        >>> ix = ipm.fisher_r2_lee_cdf(x, nu, nc); fx = fpm.fisher_r2_lee_cdf(x, nu, nc)
        >>> gx = gmp.fisher_r2_lee_cdf(x, nu, nc); ax = apm.fisher_r2_lee_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_mpm_fisher_r2_lee_qtf: 

Multiple correlation coefficient: qtf, isf (Lee and Gurland)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_r2_lee_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the qtf of the Fisher `R^2` distribution. 

    See also :cite:t:`Lee1971`, :cite:t:`Gurland1968`, :cite:t:`Gurland1970`.


    .. math:: F_{F'}(x;n_1,n_2,\rho^2)  \thickapprox  F_F\left(x/c; m_1, n_2\right), 

    where `c=A_1/n_1`, `m_1= A_1^2/A_2`, `A_1=(n_1+n_2) (\gamma-1)+n_1`, `A_2=(n_1+n_2) (\gamma^2-1)+n_1`, `\gamma=1/(1-\rho^2)`, and `F_F\left(\cdot; m_1, n_2\right)` denotes the CDF of a central `F` distribution with `m_1` and `n_2` degrees of freedom.




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_r2_lee_qtf(x, nu, nc); mx = mpm.fisher_r2_lee_qtf(x, nu, nc)
        >>> ix = ipm.fisher_r2_lee_qtf(x, nu, nc); fx = fpm.fisher_r2_lee_qtf(x, nu, nc)
        >>> gx = gmp.fisher_r2_lee_qtf(x, nu, nc); ax = apm.fisher_r2_lee_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)







.. _rst_mpm_fisher_r2_lee_cl: 

Fisher `R^2`,: confidence limit for `\rho^2` 
-----------------------------------------------------------------------------------------

.. method:: ctx.fisher_r2_lee_cl(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the confidence interval (CI) for the noncentrality parameter `\rho^2` of Fisher `R^2` distribution.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_r2_lee_cl(x, nu, nc); mx = mpm.fisher_r2_lee_cl(x, nu, nc)
        >>> ix = ipm.fisher_r2_lee_cl(x, nu, nc); fx = fpm.fisher_r2_lee_cl(x, nu, nc)
        >>> gx = gmp.fisher_r2_lee_cl(x, nu, nc); ax = apm.fisher_r2_lee_cl(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






|newpage|


.. _rst_mpm_wilks_lambda_rao_cdf: 

Central Wilks' Lambda: cdf, sf (Rao)
-------------------------------------------------------------------------------

.. method:: ctx.wilks_lambda_rao_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns Rao's F approximation to the cdf of  Wilk's `\Lambda`

    Define

    .. math:: z = \frac{1-\Lambda^{1/r}}{\Lambda^{1/r}} \frac{rt-2u}{pq},  \quad \text{where } r = v - \frac{p-q+1}{2}, u = \frac{pq-2}{4}, \quad \text{and } 


    .. math:: t=\sqrt{\frac{p^2 q^2 -4}{p^2 + q^2 -5}} \text{ if } p^2 + q^2 - 5 > 0 \text{ or } 1 \text{ otherwise.}


    Then `z` is approximately distributed as `F(z; pq, rt-2u)`.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.wilks_lambda_rao_cdf(x, nu, nc); mx = mpm.wilks_lambda_rao_cdf(x, nu, nc)
        >>> ix = ipm.wilks_lambda_rao_cdf(x, nu, nc); fx = fpm.wilks_lambda_rao_cdf(x, nu, nc)
        >>> gx = gmp.wilks_lambda_rao_cdf(x, nu, nc); ax = apm.wilks_lambda_rao_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_wilks_lambda_rao_qtf: 

Central Wilks' Lambda: qtf, isf (Rao)
-------------------------------------------------------------------------------

.. method:: ctx.wilks_lambda_rao_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns Rao's F approximation to the cdf of  Wilk's `\Lambda`

    Define

    .. math:: z = \frac{1-\Lambda^{1/r}}{\Lambda^{1/r}} \frac{rt-2u}{pq},  \quad \text{where } r = v - \frac{p-q+1}{2}, u = \frac{pq-2}{4}, \quad \text{and } 

    .. math:: t=\sqrt{\frac{p^2 q^2 -4}{p^2 + q^2 -5}} \text{ if } p^2 + q^2 - 5 > 0 \text{ or } 1 \text{ otherwise.}

    Then `z` is approximately distributed as `F(z; pq, rt-2u)`.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.wilks_lambda_rao_qtf(x, nu, nc); mx = mpm.wilks_lambda_rao_qtf(x, nu, nc)
        >>> ix = ipm.wilks_lambda_rao_qtf(x, nu, nc); fx = fpm.wilks_lambda_rao_qtf(x, nu, nc)
        >>> gx = gmp.wilks_lambda_rao_qtf(x, nu, nc); ax = apm.wilks_lambda_rao_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_hotelling_t2_mu3_cdf: 

Central Hotelling's `T^2`: cdf, sf (Pillai and Young)
-------------------------------------------------------------------------------

.. method:: ctx.hotelling_t2_mu3_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the central Hotelling's `T^2` distribution. See also :cite:t:`Pillai1971`.

    Let `m=(n_1-p-1)/2`, `n=(n_2-p-1)/2`, and `r = 2m + p +1`. Define

    .. math::    \mu_1 = \frac{pr}{2n}, \quad \mu_2 = \mu_1 \frac{(2n+r)(2n+p)}{2n(n-1)(2n+1)},  \quad \mu_3 = \mu_2 \frac{2(n+r)(n+p)}{n(n-2)(n+1)},

    .. math:: a= \frac{(2\mu_13\mu_2+3\mu_1^2\mu_3-6\mu_1\mu_2^2-\mu_2\mu_3)}{(\mu_2\mu_3+4\mu_1\mu_2^2-\mu_1^2\mu_3)}+1, \quad    b= \frac{a(a+2)-\mu_1^2/\mu_2}{a-\mu_1^2/\mu_2} - a,

    .. math:: K= \frac{\mu_1(b-1)}{a}, \quad w=\frac{x}{x+K}.


    Then `x=T^2/n_2` is approximately distributed as `I_w(a,b)`.


    .. caution
       Code in DistPillaiHotelling.Hotelling()


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hotelling_t2_mu3_cdf(x, nu, nc); mx = mpm.hotelling_t2_mu3_cdf(x, nu, nc)
        >>> ix = ipm.hotelling_t2_mu3_cdf(x, nu, nc); fx = fpm.hotelling_t2_mu3_cdf(x, nu, nc)
        >>> gx = gmp.hotelling_t2_mu3_cdf(x, nu, nc); ax = apm.hotelling_t2_mu3_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_hotelling_t2_mu3_qtf: 

Central Hotelling's `T^2`: qtf, isf (Pillai and Young)
-------------------------------------------------------------------------------

.. method:: ctx.hotelling_t2_mu3_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the qtf of the central Hotelling's `T^2` distribution, based on matching the first 3 moments.. See also :cite:t:`Pillai1971`.


    Let `m=(n_1-p-1)/2`, `n=(n_2-p-1)/2`, and `r = 2m + p +1`. Define

    .. math::    \mu_1 = \frac{pr}{2n}, \quad \mu_2 = \mu_1 \frac{(2n+r)(2n+p)}{2n(n-1)(2n+1)},  \quad \mu_3 = \mu_2 \frac{2(n+r)(n+p)}{n(n-2)(n+1)},

    .. math:: a= \frac{(2\mu_13\mu_2+3\mu_1^2\mu_3-6\mu_1\mu_2^2-\mu_2\mu_3)}{(\mu_2\mu_3+4\mu_1\mu_2^2-\mu_1^2\mu_3)}+1, \quad    b= \frac{a(a+2)-\mu_1^2/\mu_2}{a-\mu_1^2/\mu_2} - a,

    .. math:: K= \frac{\mu_1(b-1)}{a}, \quad w=\frac{x}{x+K}.


    Then `x=T^2/n_2` is approximately distributed as `I_w(a,b)`.


    .. caution
       Code in DistPillaiHotelling.Hotelling()


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hotelling_t2_mu3_qtf(x, nu, nc); mx = mpm.hotelling_t2_mu3_qtf(x, nu, nc)
        >>> ix = ipm.hotelling_t2_mu3_qtf(x, nu, nc); fx = fpm.hotelling_t2_mu3_qtf(x, nu, nc)
        >>> gx = gmp.hotelling_t2_mu3_qtf(x, nu, nc); ax = apm.hotelling_t2_mu3_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_pillay_v_mu3_cdf: 

Central Pillai's `V`: cdf, sf (Ginzberg)
-------------------------------------------------------------------------------

.. method:: ctx.pillay_v_mu3_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the central Pillai `V` distribution, based on matching the first 3 moments. See also :cite:t:`Ginzberg2013`.


    Let `m=(n_1-p-1)/2`, `n=(n_2-p-1)/2`, and `r = m + n + p`. Define

    .. math:: \mu_1 = \frac{p (2 m + p + 1)}{2 (r + 1)}, \quad \mu_2 = \mu_1  \frac{(2 n + p + 1) (2 r - p + 2)}{2 (r + 1) (r + 2) (2 r + 1)}, \quad \mu_3 = \mu_2 \frac{4 (n - m) (m + n + 1)}{(r + 1) (r + 3) (2 r)},

    .. math:: c = 4 \mu_1 \mu_2^2 - \mu_1^2 \mu_3 + \mu_2 \mu_3, \quad  d= 2 \mu_2^2 -\mu_1 \mu_3,

    .. math:: a= \frac{2 \mu_1 ( \mu_1^2 \mu_2 - \mu_2^2 + \mu_1 \mu_3)}{c}, \quad  b=\frac{a}{d} \: \frac{ \mu_2 (2 \mu_1 \mu_2 + \mu_3) }{ \mu_1 }, \quad w= \frac{d}{c} x.


    Then `x=V/n_2` is approximately distributed as `I_w(a,b)`.

    .. caution
       Code in DistPillaiHotelling.Pillai3VX()


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pillay_v_mu3_cdf(x, nu, nc); mx = mpm.pillay_v_mu3_cdf(x, nu, nc)
        >>> ix = ipm.pillay_v_mu3_cdf(x, nu, nc); fx = fpm.pillay_v_mu3_cdf(x, nu, nc)
        >>> gx = gmp.pillay_v_mu3_cdf(x, nu, nc); ax = apm.pillay_v_mu3_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_pillay_v_mu3_qtf: 

Central Pillai's `V`: qtf, isf (Ginzberg)
-------------------------------------------------------------------------------

.. method:: ctx.pillay_v_mu3_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the central Pillai `V` distribution. See also :cite:t:`Ginzberg2013`.

    Let `m=(n_1-p-1)/2`, `n=(n_2-p-1)/2`, and `r = m + n + p`. Define

    .. math:: \mu_1 = \frac{p (2 m + p + 1)}{2 (r + 1)}, \quad \mu_2 = \mu_1  \frac{(2 n + p + 1) (2 r - p + 2)}{2 (r + 1) (r + 2) (2 r + 1)}, \quad \mu_3 = \mu_2 \frac{4 (n - m) (m + n + 1)}{(r + 1) (r + 3) (2 r)},

    .. math:: c = 4 \mu_1 \mu_2^2 - \mu_1^2 \mu_3 + \mu_2 \mu_3, \quad  d= 2 \mu_2^2 -\mu_1 \mu_3,

    .. math:: a= \frac{2 \mu_1 ( \mu_1^2 \mu_2 - \mu_2^2 + \mu_1 \mu_3)}{c}, \quad  b=\frac{a}{d} \: \frac{ \mu_2 (2 \mu_1 \mu_2 + \mu_3) }{ \mu_1 }, \quad w= \frac{d}{c} x.


    Then `x=V/n_2` is approximately distributed as `I_w(a,b)`.

    .. caution
       Code in DistPillaiHotelling.Pillai3VX()


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pillay_v_mu3_qtf(x, nu, nc); mx = mpm.pillay_v_mu3_qtf(x, nu, nc)
        >>> ix = ipm.pillay_v_mu3_qtf(x, nu, nc); fx = fpm.pillay_v_mu3_qtf(x, nu, nc)
        >>> gx = gmp.pillay_v_mu3_qtf(x, nu, nc); ax = apm.pillay_v_mu3_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_beta_product_mu3_cdf: 

Product of independent beta variables: cdf, sf (Nagarsenker)
-------------------------------------------------------------------------------

.. method:: ctx.beta_product_mu3_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the product of independent beta variables distribution. 

    :cite:t:`Nagarsenker1983` proposes the following approximation:

    .. math:: \text{Pr}(W_p \leq \lambda) =  I(x; sm + d, \nu_1 + r) + O(sm^{-3}), \quad \text{where}

    .. math:: x=\lambda^{1/s}; \quad a=\frac{\nu_1 - \nu_2}{2\nu_1}; \quad d=\frac{1-\nu_1}{2};  \quad \nu_r=\sum_{i=1}^p{c_i^r - b_i^r}

    .. math:: s^2 = \frac{-2B_2((1+\nu_1)/2)}{\sum_{i=1}^p{B_3(a+b_i) - B_3(a+c_i) }}


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.beta_product_mu3_cdf(x, nu, nc); mx = mpm.beta_product_mu3_cdf(x, nu, nc)
        >>> ix = ipm.beta_product_mu3_cdf(x, nu, nc); fx = fpm.beta_product_mu3_cdf(x, nu, nc)
        >>> gx = gmp.beta_product_mu3_cdf(x, nu, nc); ax = apm.beta_product_mu3_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_beta_product_mu3_qtf: 

Product of independent beta variables: qtf, isf (Nagarsenker)
-------------------------------------------------------------------------------

.. method:: ctx.beta_product_mu3_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the qtf of the product of independent beta variables distribution. 


    :cite:t:`Nagarsenker1983` proposes the following approximation:

    .. math:: \text{Pr}(W_p \leq \lambda) =  I(x; sm + d, \nu_1 + r) + O(sm^{-3}), \quad \text{where}

    .. math:: x=\lambda^{1/s}; \quad a=\frac{\nu_1 - \nu_2}{2\nu_1}; \quad d=\frac{1-\nu_1}{2};  \quad \nu_r=\sum_{i=1}^p{c_i^r - b_i^r}

    .. math:: s^2 = \frac{-2B_2((1+\nu_1)/2)}{\sum_{i=1}^p{B_3(a+b_i) - B_3(a+c_i) }}




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.beta_product_mu3_qtf(x, nu, nc); mx = mpm.beta_product_mu3_qtf(x, nu, nc)
        >>> ix = ipm.beta_product_mu3_qtf(x, nu, nc); fx = fpm.beta_product_mu3_qtf(x, nu, nc)
        >>> gx = gmp.beta_product_mu3_qtf(x, nu, nc); ax = apm.beta_product_mu3_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)



