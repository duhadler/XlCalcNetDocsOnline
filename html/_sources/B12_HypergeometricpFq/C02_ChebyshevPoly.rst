

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|

Chebyshev, Gegenbauer and Jacobi polynomials
===============================================================================


Chebyshev polynomial (or function) of the first kind, `T_n(x)`
-------------------------------------------------------------------------------

.. method:: ctx.chebyshev_t(n, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns `\displaystyle T_n(z) = {}_2F_1\left(-n,n,\frac{1}{2},\frac{1-z}{2}\right)`, the Chebyshev polynomial of the first kind.  The `T_n (x)` are orthogonal on the interval `(-1, 1)`, with respect to the weight function `w(x) = (1 - x^2 )^{-1/2}`. 

    For integer `n`, the following recursion can be used, with `T_n (x) = T_{-n} (x)`:

    .. math::
       :nowrap:

       \begin{eqnarray}
        T_0 (x) & = & 1 \\
        T_1 (x) & = & x \nonumber \\ 
        T_{n+1} (x)& = & 2x T_{n}(x) - T_{n-1}(x).  \nonumber
       \end{eqnarray}


    See also  Wikipedia :cite:p:`WikipediaFun136`, MathWorld :cite:p:`WolframFun136`, NIST :cite:p:`DLMFun134`,  BoostMath :cite:p:`BoostFun136`, :cite:t:`Ehrhardt2018` (3.7.1), Flint :cite:p:`FlintFun134`, Flint :cite:p:`FlintFun135`, Mpmath :cite:p:`MpmathFun136`, :cite:t:`Ehrhardt2018` (3.7.5).





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.ChebyshevT(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.ChebyshevT('6, 0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.ChebyshevT(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.ChebyshevT('6, 0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10'; x = '5.0'
        >>> \mathrm{d}x = dec.chebyt(n, x); mx = mpm.chebyt(n, x); gx = gmp.chebyt(n, x)
        >>> fx = fpm.chebyt(n, x); ax = apm.chebyt(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  4.517251249000000000000000000000000000000E+9
        mpm:  4.517251249000000000000000000000000000000e+9
        gmp:  4.517251249000000000000000000000000000000E+09
        fpm:  4.51725124900000E+09
        apm:  4.517251249000000000000000000000000000000e+9 (0.0%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.chebyt(n, z); mz = mpm.chebyt(n, z); gz = gmp.chebyt(n, z)
        >>> fz = fpm.chebyt(n, z); az = apm.chebyt(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.5445350751000000000E+10        - 1.6336798500000000000E+10j
        mpm: 1.5445350751000000000e+10        - 1.6336798500000000000e+10j
        gmp: 1.5445350751000000000E+10        - 1.6336798500000000000E+10j
        fpm: 1.54453507510000E+10             - 1.63367985000000E+10j
        apm: 1.5445350751000000000e+10 (0.0%) - 1.6336798500000000000e+10 (0.0%)j




|newpage|

Chebyshev polynomial of the second kind, `U_n(x)`
-------------------------------------------------------------------------------

.. method:: ctx.chebyshev_u(n, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns `\displaystyle U_n(z) = (n+1) {}_2F_1\left(-n,n+2,\frac{3}{2},\frac{1-z}{2}\right)`, the Chebyshev polynomial of the second kind. The `U_n (x)` are orthogonal on the interval `(-1, 1)`, with respect to the weight function `w(x) = (1 - x^2 )^{1/2}`.

    For integer `n`, the following recursion can be used, with  `U_{-1} (x) = 0` and `U_n (x) = -U_{-n-2} (x)`:

    .. math::
       :nowrap:

       \begin{eqnarray}
        U_0 (x) & = & 1 \\
        U_1 (x) & = & 2x \nonumber \\ 
        U_{n+1} (x)& = & 2x U_{n}(x) - U_{n-1}(x).  \nonumber
       \end{eqnarray}

    See also  Wikipedia :cite:p:`WikipediaFun136`, MathWorld :cite:p:`WolframFun137`, NIST :cite:p:`DLMFun134`, :cite:t:`Ehrhardt2018` (3.7.2), BoostMath :cite:p:`BoostFun136`, Flint :cite:p:`FlintFun134`, Flint :cite:p:`FlintFun135`, Mpmath :cite:p:`MpmathFun137`. 





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.ChebyshevU(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.ChebyshevU('6, 0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.ChebyshevU(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.ChebyshevU('6, 0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10'; x = '5.0'
        >>> \mathrm{d}x = dec.chebyu(n, x); mx = mpm.chebyu(n, x); gx = gmp.chebyu(n, x)
        >>> fx = fpm.chebyu(n, x); ax = apm.chebyu(n, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  9.127651499000000000000000000000000000000E+9
        mpm:  9.127651499000000000000000000000000000000e+9
        gmp:  9.127651499000000000000000000000000000000E+09
        fpm:  9.12765149900000E+09
        apm:  9.127651499000000000000000000000000000000e+9 (0.0%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.chebyu(n, z); mz = mpm.chebyu(n, z); gz = gmp.chebyu(n, z)
        >>> fz = fpm.chebyu(n, z); az = apm.chebyu(n, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 3.0778307711000000000E+10        - 3.2988132600000000000E+10j
        mpm: 3.0778307711000000000e+10        - 3.2988132600000000000e+10j
        gmp: 3.0778307711000000000E+10        - 3.2988132600000000000E+10j
        fpm: 3.07783077110000E+10             - 3.29881326000000E+10j
        apm: 3.0778307711000000000e+10 (0.0%) - 3.2988132600000000000e+10 (0.0%)j







|newpage|


Chebyshev polynomials of the third kind, `V_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.chebyshev_v(n,x) 

    Returns `\displaystyle V_n(x)`, the Chebyshev polynomial of the first kind.  The `V_n (x)` are orthogonal on the interval `(-1, 1)`, with respect to the weight function `w(x) = (1 + x^2 )^{1/2}  (1 - x)^{-1/2}`. 



    The function can also be calculated as `\displaystyle V_n(x) = (-1)^n (2n+1) {}_2F_1\left(-n,n+1,\frac{3}{2},\frac{1+x}{2}\right)`, which allows for complex `n` and `x`.


    We also have `\displaystyle V_n(x) = \sqrt{\frac{2}{1+x}} T_{2n+1} \left( \sqrt{\frac{x+1}{2}} \right)` for `x \ge 0`, and `V_n (x) = (-1)^n W_{n}(-x)` for `x < 0`. 


    For integer `n` and real `x`, the following recursion can be used, with `V_{-n-1}(x) = V_{n}(x)`:

    .. math::
       :nowrap:

       \begin{eqnarray}
        V_0 (x) & = & 1 \\
        V_1 (x) & = & 2x-1 \nonumber \\ 
        V_{n+1} (x)& = & 2x V_{n}(x) - V_{n-1}(x).  \nonumber
       \end{eqnarray}


    See also  Wikipedia :cite:p:`WikipediaFun136`, MathWorld :cite:p:`WolframFun136`, NIST :cite:p:`DLMFun134`, :cite:t:`Ehrhardt2018` (3.7.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.ChebyshevV(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.ChebyshevV('6, 0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.ChebyshevV(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.ChebyshevV('6, 0.51')
        Gpr('5.3518479027559984754E-1')





|newpage|

Chebyshev polynomials of the fourth kind, `W_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.chebyshev_w(n,x)

    Returns `\displaystyle W_k(z)`, the Chebyshev polynomial of the fourth kind of degree `n \ge 0`.  The `W_n (x)` are orthogonal on the interval `(-1, 1)`, with respect to the weight function `w(x) = (1 - x)^{1/2} (1 + x^2 )^{-1/2}`. 


    The function can also be calculated as `\displaystyle W_n(z) = (-1)^n {}_2F_1\left(-n,n+1,\frac{1}{2},\frac{1+x}{2}\right)`, which allows for complex `n` and `x`.


    We also have `\displaystyle W_n(x) = U_{2n} \left( \sqrt{\frac{x+1}{2}} \right)` for `x \ge 0`, and `W_n (x) = (-1)^n V_{n}(-x)` for `x < 0`. 



    For integer `n`, the following recursion can be used, with `W_{-n-1}(x) = -W_{n}(x)`:

    .. math::
       :nowrap:

       \begin{eqnarray}
        W_0 (x) & = & 1 \\
        W_1 (x) & = & 2x+1 \nonumber \\ 
        W_{n+1} (x)& = & 2x W_{n}(x) - W_{n-1}(x).  \nonumber
       \end{eqnarray}


    See also  Wikipedia :cite:p:`WikipediaFun136`, MathWorld :cite:p:`WolframFun136`, NIST :cite:p:`DLMFun134`, :cite:t:`Ehrhardt2018` (3.7.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.ChebyshevW(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.ChebyshevW('6, 0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.ChebyshevW(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.ChebyshevW('6, 0.51')
        Gpr('5.3518479027559984754E-1')







|newpage|

Gegenbauer (ultraspherical) polynomial, `C_{n}^{\alpha}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.gegenbauer_c(n, alpha, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Returns `\displaystyle C_n^{(a)}(z)`, the Gegenbauer polynomial of degree `n` with parameter `a`. The Gegenbauer polynomials are orthogonal on the interval `(-1, 1)`, with respect to the weight function `w(x) = (1 - x^2)^{a-1/2}` .

    If `a \neq 0` the function uses the recurrence formulas

    .. math::
       :nowrap:

       \begin{eqnarray}
        C^{(a)}_0 (x) & = & 1 \\
        C^{(a)}_1 (x) & = & 2ax \nonumber \\ 
        nC^{(a)}_n (x)& = & 2(n+a-1)x C^{(a)}_{n-1}(x) - (n+2a-2)  C^{(a)}_{n-2}(x).  \nonumber
       \end{eqnarray}

    For `a = 0` the result can be expressed in Chebyshev polynomials: `\displaystyle C^{(0)}_0 (x) =  1, \quad  C^{(0)}_n (x) =  2/n T_n(x)`.

    See also  Wikipedia :cite:p:`WikipediaFun139`, MathWorld :cite:p:`WolframFun139`, NIST :cite:p:`DLMFun134`,  BoostMath :cite:p:`BoostFun139`, :cite:t:`Ehrhardt2018` (3.7.6), Flint :cite:p:`FlintFun134`, Flint :cite:p:`FlintFun135`, Mpmath :cite:p:`MpmathFun139`. 


    The function can also be expressed as

    .. math ::

        C_n^{a}(z)=\frac{(2 a)_n}{\Gamma(n+1)} {}_2F_1\left(-n,2 a+n,a+\frac{1}{2},\frac{1-z}{2}\right).

    For nonnegative integer *n*, this is a polynomial in *a* and *z*,
    even when the parameters are such that the hypergeometric series
    is undefined. In such cases, the polynomial is evaluated using
    direct methods.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.GegenbauerC(3, 2, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.GegenbauerC('6, 2, 0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.GegenbauerC(3, 2, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.GegenbauerC('6, 2, 0.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10' ; a = '7.0'; x = '5.0'
        >>> \mathrm{d}x = dec.gegenbauer(n, a, x); mx = mpm.gegenbauer(n, a, x); gx = gmp.gegenbauer(n, a, x)
        >>> fx = fpm.gegenbauer(n, a, x); ax = apm.gegenbauer(n, a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  7.565898478553800000000000000000000000000E+13
        mpm:  7.565898478553800000000000000000000000000e+13
        gmp:  7.565898478553800000000000000000000000000E+13
        fpm:  7.56589847855380E+13
        apm:  7.565898478553800000000000000000000000000e+13 (2.135e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; a = '7.0 + 1j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.gegenbauer(n, a, z); mz = mpm.gegenbauer(n, a, z); gz = gmp.gegenbauer(n, a, z)
        >>> fz = fpm.gegenbauer(n, a, z); az = apm.gegenbauer(n, a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 3.8222147440285373854E+14              + 3.3043282427731541887E+13j
        mpm: 3.8222147440285373854e+14              + 3.3043282427731541887e+13j
        gmp: 3.8222147440285373854E+14              + 3.3043282427731541887E+13j
        fpm: 3.82221474402854E+14                   + 3.30432824277315E+13j
        apm: 3.8222147440285373854e+14 (6.238e-20%) + 3.3043282427731541887e+13 (2.255e-19%)j









|newpage|

Jacobi polynomials, `P_{n}^{(a, b)}`
-------------------------------------------------------------------------------

.. method:: ctx.jacobi_p(n, a, b, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns `\displaystyle P_n^{(a,b)}(x)`, the Jacobi polynomial of degree `n \geq 0` with parameters `(a, b)`, where `a, b` should be greater than `-1`, and `a + b` must not be an integer less than `-1`. Jacobi polynomials are orthogonal on the interval `(-1, 1)`, with respect to the weight function `w(x) = (1 - x)^a (1 + x)^b`, if `a, b` are greater than `-1`.

    The cases `n \leq 1` are computed with the explicit formulas

    .. math:: P^{(a,b)}_0= 1, \quad   2P^{(a,b)}_1= (a - b) + (a + b + 2)x,

    and for `n > 1` there are the somewhat complicated recurrence relations

    .. math::
       :nowrap:

       \begin{eqnarray}
        P^{(a,b)}_{n+1} & = &  (A_n x + B_n)P^{(a,b)}_n - C_n P^{(a,b)}_{n-1} \\
        A_n & = & \frac{(2n + a + b + 1)(2n + a + b + 2)}{2(n + 1)(n + a + b + 1)}  \nonumber  \\
        B_n & = & \frac{(a^2 - b^2 )(2n + a + b + 1)}{2(n + 1)(n + a + b + 1)(2n + a + b)}  \nonumber \\ 
        C_n & = & \frac{(n + a)(n + b)(2n + a + b + 2)}{(n + 1)(n + a + b + 1)(2n + a + b)} .  \nonumber
       \end{eqnarray}


    See also  Wikipedia :cite:p:`WikipediaFun140`, MathWorld :cite:p:`WolframFun140`, NIST :cite:p:`DLMFun134`,  BoostMath :cite:p:`BoostFun140`, :cite:t:`Ehrhardt2018` (3.7.9), Mpmath :cite:p:`MpmathFun140`. 



    The function can also be expressed as

    .. math ::

        P_n^{(a,b)}(x)=\frac{(a+1)_n}{\Gamma(n+1)} {}_2F_1\left(-n,n+a+b+1,a+1,\frac{1-x}{2}\right).

    For nonnegative integer *n*, this is a polynomial in *a*, *b* and *z*,
    even when the parameters are such that the hypergeometric series
    is undefined. In such cases, the polynomial is evaluated using
    direct methods.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiP(2, 3, 2, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiP('6, 2, 0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiP(2, 3, 2, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiP('6, 2, 0.51')
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; n = '10' ; a = '7.0'; b = '8.0'; x = '5.0'
        >>> \mathrm{d}x = dec.jacobi(n, a, b, x); mx = mpm.jacobi(n, a, b, x); gx = gmp.jacobi(n, a, b, x)
        >>> fx = fpm.jacobi(n, a, b, x); ax = apm.jacobi(n, a, b, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  1.566492891288000000000000000000000000000E+12
        mpm:  1.566492891288000000000000000000000000000e+12
        gmp:  1.566492891288000000000000000000000000000E+12
        fpm:  1.56649289128800E+12
        apm:  1.566492891288000000000000000000000000000e+12 (1.611e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; n = '10'; a = '7.0 + 1j'; b = '8.0 + 2j'; z = '5.0 + 3j'
        >>> \mathrm{d}z = dec.jacobi(n, a, b, z); mz = mpm.jacobi(n, a, b, z); gz = gmp.jacobi(n, a, b, z)
        >>> fz = fpm.jacobi(n, a, b, z); az = apm.jacobi(n, a, b, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 7.8001821589253876064E+12              + 1.0625055373536412146E+12j
        mpm: 7.8001821589253876064e+12              + 1.0625055373536412146e+12j
        gmp: 7.8001821589253876064E+12              + 1.0625055373536412146E+12j
        fpm: 7.80018215892539E+12                   + 1.06250553735364E+12j
        apm: 7.8001821589253876064e+12 (4.776e-20%) + 1.0625055373536412146e+12 (1.315e-19%)j






|newpage|

Zernike radial polynomials `R_n^m(r)`
-------------------------------------------------------------------------------

.. method:: math53.zernike_r(n,m,r)

    Returns the Zernike radial polynomial `R_n^m(r)`, with  `r \ge 0`, and  `n \ge m \ge 0`, `n-m` even, zero otherwise. The orthogonality relation is

    .. math :: \int_0^1 R_n^m(r) R_{n'}^m(r) r  \, \mathrm{d}r = \frac{1}{2(n+1)} \delta_{nn'}.

    .. math :: R_n^m(r) = (-1)^{(n-m)/2} r^m P_{(n-m)/2}^{(m,0)}(1-2r^2) = r^m P_{(n-m)/2}^{(0,m)}(2r^2-1).


    See also: http://mathworld.wolfram.com/ZernikePolynomial.html

    See also https://en.wikipedia.org/wiki/Zernike_polynomials

    See also   :cite:t:`Ehrhardt2018` (3.7.20).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.ZernikeR(4, 5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.ZernikeR(4, 5,'0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.ZernikeR(4, 5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.ZernikeR(4, 5,'0.51')
        Gpr('5.3518479027559984754E-1')






