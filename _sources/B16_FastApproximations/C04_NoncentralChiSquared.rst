






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />





|newpage|



Approximations based on the noncentral chi-squared distribution
===============================================================================



.. _rst_mpm_wilks_lambda_glm_chi2_cdf: 

Non-central Wilks' Lambda (GLM): cdf and sf (Fujikoshi)
----------------------------------------------------------------------------------------------------

.. method:: ctx.wilks_lambda_glm_chi2_cdf(x, p, q, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the noncentral Wilks' Lambda (GLM) distribution. 

    :cite:t:`Fujikoshi1973` proposes the following noncentral chi-square approximation to the cdf and sf:


    .. math::
       :nowrap:

       \begin{eqnarray}
        F_{\Lambda,GLM}(p,q,n;z;\Theta) & = & F_{\chi^2}\left(pq, x; \theta_1\right) + \frac{1}{4n} \sum_{k=1}^3{a_k } F_{\chi^2}\left(pq+2k, x; \theta_1\right) \\
        & + & \frac{1}{96n^2}  \sum_{k=0}^6{b_k } F_{\chi^2}\left(pq+2k, x; \theta_1\right)  \nonumber  +  \frac{1}{96n^3}  \sum_{k=1}^9{c_k } F_{\chi^2}\left(pq+2k, x; \theta_1\right) + O(n^{-4}) \nonumber 
       \end{eqnarray}


    .. math:: \Theta = \Lambda^{-1} M M', \quad  \theta_j = \text{tr } \Theta^j, 

    .. math:: m=n+(pq-1)/2, \quad  x= m \log(z), \quad  s=(p+q+1)/4, \quad  r=pq (p^2+q^2-5)/48,


    .. math::
       :nowrap:

       \begin{eqnarray}
        a_1 & = & 2 s \theta_1 \\
        a_2 & = &  2 s \theta_1 - \theta_2  \nonumber \\
        a_3 & = &   \theta_2  \nonumber \\
        \nonumber \\
        b_0 & = & r \\
        b_1 & = & 0  \nonumber \\
        b_2 & = & r 4s^2 \theta_1 + 2s^2 \theta_1^2 + 2s \theta_2  \nonumber \\
        b_3 & = & 4 s^2 \theta_1 - (1+4 s^2) \theta_1^2 - (1+8s) \theta_2 + 2 s  \theta_1 \theta_2 + (4/3)  \theta_3  \nonumber \\
        b_4 & = & (1 + 2s^2) \theta_1^2 + (1+6s)\theta_2 - 4s\theta_1\theta_2- 4\theta_3 + \theta_2^2/2  \nonumber \\
        b_5 & = & 2s\theta_1\theta_2 + (8/3)\theta_3 - \theta_2^2   \nonumber \\
        b_6 & = & \theta_2^2/2  \nonumber \\
        \nonumber \\
        c_1 & = & 2 r s  \theta_1 \\  
        c_2 & = & r (2 s  \theta_1  \theta_2)  \nonumber \\
        c_3 & = & 2s(r+4s^2)\theta_1 + 2s(1+4 s^2)\theta_1^2 + (-r+2s+12s^2)\theta_2 - \tfrac{4}{3}s^3 \theta_1^3 -4s^2\theta_1\theta_2 -\tfrac{8}{3}s\theta_3  \nonumber \\
        c_4 & = & 2 s (r+4 s^2)  \theta_1 - (1+10s+16s^3)\theta_1^2 - (3+r+10s+36s^2)  \theta_2 + 2s(1+2s^2)\theta_1^3   \nonumber \\
        &  + & 2(2+s+12s^2)\theta_1\theta_2 + 4(1+6s)\theta_3  - 2s^2\theta_1^2\theta_2 - 2s\theta_2^2 - \tfrac{8}{3}s\theta_1\theta_3 - 2\theta_4    \nonumber \\
        c_5 & = & (1+8 s+8 s^3)\theta_1^2 + (3+r+8s+24s^2)\theta_2 - 4s(1+s^2)\theta_1^3 - 4(3+s+9s^2)\theta_1\theta_2 - 12(1+4s)\theta_3  \nonumber \\
        & + & (1+6s^2)\theta_1^2  \theta_2 + (1+10s)\theta_2^2 + \tfrac{32}{3}s\theta_1\theta_3 + 12\theta_4 - \tfrac{4}{3}\theta_2  \theta_3 - s\theta_1\theta_2^2    \nonumber \\
        c_6 & = & s (2+\tfrac{4}{3}s^2) \theta_1^3+2 (4+s+8 s^2)  \theta_1  \theta_2+8 (1+\tfrac{10}{3}s)  \theta_3 - 2 (1+3 s^2) \theta_1^2  \theta_2 - 2 (1+7 s) \theta_2^2 \nonumber \\
        &  - & \tfrac{40}{3}s  \theta_1  \theta_3 - 20\theta_4 + \tfrac{16}{3}\theta_2\theta_3 + 3s\theta_1\theta_2^2 - \tfrac{1}{6} \theta_2^3    \nonumber \\
        c_7 & = & (1+2 s^2)\theta_1^2\theta_2 + (1+6 s)\theta_2^2 + \tfrac{16}{3}s\theta_1\theta_3 + 10\theta_4 - \tfrac{20}{3}\theta_2\theta_3 - 3s\theta_1\theta_2^2 + \tfrac{1}{2}\theta_2^3  \nonumber \\
        c_8 & = & \tfrac{8}{3}\theta_2\theta_3 + s\theta_1\theta_2^2 - \tfrac{1}{2}\theta_2^3   \nonumber \\
        c_9 & = &  \tfrac{1}{6}\theta_2^3  \nonumber
       \end{eqnarray}




    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.wilks_lambda_glm_chi2_cdf(x, nu, nc); mx = mpm.wilks_lambda_glm_chi2_cdf(x, nu, nc)
        >>> ix = ipm.wilks_lambda_glm_chi2_cdf(x, nu, nc); fx = fpm.wilks_lambda_glm_chi2_cdf(x, nu, nc)
        >>> gx = gmp.wilks_lambda_glm_chi2_cdf(x, nu, nc); ax = apm.wilks_lambda_glm_chi2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)









|newpage|


:cite:t:`Fujikoshi1973`

Pillai:  coeff p. 93 (5.10), GLM p. 96 (5.2), CORR p. 113/114 (8.1)


Hotelling:  coeff p. 105 (6.18), GLM p. 105 (6.19), CORR p. 119 (9.9)





.. _rst_mpm_wilks_lambda_ind_chi2_cdf: 

Non-central Wilks' Lambda (independence): cdf and sf (Lee)
----------------------------------------------------------------------------------------------------



.. method:: ctx.wilks_lambda_ind_chi2_cdf(x, p, q, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the noncentral Wilks' Lambda (independence) distribution. 


    :cite:t:`Lee1971b` proposes the following noncentral chi-square approximation:



    .. math:: \text{cdf}_X(x) =  = F_{\chi^2}\left(pq, x; s1\right) + \frac{1}{4n} \sum_{k=0}^3{a_k } F_{\chi^2}\left(pq+2k, x; s1\right) + \frac{1}{96n^2}  \sum_{k=0}^6{b_k } F_{\chi^2}\left(pq+2k, x; s1\right)  + O(n^{-3}), 



    `\Omega = \Lambda^{-1} M M'`, `\theta_j = \text{tr } \Omega^j`, `m=n+(pq-1)/2`, `x= m \log(z)`, `f = p q`, 
    `s=(p+q+1)/4`, `r=f (p^2+q^2-5)/48`,


    `a_0=-q \theta_1+\theta_2`, `a_1=(2 s+q) \theta_1 - 2 \theta_2`, `a_2=-2 s \theta_1+2 \theta_2`, `a_3=-\theta_2`,

    `b_0= -r - q l \theta_1+(q+l) \theta_2 + \tfrac{1}{2} q^2 \theta_1^2 - \tfrac{4}{3} \theta_3 - q \theta_1 \theta_2 + \tfrac{1}{2} \theta_2^2, \\`

    `b_1=q^2 \theta_1 - 4 q \theta_2 - q (q+2s) \theta_1^2 + 4 \theta_3+(3q+2s) \theta_1 \theta_2 - 2 \theta_2^2, \\`

    `b_2= r - 2s (q+2s) \theta_1 + (2p+6q+3) \theta_2 + (\tfrac{1}{2} l^2+6qs+1) \theta_1^2 - 8 \theta_3 -(4q+6s) \theta_1 \theta_2 + 4 \theta_2^2, \\`

    `b_3=4s^2 \theta_1 -(3p+5q+5) \theta_2 -(4s^2+2qs+2) \theta_1^2 + \tfrac{32}{3} \theta_3 +(3q+8s) \theta_1 \theta_2 - 5\theta_2^2, \\`

    `b_4=(6s+1) \theta_2 + (2s^2+1) \theta_1^2 - 8\theta_3 -(q+6s)\theta_1\theta_2 + 4 \theta_2^2, \\`

    `b_5 = \tfrac{8}{3} \theta_3 + 2s\theta_1\theta_2 - 2\theta_2^2, \\`

    `b_6=\tfrac{1}{2} \theta_2^2`.



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.wilks_lambda_ind_chi2_cdf(x, nu, nc); mx = mpm.wilks_lambda_ind_chi2_cdf(x, nu, nc)
        >>> ix = ipm.wilks_lambda_ind_chi2_cdf(x, nu, nc); fx = fpm.wilks_lambda_ind_chi2_cdf(x, nu, nc)
        >>> gx = gmp.wilks_lambda_ind_chi2_cdf(x, nu, nc); ax = apm.wilks_lambda_ind_chi2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






|newpage|


.. _rst_mpm_pillai_v_glm_chi2_cdf: 

Non-central Pillai's V (GLM): cdf and sf Fujikoshi
----------------------------------------------------------------------------------------------------

.. method:: ctx.pillai_v_glm_chi2_cdf(x, p, q, n, lambda)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the noncentral Pillai's V (GLM) distribution. 


    :cite:t:`Fujikoshi1974` proposes the following noncentral chi-square approximation to the cdf and sf:



    .. math:: \text{cdf}_X(x) =  = F_{\chi^2}\left(pq, x; s1\right) + \frac{1}{4n} \sum_{k=0}^3{a_k } F_{\chi^2}\left(pq+2k, x; s1\right) + \frac{1}{96n^2}  \sum_{k=0}^6{b_k } F_{\chi^2}\left(pq+2k, x; s1\right)  + O(n^{-3}), 



    `l_0 = (3  f - 8)  g^2 + 4  g + 4  (f + 2)`

    `l_1 = -12  f  g^2`

    `l_2 = 6  (3  f + 8)  g^2`

    `l_3 = -4  ((3  f + 16)  g^2 + 4  g + 4  (f + 2))`

    `l_4 = 3  ((f + 8)  g^2 + 4  g + 4  (f + 2))`


    `a_0 = -f  g`

    `a_1 = 2  f  g`

    `a_2 = -f  g + 4  g  \lambda_1 + 4  \lambda_2`

    `a_3 = -4  g  \lambda_1`

    `a_4 = -4  \lambda_2`


    `b_0 = f  l_0`

    `b_1 = f  l_1`

    `b_2 = f  l_2 + 2  l_1  \lambda_1 - 24  f  g  \lambda_2`

    `b_3 = f  l_3 + 4  l_2  \lambda_1 + 48  (f + 4)  g  \lambda_2 + 128  \lambda_3`

    `b_4 = f  l_4 + 6  l_3  \lambda_1 + 48  (g^2 - 2)  \lambda_1^2 - 96  (g + 1)  \lambda_2 + 96  g  \lambda_1  \lambda_2 + 48  \lambda_2^2`

    `b_5 = 8  (l_4  \lambda_1 - 12  (g^2 + 2)  \lambda_1^2 - 6  ((f + 12)  g + 4)  \lambda_2 - 12  g  \lambda_1  \lambda_2 - 48  \lambda_3)`

    `b_6 = 8  (6  (g^2 + 6)  \lambda_1^2 + 3  ((f + 20)  g + 12)  \lambda_2 - 12  g  \lambda_1  \lambda_2 - 16  \lambda_3 - 12  \lambda_2^2)`

    `b_7 = 96  (g  \lambda_1  \lambda_2 + 4  \lambda_3)`

    `b_8 = 48  \lambda_2^2`



    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pillai_v_glm_chi2_cdf(x, nu, nc); mx = mpm.pillai_v_glm_chi2_cdf(x, nu, nc)
        >>> ix = ipm.pillai_v_glm_chi2_cdf(x, nu, nc); fx = fpm.pillai_v_glm_chi2_cdf(x, nu, nc)
        >>> gx = gmp.pillai_v_glm_chi2_cdf(x, nu, nc); ax = apm.pillai_v_glm_chi2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)






|newpage|


.. _rst_mpm_pillai_v_ind_chi2_cdf: 

Non-central Pillai's V (independence): cdf and sf (Lee)
----------------------------------------------------------------------------------------------------


.. method:: ctx.pillai_v_ind_chi2_cdf(x, p, q, n, lambda)


    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the noncentral Pillai's V (independence) distribution. 

    :cite:t:`Lee1971b` proposes the following noncentral chi-square approximation. See also



    .. math:: \text{cdf}_X(x) =  = F_{\chi^2}\left(pq, x; s1\right) + \frac{1}{4n} \sum_{k=0}^3{a_k } F_{\chi^2}\left(pq+2k, x; s1\right) + \frac{1}{96n^2}  \sum_{k=0}^6{b_k } F_{\chi^2}\left(pq+2k, x; s1\right)  + O(n^{-3}), 


   
    `a_0 = -f  g - 4  \lambda_2`

    `a_1 = 2  f  g`

    `a_2 = -f  g + 4  g  \lambda_1 + 8  \lambda_2`

    `a_3 = -4  g  \lambda_1`

    `a_4 = -4  \lambda_2`


    `b_0 = f  l_0 + 24  f  g  \lambda_2 - 128  \lambda_3 + 48  \lambda_2^2`

    `b_1 = f  l_1 - 48  f  g  \lambda_2`

    `b_2 = f  l_2 + 2  l_1  \lambda_1 + 96  \lambda_1^2 - 24  (q  p^2 + q  (q + 1)  p - 4)  \lambda_2 - 96  g  \lambda_1  \lambda_2 - 192  \lambda_2^2`

    `b_3 = f  l_3 + 4  l_2  \lambda_1 + 96  (q  p^2 + (q^2 + q + 4)  p + 4  (q + 1))  \lambda_2 + 96  g  \lambda_1  \lambda_2 + 640  \lambda_3`

    `b_4 = f  l_4 + 6  l_3  \lambda_1 + 48  (p^2 + 2  (q + 1)  p + q^2 + 2  q - 3)  \lambda_1^2 - 24  (q  p^2 + (q^2 + q + 12)  p + 4  (3  q + 5))  \lambda_2 + 192  g  \lambda_1  \lambda_2 + 288  \lambda_2^2` 


    `b_5 = 8  l_4  \lambda_1 - 96  (p^2 + 2  (q + 1)  p + q^2 + 2  q + 3)  \lambda_1^2 - 48  (q  p^2 + (q^2 + q + 12)  p + 4  (3  q + 4))  \lambda_2 - 192  g  \lambda_1  \lambda_2 - 768  \lambda_3`

    `b_6 = 48  (p^2 + 2  (q + 1)  p + q^2 + 2  q + 7)  \lambda_1^2 + 24  (q  p^2 + (q^2 + q + 20)  p + 4  (5  q + 8))  \lambda_2 - 96  g  \lambda_1  \lambda_2 - 128  \lambda_3 - 192  \lambda_2^2`

    `b_7 = 96  (g  \lambda_1  \lambda_2 + 4  \lambda_3)`

    `b_8 = 48  \lambda_2^2`


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.pillai_v_ind_chi2_cdf(x, nu, nc); mx = mpm.pillai_v_ind_chi2_cdf(x, nu, nc)
        >>> ix = ipm.pillai_v_ind_chi2_cdf(x, nu, nc); fx = fpm.pillai_v_ind_chi2_cdf(x, nu, nc)
        >>> gx = gmp.pillai_v_ind_chi2_cdf(x, nu, nc); ax = apm.pillai_v_ind_chi2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)








|newpage|



.. _rst_mpm_hotelling_t2_glm_chi2_cdf: 

Non-central Hotelling `T^2` (GLM): cdf and sf (Fujikoshi)
----------------------------------------------------------------------------------------------------

.. method:: ctx.hotelling_t2_glm_chi2_cdf(x)


    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the noncentral Hotelling `T^2` (GLM) distribution. 


    :cite:t:`Fujikoshi1974`  proposes the following noncentral chi-square approximation to the pdf and cdf:



    .. math:: \text{cdf}_X(x) =  = F_{\chi^2}\left(pq, x; s1\right) + \frac{1}{4n} \sum_{k=0}^3{a_k } F_{\chi^2}\left(pq+2k, x; s1\right) + \frac{1}{96n^2}  \sum_{k=0}^6{b_k } F_{\chi^2}\left(pq+2k, x; s1\right)  + O(n^{-3}), 



    `a_0 = f  g`

    `a_1 = -2  g  (f - 2  \lambda_1)`

    `a_2 = f  g - 8  g  \lambda_1 + 4  \lambda_2`

    `a_3 = 4  (g  \lambda_1 - 2  \lambda_2)`

    `a_4 = 4  \lambda_2`


    `b_0 = f  l_0`

    `b_1 = l_1  (f - 2  \lambda_1)`

    `b_2 = f  l_2 + 2  (l_1 - 2  l_2)  \lambda_1 + 48  g^2  \lambda_1^2 + 24  (f + 4)  g  \lambda_2`

    `b_3 = f  l_3 + 2  (2  l_2 - 3  l_3)  \lambda_1 - 192  (g^2 + 1)  \lambda_1^2 - 96  ((f + 8)  g + 2)  \lambda_2 + 96  g  \lambda_1  \lambda_2 + 128  \lambda_3`

    `b_4 = f  l_4 + 2  (3  l_3 - 4  l_4)  \lambda_1 + 96  (3  g^2 + 7)  \lambda_1^2 + 48  (3  (f + 12)  g + 14)  \lambda_2 - 384  g  \lambda_1  \lambda_2 - 768  \lambda_3 + 48  \lambda_2^2`

    `b_5 = 8  l_4  \lambda_1 - 192  (g^2 + 4)  \lambda_1^2 - 96  ((f + 16)  g + 8)  \lambda_2 + 576  g  \lambda_1  \lambda_2 + 1536  \lambda_3 - 192  \lambda_2^2`

    `b_6 = 48  (g^2 + 6)  \lambda_1^2 + 24  ((f + 20)  g + 12)  \lambda_2 - 384  g  \lambda_1  \lambda_2 - 1280  \lambda_3 + 288  \lambda_2^2`

    `b_7 = 96  g  \lambda_1  \lambda_2 + 384  \lambda_3 - 192  \lambda_2^2`

    `b_8 = 48  \lambda_2^2`


    An example (CDF):

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm
        >>> mpm.dps = 40; x = 12; nu = 10; nc = 30
        >>> dx = dec.hotelling_t2_glm_chi2_cdf(x, nu, nc); mx = mpm.hotelling_t2_glm_chi2_cdf(x, nu, nc)
        >>> ix = ipm.hotelling_t2_glm_chi2_cdf(x, nu, nc); fx = fpm.hotelling_t2_glm_chi2_cdf(x, nu, nc)
        >>> gx = gmp.hotelling_t2_glm_chi2_cdf(x, nu, nc); ax = apm.hotelling_t2_glm_chi2_cdf(x, nu, nc)
        >>> mpm.show([dx, mx, ix, fx, gx, ax])
        dec:  3.113877423416836055714616090074444149943E-1
        mpm:  3.113877423416836055714616090074444149943e-1
        ipm:  3.113877423416836055714616090074444149944e-1 (4.147e-38%)
        fpm:  3.11387742341684E-01
        gmp:  3.113877423416836055714616090074444149943E-01
        ipm:  3.113877423416836055714616090074444149943e-1 (4.055e-38%)







|newpage|




.. _rst_mpm_hotelling_t2_ind_chi2_cdf: 

Non-central Hotelling `T^2` (independence): cdf and sf (Lee)
----------------------------------------------------------------------------------------------------


.. method:: ctx.hotelling_t2_ind_chi2_cdf(x)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Returns an approximation to the cdf of the noncentral Hotelling `T^2` (independence) distribution. 

    :cite:t:`Lee1971b` proposes the following noncentral chi-square approximation:



    .. math:: \text{cdf}_X(x) =  = F_{\chi^2}\left(pq, x; s1\right) + \frac{1}{4n} \sum_{k=0}^3{a_k } F_{\chi^2}\left(pq+2k, x; s1\right) + \frac{1}{96n^2}  \sum_{k=0}^6{b_k } F_{\chi^2}\left(pq+2k, x; s1\right)  + O(n^{-3}), 



    `s_1 = 2\lambda_1`

    `s_2 = 4\lambda_2`

    `s_3 = 8\lambda_3`


    `a_0 = q  p  (q - p - 1) - 2  q  s_1 + s_2`

    `a_1 = -2  q^2  p + 4  q  s_1 - 2  s_2`

    `a_2 = q  p  (q + p + 1) - 2  (2  q + p + 1)  s_1 + 2  s_2`

    `a_3 = 2  (q + p + 1)  s_1 - 2  s_2`

    `a_4 = s_2`

    `b_0 = q  p  (3  q  p^3 - 2  (3  q^2 - 3  q + 4)  p^2 + 3  (q^3 - 2  q^2 + 5  q - 4)  p - 8  q^2 + 12  q + 4) - 12  q^2  p  (q - p - 1)  s_1 - 6  q  (p^2 - q  p + p - 4)  s_2 + 12  q^2  s_1^2 - 16  s_3 - 12  q  s_1  s_2 + 3  s_22`

    `b_1 = -12  q^3  p^2  (q - p - 1) - 24  q^2  (p^2 - 2  q  p + p - 2)  s_1 + 12  q  (p^2 - 2  q  p + p - 8)  s_2 - 48  q^2  s_1^2 + 48  s_3 + 48  q  s_1  s_2 - 12  s_22`

    `b_2 = -6  q^2  p^4 - 12  q^2  p^3 + 18  q^2  (q^2 + 1)  p^2 + 24  q^2  (2  q + 1)  p + 12  q  (p^3 + 2  p^2 - 7  (q^2 + 1)  p - 16  q - 8)  s_1 - 6  (q  p^2 - (7  q^2 - q + 8)  p - 40  q - 12)  s_2 + 24  (q  p + 4  q^2 + q + 1)  s_1^2 - 12  (p + 8  q + 1)  s_1  s_2 - 96  s_3 + 24  s_22`

    `b_3 = -(12  q^3 + 16  q)  p^3 - (12  q^4 + 12  q^3 + 96  q^2 + 48  q)  p^2 - (64  q^3 + 96  q^2 + 64  q)  p + 12  (-q  p^3 + (4  q^2 - 2  q + 4)  p^2 + (7  q^3 + 4  q^2 + 31  q + 12)  p + 4  (7  q^2 + 8  q + 4))  s_1 - 48  ((q^2 + 3)  p + 9  q + 5)  s_2 - 24  (3  q  p + 5  q^2 + 3  q + 4)  s_1^2 + 176  s_3 + 12  (3  p + 11  q + 3)  s_1  s_2 - 36  s_22`

    `b_4 = 3  q^2  p^4 + (6  q^3 + 6  q^2 + 24  q)  p^3 + (3  q^4 + 6  q^3 + 63  q^2 + 60  q)  p^2 + (24  q^3 + 60  q^2 + 60  q)  p - 12  (q  p^3 + (5  q^2 + 2  q + 12)  p^2 + (4  q^3 + 5  q^2 + 45  q + 32)  p + 4  (6  q^2 + 11  q + 9))  s_1 + 6  (q  p^2 + (7  q^2 + q + 44)  p + 88  q + 76)  s_2 + 12  (p^2 + 2  (4  q + 1)  p + 8  q^2 + 8  q + 17)  s_1^2 - 12  (4  p + 11  q + 4)  s_1  s_2 - 240  s_3 + 42  s_22`

    `b_5 = (12  q  p^3 + 24  (q^2 + q + 4)  p^2 + 12  (q^3 + 2  q^2 + 21  q + 20)  p + 48  (2  q^2 + 5  q + 5))  s_1 - 12  (q  p^2 + (2  q^2 + q + 24)  p + 32  q + 40)  s_2 - 24  (p^2 + (3  q + 2)  p + 2  q^2 + 3  q + 9)  s_1^2 + 240  s_3 + 48  (p + 2  q + 1)  s_1  s_2 - 36  s_22`

    `b_6 = (6  q  p^2 + 6  (q^2 + q + 20)  p + 120  q + 192)  s_2 + (12  p^2 + 24  (q + 1)  p + 12  (q^2 + 2  q + 7))  s_1^2 - 12  (3  p + 4  q + 3)  s_1  s_2 - 160  s_3 + 24  s_22`

    `b_7 = 48  s_3 + 12  (q + p + 1)  s_1  s_2 - 12  s_22`

    `b_8 = 3  s_22`



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





