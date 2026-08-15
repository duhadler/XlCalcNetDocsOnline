

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





|newpage|

Mpmath: Asymptotic expansions
===============================================================================


Edgeworth expansion: general approximation of the pdf, cdf and sf
-------------------------------------------------------------------------------

.. method:: ctx.edgeworth(x, cumulants)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Edgeworth expansion approximations of the pdf, cdf and sf by using the cumulants of the distribution.


    See also Wikipedia :cite:p:`WikipediaAlg11`, :cite:t:`Blinnikov1998`, Wikipedia :cite:p:`WikipediaAlg12`, Wikipedia :cite:p:`WikipediaFun135`.

    Using the first 4 cumulants, we have

    .. math::  \text{Pr}\left[\frac{u-\mu}{\sigma} \le x \right] = \Phi(x) + \phi(x)\left[\frac{\gamma_1}{6}(1-x^2) + \frac{\gamma_2}{24}(3x-x^3) +  \frac{\gamma_1^2}{72}(15x-10x^3+x^5)\right] + O(N^{-3/2}) 


    :cite:t:`Withers2009` and :cite:t:`Withers2015` have shown that the Edgeworth expansion can also be expressed in terms of standardized cumulants `\alpha_r = \kappa_r/\kappa_2^{r/2}` (with `\alpha_1 = \alpha_2 = 0)`, partial exponential Bell polynomials `B_{r,k}(\boldsymbol{\alpha}),  \boldsymbol{\alpha} = (\alpha_1, \cdots, \alpha_r)`, and Hermite polynomials `H_r(x)`:

    .. math::  f(x) = \phi(x) + \phi(x) \sum_{j=1}^{\infty} h_{1j}(x) n^{-j/2}, \quad  \text{where}  

    .. math::  h_{1j}(x) = \sum_{k=1}^j B_{r,k}(\boldsymbol{\alpha}) H_{r}(x) / r! , \quad  \text{with } r = j+2k.


    .. math::  F(x) = \Phi(x) - \phi(x) \sum_{j=1}^{\infty} h_{0j}(x) n^{-j/2}, 

    .. math::  1 - F(x) = \Phi(-x) + \phi(x) \sum_{j=1}^{\infty} h_{0j}(x) n^{-j/2}, \quad  \text{where}  

    .. math::  h_{0j}(x) = \sum_{k=1}^j B_{r,k}(\boldsymbol{\alpha}) H_{r-1}(x) / r! , \quad  \text{with } r = j+2k.


    The partial Bell polynomials can be computed efficiently by a recurrence relation: 

    .. math::  B_{r,k}(\boldsymbol{\alpha}) =\sum _{i=1}^{r-k+1}{\binom {r-1}{i-1}}\alpha_{i}B_{r-i,k-1}(\boldsymbol{\alpha}), \quad  \text{where }



    .. math::  B_{0,0}=1; \quad B_{r,0}=0{\text{ (for }}r\geq 1); \quad B_{0,k}=0{\text{ (for }}k\geq 1); \quad B_{r,1}(\boldsymbol{\alpha})=\alpha_r.

    The Hermite polynomials are defined by 

    .. math::  H_0(x) = 1, \quad  H_1(x) = x, \quad H_{r+1}(x) = x H_r(x)- r H_{r-1}(x)



    The following code shows how to call the Edgeworth  expansion for the central cdf.

    .. code-block:: python
    
        def EdgeworthWhithersDemo(self):
            Order = 30
            F = 100
            X = mp.mpf(110)
        
            kappa = mp.matrix(Order+1, 1)
            kappa[1] = F
            for i in range(2, Order+1):
                kappa[i] = kappa[i - 1] * 2 * (i - 1)

            LeftTail1, RightTail1 = self.EdgeworthWhithers(X, Order, kappa)
            print("EdgeworthWhithers LeftTail1: ", LeftTail1, " RightTail1: ",  RightTail1)

    This gives the following results:    

    .. parsed-literal::

        Hello!
        X:  110.0 , Z:  0.7071067811865475244008443621048490392848 , 
        mean:  100.0 , sigma:  14.1421356237309504880168872420969807857
        s3:  0.7602499389065232688413733269459822643682 , 
        s4:  0.3106965603769277448709088912288091945547

        j:  1 , s2:  0.007323188157795373284114366290203815819688
        j:  2 , s2:  0.000244106271926512442803812209673460527323
        j:  3 , s2:  -0.00002427501259713651514549021418419413021711
        j:  4 , s2:  0.000002526386902276474842073713864467689855687
        j:  5 , s2:  -0.0000002843964533935719011627505046640421102775
        j:  6 , s2:  0.00000002087338535959227300224647267964356971442
        j:  7 , s2:  -0.000000001797321695705282603398930576647079128807
        j:  8 , s2:  0.0000000001105716283451282215450868950557968496009

        LeftTail1:  0.7677952195007321931882055465876641482851  
        RightTail1:  0.2322047804992678068117944534123358517149



Cornish-Fisher expansion: general approximation of the qtf and isf
-------------------------------------------------------------------------------

.. method:: ctx.cornish_fisher(x, cumulants)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the Cornish-Fisher approximation of the quantile by using the cumulants of the distribution.

    The quantiles of many distribution functions can be approximated by the classical Cornish and Fisher expansion :cite:t:`Cornish1938`, :cite:t:`Fisher1960`), provided that the cumulants `\kappa_r` of the distribution are known (see also Wikipedia :cite:p:`WikipediaAlg14`): 

    .. math:: x = z + \sum_{k=1}^{\infty} n^{-k/2} \xi_k(z)

    where `\xi_k(z)` is the collection of all the terms that belong to the `k`-th power of `n^{-1/2}`. It seems to be easier to describe algorithm AS269 (see :cite:t:`Lee1992`), which is used to calculate the `k`-th adjustment term `\xi_k(z)`, by giving a program which implements it, rather than to describe it using mathematical formulas:



    .. code-block:: python

        def CornishFisherLee(self, r, x0, ac, adj):
            a = iv.matrix(r+3, 1); d = iv.matrix(r+3, 1)
            h = iv.matrix(3 * (r+3), 1)
            p = iv.matrix((3 * (r+3)) * ((r+3) + 1) // 2, 1)
            x = iv.mpf(x0); cc = -1
            for j in range(1, r+1):
                a[j] = cc * ac[j] / ((j + 1) * (j + 2))
                cc = -cc            
            h[1] = -x; h[2] = x * x - 1
            for j in range(3, (3 * r)+1):
                h[j] = -(x * h[j - 1] + (j - 1) * h[j - 2])
            d[1] = -a[1] * h[2]; adj[1] = d[1]; p[1] = d[1]
            p[3] = a[1]; fac = iv.mpf(1); ja = 0
            for j in range(2, r+1):    
                fac = fac * j
                bc = iv.mpf(1)
                ja = ja + 3 * (j - 1)
                jb = ja
                for k in range(1, j):    
                    bcd = bc * d[k]
                    bca = bc * a[k]
                    jb -= 3 * (j - k)
                    for m in range(1, (3 * (j - k))+1):
                        jbl = jb + m; jal = ja + m
                        p[jal + 1] += bcd * p[jbl]
                        p[jal + k + 2] += bca * p[jbl]
                    bc = (bc * (j - k)) / k
                p[ja + j + 2] += a[j]; d[j] = 0
                for m in range(2, (3 * j)+1):     
                    d[j] -= p[ja + m] * h[m - 1]
                p[ja + 1] = d[j]
                adj[j] = d[j] / fac




    However, if one prefers mathematical formulas, :cite:t:`Jaschke2001` gives the following description of the algorithm:
    "Lee developed a recurrence formula for the `k`-th adjustment term `\xi_k(z)` in the Cornish-Fisher expansion, which is implemented in the algorithm AS269 :

    .. math:: \xi_k(H) = a_k H^{*(k+1)} - \sum_{j=1}^{k-1} \frac{j}{k} \left( \xi_{k-j}(H) - \xi_{k-j} \right) * \left( \xi_j - a_j H^{*(j+1)}  \right)  * H, \quad \text{where } a_k = \frac{\kappa_{k+2}}{(k+2)!}.

    `\xi_k(H)` is a formal polynomial expression in `H` with the usual algebraic relations between the summation 
    `"+"` and the "multiplication" `"*"`. Once `\xi_k(H)` is multiplied out in `*\text{-powers}` of `H`, 
    each `H^{*k}` is to be interpreted as the Hermite polynomial `H_k` and then the whole term becomes a polynomial 
    in `z` with the "normal" multiplication `"\cdot"`. `\xi_k` denotes the scalar that results when
    the "normal" polynomial `\xi_k(H)` is evaluated at the fixed quantile `z`, while `\xi_k(H)` denotes the 
    expression in the `(+,*)\text{-algebra}`. In this formula the adjustment of a given order is calculated recursively, the values of lower order adjustments being used in each stage of calculation."





Sheppard correction, cumulants
-------------------------------------------------------------------------------


.. method:: ctx.sheppard(cumulants)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Returns the Sheppard correction term for a vector of cumulants.


    The Sheppard correction is typically applied to the cumulants computed from normally distributed data which have been binned. If `\kappa_r^*` is the `r`-th cumulant of an ungrouped distribution and `\kappa_r` the `r`-th cumulant of an grouped distribution with class interval `c`, the corrected cumulants (under rather restrictive conditions) are

    .. math::  

        \kappa_r^*=\begin{cases}
        \kappa_r & \text{for } r \text{ odd} \\
        \kappa_r - \frac{B_r}{r} c^r & \text{for } r \text{ even}.
        \end{cases}

    where `B_r` is the `r`-th Bernoulli number. The same correction can be applied to the cumulants of the continuity-corrected test statistic of a random variable following a lattice distribution with step `c`. The (continuous) Edgeworth and Cornish-Fisher expansions using these corrected cumulants will then achieve the usual `o(n^{1-r/2})` error terms of these expansions (see :cite:t:`Kolassa1990`), despite the fact that the approximated CDF is discontinuous with jumps of order `O(n^{-1/2})`.

    A similar correction can be applied to the cumulant generating function (and its derivatives), as it is needed by the Luggannani-Rice saddle point approximation.




The Sheppard correction, cumulant generating function
-------------------------------------------------------------------------------


.. method:: ctx.sheppard_per_cgf(cgf)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Returns the Sheppard correction term for cumulant generating function of a discrete ("lattice") random variable.


    The Sheppard correction is typically applied to the cumulants computed from normally distributed data which have been binned. If `\kappa_r^*` is the `r`-th cumulant of an ungrouped distribution and `\kappa_r` the `r`-th cumulant of an grouped distribution with class interval `c`, the corrected cumulants (under rather restrictive conditions) are

    .. math::  

	    \kappa_r^*=\begin{cases}
	    \kappa_r & \text{for } r \text{ odd} \\
	    \kappa_r - \frac{B_r}{r} c^r & \text{for } r \text{ even}.
	    \end{cases}

    where `B_r` is the `r`-th Bernoulli number. The same correction can be applied to the cumulants of the continuity-corrected test statistic of a random variable following a lattice distribution with step `c`. The (continuous) Edgeworth and Cornish-Fisher expansions using these corrected cumulants will then achieve the usual `o(n^{1-r/2})` error terms of these expansions  (see :cite:t:`Kolassa1990`), despite the fact that the approximated CDF is discontinuous with jumps of order `O(n^{-1/2})`.

    A similar correction can be applied to the cumulant generating function (and its derivatives), as it is needed by the Luggannani-Rice saddlepoint approximation.











Luggannini-Rice expansion: general approximation of the pdf, cdf, and sf 
-------------------------------------------------------------------------------

.. method:: ctx.luggannini_rice(x, s, poly_t cgf_series)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Luggannini-Rice saddlepoint approximation of the pdf by using the cumulant generating function and its derivatives.


    See also :cite:t:`Butler2007`, :cite:t:`Daniels1954`, :cite:t:`Daniels1987`, :cite:t:`Lugannani1980`, Wikipedia :cite:p:`WikipediaDef11`, Wikipedia :cite:p:`WikipediaDef12`.

    Suppose the moment generating function of the random variable `X` is analytic and given by `M(t)` for `t` in some open neighbourhood of zero. Let `K(t)` = `\log (M(t))`  be the cumulant generating function of `X`, and denote by `K^{(j)}(t)` the `j^{\text{th}}` derivative of `K(t)`. 

    Let `F(x)` and `f(x)` denote the CDF and pdf of `X`, respectively, and `\Phi(\cdot)` and `\phi(\cdot)` denote the CDF and pdf  of the normal distribution, respectively. Let `s` be the solution to the saddlepoint equation `K^{(1)}(s)=x`, which in general needs to be solved numerically. Then 

    .. math:: f(x)   \thickapprox \phi(w)  \sum_{k=0}^{\infty} C_k, 

    .. math:: F(x) \thickapprox \Phi(w) + \phi(w) \sum_{k=0}^{\infty}   \left( A_k - B_k \right), \quad \text{and}

    .. math:: 1 - F(x) \thickapprox \Phi(-w) - \phi(w) \sum_{k=0}^{\infty}   \left( A_k - B_k \right),  \quad \text{where }


    .. math:: w  = \text{sgn}(s) \sqrt{2 (s K^{(1)}(s) - K(s))}; \quad t =  \sqrt{K^{(2)}(s)}; \quad u = s t.


    The coefficients `A_k`, `B_k` and `C_k` are calculated as follows:


    .. math:: A_0 = \frac{1}{u}, \quad A_j = A_0 \sum_{n=0}^{2j} \left(\frac{1}{u} \right)^{2j-n} \sum_{m=0}^{n} d_{m,n} \left(-2 \right)^{m+j} \left(\tfrac{1}{2} \right)_{m+j},

    where `d_{m,n}` is computed (with `d_{0,0}=1` and `d_{0,n}=0` for `n>0`) from


    .. math:: d_{m+1,n+1} = \frac{1}{n+1} \sum_{j=1}^{n-m+1} \frac{j}{(j+2)!}  \frac{K^{(j+2)}(s)}{ t^{j+2}}  \:   d_{m,n-j+1}, \quad 0 \le m \le n.


    .. math:: B_0 = \frac{1}{w},  \quad B_j =\frac{-2 (j-\tfrac{1}{2})  B_{j-1}}{w^2}.

    .. math:: C_0 = \frac{1}{t}, \quad C_j = \sum_{m=1}^{2j} d_{m,2j} \left(-2 \right)^{m+j} \left(\tfrac{1}{2} \right)_{m+j}.





Jensen expansion: general approximation of the qtf and isf
-------------------------------------------------------------------------------

.. method:: ctx.jensen_inv(q, s, , x0, poly_t cgf_series)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Jensen approximation of the qtf and isf


    Using the same notation as above, :cite:t:`Jensen1992` derived the following approximation (see also :cite:t:`Wang1995`):


    .. math::  	F(x)   \thickapprox   \Phi(r(s)),  \quad \text{where}    

    .. math::  	w(s) = \text{sgn}(s) \sqrt{2 (s K'(s) - K(s))},

    .. math::  	u(s) = s \sqrt{K''(s)} ,

    .. math::  	r(s) = w(s) + \frac{v(s)}{w(s)} , \quad \text{where } v(s)=\log \frac{u(s)}{w(s)}.


    To obtain an approximation to the `\alpha`-quantile of `F(x)`, we start with a reasonable estimate, say, `x_0`, and convert this to the corresponding saddlepoint, say `s_0`, such that `K'(s_0)=x_0`.


    Let `z_\alpha` be the `\alpha`-quantile of the standard normal distribution. We wish to solve for `s` in the equation

    .. math::  	h(s) = w(s) + \frac{v(s)}{w(s)}  - z_\alpha = 0.


    Starting with `n=0`, we compute successive approximations using Newton iterations as

    .. math::  	s_{n+1} = s_n - \frac{h(s_n)}{h'(s_n)},  \quad \text{where}  

    .. math::  	h'(s) = w'(s) + \frac{w(s) u'(s) - u(s) w'(s)\left(v(s)+1\right)}{u(s) w(s)^2},

    .. math::  	w'(s) = \text{sgn}(s) \frac{s K''(s)}{\sqrt{2 s K'(s) - 2 K(s)}} = \text{sgn}(s) \frac{s K''(s)}{w(s)},

    .. math::  	u'(s) = \frac{s K^{(3)}(s) + 2 K''(s)}{2 \sqrt{K''(s)}}.

    The final estimate `x_{n+1}` of the `\alpha`-quantile of `F(x)` is then obtained as `x_{n+1} = K'(s_{n+1})`.






Box-Davis expansion: general approximation of the pdf, cdf and sf
-------------------------------------------------------------------------------

.. method:: ctx.box_davis_expansion(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the Box-Davis approximation of the pdf, cdf and sf


    The Box-Davis expansion supports a general class of random variables, say `X`, with absolutely continuous distribution functions, for which the logarithm of the characteristic function, say `\log \left[ C_X(t) \right]`, may be validly represented by an asymptotic series

    .. math::   \log \left[ C_X(t) \right] \sim -\frac{1}{2} f \log(1-2it) + \sum_{r=1}^{\infty} \omega_r(\rho) \left[(1-2it)^{-r} -1\right],

    corresponding to a limiting chi-squared distribution with `f` degrees of freedom, where `\rho` is chosen in such a way that `\omega_1 = 0`, whenever this is possible. 

    The first comprehensive review of this type of expansion for the CDF is due to Box (see :cite:t:`Box1949`). The corresponding expansion for the inverse CDF is due to Davis (see :cite:t:`Davis1971`), who also gave algorithms for variables with characteristic functions different from those considered by Box. We refer therefore to this system of asymptotic expansions as the Box-Davis expansion. Distributions covered by this expansion include the beta distribution, the distribution of the product of independent beta variables, Wilks' Lambda, Mauchley's test for sphericity, Bartletts test for equality of independent covariance matrices, Hotelling's `T^2` and Pillai's `V`. For more information, see :cite:t:`Anderson2003` and :cite:t:`Ginzberg2013`.


    Let `\theta` be a suitably chosen constant (which will usually be proportional to sample size). We define

    .. math::  a_0 = 1; \quad a_j = \frac{1}{j} \sum_{l=1}^j l \omega_l a_{j-l}, \quad j>0. 

    .. math:: \log(K_B)  = -\sum_{j=1}^{r} \omega_j + O(\theta^{-r-1}), 

    Then `X` follows asymptotically (with `\theta \rightarrow \infty`) a `\chi^2`-distribution with `f` degrees of freedom, and the pdf, CDF of `M` can be developed into asymptotic expansions including terms of order `O(\theta^{-r})`, depending only on `f`, `\rho, K_B` and `a_j`:

    .. math::   \text{pdf}_X(x)) = \rho K_B \sum_{j=0}^{r} a_j f_{\chi_{f+2j}^2}(\rho x) + O(\theta^{-r-1}) 

    .. math::   \text{cdf}_X(x) = K_B \sum_{j=0}^{r} a_j F_{\chi_{f+2j}^2}(\rho x) + O(\theta^{-r-1}) 


    .. math::   1-\text{cdf}_X(x) = K_B \sum_{j=0}^{r} a_j \left[1 - F_{\chi_{f+2j}^2}(\rho x) \right] + O(\theta^{-r-1}) 




    Gupta and Tang (see :cite:t:`Gupta1988`) show that the above series are convergent as `r \rightarrow \infty` for fixed `x < 4\pi \theta`.


    When calling the following functions, only  `f`, `\rho`  and `\omega_j` need to be supplied by the user.
    `K_B` and `a_j` are calculated internally.




Box-Davis expansion: general approximation of the qtf and isf  (for `\omega_1 = 0`)
-------------------------------------------------------------------------------------------

.. method:: ctx.box_davis_expansion_inv(x, f, rho, omega)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    The Box-Davis expansion can be inverted efficiently in a two-step procedure. In the first step, an initial estimate is obtained, using the procedure given below. In the second step, the initial estimate is used as starting point of a Newton iteration, using the functions of the previous section.

    Assuming `\omega_1 = 0`, an approximation of the quantile function of `X`, `\text{qtf}_X(q))`, in terms of the quantiles of a `\chi^2`-distribution with `f` degrees of freedom, say `u = \chi_{f,\alpha}^2`, can be given as `\text{qtf}_X(q)) = (u + 2S)/\rho + O(\theta^{-8})`, where `S` is a polynomial in `u`, whose coefficients depend only on `f` and `\omega_j` (see :cite:t:`Davis1971`).




    .. math::
       :nowrap:

       \begin{eqnarray}
        S & = & \omega_2 P_2(u) \nonumber \\ \nonumber
        & + & \omega_3 P_3(u)  \\    \nonumber
        & + & \omega_4 P_4(u) + \tfrac{1}{2} \omega_2^2P_{2,2}(u) \\   \nonumber
        & + & \omega_5 P_5(u) + \omega_3 \omega_2P_{3,2}(u)  \\  \nonumber
        & + & \omega_6 P_6(u) + \omega_4 \omega_2P_{4,2}(u)   + \tfrac{1}{2} \omega_3^2P_{3,3}(u) + \tfrac{1}{6} \omega_2^3P_{2,2,2}(u) \\  \nonumber
        & + & \omega_7 P_7(u) + \omega_5 \omega_2P_{5,2}(u) + \omega_4 \omega_3P_{4,3}(u)  +  \tfrac{1}{2} \omega_3 \omega_2^2P_{3,2,2}(u),   \nonumber
       \end{eqnarray}



    .. math::   P_r(u) = \frac{u}{f_1} +  \ldots + \frac{u^r}{f_r}, \quad  f_r = f(f+2) \ldots (f+2r-2), \nonumber



    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{2,2} & = & - \frac{8 u^4 (f+3)}{(f_2 f_4)} + \frac{8 u^3}{(f_2 f_3)} + \frac{6 u^2}{(f f_2)} + \frac{2 u}{f^2}   \nonumber
       \end{eqnarray}


    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{3,2} & = & - \frac{12 u^5 (f+4)}{(f_2 f_5)} - \frac{2u^4 (f-6)}{(f_2 f_4)} + \frac{2 u^3 (3 f+10)}{(f_2 f_3)} + \frac{6 u^2}{(f f_2)} + \frac{2 u}{f^2}   \nonumber
       \end{eqnarray}


    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{4,2}(u) & = & -\frac{16 u^6 (f+5)}{f_2 f_6} -\frac{4 u^5 (f-4}{f_2 f_5} ) + \frac{2 u^4 (3 f+14)}{f_2 f_4} +\frac{2 u^3 (3 f+10)}{f_2 f_3} + \frac{6 u^2}{f f_2}  + \frac{2 u}{f^2}, \nonumber
       \end{eqnarray}


    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{3,3}(u) & = & -\frac{6 u^6 (3 f^2+30 f+80)}{f_3 f_6}  - \frac{6 u^5 (f_2+2 f-16)}{f_3 f_5} + \frac{4 u^4 (f+12)}{f_2 f_4} + \frac{4 u^3 (3 f+8)}{f_2 f_3} + \frac{6 u^2}{f f_2} + \frac{2 u}{f^2}, \nonumber
       \end{eqnarray}


    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{2,2,2}(u) & = & \frac{32 u^6 (7 f^2+62 f+120)}{f_2^2 f_6}  - \frac{32 u^5 (2 f^2+37 f+96)}{f_2^2 f_5}  - \frac{8 u^4 (23 f^2+124 f+132)}{f_2^2 f_4} \nonumber  \\ \nonumber
        & \: & - \frac{8 u^3 (f-10)}{f f_2 f_3} + \frac{28 u^2}{f^2 f_2} + \frac{4 u}{f^3}, \nonumber
       \end{eqnarray}


    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{5,2} & = & - \frac{20 u^7 (f+6)}{(f_2 f_7)}  - \frac{2 u^6 (3 f-10)}{(f_2 f_6)} +\frac{2 u}{f^2} +  2 \sum_{r=2}^5 \frac{u^r (3f+4r-2)}{f_2 f_r}    \nonumber
       \end{eqnarray}



    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{4,3}(u) & = &  - \frac{24 u^7 (f_2+12 f+40)}{f_3 f_7} - \frac{2 u^6 (5 f_2+18 f-80)}{f_3 f_6} + \frac{2 u^5 (f_2+42 f+176)}{f_3 f_5}  \nonumber \\ \nonumber
        & \: & +\frac{4 u^4 (3 f+16)}{f_2 f_4} + \frac{4 u^3 (3 f+8)}{f_2 f_3}  + \frac{6 u^2}{f f_2} + \frac{2 u}{f^2},
       \end{eqnarray}



    .. math::
       :nowrap:

       \begin{eqnarray}
	    P_{3,2,2}(u) & = & \frac{192 u^7 (2 f^3+31 f^2+154 f+240)}{f_2 f_3 f_7} - \frac{16 u^6 (4 f^3+153 f^2+1106 f+2160)}{f_2 f_3 f_6}  \nonumber   \\ \nonumber
        & \: &  - \frac{8 u^5 (35 f^3420 f^2+1540 f+1632)}{f_2 f_3 f_5}  - \frac{4 u^4 (25 f^2+80 f+12)}{f_2^2 f_4} + \frac{4 u^3 (7 f+38)}{f f_2 f_3} + \frac{28 u^2}{f^2 f_3} +  \frac{4 u}{f^3}. \\ \nonumber
       \end{eqnarray}




    When calling the following functions, only  `f`, `\rho`  and `\omega_j` need to be supplied by the user.
    `K_B` and `a_j` are calculated internally.







