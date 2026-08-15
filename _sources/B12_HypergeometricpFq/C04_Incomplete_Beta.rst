

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|


Incomplete beta functions
===============================================================================




Non-normalized lower incomplete beta function, `B_{\mathrm{lower}}(a,b;x)`
-------------------------------------------------------------------------------

.. method:: ctx.beta_lower(a, b, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Note: math53.beta3(a, b, x), ctxboost.IBetaNonNormalized(a, b, x)

    Returns the non-normalized incomplete beta function `\displaystyle B_x(a,b) =  B_{\mathrm{lower}}(a,b;x)  = \int_0^x t^{a-1} (1-t)^{b-1}  \, \mathrm{d}t, \,` for `a>0`, `b>0`, and `0 \leq x \leq 1`. 


    We also have `\displaystyle B_{\mathrm{lower}}(a,b;x)  = \frac{x^a}{a} {}_2F_1(a,1-b,a+1,x)`


    The function is undefined for nonpositive integer `a`.


    See also  Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun04a`, NIST :cite:p:`DLMFun04`,  BoostMath :cite:p:`BoostFun04`,  BoostMath :cite:p:`BoostFun05`, :cite:t:`Ehrhardt2018` (3.5.3.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Beta3(3.1, 0.5, 0.3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Beta3(3.4, '0.51', 0.3)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Beta3(3.1, 0.5, 0.3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Beta3(3.4, '0.51', 0.3)
        Gpr('5.3518479027559984754E-1')





|newpage|

.. _rst_mpm_ibeta: 

Normalized incomplete beta function, `I_{x}(a,b)`
---------------------------------------------------------------------------------------------------

.. method:: ctx.ibeta(a, b, x)

    where ``ctx`` is ``math53``, ``ctxboost``, ``ctxflint``.

    Returns the normalized incomplete beta function `\displaystyle I_x(a,b) = \frac{1}{B(a,b)}  \int_0^x t^{a-1} (1-t)^{b-1}  \, \mathrm{d}t, \,` for `a>0`, `b>0`, and `0 \leq x \leq 1`. 

    See also  Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun04b`, NIST :cite:p:`DLMFun04`,  BoostMath :cite:p:`BoostFun04`,  BoostMath :cite:p:`BoostFun05`, :cite:t:`Ehrhardt2018` (3.5.3.3), Flint :cite:p:`FlintFun01`, Flint :cite:p:`FlintFun02`.



    Returns the normalised incomplete beta function `I_x(a,b)` for `a>0`, `b>0`, and `0 \leq x \leq 1`.

    .. math :: I_x(a,b) = \frac{B_x(a,b)}{B(a,b)}, \quad B_x(a,b) = \int_0^x t^{a-1} (1-t)^{b-1} \mathrm{d}t.

    There are some special cases

    .. math :: I_0(a,b)=0, \quad I_1(a,b)=1, \quad I_x(a,1)=x^a,

    and the symmetry relation `I_x(a,b)=1-I_{1-x}(b,a)`, which is used for `x>a/(a+b)`.


    Computes the (lower) incomplete beta function, defined by
    `B(a,b;z) = \int_0^z t^{a-1} (1-t)^{b-1}`,
    optionally the regularized incomplete beta function
    `I(a,b;z) = B(a,b;z) / B(a,b;1)`.

    In general, the integral must be interpreted using analytic continuation.
    The precise definitions for all parameter values are

    .. math ::

        B(a,b;z) = \frac{z^a}{a} {}_2F_1(a, 1-b, a+1, z)

    .. math ::

        I(a,b;z) = \frac{\Gamma(a+b)}{\Gamma(b)} z^a {}_2{\widetilde F}_1(a, 1-b, a+1, z).

    Note that both functions with this definition are undefined
    for nonpositive integer *a*, and *I* is undefined for nonpositive integer
    `a + b`.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.IBeta(3.1, 0.5, 0.3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.IBeta(3.4, '0.51', 0.3)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.IBeta(3.1, 0.5, 0.3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.IBeta(3.4, '0.51', 0.3)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a = '10'; b = '7'; x = '0.1'
        >>> \mathrm{d}x = dec.ibeta(a, b, x); mx = mpm.ibeta(a, b, x); gx = gmp.ibeta(a, b, x)
        >>> fx = fpm.ibeta(a, b, x); ax = apm.ibeta(a, b, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 4.526064685000000000000000000000000000000E-7
        mpm: 4.526064685000000000000000000000000000000e-7
        gmp: 4.526064685000000000000000000000000000000E-07
        fpm: 4.52606468500001E-07
        apm: 4.526064685000000000000000000000000000000e-7 (9.07e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a = '10 + 0j'; b = '7 + 1j'; z = '0.1 + 03j'
        >>> \mathrm{d}z = dec.ibeta(a, b, z); mz = mpm.ibeta(a, b, z); gz = gmp.ibeta(a, b, z)
        >>> fz = fpm.ibeta(a, b, z); az = apm.ibeta(a, b, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -9.8493766176109694014E+11               - 4.2724835564105819032E+11j
        mpm: -9.8493766176109694014e+11               - 4.2724835564105819032e+11j
        gmp: -9.8493766176109694014E+11               - 4.2724835564105819032E+11j
        fpm: -9.84937661761097E+11                    - 4.27248355641058E+11j
        apm: -9.8493766176109694013e+11 (-4.728e-19%) - 4.2724835564105819032e+11 (-1.199e-18%)j






|newpage|

Derivative of the incomplete beta function
-------------------------------------------------------------------------------

.. method:: ctx.real_ibeta_prime(a, b, x)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the partial derivative with respect to `x` of the incomplete beta function `I_x(a,b)`. See also BoostMath :cite:p:`BoostFun06`. The function is defined as:

    .. math:: \frac{\partial}{\partial x}I_x(a,b) = \frac{x^{a-1} (1-x)^{b-1}}{B(a,b)}    .



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = '8.3'; b = '10.4'; x = '0.7'
        >>> \mathrm{d}x = dec.real_beta_derivative(a, b, x); mx = mpm.real_beta_derivative(a, b, x)
        >>> ix = ipm.real_beta_derivative(a, b, x); fx = fpm.real_beta_derivative(a, b, x)
        >>> gx = gmp.real_beta_derivative(a, b, x); ax = apm.real_beta_derivative(a, b, x)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  2.878999879544799566557091075303033672075E-1
        mpm:  2.878999879544799566557091075303033672075e-1
        ipm:  2.878999879544799566557091075303033672074e-1 (1.396e-37%)
        fpm:  2.87899987954481E-01
        gmp:  2.878999879544799566557091075303033672076E-01
        apm:  2.878999879544799566557091075303033672074e-1 (3.01e-37%)






|newpage|

Real non-normalized upper incomplete beta function, `B_{\mathrm{upper}}(a,b;x)`
---------------------------------------------------------------------------------------

.. method:: ctx.beta_upper(a, b, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Note: math53.betac(a, b, x), ctxboost.IBetacNonNormalized(a, b, x)


    Returns the non-normalized incomplete beta function `\displaystyle B_{1-x}(a,b) =  B_{\mathrm{upper}}(a,b;x)  = \int_x^1 t^{a-1} (1-t)^{b-1}  \, \mathrm{d}t, \,` for `a>0`, `b>0`, and `0 \leq x \leq 1`. 

    This can be generalized to complex `a, b` and `x` as `\displaystyle B_{\mathrm{upper}}(a,b;x) = B(a,b) - B_x(a,b)`.



    See also  Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun04a`, NIST :cite:p:`DLMFun04`,  BoostMath :cite:p:`BoostFun04`,  BoostMath :cite:p:`BoostFun05`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Betac(3.1, 0.5, 0.3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Betac(3.4, '0.51', 0.3)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Betac(3.1, 0.5, 0.3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Betac(3.4, '0.51', 0.3)
        Gpr('5.3518479027559984754E-1')






|newpage|

.. _rst_mpm_ibetac: 

Real normalized complementory incomplete beta function, `I_{1-x}(a,b)`
-------------------------------------------------------------------------------

.. method:: ctx.ibetac(a, b, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the complement of the normalized incomplete beta function `\displaystyle 1-I_x(a,b) = \frac{1}{B(a,b)} \int_x^1 t^{a-1} (1-t)^{b-1} \, \mathrm{d}t, \,` for `a>0`, `b>0`, and `0 \leq x \leq 1`. 

    See also  Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun04b`, NIST :cite:p:`DLMFun04`,  BoostMath :cite:p:`BoostFun04`,  BoostMath :cite:p:`BoostFun05`, Flint :cite:p:`FlintFun01`, Flint :cite:p:`FlintFun02`.



    Returns the non-normalised incomplete beta function `I_x(a,b)` for `a>0`, `b>0`, and `0 \leq x \leq 1`:

    .. math:: I_x(a,b) = \frac{B_x(a,b)}{B(a,b)}, \quad B_x(a,b) = \int_0^x t^{a-1} (1-t)^{b-1} \mathrm{d}t.


    .. math :: B_x(a,b) = \int_0^x t^{a-1} (1-t)^{b-1} \mathrm{d}t.

    There are some special cases

    .. math :: B_0(a,b)=0, \quad B_1(a,b)=B(a,b), \quad B_x(a,1)= \frac{x^a}{a}, \quad B_x(1,b)= \frac{1-(1-x)^b}{b},

    and the relation `B_{1-x}(a,b)=B(a,b)-B_x(b,a)`, which is used if `x>a/(a+b)`. When `a \leq 0` or `b \leq 0`, the Gauss hypergeometric function `{}_2F_2(\cdot)` is applied: If `a \neq 0` is not a negative integer, the result is

    .. math :: B_x(a,b)=\frac{x^a}{a} {}_2F_2(a,1-b,a+1,x), \quad -a \notin \mathbb{N}

    else if `b \neq 0`  is not a negative integer, the result is

    .. math :: B_x(a,b)=B(a,b) - \frac{(1-x)^b x^a}{b} {}_2F_2(1,a+b,b+1,1-x), \quad -b \notin \mathbb{N}.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.Ibetac(3.1, 0.5, 0.3)
        xreal('5.2359877559829887307E-1')
        >>> xreal.Ibetac(3.4, '0.51', 0.3)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.Ibetac(3.1, 0.5, 0.3)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.Ibetac(3.4, '0.51', 0.3)
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a = '10'; b = '7'; x = '0.1'
        >>> \mathrm{d}x = dec.beta3(a, b, x); mx = mpm.beta3(a, b, x); gx = gmp.beta3(a, b, x)
        >>> fx = fpm.beta3(a, b, x); ax = apm.beta3(a, b, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 5.651928927322677322677322677322677322677E-12
        mpm: 5.651928927322677322677322677322677322677e-12
        gmp: 5.651928927322677322677322677322677322677E-12
        fpm: 5.65192892732268E-12
        apm: 5.651928927322677322677322677322677322677e-12 (8.867e-39%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a = '10 + 0j'; b = '7 + 1j'; z = '0.1 + 03j'
        >>> \mathrm{d}z = dec.beta3(a, b, z); mz = mpm.beta3(a, b, z); gz = gmp.beta3(a, b, z)
        >>> fz = fpm.beta3(a, b, z); az = apm.beta3(a, b, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: -1.1121024734248714310E+7               + 6.3403283967816369421E+6j
        mpm: -1.1121024734248714310e+7               + 6.3403283967816369421e+6j
        gmp: -1.1121024734248714310E+07              + 6.3403283967816369421E+06j
        fpm: -1.11210247342487E+07                   + 6.34032839678164E+06j
        apm: -1.1121024734248714310e+7 (-4.472e-19%) + 6.3403283967816369421e+6 (5.603e-19%)j







|newpage|

.. _rst_mpm_real_ibeta_inv: 

Inverse of the real normalised incomplete beta function
-------------------------------------------------------------------------------

.. method:: ctx.real_ibeta_inv(a, b, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the inverse of the normalised incomplete beta function calculates `x` with `Q(a,x) = p`. The input parameters are `a>0`, `b>0`, `p \geq 0`. 
    
    
    See also  Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun04b`, NIST :cite:p:`DLMFun04`,  BoostMath :cite:p:`BoostFun04`,  BoostMath :cite:p:`BoostFun05`, :cite:t:`Ehrhardt2018` (3.5.3.5).



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = '8.3'; b = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_ibeta_inv(a, b, prob); mx = mpm.real_ibeta_inv(a, b, prob)
        >>> ix = ipm.real_ibeta_inv(a, b, prob); fx = fpm.real_ibeta_inv(a, b, prob)
        >>> gx = gmp.real_ibeta_inv(a, b, prob); ax = apm.real_ibeta_inv(a, b, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  5.031911971011064339721270139988401063680E-1
        mpm:  5.031911971011064339721270139988401063680e-1
        ipm:  5.031911971011064339721270139988401063680e-1 (1.141e-39%)
        fpm:  5.03191197101107E-01
        gmp:  5.031911971011064339721270139988401063680E-01
        apm:  5.031911971011064339721270139988401063680e-1 (1.141e-39%)

        >>> fx = fpm.real_ibeta_inv(a, b, prob); mpm.show([fx]) # boost
        fpm:  5.03191197101107E-01
        >>> fx = fpm.real_ibeta(a, b, fx); mpm.show([fx]) # boost
        fpm:  7.00000000000000E-01





|newpage|

.. _rst_mpm_real_ibetac_inv: 

Inverse of the real normalised complementary incomplete beta function
-------------------------------------------------------------------------------

.. method:: ctx.real_ibetac_inv(a, b, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the functional inverse of the complement of the upper normalized incomplete beta function calculates `x` 
    with `I_{1-x}(a,b) = p`. The input parameters are `a>0`, `b>0`, `p \geq 0, \leq 1`. 
    
    
    See also BoostMath :cite:p:`BoostFun05`, Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun05`, NIST :cite:p:`DLMFun04`.




    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = '8.3'; b = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_ibetac_inv(a, b, prob); mx = mpm.real_ibetac_inv(a, b, prob)
        >>> ix = ipm.real_ibetac_inv(a, b, prob); fx = fpm.real_ibetac_inv(a, b, prob)
        >>> gx = gmp.real_ibetac_inv(a, b, prob); ax = apm.real_ibetac_inv(a, b, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  3.815974615561709692459929991591600387688E-1
        mpm:  3.815974615561709692459929991591600387688e-1
        ipm:  3.815974615561709692459929991591600387688e-1 (7.521e-40%)
        fpm:  3.81597461556171E-01
        gmp:  3.815974615561709692459929991591600387688E-01
        apm:  3.815974615561709692459929991591600387688e-1 (7.521e-40%)

        >>> fx = fpm.real_ibetac_inv(a, b, prob); mpm.show([fx]) # boost
        fpm:  3.81597461556171E-01
        >>> fx = fpm.real_ibetac(a, b, fx); mpm.show([fx]) # boost
        fpm:  7.00000000000000E-01




|newpage|

Inverse (on parameter `a`) of the real normalised incomplete beta function
-------------------------------------------------------------------------------

.. method:: ctx.real_ibeta_inva(b, x, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the inverse of the normalized incomplete beta function with regard to parameter `a`, i.e. calculates `a` with `I_{x}(a,b) = p`. The input parameters are `x>0`, `b>0`, `p \geq 0, \leq 1`. 


    See also BoostMath :cite:p:`BoostFun05`, Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun05`, NIST :cite:p:`DLMFun04`.



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; b = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_ibeta_inva(b, x, prob); mx = mpm.real_ibeta_inva(b, x, prob)
        >>> ix = ipm.real_ibeta_inva(b, x, prob); fx = fpm.real_ibeta_inva(b, x, prob)
        >>> gx = gmp.real_ibeta_inva(b, x, prob); ax = apm.real_ibeta_inva(b, x, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  3.434764629588725033018175504012263060447E+0
        mpm:  3.434764629588725033018175504012263060447e+0
        ipm:  3.434764629588725033018175504012263060447e+0 (6.684e-40%)
        fpm:  3.43476462958872E+00
        gmp:  3.434764629588725033018175504012263060447E+00
        apm:  3.434764629588725033018175504012263060447e+0 (6.684e-40%)

        >>> fxa = fpm.real_ibeta_inva(b, x, prob); mpm.show([fxa]) # boost
        fpm:  3.43476462958872E+00
        >>> fx = fpm.real_ibeta(fxa, b, x); mpm.show([fx]) # boost
        fpm:  7.00000000000000E-01





|newpage|

Inverse (on parameter `a`) of the real normalised complementary incomplete beta function
---------------------------------------------------------------------------------------------

.. method:: ctx.real_ibetac_inva(b, x, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the inverse of the complement of the normalized incomplete beta function with regard to parameter `a`, i.e. calculates `a` with `I_{1-x}(a,b) = p`. The input parameters are `x>0`, `b>0`, `p \geq 0, \leq 1`. 


    See also BoostMath :cite:p:`BoostFun05`, Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun05`, NIST :cite:p:`DLMFun04`.



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; b = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_ibetac_inva(b, x, prob); mx = mpm.real_ibetac_inva(b, x, prob)
        >>> ix = ipm.real_ibetac_inva(b, x, prob); fx = fpm.real_ibetac_inva(b, x, prob) 
        >>> gx = gmp.real_ibetac_inva(b, x, prob); ax = apm.real_ibetac_inva(b, x, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  6.022956553898772220485519886468373977550E+0
        mpm:  6.022956553898772220485519886468373977550e+0
        ipm:  6.022956553898772220485519886468373977550e+0 (7.624e-40%)
        fpm:  6.02295655389877E+00
        gmp:  6.022956553898772220485519886468373977550E+00
        apm:  6.022956553898772220485519886468373977550e+0 (7.624e-40%)

        >>> fxa = fpm.real_ibetac_inva(b, x, prob); mpm.show([fxa]) # boost
        fpm:  6.02295655389877E+00
        >>> fx = fpm.real_ibetac(fxa, b, x); mpm.show([fx]) # boost
        fpm:  7.00000000000000E-01




|newpage|

.. _rst_mpm_real_ibeta_invb: 

Inverse (on parameter `b`) of the real normalised incomplete beta function
-------------------------------------------------------------------------------

.. method:: ctx.real_ibeta_invb(a, x, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Returns the inverse of the normalised incomplete beta function with regard to parameter `b`, i.e. calculates `a` with `Q(a,x) = p`. The input parameters are `a>0`, `b>0`, `p \geq 0`. 
    
    See also BoostMath :cite:p:`BoostFun05`, Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun05`, NIST :cite:p:`DLMFun04`.



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; a = '7.8'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_ibeta_invb(a, x, prob); mx = mpm.real_ibeta_invb(a, x, prob)
        >>> ix = ipm.real_ibeta_invb(a, x, prob); fx = fpm.real_ibeta_invb(a, x, prob)
        >>> gx = gmp.real_ibeta_invb(a, x, prob); ax = apm.real_ibeta_invb(a, x, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  2.200429591655521454353795394649129346838E+1
        mpm:  2.200429591655521454353795394649129346838e+1
        ipm:  2.200429591655521454353795394649129346838e+1 (8.347e-40%)
        fpm:  2.20042959165552E+01
        gmp:  2.200429591655521454353795394649129346838E+01
        apm:  2.200429591655521454353795394649129346838e+1 (8.347e-40%)

        >>> fxb = fpm.real_ibeta_invb(a, x, prob); mpm.show([fxb]) # boost
        fpm:  2.20042959165552E+01
        >>> fx = fpm.real_ibeta(a, fxb, x); mpm.show([fx]) # boost
        fpm:  7.00000000000000E-01




|newpage|

.. _rst_mpm_real_ibetac_invb: 

Inverse (on parameter `b`) of the real normalised complementary incomplete beta function
---------------------------------------------------------------------------------------------

.. method:: ctx.real_ibetac_invb(a, x, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Returns the inverse of the complement of the normalized incomplete beta function with regard to parameter `b`, i.e. calculates `b` with `I_{1-x}(a,b) = p`. The input parameters are `a>0`, `x>0`, `p \geq 0, \leq 1`. 

    See also BoostMath :cite:p:`BoostFun05`, Wikipedia :cite:p:`WikipediaFun04`, MathWorld :cite:p:`WolframFun05`, NIST :cite:p:`DLMFun04`.



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '0.3'; a = '7.8'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_ibetac_invb(a, x, prob); mx = mpm.real_ibetac_invb(a, x, prob)
        >>> ix = ipm.real_ibetac_invb(a, x, prob); fx = fpm.real_ibetac_invb(a, x, prob)
        >>> gx = gmp.real_ibetac_invb(a, x, prob); ax = apm.real_ibetac_invb(a, x, prob)
        >>> mpm.show([gx, fx, ax])
        dec:  1.403576906076099557240805034104910405788E+1
        mpm:  1.403576906076099557240805034104910405788e+1
        ipm:  1.403576906076099557240805034104910405788e+1 (6.543e-40%)
        fpm:  1.40357690607610E+01
        gmp:  1.403576906076099557240805034104910405788E+01
        apm:  1.403576906076099557240805034104910405788e+1 (6.543e-40%)

        >>> fxb = fpm.real_ibetac_invb(a, x, prob); mpm.show([fxb]) # boost
        fpm:  1.40357690607610E+01
        >>> fx = fpm.real_ibetac(a, fxb, x); mpm.show([fx]) # boost
        fpm:  6.99999999999999E-01







