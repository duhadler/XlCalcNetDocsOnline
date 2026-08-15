






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />









|newpage|

Approximations based on the chi-squared distribution
===============================================================================



.. _rst_chi2_nc_mu2_cdf: 

Non-Central chi-squared : cdf, sf  (Patnaik)
-------------------------------------------------------------------------------

.. method:: ctx.chi2_nc_mu2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the noncentral chi-squared distribution by matching the first 2 moments.

    :cite:t:`Patnaik1949` gives the following 2-moment approximation based on the central `\chi^2`-distribution:

    .. math:: F_{\chi^2}\left(n, x; \lambda\right) \thickapprox F_{\chi^2}\left(n_1, x_1;\right), \quad \text{where } n_1= \frac{(n+\lambda)^2}{n+2\lambda} , \quad  x_1= \frac{x(n+\lambda)}{n+2\lambda}

    where `F_{\chi^2}(n, \cdot)` is the cdf of the (central) `\chi^2` distribution (see section \ref{sec:ChiSquareDistribution_cdf}).



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.chi2_nc_mu2_cdf(x, nu, nc); mx = mpm.chi2_nc_mu2_cdf(x, nu, nc)
        >>> ix = ipm.chi2_nc_mu2_cdf(x, nu, nc); fx = fpm.chi2_nc_mu2_cdf(x, nu, nc)
        >>> gx = gmp.chi2_nc_mu2_cdf(x, nu, nc); ax = apm.chi2_nc_mu2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_chi2_nc_mu2_qtf: 

Non-Central chi-squared: qtf, isf  (Patnaik)
-------------------------------------------------------------------------------

.. method:: ctx.chi2_nc_mu2_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the qtf of the noncentral chi-squared distribution.

    The noncentral quantile is approximated as in :cite:t:`Patnaik1949`:

    .. math:: \chi^2_{n,\lambda,\alpha}  \thickapprox  (1+b) \chi^2_{n_1,\alpha} , \quad \text{where } n_1= \frac{(n+\lambda)^2}{n+2\lambda} , \quad  b = \frac{\lambda}{n+\lambda}



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.chi2_nc_mu2_qtf(x, nu, nc); mx = mpm.chi2_nc_mu2_qtf(x, nu, nc)
        >>> ix = ipm.chi2_nc_mu2_qtf(x, nu, nc); fx = fpm.chi2_nc_mu2_qtf(x, nu, nc)
        >>> gx = gmp.chi2_nc_mu2_qtf(x, nu, nc); ax = apm.chi2_nc_mu2_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_chi2_nc_wb_cl: 

Non-Central chi-squared: confidence limit for `\lambda` (Winterbottom)
-------------------------------------------------------------------------------------------------------

.. method:: ctx.chi2_nc_wb_cl(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the confidence interval (CI) for the noncentrality parameter `\lambda` of noncentral chi-squared distribution, as decribed in :cite:t:`Winterbottom1980`.


    [Winterbottom1979` gives the following formula to determine the paramter `\lambda` of a noncentral `\chi^2` distribution with `n` degrees of freedom, 
    so that `F_{\chi^2}\left(n, x; 0\right)=1-\alpha` and `F_{\chi^2}\left(n, x; \lambda\right)=1-\beta`. Let c be the `1-\alpha` percentage point of a `\chi^2`-distribution with `n` degrees of freedom, 
    let `x` be the `1-\beta` percentage point of a `N(0,1)` distribution, and `T=(c-n)/n`, `Y=2T+1`. Then


    .. math::
       :nowrap:

       \begin{eqnarray}
        \lambda & \thickapprox & nT + \sqrt{2nY}x + \frac{2((3T+2)x^2+3T+1))}{3Y} - \frac{(6T+5)x^3-(36T^2+42T+17)x}{18\sqrt{nY^5/2}} \\
        && +\: \frac{(324T^2+594T+276)x^4}{405nY^4} - \frac{(1080T^3+2484T^2+976)x^2}{405nY^4}  \nonumber \\
        && +\: \frac{1080T^3+1512T^2+612T+148}{405nY^4} - \frac{(10368T^3+30780T^2+30564T+10143)x^5}{9720\sqrt{n^3Y^{11}/2}} \nonumber \\
        && +\: \frac{(25920T^4+98928T^3+163080T^2+137544T+47188)x^3}{9720\sqrt{n^3Y^{11}/2}}\nonumber \\
        && +\: \frac{(45360T^4+106704T^3+80460T^2+31092T+13489)x}{9720\sqrt{n^3Y^{11}/2}}\nonumber 
       \end{eqnarray}



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.chi2_nc_wb_cl(x, nu, nc); mx = mpm.chi2_nc_wb_cl(x, nu, nc)
        >>> ix = ipm.chi2_nc_wb_cl(x, nu, nc); fx = fpm.chi2_nc_wb_cl(x, nu, nc)
        >>> gx = gmp.chi2_nc_wb_cl(x, nu, nc); ax = apm.chi2_nc_wb_cl(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_mpm_roy_chiani_pdf: 

Roy's largest root `\theta`: pdf  (Chiani)
-------------------------------------------------------------------------------

.. method:: ctx.roy_chiani_pdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the pdf of the distribution of Roy's largest root `\theta`.

    See :cite:t:`Chiani2012`, :cite:t:`Chiani2014` proposes the following algorithm:

    .. math::	F_{\Theta_1}(\theta_1) \approx P \left(k, \frac{\log(\theta_1/(1-\theta_1))-\mu + \sigma \alpha}{\delta}  \right)

    and for its inverse, useful for evaluating the percentiles,

    .. math::	F_{\Theta_1}^{-1}(\theta_1) \approx \frac{\exp(\sigma(\delta P^{-1}(k,y)-\alpha))+\mu}{1+\exp(\sigma(\delta P^{-1}(k,y)-\alpha))+\mu}, 

    where

    .. math::	\mu = 2 \log \tan \left(\frac{\gamma + \phi}{2}\right), \quad \sigma^3 = \frac{16}{(m+n+1)^2} \frac{1}{\sin^2(\gamma + \phi) \sin \gamma \sin \phi}

    .. math::	\gamma = \arccos \left(\frac{m+n-2p}{m+n-1}\right), \quad  \phi = \arccos \left(\frac{m-n}{m+n-1}\right),

    and the constants `k = 46.446`, `\delta = 0.186054`, `\alpha = 9.84801` have been
    chosen to match the moments of the approximation to that of the Tracy-Widom.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.roy_chiani_pdf(x, nu, nc); mx = mpm.roy_chiani_pdf(x, nu, nc)
        >>> ix = ipm.roy_chiani_pdf(x, nu, nc); fx = fpm.roy_chiani_pdf(x, nu, nc)
        >>> gx = gmp.roy_chiani_pdf(x, nu, nc); ax = apm.roy_chiani_pdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_roy_chiani_cdf: 

Roy's largest root: cdf and sf  (Chiani)
-------------------------------------------------------------------------------

.. method:: ctx.roy_chiani_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the distribution of Roy's largest root `\theta`.


    See :cite:t:`Chiani2012`, :cite:t:`Chiani2014` proposes the following algorithm:

    .. math::	F_{\Theta_1}(\theta_1) \approx P \left(k, \frac{\log(\theta_1/(1-\theta_1))-\mu + \sigma \alpha}{\delta}  \right)

    and for its inverse, useful for evaluating the percentiles,

    .. math::	F_{\Theta_1}^{-1}(\theta_1) \approx \frac{\exp(\sigma(\delta P^{-1}(k,y)-\alpha))+\mu}{1+\exp(\sigma(\delta P^{-1}(k,y)-\alpha))+\mu}, 

    where

    .. math::	\mu = 2 \log \tan \left(\frac{\gamma + \phi}{2}\right), \quad \sigma^3 = \frac{16}{(m+n+1)^2} \frac{1}{\sin^2(\gamma + \phi) \sin \gamma \sin \phi}

    .. math::	\gamma = \arccos \left(\frac{m+n-2p}{m+n-1}\right), \quad  \phi = \arccos \left(\frac{m-n}{m+n-1}\right),

    and the constants `k = 46.446`, `\delta = 0.186054`, `\alpha = 9.84801` have been
    chosen to match the moments of the approximation to that of the Tracy-Widom.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.roy_chiani_cdf(x, nu, nc); mx = mpm.roy_chiani_cdf(x, nu, nc)
        >>> ix = ipm.roy_chiani_cdf(x, nu, nc); fx = fpm.roy_chiani_cdf(x, nu, nc)
        >>> gx = gmp.roy_chiani_cdf(x, nu, nc); ax = apm.roy_chiani_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_roy_chiani_qtf: 

Roy's largest root: qtf and isf  (Chiani)
-------------------------------------------------------------------------------

.. method:: ctx.roy_chiani_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the qtf of the distribution of Roy's largest root `\theta`.


    See :cite:t:`Chiani2012`, :cite:t:`Chiani2014` proposes the following algorithm:

    .. math::	F_{\Theta_1}(\theta_1) \approx P \left(k, \frac{\log(\theta_1/(1-\theta_1))-\mu + \sigma \alpha}{\delta}  \right)

    and for its inverse, useful for evaluating the percentiles,

    .. math::	F_{\Theta_1}^{-1}(\theta_1) \approx \frac{\exp(\sigma(\delta P^{-1}(k,y)-\alpha))+\mu}{1+\exp(\sigma(\delta P^{-1}(k,y)-\alpha))+\mu}, 

    where

    .. math::	\mu = 2 \log \tan \left(\frac{\gamma + \phi}{2}\right), \quad \sigma^3 = \frac{16}{(m+n+1)^2} \frac{1}{\sin^2(\gamma + \phi) \sin \gamma \sin \phi}

    .. math::	\gamma = \arccos \left(\frac{m+n-2p}{m+n-1}\right), \quad  \phi = \arccos \left(\frac{m-n}{m+n-1}\right),

    and the constants `k = 46.446`, `\delta = 0.186054`, `\alpha = 9.84801` have been
    chosen to match the moments of the approximation to that of the Tracy-Widom.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.roy_chiani_qtf(x, nu, nc); mx = mpm.roy_chiani_qtf(x, nu, nc)
        >>> ix = ipm.roy_chiani_qtf(x, nu, nc); fx = fpm.roy_chiani_qtf(x, nu, nc)
        >>> gx = gmp.roy_chiani_qtf(x, nu, nc); ax = apm.roy_chiani_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)


