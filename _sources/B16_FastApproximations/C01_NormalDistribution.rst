






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />









Approximations based on the normal distribution
===============================================================================


.. _rst_mpm_chi2_nc_penev_cdf: 

Non-central chi-squared distribution: cdf and sf (Penev)
-------------------------------------------------------------------------------

.. method:: ctx.chi2_nc_penev_cdf(x, nu, nc)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the (non-)central chi-squared distribution.

    [Penev2000` give the following first and second order Wiener germ approximation:

    .. math:: F_{\chi^2}\left(n, x; \lambda\right) \thickapprox \Phi \left(\text{sgn}(s) \sqrt{n(s-1)^2(1/(2s) + m- h(1-s)/s) - \log(A(s)) + 2B(s)/n} \right)

    .. math:: \text{where } m = \lambda/n; \quad h(y) = \frac{(1-y) \log(1-y)+y- \tfrac{1}{2}y^2}{y^2} ; \quad s= \frac{\sqrt{1+4xm/n}-1}{2m} 

    .. math:: A(s) = \frac{1}{s} - \frac{2}{s} \cdot  \frac{h(1-s)}{1+2ms}; \quad  B(s) = \frac{(1+3m)^2}{9(1+2m)^3}

    where  `\Phi(\cdot)` denotes the cdf of the normal distribution (see ).




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.cdisn_penev(x, nu, nc); mx = mpm.cdisn_penev(x, nu, nc)
        >>> ix = ipm.cdisn_penev(x, nu, nc); fx = fpm.cdisn_penev(x, nu, nc)
        >>> gx = gmp.cdisn_penev(x, nu, nc); ax = apm.cdisn_penev(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)



.. _rst_mpm_chi_squared_nc_canal_qtf: 

(Non-central) chi-squared distribution: qtf and isf  (Canal)
-------------------------------------------------------------------------------

.. method:: ctx.chi2_nc_canal_qtf(LeftTail, RightTail, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the quantile of the (non-)central chi-squared distribution.

    Let `z_\alpha` and `\chi^2_{n,\alpha}` be the `\alpha`-quantiles  of the standard normal distribution and central chi-square distribution with `n` the degrees of freedom. For `n=1` and `n=2`, the following closed form expressions can be used:

    .. math:: \chi^2_{1,\alpha} = z^2_{\alpha}, \quad \chi^2_{2,\alpha} = 2 \log(1 - \alpha)


    At the extreme left tail of the distribution, for small `x`, the CDF of a `\chi^2` variable with `n` degrees of freedom can be approximated by the density of a `\chi^2` variable with `n+2` degrees of freedom:

    .. math:: F_{\chi^2}(n,x)  \thickapprox 2 f_{\chi^2}(n+2,x).

    The density of a `\chi^2` variable with `n+2` degrees of freedom can be inverted in closed form using the Lambert `W` function, which leads to the following approximation:

    .. math:: \chi^2_{n,\alpha} \thickapprox  f^{-1}_{\chi^2}(n+2,\alpha) = -2 W(t)/a  , \quad \text{where} 

    .. math:: a=\frac{1}{(n+2)/2-1}, \quad k=\log(\Gamma((n+2)/2), \quad d=a-\log(1-\alpha)+k, \quad t=-a e^{p+d}

    This approximation is used for `|t|<0.1`, and the Lambert `W` function is approximated as

    .. math:: W(x)  \thickapprox x - x^2 + \tfrac{3}{2} x^3 - \tfrac{8}{3} x^4 - \tfrac{125}{24} x^5.



    Otherwise, the quantile is approximated by inverting a formula proposed by  :cite:t:`Canal2005`:

    .. math:: \chi^2_{n,\alpha}  \thickapprox  n\left( \frac{1}{2}+  \frac{t}{2}- \frac{3}{2t}\right)^6, \quad \text{where}

    .. math:: t = \left({-5+2L + 2 \sqrt{13-5L+L^2}} \right)^{1/3} , \quad L = 6 \left(m + s \left(z_{\alpha} + a (z^2_{\alpha} - 1) -   a^2 (2 z^3_{\alpha} - 5 z_{\alpha})  \right) \right)

    .. math:: m =  \frac{5}{6} -  \frac{1}{9n}  - \frac{7}{648n^2} - \frac{25}{2187n^3}, \quad s^2 =  \frac{1}{18n}  + \frac{1}{162n^2} - \frac{37}{11664n^3}, \quad a = \frac{1}{162 \sqrt{2n^3}} = \gamma_1/6.


    The noncentral quantile is approximated as

    .. math:: \chi^2_{n,\lambda,\alpha}  \thickapprox  (1+b) \chi^2_{n_1,\alpha} , \quad \text{where } n_1= \frac{(n+\lambda)^2}{n+2\lambda} , \quad  b = \frac{\lambda}{n+\lambda}



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.chi2_nc_canal_qtf(x, nu, nc); mx = mpm.chi2_nc_canal_qtf(x, nu, nc)
        >>> ix = ipm.chi2_nc_canal_qtf(x, nu, nc); fx = fpm.chi2_nc_canal_qtf(x, nu, nc)
        >>> gx = gmp.chi2_nc_canal_qtf(x, nu, nc); ax = apm.chi2_nc_canal_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_gamma_canal_qtf: 

Gamma distribution: qtf and isf  (Canal)
-------------------------------------------------------------------------------

.. method:: ctx.gamma_canal_qtf(LeftTail, RightTail, a)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the quantile of the gamma distribution.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.gamma_canal_qtf(x, nu, nc); mx = mpm.gamma_canal_qtf(x, nu, nc)
        >>> ix = ipm.gamma_canal_qtf(x, nu, nc); fx = fpm.gamma_canal_qtf(x, nu, nc)
        >>> gx = gmp.gamma_canal_qtf(x, nu, nc); ax = apm.gamma_canal_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_fisher_f_davis_qtf: 

F distribution: qtf and isf  (Davis)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_f_davis_qtf(LeftTail, RightTail, m, n)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the quantile of the F distribution.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.fisher_f_davis_qtf(x, nu, nc); mx = mpm.fisher_f_davis_qtf(x, nu, nc)
        >>> ix = ipm.fisher_f_davis_qtf(x, nu, nc); fx = fpm.fisher_f_davis_qtf(x, nu, nc)
        >>> gx = gmp.fisher_f_davis_qtf(x, nu, nc); ax = apm.fisher_f_davis_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_beta_davis_qtf: 

Beta distribution: qtf and isf  (Davis)
-------------------------------------------------------------------------------

.. method:: ctx.beta_davis_qtf(LeftTail, RightTail, a, b)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the quantile of the beta distribution.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.beta_davis_qtf(x, nu, nc); mx = mpm.beta_davis_qtf(x, nu, nc)
        >>> ix = ipm.beta_davis_qtf(x, nu, nc); fx = fpm.beta_davis_qtf(x, nu, nc)
        >>> gx = gmp.beta_davis_qtf(x, nu, nc); ax = apm.beta_davis_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_pearson_rho_wb_pdf: 

Pearson's rho distribution: pdf (Winterbottom)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_wb_pdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns an approximation to the pdf of Pearson's rho distribution. See also :cite:t:`Winterbottom1979`, :cite:t:`Winterbottom1980`.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pearson_rho_wb_pdf(x, nu, nc); mx = mpm.pearson_rho_wb_pdf(x, nu, nc)
        >>> ix = ipm.pearson_rho_wb_pdf(x, nu, nc); fx = fpm.pearson_rho_wb_pdf(x, nu, nc)
        >>> gx = gmp.pearson_rho_wb_pdf(x, nu, nc); ax = apm.pearson_rho_wb_pdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_mpm_pearson_rho_wb_cdf: 

Pearson's rho distribution: cdf and sf (Winterbottom)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_wb_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns an approximation to the cdf of Pearson's rho distribution. See also :cite:t:`Winterbottom1979`, :cite:t:`Winterbottom1980`.


    An improved approximation has been found by inverting Winterbottom's approximation for the confidence limits of `\rho`:

    .. math:: F_R(N, r,\rho)  \approx \Phi \left(\frac{k}{6} - \frac{2c}{k} - \frac{b}{3}\right), \quad \text{where} \quad m = N - 1,

    .. math:: a = \frac{1}{12\sqrt{m^3}} + \frac{6 r^4 - 3r^2 + 2}{48\sqrt{m^5}}, \quad  b = \frac{-r3}{6 a m^2}, \quad s=\frac{1}{a\sqrt{m}} + \frac{1+r^2}{4a\sqrt{m^3}} + \frac{11 r^4 - 2r^2 + 1}{32a\sqrt{m^5}}

    .. math:: t = \frac{Z(r)-Z(\rho)}{a} + \frac{r}{2 a m} + \frac{5 r^3 + 9r}{24 a m^2}, \quad d=t+ \frac{bs}{3} - \frac{2b^3}{27}

    .. math:: c = s-b^2/3, \quad p=\sqrt{|12c^3+81d^2|}, \quad k=(108d+12p)^{1/3}


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pearson_rho_wb_cdf(x, nu, nc); mx = mpm.pearson_rho_wb_cdf(x, nu, nc)
        >>> ix = ipm.pearson_rho_wb_cdf(x, nu, nc); fx = fpm.pearson_rho_wb_cdf(x, nu, nc)
        >>> gx = gmp.pearson_rho_wb_cdf(x, nu, nc); ax = apm.pearson_rho_wb_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_pearson_rho_wb_qtf: 

Pearson's rho distribution: qtf and isf  (Winterbottom)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_wb_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.

    Returns an approximation to the qtf of Pearson's rho distribution. See also :cite:t:`Winterbottom1979`, :cite:t:`Winterbottom1980`.


    Asymptotic expansions typically rely on the Fisher `z`-transform `Z(a)= \text{atanh}(a)` and its inverse `Z^{-1}(a) = \tanh(a)`.

    Let `m = N - 1` and let `u_\alpha` = `\Phi^{-1}(\alpha)` be the lower `100\alpha` percentage point of the standard normal distribution. An approximation to the `100\alpha` percentage point `r_\alpha` and the lower `100(1-\alpha)` confidence limit on `\rho`, `\rho_L`, is then obtained by  `r_\alpha \approx Z^{-1}(y_1)` , where

    .. math::
       :nowrap:

       \begin{eqnarray}
        y_1 & = & Z(\rho) + \frac{u_\alpha}{\sqrt{m}} + \frac{\rho}{2m} + \frac{u_\alpha^3+3(3-\rho^2)u_\alpha}{12\sqrt{m^3}} + \frac{4\rho^3 u_\alpha^2 + 15\rho-\rho^3}{24m^2} \\
        && +\: \frac{u_\alpha^5+(-60\rho^4+30\rho^2+80)u_\alpha^3 + (45\rho^4-21\rho^2+375)u_\alpha}{480\sqrt{m^5}}, \quad \text{and}   \nonumber  
       \end{eqnarray}



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pearson_rho_wb_qtf(x, nu, nc); mx = mpm.pearson_rho_wb_qtf(x, nu, nc)
        >>> ix = ipm.pearson_rho_wb_qtf(x, nu, nc); fx = fpm.pearson_rho_wb_qtf(x, nu, nc)
        >>> gx = gmp.pearson_rho_wb_qtf(x, nu, nc); ax = apm.pearson_rho_wb_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_pearson_rho_wb_cl: 

Pearson's rho distribution: confidence limit for `\rho`  (Winterbottom)
--------------------------------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_wb_cl(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the confidence interval (CI) for the noncentrality parameter `\rho` of Pearson's rho distribution, as decribed in :cite:t:`Winterbottom1980`.

    We use the Fisher `z`-transform `Z(a)= \text{atanh}(a)` and its inverse `Z^{-1}(a) = \tanh(a)`.

    Let `m = N - 1` and let `u_\alpha` = `\Phi^{-1}(\alpha)` be the lower `100\alpha` percentage point of the standard normal distribution. An approximation to the `100\alpha` percentage point `r_\alpha` and the lower `100(1-\alpha)` confidence limit on `\rho`, `\rho_L`, is then obtained by   `\rho_L \approx Z^{-1}(y_2)`, where

    .. math::
       :nowrap:

       \begin{eqnarray}
        y_2 & = & Z(r) + \frac{u_\alpha}{\sqrt{m}} - \frac{r}{2m} + \frac{u_\alpha^3+3(1+r^2)u_\alpha}{12\sqrt{m^3}} - \frac{4r^3 u_\alpha^2 + 5r^3+9r}{24m^2} \\
        && +\: \frac{u_\alpha^5+(60r^4-30r^2+20)u_\alpha^3 + (165r^4+30r^2+15)u_\alpha}{480\sqrt{m^5}}.   \nonumber  
       \end{eqnarray}




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pearson_rho_wb_cl(x, nu, nc); mx = mpm.pearson_rho_wb_cl(x, nu, nc)
        >>> ix = ipm.pearson_rho_wb_cl(x, nu, nc); fx = fpm.pearson_rho_wb_cl(x, nu, nc)
        >>> gx = gmp.pearson_rho_wb_cl(x, nu, nc); ax = apm.pearson_rho_wb_cl(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_student_t_nc_broda_pdf: 

Singly noncentral t: pdf (Broda)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_nc_broda_pdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the pdf of the singly noncentral t distribution, as decribed in :cite:t:`Witkovsky2013`, using the approximation to the cdf of the singly noncentral t distribution as decribed :cite:t:`Broda2007`.



    .. math:: f_{\text{StudentT}}\left(x, n, \delta\right) = \frac{n}{x} \left( F_{\text{StudentT}}\left(x \sqrt{(n+2)/n}, n+2, \delta\right) - F_{\text{StudentT}}\left(x, n, \delta\right)  \right), \quad x \ne 0,



    .. math:: f_{\text{StudentT}}\left(x, n, \delta\right) = \frac{\Gamma((n+1)/2)}{\sqrt{n \pi} \Gamma(n/2)} e^{- \frac{1}{2} \delta^2}




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.student_t_nc_broda_pdf(x, nu, nc); mx = mpm.student_t_nc_broda_pdf(x, nu, nc)
        >>> ix = ipm.student_t_nc_broda_pdf(x, nu, nc); fx = fpm.student_t_nc_broda_pdf(x, nu, nc)
        >>> gx = gmp.student_t_nc_broda_pdf(x, nu, nc); ax = apm.student_t_nc_broda_pdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)









.. _rst_mpm_student_t_nc_broda_cdf: 

Singly noncentral t: cdf, sf (Broda)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_nc_broda_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the singly noncentral t distribution, as decribed in :cite:t:`Broda2007`.

    Singly noncentral t: A saddlepoint approximation based on the joint cumulant generating function of `(x_1, x_2)`, with `x_1 \sim N(\mu, 1)` and  `x_2 \sim \chi^2(n)`, is possible (see Broda (2007)), and takes the following form:

    .. math:: F_{t'}(x;n,\mu)  =  \Phi(w)+\phi(w)\left( \frac{1}{w} - \frac{d}{u}  \right) + O(n^{-3/2}) , \quad \text{where}

    .. math:: s = \left(\mu x + \sqrt{4n(x^2+n)+\mu^2 x^2}\right) / (2x^2+2n), 

    .. math:: t_1 = -\mu + x s, \quad t_2 = -x t_1 / (2 n s), \quad  d = 1 / (t_1 s), 
    
    .. math:: u = \sqrt{(\mu x s + 2n ) / (2n)} / s, \quad  w = \text{sgn} (x - \mu) \sqrt{-\mu t_1 - 2n \log(s)}, 

    and `\Phi(\cdot)` and `\phi(\cdot)` denote the cdf  and pdf of the normal distribution, respectively.

    For `\mu = 0`, these equations simplify to 

    .. math:: s = \sqrt{n / (x^2+n)}, \quad d = 1 / (x s), \quad  u = 1 / s, \quad  w = \text{sgn} (x) \sqrt{- 2n \log(s)}, 



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.student_t_nc_broda_cdf(x, nu, nc); mx = mpm.student_t_nc_broda_cdf(x, nu, nc)
        >>> ix = ipm.student_t_nc_broda_cdf(x, nu, nc); fx = fpm.student_t_nc_broda_cdf(x, nu, nc)
        >>> gx = gmp.student_t_nc_broda_cdf(x, nu, nc); ax = apm.student_t_nc_broda_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_mpm_student_t_nc_harley_qtf: 

Singly noncentral t: qtf, isf (Harley)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_nc_harley_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the qtf of the singly noncentral t distribution, as decribed in :cite:t:`Harley1957`.

    The qtf of the noncentral t-distribution can be approximated by the qtf of Pearson's rho as follows: Let `N=f+2` and

    .. math:: \rho = \Re \left( \delta \sqrt{\frac{2}{2N-3 + \delta^2}}   \right).

    Determine `r_{\alpha;\rho;N} = r_{\alpha}`, using Winterbottom's approximation. Calculate `t_{\alpha;\delta;f} = t_{\alpha}` as

    .. math:: t_{\alpha} = \Re \left(\frac{r_{\alpha}}{1-r_{\alpha}^2} \sqrt{\frac{2f(1-\rho^2)}{1-\rho^2}}  \right)

    Note that in these equations both `\rho` and `r_{\alpha}` can assume values `>1`. Luckily, Winterbottom's approximation can handle this; we always take only the real part of the functions results to avoid issues with the branch cuts of the complex square root.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.student_t_nc_broda_qtf(x, nu, nc); mx = mpm.student_t_nc_broda_qtf(x, nu, nc)
        >>> ix = ipm.student_t_nc_broda_qtf(x, nu, nc); fx = fpm.student_t_nc_broda_qtf(x, nu, nc)
        >>> gx = gmp.student_t_nc_broda_qtf(x, nu, nc); ax = apm.student_t_nc_broda_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_mpm_student_t_nc_akahira_cl: 

Singly noncentral t: confidence limit for `\delta` (Akahira)
-----------------------------------------------------------------------------

.. method:: ctx.student_t_nc_akahira_cl(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the confidence interval (CI) for the noncentrality parameter of the singly noncentral t distribution, as decribed in :cite:t:`Akahira1995`.

    Let `T` be a statistic according to the non-central `t`-distribution with `n` degrees of freedom and a non-centrality parameter `\delta`. Then the lower confidence limit `\widehat{\delta}` of level `1-\alpha` and the two-sided confidence interval `( \underline{\delta},\overline{\delta})` of the non-centrality parameter `\delta` of level `1-\alpha` are given by :cite:t:`Akahira1995`:

    .. math:: \widehat{\delta} = bT - z_\alpha \sqrt{k} +  h T^3 (z_\alpha^2 - 1)/k,

    .. math:: \underline{\delta} = bT - z_{\alpha/2} \sqrt{k} +  h T^3 (z_{\alpha/2}^2 - 1)/k,

    .. math:: \overline{\delta} = bT + z_{\alpha/2} \sqrt{k} -  h T^3 (z_{\alpha/2}^2 - 1)/k,

    .. math:: h=\frac{1}{24}\left(\frac{1}{n^2}+ \frac{1}{4n^3}\right) \quad b=\sqrt{\frac{2}{n}}\frac{\Gamma(\tfrac{1}{2} n+\tfrac{1}{2})}{\Gamma(\tfrac{1}{2} n)} 

    where `k=1+(1-b^2)T^2`, and `z_\alpha` denotes the `\alpha`-quantile of the normal distribution.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.student_t_nc_akahira_cl(x, nu, nc); mx = mpm.student_t_nc_akahira_cl(x, nu, nc)
        >>> ix = ipm.student_t_nc_akahira_cl(x, nu, nc); fx = fpm.student_t_nc_akahira_cl(x, nu, nc)
        >>> gx = gmp.student_t_nc_akahira_cl(x, nu, nc); ax = apm.student_t_nc_akahira_cl(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_mpm_student_t_nc2_broda_cdf: 

Doubly noncentral t: cdf, sf (Broda)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_nc2_broda_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the doubly noncentral t distribution, as decribed in :cite:t:`Broda2007`.

    A saddlepoint approximation based on the joint cumulant generating function of `(x_1, x_2)`, with `x_1 \sim N(\mu, 1)` and  `x_2 \sim \chi^2(n, \theta)`, is possible (see Broda (2007)), and takes the following form:

    .. math:: F_{t''}(x;n;\mu,\theta)  =  \Phi(w)+\phi(w)\left( \frac{1}{w} - \frac{d}{u}  \right) + O(n^{-3/2}) , \quad \text{where}
	
    .. math:: a = x^4 + 2 n x^2 + n^2, \quad  c_2 = (-2 x^3 \mu - 2 x n \mu)/a, \quad  c_1 = (x^2 \mu^2 - n x^2 - n^2 - \theta n) / a, \quad  c_0 = (x n  \mu)/a,

    .. math:: q= \tfrac{1}{3}c_1 - \tfrac{1}{9}c_2^2, \quad r= \tfrac{1}{6}(c_1c_2-3c_0)- \tfrac{1}{27}c_2^3, 

    .. math:: s = \sqrt{-4q} \cos \left(\tfrac{1}{3} \arccos\left(r/ \sqrt{-q^3}\right) \right) - \tfrac{1}{3} c_2,

    .. math:: t_1 = -\mu + x s, t_2 = -x t_1 / (2 n s), \quad  d = 1 / (t_1 s), \quad  \nu = 1 / (1 - 2 t_2), \quad  \alpha = \mu / \sqrt{1 + \theta / n)},

    .. math:: u = \sqrt{(x^2 + 2 n t_2) (2 n \nu^2 + 4 \theta \nu^3) + 4 n^2 s^2} / (2 n s^2), \quad  w = \text{sgn} (x - \alpha) \sqrt{-\mu t_1 - n \log(\nu) - 2 \theta \nu t_2}, 

    and `\Phi(\cdot)` and `\phi(\cdot)` denote the cdf and pdf of the normal distribution, respectively.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.student_t_nc2_broda_cdf(x, nu, nc); mx = mpm.student_t_nc2_broda_cdf(x, nu, nc)
        >>> ix = ipm.student_t_nc2_broda_cdf(x, nu, nc); fx = fpm.student_t_nc2_broda_cdf(x, nu, nc)
        >>> gx = gmp.student_t_nc2_broda_cdf(x, nu, nc); ax = apm.student_t_nc2_broda_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)








.. _rst_mpm_student_t_nc2_broda_qtf: 

Doubly noncentral t: qtf, isf (Broda)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_nc2_broda_qtf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the qtf of the doubly noncentral t distribution, as decribed in :cite:t:`Broda2007`.


    Broda_2007_WorkingPaper proposes the following approximation:

    .. math:: F_{t''}(t;n;\mu,\theta) \approx F_{t'}(t/c;f;\mu), \quad \text{where}

    .. math:: f=\frac{7}{2} \left(-1+\sqrt{15-7g^2/h}\right)^{-1}, \quad c=\sqrt{h(1-2/f)}, \quad g=m_1/\sqrt{\mu^2/2}, h=m_2/(1+\mu^2),


    .. math:: m_1 = \mu \binom{n}{2}^{1/2} \frac{\Gamma((n-1)/2)}{\Gamma(n/2)} {}_1F_1 \left(\frac{1}{2}, \frac{n}{2}, -\frac{\theta}{2}  \right)


    .. math:: m_2 = (1+\mu^2)  \frac{n}{n-2} {}_1F_1 \left(\frac{2}{2}, \frac{n}{2}, -\frac{\theta}{2}  \right)


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.student_t_nc2_broda_qtf(x, nu, nc); mx = mpm.student_t_nc2_broda_qtf(x, nu, nc)
        >>> ix = ipm.student_t_nc2_broda_qtf(x, nu, nc); fx = fpm.student_t_nc2_broda_qtf(x, nu, nc)
        >>> gx = gmp.student_t_nc2_broda_qtf(x, nu, nc); ax = apm.student_t_nc2_broda_qtf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





Spearman's rho, first 8 cumulants (David)
-------------------------------------------------------------------------------


.. method:: ctx.spearman_mu8(N)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.

    Returns an approximation to the central distribution of Spearman's `\rho`, based on the first 8 moments.


    Spearman's `\rho` is calculated like Pearsons's correlation coefficient, using the rank-transform on the `x_i` and `y_i`. The exact test for `H_0` is the permutation test. Techniques for obtaining the exact distribution and approximations are given below



    The first 8 cumulants are given by :cite:t:`David1951`

    .. math:: \kappa_2 = \frac{1}{n-1}

    .. math:: \kappa_4 = \frac{-6(19n^2+5n-36)}{25n(n+1)(n-1)^3}

    .. math:: \kappa_6 = \frac{48(583n^6+723n^5-2603n^4-2637n^3+4054n^2+2760n-1800)}{(245n^3(n-1)^5n1^3)}


    .. math::
        :nowrap:

        \begin{eqnarray}
        \kappa_8  & = &\frac{144(41939n^{10}-83709n^9+304254n^8+578442n^7-1012323n^6- 1690125n^5)}{875n^5 (n+1)^5 (n-1)^7} \quad \\
        & + &\frac{144(1800776n^4+2358048n^3-1616688n^2- 1080567n+846720)}{875n^5 (n+1)^5 (n-1)^7}  \nonumber
        \end{eqnarray}


    Note: See PermCumulants.SpearmanCum for further details.


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.spearman_mu8(x, nu, nc); mx = mpm.spearman_mu8(x, nu, nc)
        >>> ix = ipm.spearman_mu8(x, nu, nc); fx = fpm.spearman_mu8(x, nu, nc)
        >>> gx = gmp.spearman_mu8(x, nu, nc); ax = apm.spearman_mu8(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





Mann-Whitney U distribution: general alternatives specified by rank order probabilities (Sundrum)
---------------------------------------------------------------------------------------------------


.. method:: ctx.mannwhitney_nc_mu4(N)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.

    Returns an approximation to the noncentral distribution of Mann-Whitney's `U`, based on the first 4 moments.


    The first 4 moments under the alternative are given by :cite:t:`Sundrum1954` (note that `\kappa_4 = \mu_4 - 3\mu2^3`):

    .. math:: \mu_1 = p

    .. math:: \mu_2 = (p^2 + p - q - r)/mn + (q - p^2 )/n + (r - p^2 )/m + p^2 

    .. math::
	    :nowrap:

	    \begin{eqnarray}
	    \mu_3 & = & 6(p^3 + u - pq - pr)/mn + (2p^3 + s - 3pq)/n^2 + (2p^3 + t - 3pr)/m^2 \\ \nonumber
	    & + & 3(3pq + 2(pr - u - p^3) + q - s - p^2)/mn^2 + 3(3pr + 2(pq - u - p^3)  \\ \nonumber
	    & + & r - t - p^2)/m^2n +(4p^3 + 3p^2 + p + 6u + 2(s + t) - 3(q + r)(1 + 2p))/m^2n^2 \nonumber
	    \end{eqnarray}


    .. math::
	    :nowrap:

	    \begin{eqnarray}
	    \mu_4 & = &  3(q - p^2)2/n^2 + 6(q - p^2)(r - p^2)/mn + 3(r - p^2)2/m^2  \\ \nonumber
	    & + &  (12qp^2 + a - 4sp - 3q^2 - 6p^4)/n^3 + (12rp^2 + b - 4tp - 3r2 - 6p^4)/m^3  \\ \nonumber
	    & + &  6(7(rp^2 - p^4) + 12qp^2 + qp + 2(w-sp) - 3(q^2 + qr) - 8up - p^3)/mn^2  \\ \nonumber
	    & + &  (42qp^2 + 72rp^2 + 6rp+ 12x - 42p^4 - 18r2 - 18qr - 12tp - 48up - 6p^3)/m^2n  \\ \nonumber
	    & + &  6(6(p^4 - rp^2) + 3(q^2 - qp) - 12qp^2 + 4sp + 8up + 2(p^3 + qr - w) + s - a)/mn^3  \\ \nonumber
	    & + &  (36p^4 + 18r2 + 12qr - 72rp^2 - 36qp^2 + 24tp - 6b + 48up   \\ \nonumber
	    & - &  12x + 12p^3 - 18rp+ 6t)/m^3 n  \\ \nonumber
	    & + &  (105p^4 + 42p^3 + 3p^2 + 33q^2 + 33r2 + 54qr - 174qp^2 - 174rp^2 - 42pq  \\ \nonumber
	    & - &  42pr + 36sp + 36tp + 192up - 36w - 36x + 6v + 36u)/ m^2n^2  \\ \nonumber
	    & + &  (132qp^2 + 108rp^2 - 66p^4 - 33q^2 - 36qr - 18r2 - 44sp - 24tp + 11a  \\ \nonumber
	    & - &  144up + 36w + 24x - 6v - 36p^3 - 36u - 7p^2 + 54pq + 36pr - 18s + 7q)/m^2n^3  \\ \nonumber
	    & + &  (132rp^2 + 108qp^2 - 66p^4 - 33r2 - 36qr - 18q^2 - 44tp - 24sp + 11b  \\ \nonumber
	    & - &  144up + 24w + 36x - 6v - 36p^3 - 36u - 7p^2 + 54pr + 36pq - 18t + 7r)/m^3n^2  \\ \nonumber
	    & + &  (6(3(q^2 + r2)- 12((q + r)p^2) + 4(p^3 + qr + sp + tp - w - x) - (a + b - v) + 16up  \\ \nonumber
	    & - &  6(p^4 + pq + pr + u) + 2(s + t)) - 7(q + r - p^2) + p)/ m^3n^3  \nonumber
	    \end{eqnarray}

    The parameters `p, q, r, s, t, v, u, a, b, w` and `x` can be calculated from the following rank order probabilities:

    .. math::
	    :nowrap:

	    \begin{eqnarray}
	    p & = & P_{1,1}(0,0)   \\ \nonumber
	    q & = & P_{2,1}(0,0,1)  \\ \nonumber
	    r & = & P_{1,2}(0,1,1)  \\ \nonumber
	    s & = & P_{3,1}(0,0,0,1)  \\ \nonumber
	    t & = & P_{1,3}(0,1,1,1)  \\ \nonumber
	    v & = & P_{2,2}(0,0,1,1)  \\ \nonumber
	    u & = & v + (1/4) P_{2,2}(0,1,0,1)  \\ \nonumber
	    a & = & P_{4,1}(0,0,0,0,1)  \\ \nonumber
	    b & = & P_{1,4}(0,1,1,1,1)  \\ \nonumber
	    w & = & 2a + (2/3) P_{3,2}(0,0,1,0,1) + (1/6) P_{3,2}(0,1,0,0,1)  \\ \nonumber
	    x & = & 2b + (2/3) P_{2,3}(0,1,0,1,1) + (1/6) P_{2,3}(0,1,1,0,1)  \\ \nonumber
	    \end{eqnarray}

    The rank order probabilities which are required for the calculation of the first 4 moments can be estimated
    from the sample as follows: Let `U_i` be the number of `Y`s in the sample greater than `X_{(i)}`, 
    where `X_{(i)}` is the ith ordered values of the `X` amongst themselves. Then the probabilities are calculated 
    according to the following scheme :


    .. math:: P_{1,1}(0,1) = \frac{1}{mn} \sum_{i=1}^m U_i

    .. math:: P_{2,1}(0,0,1) = \frac{2}{mn(m-1)} \sum_{i=1}^m (i-1)U_i

    .. math:: P_{3,1}(0,0,0,1) = \frac{3}{mn(m-1)(m-2)} \sum_{i=1}^m (i-1)(i-2)U_i

    .. math:: P_{4,1}(0,0,0,0,1) = \frac{4}{mn(m-1)(m-2)(m-3)} \sum_{i=1}^m (i-1)(i-2)(i-3)U_i

    .. math:: P_{1,2}(0,1,1) = \frac{1}{mn(n-1)} \sum_{i=1}^m U_i(U_i-1)

    .. math:: P_{1,3}(0,1,1,1) = \frac{1}{mn(n-1)(n-2)} \sum_{i=1}^m U_i(U_i-1)(U_i-2)

    .. math:: P_{1,4}(0,1,1,1,1) = \frac{1}{mn(n-1)(n-2)(n-3)} \sum_{i=1}^m U_i(U_i-1)(U_i-2)(U_i-3)

    .. math:: P_{2,2}(0,0,1,1) = \frac{2}{mn(m-1)(n-1)} \sum_{i=1}^m (i-1)U_i(U_i-1)

    .. math:: P_{3,2}(0,0,0,1,1) = \frac{3}{mn(m-1)(m-2)(n-1)} \sum_{i=1}^m (i-1)(i-2)U_i(U_i-1)

    .. math:: P_{2,3}(0,0,1,1,1) = \frac{2}{mn(m-1)(n-1)(n-2)} \sum_{i=1}^m (i-1)U_i(U_i-1)(U_i-2)

    .. math:: P_{2,2}(0,1,0,1) = \frac{4}{mn(m-1)(n-1)} \sum_{i=1}^m  \sum_{j=i+1}^m (U_i - U_j) U_j

    .. math:: P_{3,2}(0,0,1,0,1) = \frac{12}{mn(m-1)(m-2)(n-1)} \sum_{i=1}^m  \sum_{j=i+1}^m (i-1)(U_i - U_j) U_j

    .. math:: P_{3,2}(0,1,0,0,1) = \frac{12}{mn(m-1)(m-2)(n-1)} \sum_{i=1}^m  \sum_{j=i+1}^m (i-j-1)(U_i - U_j) U_j

    .. math:: P_{2,3}(0,1,0,1,1) = \frac{6}{mn(m-1)(n-1)(n-2)} \sum_{i=1}^m  \sum_{j=i+1}^m (U_i - U_j) U_j (U_j-1)

    .. math:: P_{2,3}(0,1,0,1,1) = \frac{6}{mn(m-1)(n-1)(n-2)} \sum_{i=1}^m  \sum_{j=i+1}^m (U_i - U_j) U_j (U_j - 1)

    .. math:: P_{2,3}(0,1,1,0,1) = \frac{6}{mn(m-1)(n-1)(n-2)} \sum_{i=1}^m  \sum_{j=i+1}^m (U_i - U_j) (U_i - U_j - 1) U_j 


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.mannwhitney_nc_mu4(x, nu, nc); mx = mpm.mannwhitney_nc_mu4(x, nu, nc)
        >>> ix = ipm.mannwhitney_nc_mu4(x, nu, nc); fx = fpm.mannwhitney_nc_mu4(x, nu, nc)
        >>> gx = gmp.mannwhitney_nc_mu4(x, nu, nc); ax = apm.mannwhitney_nc_mu4(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






First 4 moments of Kendalls `\tau` in the general case (Sundrum)
-------------------------------------------------------------------------------


.. method:: ctx.kendall_tau_nc_mu4(N)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.

    Returns an approximation to the noncentral distribution of Kendall's `\tau`, based on the first 4 moments.


    Consider `k` pairs of random variables `(x_1,y_1),\ldots,(x_k,y_k)`. Let `r_1,\ldots,r_k` be a permutaton of `1,\ldots,k` and let `s_1,\ldots,s_k` be its reciprocal. We define as in  :cite:t:`Snow1962`.

    `P(r_1,\ldots,r_k)` = Pr[if `x`'s are ranked in order, ranks of corresponding `y`'s are `r_1,\ldots,r_k`]. 

    `P(r_1,\ldots,r_k)` = Pr[if `y`'s are ranked in order, ranks of corresponding `x`'s are `s_1,\ldots,s_k`]. 

    Let `H(t) = 1` if `t>0` and `H(t)=0` otherwise. Then

    .. math:: P(r_1,\ldots,r_k) = k! P \left[ \prod_{i=2}^k H(x_i - x_{i-1})  H(y_{s_i} - y_{s_{i-1}}) \right] = k! P \left[ \prod_{i=2}^k H(y_i - y_{i-1})  H(x_{r_i} - x_{r_{i-1}}) \right]

    The rank order probabilities can then be estimated from the sample as

    .. math:: \hat{P}_{(12)} = \frac{1}{n(n-1)} \sum_{i \ne j} I\left[ (x_i-x_j)(y_i-y_j) > 0 \right]


    .. math:: \hat{P}_{(123)} = \frac{1}{n(n-1)(n-2)} \sum_{i \ne j_1 \ne j_2} I\left[ (x_i-x_{j_1})(y_i-y_{j_1})  (x_i-x_{j_2})(y_i-y_{j_2}) > 0 \right]





    The first 4 moments of `T_N` are given as :cite:t:`Sundrum1953`:

    .. math:: \mu_1 = p

    .. math:: \mu_2 = 2 [p(1 - p) + 2(k - p^2)(n - 2)] / [n (n - 1)]

    .. math::
        :nowrap:

        \begin{eqnarray}
        \mu_3 & = & 4 [(t - 18kp + 10p^3) n^2 +  (6k + 2u - 6p^2 - 5t + 72kp - 34p^3) n   \\ \nonumber
        & + & (p + 9p^2 + 30p^3 - 12k - 4u + 6t - 72kp)] / [n (n - 1)]^2   \nonumber
        \end{eqnarray}


    .. math::
        :nowrap:

        \begin{eqnarray}
        \mu_4 & = & 8 [6(k - p^2)2 n^4  + (6kp + 2y - 6p^3 - 16tp - 84k2 + 270kp^2 - 108p4) n^3  \\ \nonumber
        & + & (1.5p^2 + 6t + 2b - 126kp - 24up - 18y + 75p^3 + 120tp + 426k2 - 1446kp^2 + 505.5p4) n^2  \\ \nonumber
        & + & (14k + 12u - 15.5p^2 - 30t - 10b + 444kp + 96up + 52y - 213p^3 - 296tp - 924k2   \\ \nonumber
        & + & 2988kp^2 - 943.5p4)n   \\ \nonumber
        & + & (p - 28k - 24u + 21p^2 + 36t + 12b - 432kp - 96up - 48y + 180p^3  + 240tp + 720k2   \\ \nonumber
        & - & 2160kp^2 + 630p4)] / [n (n - 1)]^3   \nonumber
        \end{eqnarray}

    The parameters `p, k, u, t, b, y` can be calculated from the following rank order probabilities, writing `P_{(1423)}` for the probility that the ranks of the `Y` occur in this order when the `X` are sorted in ascending order:

    .. math::
        :nowrap:

        \begin{eqnarray}
        p & = & P_{(12)}  \\ \nonumber
        u & = & P_{(123)}  \\ \nonumber
        k & = & P_{(123)} + \tfrac{1}{4}P_{(132)}   \\ \nonumber
        t & = & 8(P_{(1234)} + P_{(1243))} + 6P_{(1342)} + 4P_{(1324)} + 2P_{(2143)} + P_{(2413)} + P_{(1432)}  \\ \nonumber
        b & = & 15P_{(1234)} + 10P_{(1243)} + 5P_{(1324)} + 4P_{(1342)} + P_{(2143)}  \\ \nonumber
        y & = & (160P_{(12453)} + 150(P_{(12435)} + P_{(12354))} + 125P_{(12345)} + 96P_{(21453)} + 90P_{(13254)} + 84P_{(13524)}  \\ \nonumber
        &+& 80P_{(13425)} + 64P_{(13452)} + 45P_{(21354)} + 40P_{(12543)} + 32(P_{(23514)} + P_{(14352)} + P_{(13542)) } \\ \nonumber
        &+& 24P_{(21543)} + 22P_{(24153)} + 20P_{(14325)} + 18P_{(14523)} + 16P_{(25143)} + 12(P_{(24513)} + P_{(14532))}  \\ \nonumber
        &+& 6(P_{(25314)} + P_{(15342))} + 4P_{(25413)} + 2(P_{(15432)} + P_{(35142)}))/5   \nonumber
        \end{eqnarray}

    When `(x_i,y_i)`, `i=1,2,\ldots,k`, are normal variables with correlation `\rho`, then closed form expressions exist for `p, k` and `u` (writing `a = \arcsin\left(\rho\right)/\pi` and `b = 2\arcsin\left(\tfrac{1}{2}\rho\right)/\pi`:

    .. math:: 
        :nowrap:

        \begin{eqnarray}
        p & = & \tfrac{1}{2} + a  \\ \nonumber
        k & = & \tfrac{1}{4} (\tfrac{10}{9} + 4a + 4a^2 - b^2)  \\ \nonumber
        u & = & \tfrac{3}{8} (\tfrac{4}{9} + 4a -2b + 4a^2 - b^2)   \nonumber
        \end{eqnarray}

    The parameters `t, b` and `y` have to be evaluated by numerical intergration of the rank order probabilities



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.kendall_tau_nc_mu4(x, nu, nc); mx = mpm.kendall_tau_nc_mu4(x, nu, nc)
        >>> ix = ipm.kendall_tau_nc_mu4(x, nu, nc); fx = fpm.kendall_tau_nc_mu4(x, nu, nc)
        >>> gx = gmp.kendall_tau_nc_mu4(x, nu, nc); ax = apm.kendall_tau_nc_mu4(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)









