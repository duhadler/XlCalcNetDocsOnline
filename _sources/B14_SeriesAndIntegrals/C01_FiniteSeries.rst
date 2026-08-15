








.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />







Finite series algorithms for selected distributions
======================================================================================

This section provides distribution functions in interval arithmetic for some special cases. These function can be used to assess the accuracy for other algorithms without verification.



.. _rst_chi2_cohen_cdf: 

Central `\chi^2` distribution, cdf (integer degrees of freedom)
-------------------------------------------------------------------------------

.. method:: ctx.chi2_cohen_cdf(x, nu, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the central chi-square distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis06`, MathWorld :cite:p:`WolframDis06`, BoostMath :cite:p:`BoostDis06`, :cite:t:`CharfunDis06`.


    The cdf can be expressed as a finite sum if `n` is an integer:


    .. math:: F_{\chi^2}\left(n, x\right) = 1+2\Phi(-\sqrt{x})+2\phi \left(\sqrt{x}\right) \sum_{r=1}^{(n-1)/2} \frac{\sqrt{x}^{2r-1}}{1 \cdot 3 \cdot 5 \ldots (2r-1)}, \qquad \text{for } n \text{ odd},


    .. math:: F_{\chi^2}\left(n, x\right) = e^{-x/2} \left(1+ \sum_{r=1}^{(n-2)/2} \frac{x^{r}}{2 \cdot 4 \cdot 6 \ldots (2r)}\right), \qquad \text{for } n \text{ even},

    where `\phi(\cdot)` denotes the pdf of the normal distribution (see ) and  `\Phi(\cdot)` denotes the cdf of the normal distribution (see ).



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 12; n = 10
        >>> dx = dec.chi2_cohen_cdf(x, n); mx = mpm.chi2_cohen_cdf(x, n)
        >>> ix = ipm.chi2_cohen_cdf(x, n); fx = fpm.chi2_cohen_cdf(x, n)
        >>> gx = gmp.chi2_cohen_cdf(x, n); ax = apm.chi2_cohen_cdf(x, n)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)



.. _rst_student_t_owen_cdf: 

Central Student `t` distribution, cdf (integer degrees of freedom)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_owen_cdf(x, nu, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the central Student t distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis07`, MathWorld :cite:p:`WolframDis07`, BoostMath :cite:p:`BoostDis07`, :cite:t:`Broda2007`, :cite:t:`Witkovsky2001`, :cite:t:`CharfunDis07`.


    The cdf can be expressed as a finite sum if `n` is an integer:

    .. math:: F_t\left(n,x\right) =  \tfrac{1}{2} + z_n + (c_1 + c_3 +  \cdots +c_{n-2}), \qquad \text{for } n \text{ odd},

    .. math:: \text{where } z_n=\frac{1}{\pi} \arctan(\frac{x}{\sqrt{n}}); a_n=\frac{1}{\sqrt{n}\pi}; b_n=\frac{n}{n+x^2}; c_1=xa_nb_n; c_k=c_{k-2}b_n(1-1/k) 



    .. math:: F_t\left(n,x\right) =  \tfrac{1}{2} + (c_0 + c_2 +  \cdots +c_{n-2}), \qquad \text{for } n \text{ even},

    .. math:: \text{where } d_n=\frac{1}{2\sqrt{n+x^2}};  b_n=\frac{n}{n+x^2}; c_0=xd_n; c_k=c_{k-2}b_n(1-1/k)


    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 2; n = 10;
        >>> dx = dec.student_t_owen_cdf(x, n); mx = mpm.student_t_owen_cdf(x, n)
        >>> ix = ipm.student_t_owen_cdf(x, n); fx = fpm.student_t_owen_cdf(x, n)
        >>> gx = gmp.student_t_owen_cdf(x, n); ax = apm.student_t_owen_cdf(x, n)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_fisher_f_seber_cdf: 

Central Fisher `F` distribution, cdf (integer degrees of freedom)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_f_seber_cdf(x, m, n, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the central Fisher F distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis09`, MathWorld :cite:p:`WolframDis09`, BoostMath :cite:p:`BoostDis09`, :cite:t:`CharfunDis09`, :cite:t:`AbramowitzDis09`, :cite:t:`Butler2002`, :cite:t:`Chattamvelli1995`, :cite:t:`Witkovsky2001`.



    The cdf can be expressed as a finite sum if `m` is an integer, and `n` is a positive real number:

    .. math:: 1-F_F\left(m,n,x\right) =  a_m + b_m(c_1 + c_3 +  \cdots +c_{m-2}), \qquad \text{for } m \text{ odd},

    .. math:: \text{where } a_m=2T(n,-z_m); b_m=2t(n,z_m)\cdot z_m; z_m=\sqrt{mx};

    .. math:: 1-F_F\left(m,n,x\right) =  d_m  (c_0 + c_2 +  \cdots +c_{m-2}), \qquad \text{for } m \text{ even},

    .. math:: \text{where } d_m=(1-u_m)^{n/2}

    .. math:: \text{and } u_m=mx/(mx+n), \quad c_0=c_1=1, \quad c_k=c_{k-2}u_m \cdot (n+k-2)/k



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 3; m = 10; n = 20
        >>> dx = dec.fisher_f_seber_cdf(x, m, n); mx = mpm.fisher_f_seber_cdf(x, m, n)
        >>> ix = ipm.fisher_f_seber_cdf(x, m, n); fx = fpm.fisher_f_seber_cdf(x, m, n)
        >>> gx = gmp.fisher_f_seber_cdf(x, m, n); ax = apm.fisher_f_seber_cdf(x, m, n)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_beta_seber_cdf: 

Central Beta distribution, cdf (`2a` an integer, `2b` an integer)
-------------------------------------------------------------------------------

.. method:: ctx.beta_seber_cdf(x, a, b, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the central Fisher F distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis08`, MathWorld :cite:p:`WolframDis08`, BoostMath :cite:p:`BoostDis08`, :cite:t:`CharfunDis08`.


    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; a = '10'; b = '20'
        >>> dx = dec.beta_seber_cdf(x, a, b); mx = mpm.beta_seber_cdf(x, a, b)
        >>> ix = ipm.beta_seber_cdf(x, a, b); fx = fpm.beta_seber_cdf(x, a, b)
        >>> gx = gmp.beta_seber_cdf(x, a, b); ax = apm.beta_seber_cdf(x, a, b)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_chi2_nc_cohen_cdf: 

Noncentral `\chi^2` distribution, cdf (integer degrees of freedom)
-------------------------------------------------------------------------------

.. method:: ctx.chi2_nc_cohen_cdf(x, nu, lambda1, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the central chi-square distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis01`, MathWorld :cite:p:`WolframDis01`, :cite:t:`Patnaik1949`, :cite:t:`Penev2000`, :cite:t:`Wang1993`, :cite:t:`Winterbottom1979`, BoostMath :cite:p:`BoostDis01`, :cite:t:`CharfunDis01`, :cite:t:`Kerns2018`, :cite:t:`András2008`.


    For odd degrees of freedom, the pdf and cdf can be expressed as a finite sum, using the recurrence relations given in section \ref{NoncentralChiSquareDistributionRecur}, and defining `h(n,x,\lambda) = e^{(1/2)(x+\lambda)} f_{\chi^2}\left(n, x; \lambda\right)`:

    .. math:: F_{\chi^2}\left(1, x;\delta^2 \right) = \Phi(x-\delta)-\Phi(-x-\delta)

    .. math:: h(1, x;\lambda)   = \frac{\cosh (\sqrt{x\lambda})}{\sqrt{2\pi x}}, \quad h(3, x;\lambda)   = \frac{\sinh (\sqrt{x\lambda})}{\sqrt{2\pi \lambda}}

    where  `\Phi(\cdot)` denotes the cdf of the normal distribution.


    NOTE: This needs to be extended using Marcum Q.


    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 12; nu = 7; l = 30
        >>> dx = dec.chi2_nc_cohen_cdf(x, n, l); mx = mpm.chi2_nc_cohen_cdf(x, n, l)
        >>> ix = ipm.chi2_nc_cohen_cdf(x, n, l); fx = fpm.chi2_nc_cohen_cdf(x, n, l)
        >>> gx = gmp.chi2_nc_cohen_cdf(x, n, l); ax = apm.chi2_nc_cohen_cdf(x, n, l)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_student_t_nc_owen_cdf: 

Noncentral Student `t` distribution, cdf (integer degrees of freedom)
-------------------------------------------------------------------------------

.. method:: ctx.student_t_nc_owen_cdf(x, n, delta, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the noncentral Student t distribution for integer degrees of freedom `n \ge 1`, noncentrality parameter `\delta \in \mathbb{R}` and the support interval `(-\infty, +\infty)` . See also Wikipedia :cite:p:`WikipediaDis03`, MathWorld :cite:p:`WolframDis03`, BoostMath :cite:p:`BoostDis03`, :cite:t:`Benton2003`, :cite:t:`Broda2007`, :cite:t:`Owen1968`, :cite:t:`Wang1993`, :cite:t:`Witkovsky2013`, :cite:t:`Kerns2018`.


    The function uses the following algorithm given by :cite:t:`Owen1968`:

    .. math:: F_{t'}\left(n,x, \delta\right) =  \Phi(-\delta \sqrt{B}) + 2(M_1+M_3 + \cdots + M_n) \quad \text{ for odd degrees of freedom}

    .. math:: F_{t'}\left(n,x, \delta\right) =  \Phi(-\delta) + \sqrt{2\pi}(M_2+M_4 + \cdots + M_n) \quad \text{ for even degrees of freedom}

    .. math:: A=\frac{t}{\sqrt{n}},\quad B=\frac{n}{n+t^2}

    .. math:: M_1 = T_{\text{Owen}}(\delta \sqrt{B}, A), \quad M_2 = A \sqrt{B} \phi(\delta \sqrt{B})-\Phi(\delta A \sqrt{B})

    .. math:: M_3=B(\delta A M_2 + A \phi(\delta)/\sqrt{2\pi}), \quad M_4= \tfrac{1}{2}B(\delta A M_3 + M_2)

    .. math:: M_k= \frac{k-3}{k-2}B(a_k \delta A M_{k-1} + M_{k-2}), \quad a_k = \frac{1}{(k-4)a_{k-1}} \quad \text{for } k \geq 5,

    where `T_{\text{Owen}}(\cdot,\cdot)` denotes Owen's T function , and `\Phi(\cdot)` and `\phi(\cdot)` denote the cdf and pdf  of the normal distribution, respectively.




    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 20; n = 10; d = 30
        >>> dx = dec.student_t_nc_owen_cdf(x, n, d); mx = mpm.student_t_nc_owen_cdf(x, n, d)
        >>> ix = ipm.student_t_nc_owen_cdf(x, n, d); fx = fpm.student_t_nc_owen_cdf(x, n, d)
        >>> gx = gmp.student_t_nc_owen_cdf(x, n, d); ax = apm.student_t_nc_owen_cdf(x, n, d)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_fisher_f_nc_seber_cdf: 

Noncentral Fisher `F` distribution, cdf (`m` an even integer)
-------------------------------------------------------------------------------

.. method:: ctx.fisher_f_nc_seber_cdf(x, m, n, lambda1, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the noncentral Fisher F distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis02`, MathWorld :cite:p:`WolframDis02`, BoostMath :cite:p:`BoostDis02`, :cite:t:`Benton2003`, :cite:t:`Butler2002`, :cite:t:`Chou1985`, :cite:t:`Chattamvelli1995`, :cite:t:`Wang1993`, :cite:t:`CharfunDis02`, :cite:t:`Kerns2018`.

    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 13; m = 10; n = 20; l1 = 30
        >>> dx = dec.fisher_f_nc_seber_cdf(x, m, n, l1); mx = mpm.fisher_f_nc_seber_cdf(x, m, n, l1)
        >>> ix = ipm.fisher_f_nc_seber_cdf(x, m, n, l1); fx = fpm.fisher_f_nc_seber_cdf(x, m, n, l1)
        >>> gx = gmp.fisher_f_nc_seber_cdf(x, m, n, l1); ax = apm.fisher_f_nc_seber_cdf(x, m, n, l1)
        >>> mpm.show([dx, mx, ix]); mpm.show([fx, gx, ax])
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_beta_nc_seber_cdf: 

Noncentral Beta distribution, cdf (`b` an integer)
-------------------------------------------------------------------------------

.. method:: ctx.beta_nc_seber_cdf(x, a, b, lambda1, cdf=True)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the noncentral Fisher F distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis04`, BoostMath :cite:p:`BoostDis04`, :cite:t:`Wang1993`, :cite:t:`CharfunDis04`, :cite:t:`Seber1963`, :cite:t:`Kerns2018`.




    CDF: Finite Series for even error degrees of freedom:

    This is code for noncentral beta and needs to be adapted for noncentral F.

    The cdf can be calculated using the following finite series, if `b` is an integer:

    .. math:: I(x;a,b,\lambda) = e^{-\lambda(1-x)} \sum_{n=0}^{b-1}{L_n}, \quad \text{where }

    .. math:: L_0=1, \quad L_1=(1-x)(a+\lambda x),

    .. math:: L_n=\frac{1-x}{n}\left((2n-2+a+\lambda x)L_{n-1}-(n+a-2)(1-x)L_{n-2}\right)



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = 0.25; a = 10; b = 20; l = 30
        >>> dx = dec.beta_nc_seber_cdf(x, a, b, l); mx = mpm.beta_nc_seber_cdf(x, a, b, l)
        >>> ix = ipm.beta_nc_seber_cdf(x, a, b, l); fx = fpm.beta_nc_seber_cdf(x, a, b, l)
        >>> gx = gmp.beta_nc_seber_cdf(x, a, b, l); ax = apm.beta_nc_seber_cdf(x, a, b, l)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)





.. _rst_pearson_rho_nc_owen_pdf: 

Pearson's `\rho` distribution, pdf (integer `N`)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_nc_owen_pdf(r, N, rho)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the Pearson rho distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis05`, MathWorld :cite:p:`WolframDis05`, :cite:t:`Hotelling1953`, :cite:t:`Odeh1986`.


    See :cite:t:`Hotelling1953`.

    For `N = 3,4` the probability density function can be expressed in closed form :cite:t:`Odeh1986`:

    .. math:: f_R(3, r; \rho) = \frac{A^2(1+xU)}{\pi B^2C} 

    .. math:: f_R(4, r; \rho) =\frac{AC^3 (B^2U + 3x(1+xU))}{\pi B^4} 

    where `x, A, B, C` and `U` are defined as follows:

    .. math:: x = \rho r,\quad \quad  A=\sqrt{1-\rho^2}, \quad B=\sqrt{1-x^2}, \quad C=\sqrt{1-r^2}, \quad U=\frac{\arccos(-x)}{B}


    The probability density function `f_R(N, r;\rho)` satisfies the following recurrence formula for `N \geq 5`  (see :cite:t:`Hotelling1953`):

    .. math:: f_R(N, r; \rho) = \frac{2N-5}{B^2(N-3)} x A C f_R(N-1, r; \rho) + \frac{N-3}{B^2(N-4)} A^2 C^2 f_R(N-2, r; \rho)  


    For `0 \leq x \leq 1`,this recurrence formula can be safely used to find a sequence of values for `f_R(5, r;\rho)`, `f_R(6, r;\rho),...,f_{R}(N, r;\rho)`. However, for `-1 < x < 0` the recurrence formula is numerically unstable, since the two terms on the right-hand of the equation are of opposite sign. 





    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; r = '0.25'; N = '20'; rho = '0.1'
        >>> dx = dec.pearson_rho_nc_owen_pdf(x, N, rho); mx = mpm.pearson_rho_nc_owen_pdf(x, N, rho)
        >>> ix = ipm.pearson_rho_nc_owen_pdf(x, N, rho); fx = fpm.pearson_rho_nc_owen_pdf(x, N, rho)
        >>> gx = gmp.pearson_rho_nc_owen_pdf(x, N, rho); ax = apm.pearson_rho_nc_owen_pdf(x, N, rho)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)




.. _rst_pearson_rho_nc_owen_cdf: 

Pearson's `\rho` distribution, cdf (integer `N`)
-------------------------------------------------------------------------------

.. method:: ctx.pearson_rho_nc_owen_cdf(x, N, rho)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the Pearson rho distribution for integer degrees of freedom. See also Wikipedia :cite:p:`WikipediaDis05`, MathWorld :cite:p:`WolframDis05`, :cite:t:`Hotelling1953`, :cite:t:`Odeh1986`.



    For `N = 3,4,5,6` the cumulative distribution function `F_R(N, r;\rho)` can be expressed in closed form 

    .. math:: F_R(3, r; \rho) = \frac{\arccos(-r)}{\pi} - \frac{\rho C U}{\pi}

    .. math:: F_R(4, r; \rho) =\frac{\arccos(\rho)}{\pi} - \frac{\rho AC^2}{\pi B^2} - \frac{rA^3U}{\pi B^2}

    .. math:: F_R(5, r; \rho) =\frac{\arccos(-r)}{\pi} - \frac{(x^2-3\rho^3+2) r A^2C}{2\pi B^4} + \frac{(\rho^2-3+2\rho^2 x^2) \rho C^3U}{2\pi B^4} 

    .. math::
       :nowrap:

       \begin{eqnarray}
        F_R(6, r; \rho) & = &\frac{\arccos(\rho)}{\pi} - \frac{[\rho r^2(2x^2+13) - 2\rho(4x^4+6x^2+5) + \rho^3(11x^2+4)` AC^2}{6\pi B^6} \\
        && + \frac{2x^2(-2r^2+1)rA^5U}{6\pi B^6}  \nonumber
       \end{eqnarray}

    where `x, A, B, C` and `U` are defined as follows:

    .. math:: x = \rho r,\quad \quad  A=\sqrt{1-\rho^2}, \quad B=\sqrt{1-x^2}, \quad C=\sqrt{1-r^2}, \quad U=\frac{\arccos(-x)}{B}




    The cumulative distribution function `F_R(N, r;\rho)` satisfies the following recurrence formula  for `N \geq 7` (see :cite:t:`Hotelling1953`):

    .. math::
       :nowrap:

       \begin{eqnarray}
        F_{R}(N, r;\rho) & = & \frac{2 (N - 4) \rho^2 - N + 5}{(N-3)\rho^2} F_R(N-2, r;\rho) \\
        && +\: \frac{(N-5)A^2}{(N-3)\rho^2} F_R(N-4, r;\rho) \nonumber \\
        && +\: \frac{(N-4)A^2C^2-(2N-9) B^2}{(N-4)(N-3)\rho^2 AC} \rho f_R(N-1, r;\rho)  \nonumber \\
        && +\: \frac{(N-4)^2 +(3N(N-8)+47)\rho^2}{(N-4)^2 (N-3)\rho^2} r f_R(N-2, r;\rho)    \nonumber 
       \end{eqnarray}


    For `N` odd, the above formula can be used repeatedly to find `F_7, F_9, ..., F_N` starting with values of `F_3` and `F_5`. 

    For `N` even, the formula can be used repeatedly to find `F_8, F_{10}, ..., F_N` starting with values of `F_4` and `F_6`.

    However, in many situations the formula is numerically unstable, e.g.  if `\rho^2 < \frac{N-5}{2(N-4)}`, the first two terms on the right hand side of equation (\ref{eq:PearsonRho_Closed_Recur_1}) are of opposite sign.






    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; r = '0.25'; N = '20'; rho = '0.1'
        >>> dx = dec.pearson_rho_nc_owen_cdf(x, N, rho); mx = mpm.pearson_rho_nc_owen_cdf(x, N, rho)
        >>> ix = ipm.pearson_rho_nc_owen_cdf(x, N, rho); fx = fpm.pearson_rho_nc_owen_cdf(x, N, rho)
        >>> gx = gmp.pearson_rho_nc_owen_cdf(x, N, rho); ax = apm.pearson_rho_nc_owen_cdf(x, N, rho)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






.. _rst_fisher_r2_gd1_cdf: 

Fisher's `R^2` distribution, cdf (finite sum for `N-p` even) 
-------------------------------------------------------------------------------

.. method:: ctx.fisher_r2_gd1_cdf(x, a, b,  lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns the cdf of the multiple correlation coefficient distribution for `N-p` an even integer. See also :cite:t:`Lee1971`, :cite:t:`Lee1972`, :cite:t:`Gurland1968`, :cite:t:`Gurland1970`, :cite:t:`Gurland1991`, :cite:t:`Muirhead1982`, :cite:t:`Benton2003`, :cite:t:`Fisher1928`, :cite:t:`Gatsonis1989`.



    CDF: Finite Series of Gurland:


    .. math:: F_{R^2}(x;p,N,\rho^2) = \sum_{j=0}^{k}{b_j I_y\left(\tfrac{1}{2}(p-1+2j),k \right)} \quad \text{where}

    .. math:: k = \tfrac{1}{2}(N-p), \quad y=\frac{x(1-\rho^2)}{1-x\rho^2}, \quad b_j = \binom{k}{j}(\rho^2)^j (1-\rho^2)^{k-j}



    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; r2 = '0.25'; p = '3'; N = '20'; rho2 = '0.1'
        >>> dx = dec.fisher_r2_gd1_cdf(r2, p, N, rho2); mx = mpm.fisher_r2_gd1_cdf(r2, p, N, rho2)
        >>> ix = ipm.fisher_r2_gd1_cdf(r2, p, N, rho2); fx = fpm.fisher_r2_gd1_cdf(r2, p, N, rho2)
        >>> gx = gmp.fisher_r2_gd1_cdf(r2, p, N, rho2); ax = apm.fisher_r2_gd1_cdf(r2, p, N, rho2)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)







.. _rst_roy_pdf_cdf_sf: 


Roy's largest root distribution, pdf, cdf and sf
-------------------------------------------------------------------------------

.. method:: ctx.roy_pdf_cdf_sf(x, p, n1, n2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns simultaneouly  `\text{pdf}_X(r)`, the probability density function ,  `\text{cdf}_X(x)`, the cumulative distribution function, and `\text{sf}_X(x)`, the survival function, of a random variable `X`, following the distribution of Roy's largest root, with parameters *p*, *n1* and *n2* and  the support interval `(0,1)`.

    Let `X`, `Y` denote two independent real Gaussian `p \times n_1` and `p \times n_2` matrices with `n_1, n_2 \geq p`, each constituted by zero mean independent, identically distributed columns with common covariance. Then Roy's largest root criterion, used in multivariate analysis of variance (MANOVA), is based on the statistic of the largest eigenvalue, `\Theta_1`, of `(X + Y)^{-1}Y`, where `X` and `Y` are independent central Wishart matrices. 

    See also :cite:t:`Anderson2003`, :cite:t:`Muirhead1982`, :cite:t:`Butler2007`, :cite:t:`Chiani2012`, :cite:t:`Chiani2014`, and  :ref:`dist_roy() <rst_dist_roy_largest_root>`.

    See also Chen 2002 (Tables), Turgeon (2018), R Package rootWishart.



    The pdf and cdf of  `\Theta_1`  are given by:

    .. math:: \text{pdf}_X(\theta_1) =  C \sqrt{|A(\theta_1)|} \times \tfrac{1}{2} \text{tr} \left( A(\theta_1)^{-1} \cdot \frac{\mathrm{d} A(\theta_1)}{ \mathrm{d}\theta_1} \right)

    .. math:: \text{cdf}_X(\theta_1) = C \sqrt{|A(\theta_1)|}, \quad \text{where}

    .. math:: C= \pi^{s/2} \prod_{i=1}^s \frac{\Gamma\left(\tfrac{1}{2} (i+2m+2n+s+2)  \right)}{\Gamma\left(\tfrac{i}{2}   \right)\Gamma\left(\tfrac{1}{2} (i+2m+1)   \right)\Gamma\left(\tfrac{1}{2} (i+2n+1)  \right)},

    .. math:: s=p, \quad  m=(n_1-p-1)/2, \quad  n=(n_2-p-1)/2.


    When `s` is even, we have `n_{mat} = s` and the elements of the `s \times s` skew-symmetric matrix `A(\theta_1)` are:

    .. math:: a_{i,j}(\theta_1) = E (\theta_1;m + j,m + i) - E (\theta_1;m + i,m + j) \quad i, j = 1, \ldots, s , \quad \text{where}

    .. math:: E(x;a,b) = \int_{0}^x t^{a-1} (1-t)^n B(t;b,n+1) \mathrm{d} t. \label{eq:RoyMatrixIntegral}


    When `s` is odd, we have `n_{mat} = s+1` and the elements of the `(s+1) \times (s+1)` skew-symmetric 
    matrix `A(\theta_1)` are as above, with the additional elements

    .. math:: a_{i,s+1}(\theta_1) = I(\theta_1;m + i,n + 1) \quad i = 1, \ldots, s; \quad a_{s+1,j}(\theta_1) = -a_{j,s+1}(\theta_1) \quad j = 1, \ldots, s..

    Note that `a_{i,j}(\theta_1) = -a_{j,i}(\theta_1)` and `a_{i,i}(\theta_1) = a_{s+1,s+1}(\theta_1) = 0`.





    An example:

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; p = 3; n1 = 10; n2 = 12
        >>> dx = dec.roy_pdf_cdf_sf(x, p, n1, n2); mx = mpm.roy_pdf_cdf_sf(x, p, n1, n2); 
        >>> ix = ipm.roy_pdf_cdf_sf(x, p, n1, n2); fx = fpm.roy_pdf_cdf_sf(x, p, n1, n2); 
        >>> gx = gmp.roy_pdf_cdf_sf(x, p, n1, n2); ax = apm.roy_pdf_cdf_sf(x, p, n1, n2)
        >>> mpm.show([dx, mx, ix])
        dec:  9.727307040581953720491613246746146674676E-1
        mpm:  9.727307040581953720491613246746146674676e-1
        ipm:  9.727307040581953720491613246746146674676e-1 (5.901e-40%)
        fpm:  9.72730704058195E-01
        gmp:  9.727307040581953720491613246746146674676E-01
        ipm:  9.727307040581953720491613246746146674676e-1 (5.901e-40%)




