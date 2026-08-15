

.. |newpage| raw:: latex

   \newpage


.. |vspace| raw:: html

   <br />




|newpage|

Raw Moments
========================================================

See also Wikipedia :cite:p:`WikipediaDef13`





Calculating the raw moments from the pdf 
----------------------------------------------------------------------------------------

.. method:: ctx.rawmoments_from_pdf(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.

    The n-th moment of a real-valued continuous function f(x) of a real variable about a value c is 

    .. math:: \mu _{n}=\int _{-\infty }^{\infty }(x-c)^{n}\,f(x)\,\mathrm {d} x.

    It is possible to define moments for random variables in a more general fashion than moments for real values—see moments in metric spaces. The moment of a function, without further explanation, usually refers to the above expression with c = 0. 




Calculating the raw moments from the pmf 
----------------------------------------------------------------------------------------

.. method:: ctx.rawmoments_from_pmf_vector(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    If `X` is a purely discrete random variable, then it attains values `x_{1},x_{2},\ldots` with probability `p_{i}=p(x_{i})`, and the CDF of `X` will be discontinuous at the points `x_{i}`: 

    .. math::  \mu _{n} = \sum _{x_{i}\leq x}  x_{i}^n  p(x_{i}).







Calculating the raw moments from the factorial moments
---------------------------------------------------------------

.. method:: ctx.rawmoments_from_factorial_moments(x, cf)

    where ``ctx`` is ``dec``, ``mpm``, or ``gmp``.


    Calculates the raw moments `\mu'_r` from the  factorial moments `\mu'_{[r]}` 

    .. math::  \mu'_r = \sum_{j=0}^r S(r,j) \mu'_{[j]},

    where `S(r,j)` is the Stirling number of the second kind (see :ref:`stirling2() <rst_mpm_stirling2>`).





Calculating the raw moments from the central moments
----------------------------------------------------------------------------------------

.. method:: ctx.rawmoments_from_centralmoments(central, raw)

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    Calculates the raw moments `\mu_r'` from the central moments `\mu_r` (see :cite:t:`Lee1992`, :cite:t:`Rinne2008`, p. 36): 

    .. math:: \mu_r' = \sum_{j=0}^r \binom{r}{j} \mu_{r-j} (\mu'_1)^{r}

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpr, ivr, ivc
        >>> ivr.dps = 25; ivr.pretty = True
        >>> ivr.exp([-inf,0])
        [0.0, 1.0]
        >>> ivr.exp([0,1])
        [1.0, 2.71828182845904523536028749558]






Calculating the raw moments from the cumulants 
----------------------------------------------------------------------------------------

.. method:: ctx.rawmoments_from_cumulants()

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Calculates the raw  moments `\mu_r'` from the cumulants `\kappa_r`  (see :cite:t:`Lee1992`, :cite:t:`Rinne2008`, p. 36): 

    .. math:: \mu_r' = \kappa_r + \sum_{j=1}^{r-1} \binom{r-1}{j-1} \mu'_{r-j} \kappa_j

    .. code-block:: pycon

        >>> from mpfunlab import dec, mpr, ivr, ivc
        >>> ivr.dps = 25; ivr.pretty = True
        >>> ivr.exp([-inf,0])
        [0.0, 1.0]
        >>> ivr.exp([0,1])
        [1.0, 2.71828182845904523536028749558]





Calculating the raw moments from the moment-generating function 
----------------------------------------------------------------------------------------

.. method:: ctx.rawmoments_from_mgf()

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.


    The moment-generating function is so called because if it exists on an open interval around t = 0, then it is the exponential generating function of the moments of the probability distribution: 

    .. math::  m_{n}=E\left(X^{n}\right)=M_{X}^{(n)}(0)=\left.{\frac {d^{n}M_{X}}{\mathrm{d} t^{n}}}\right|_{t=0}.

    That is, with n being a nonnegative integer, the nth moment about 0 is the nth derivative of the moment generating function, evaluated at t = 0. 



Calculating the raw moments from the characteristic function 
----------------------------------------------------------------------------------------

.. method:: ctx.rawmoments_from_cf()

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    Characteristic functions can also be used to find moments of a random variable. Provided that the nth moment exists, the characteristic function can be differentiated n times and

    .. math:: \operatorname {E} \left[X^{n}\right]=i^{-n}\,\varphi _{X}^{(n)}(0)=i^{-n}\,\left[{\frac {d^{n}}{\mathrm{d} t^{n}}}\varphi _{X}(t)\right]{t=0}\,\!




Calculating the raw moments from the probability-generating function 
----------------------------------------------------------------------------------------

.. method:: ctx.rawmoments_from_pgf()

    where ``ctx`` is ``ipm``, ``dec``, ``mpm``, or ``gmp``.

    The kth raw moment of X is given by
    
    .. math::  \operatorname {E} (X^{k})=\left(z{\frac {\partial }{\partial z}}\right)^{k}G(z){\Big |}_{z=1^{-}} 

    More generally, the kth factorial moment, 

    `\operatorname {E} (X(X-1)\cdots (X-k+1))` of `X` is given by
   
    .. math::  \operatorname {E} \left({\frac {X!}{(X-k)!}}\right)=G^{(k)}(1^{-}),\quad k\geq 0.





