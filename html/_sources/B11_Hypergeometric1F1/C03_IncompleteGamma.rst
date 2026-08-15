

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Incomplete gamma functions
===============================================================================


.. _rst_mpm_gamma_p: 

Lower normalized incomplete gamma function, `P(a,x)`
---------------------------------------------------------------------------------------------------

.. method:: ctx.gamma_p(a, x)

    where ``ctx`` is ``math53``, ``ctxboost``, ``ctxflint``.

    Note: math53.incGammaP(a, x)

    Returns the lower normalized incomplete gamma function `\displaystyle P(a,x)=\frac{1}{\Gamma(a)} \int_0^x t^{a-1} e^{-t} \, \mathrm{d}t, \,` for `a \geq 0` and `x \geq 0`.

    See also  Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun01b`, NIST :cite:p:`DLMFun01`,  BoostMath :cite:p:`BoostFun01`, :cite:t:`Ehrhardt2018` (3.5.2.1), Flint :cite:p:`FlintFun01`, Flint :cite:p:`FlintFun02`, Mpmath :cite:p:`MpmathFun01`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.IncGammaP(3.1, 1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.IncGammaP(3.4, '1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.IncGammaP(3.1, 1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.IncGammaP(3.4, '1.51')
        Gpr('5.3518479027559984754E-1')


    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a= 10; x = 30
        >>> \mathrm{d}x = dec.gamma_p(a, x); mx = mpm.gamma_p(a, x); gx = gmp.gamma_p(a, x)
        >>> fx = fpm.gamma_p(a, x); ax = apm.gamma_p(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  9.999928782491371844229083533391656597094E-1
        mpm:  9.999928782491371844229083533391656597094e-1
        gmp:  9.999928782491371844229083533391656597094E-01
        fpm:  9.99992878249137E-01
        apm:  9.999928782491371844229083533391656597094e-1 (5.74e-40%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a= '10 + 3j'; z = '3 + 2j'
        >>> \mathrm{d}z = dec.gamma_p(a, z); mz = mpm.gamma_p(a, z); gz = gmp.gamma_p(a, z)
        >>> fz = fpm.gamma_p(a, z); az = apm.gamma_p(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.3425210462984343451E-3              + 1.2911646547819672560E-3j
        mpm: 1.3425210462984343451e-3              + 1.2911646547819672560e-3j
        gmp: 1.3425210462984343451E-03             + 1.2911646547819672560E-03j
        fpm: 1.34252104629843E-03                  + 1.29116465478197E-03j
        apm: 1.3425210462984343451e-3 (3.697e-19%) + 1.2911646547819672560e-3 (3.203e-19%)j





|newpage|


.. _rst_mpm_gamma_q: 

Upper normalized incomplete gamma functions , `Q(a,x)`
---------------------------------------------------------------------------------------------------

.. method:: ctx.gamma_q(a, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Note: math53.incGammaQ(a, x)

    Returns the upper normalized incomplete gamma function `\displaystyle Q(a,x)=\frac{1}{\Gamma(a)} \int_x^{\infty} t^{a-1} e^{-t} \, \mathrm{d}t, \,` for `a \geq 0` and `x \geq 0`.

    See also  Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun01b`, NIST :cite:p:`DLMFun01`,  BoostMath :cite:p:`BoostFun01`, :cite:t:`Ehrhardt2018` (3.5.2.1), Flint :cite:p:`FlintFun01`, Flint :cite:p:`FlintFun02`, Mpmath :cite:p:`MpmathFun01`.



    The normalised incomplete gamma function `Q(a,x)` is defined as

    .. math :: Q(a,x)=\frac{1}{\Gamma(a)} \int_x^{\infty} t^{a-1} e^{-t}\mathrm{d}t

    for `a \geq 0` and `x \geq 0`.


    If *regularized* is 0, computes the upper incomplete gamma function
    `\Gamma(s,z)`.

    If *regularized* is 1, computes the regularized upper incomplete
    gamma function `Q(s,z) = \Gamma(s,z) / \Gamma(s)`.

    If *regularized* is 2, computes the generalized exponential integral
    `z^{-s} \Gamma(s,z) = E_{1-s}(z)` .

    The different methods respectively implement the formulas

    .. math ::

        \Gamma(s,z) = e^{-z} U(1-s,1-s,z)

    .. math ::

        \Gamma(s,z) = \Gamma(s) - \frac{z^s}{s} {}_1F_1(s, s+1, -z)

    .. math ::

        \Gamma(s,z) = \Gamma(s) - \frac{z^s e^{-z}}{s} {}_1F_1(1, s+1, z)

    .. math ::

        \Gamma(s,z) = \frac{(-1)^n}{n!} (\psi(n+1) - \log(z))
                    + \frac{(-1)^n}{(n+1)!} z \, {}_2F_2(1,1,2,2+n,-z)
                    - z^{-n} \sum_{k=0}^{n-1} \frac{(-z)^k}{(k-n) k!},
                    \quad n = -s \in \mathbb{Z}_{\ge 0}

    and an automatic algorithm choice. The automatic version also handles
    other special input such as `z = 0` and `s = 1, 2, 3`.
    The *singular* version evaluates the finite sum directly and therefore
    assumes that *s* is not too large.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.IncGammaQ(3.1, 1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.IncGammaQ(3.4, '1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.IncGammaQ(3.1, 1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.IncGammaQ(3.4, '1.51')
        Gpr('5.3518479027559984754E-1')




    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a= 10; x = 30
        >>> \mathrm{d}x = dec.gamma_q(a, x); mx = mpm.gamma_q(a, x); gx = gmp.gamma_q(a, x)
        >>> fx = fpm.gamma_q(a, x); ax = apm.gamma_q(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  7.121750862815577091646660834340290593535E-6
        mpm:  7.121750862815577091646660834340290593535e-6
        gmp:  7.121750862815577091646660834340290593535E-06
        fpm:  7.12175086281558E-06
        apm:  7.121750862815577091646660834340290595390e-6 (4.704e-35%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a= '10 + 3j'; z = '3 + 2j'
        >>> \mathrm{d}z = dec.gamma_q(a, z); mz = mpm.gamma_q(a, z); gz = gmp.gamma_q(a, z)
        >>> fz = fpm.gamma_q(a, z); az = apm.gamma_q(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 9.9865747895370156565E-1              - 1.2911646547819672560E-3j
        mpm: 9.9865747895370156565e-1              - 1.2911646547819672560e-3j
        gmp: 9.9865747895370156565E-01             - 1.2911646547819672560E-03j
        fpm: 9.98657478953702E-01                  - 1.29116465478197E-03j
        apm: 9.9865747895370156566e-1 (4.241e-20%) - 1.2911646547819672560e-3 (-3.844e-19%)j




|newpage|

Lower non-normalized incomplete gamma function, `\gamma(a,x)`
-------------------------------------------------------------------------------

.. method:: ctx.gamma_lower(a, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Note: math53.incgammaL(a, x), ctxboost.TgammaLower(a, x)

    Returns the real lower non-normalized incomplete gamma function `\displaystyle \gamma(a,x)= \int_0^x t^{a-1} e^{-t} \, \mathrm{d}t, \,` for `a \geq 0` and `x \geq 0`.

    See also  Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun01a`, NIST :cite:p:`DLMFun01`,  BoostMath :cite:p:`BoostFun01`, :cite:t:`Ehrhardt2018` (3.5.2.2), Flint :cite:p:`FlintFun01`, Flint :cite:p:`FlintFun02`, Mpmath :cite:p:`MpmathFun01`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.IncgammaL(3.1, 1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.IncgammaL(3.4, '1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.IncgammaL(3.1, 1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.IncgammaL(3.4, '1.51')
        Gpr('5.3518479027559984754E-1')





|newpage|

Upper non-normalized incomplete gamma function, `\Gamma(a,x)`
-------------------------------------------------------------------------------

.. method:: ctx.gamma_upper(a, x)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Note: math53.incGammaU(a, x)

    Returns the real upper non-normalized incomplete gamma function `\displaystyle \Gamma(a,x) = \int_x^{\infty} t^{a-1} e^{-t} \, \mathrm{d}t, \,` for `a \geq 0` and `x \geq 0`.

    See also  Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun01a`, NIST :cite:p:`DLMFun01`,  BoostMath :cite:p:`BoostFun01`, :cite:t:`Ehrhardt2018` (3.5.2.2), Flint :cite:p:`FlintFun01`, Flint :cite:p:`FlintFun02`, Mpmath :cite:p:`MpmathFun01`. 


    The function is defined as:

    .. math:: \Gamma(a,x) = \int_x^{\infty} t^{a-1} e^{-t}\mathrm{d}t

    for `a \geq 0` and `x \geq 0`.



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.IncGammaU(3.1, 1.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.IncGammaU(3.4, '1.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.IncGammaU(3.1, 1.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.IncGammaU(3.4, '1.51')
        Gpr('5.3518479027559984754E-1')



    An example with real input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; a= 10; x = 30
        >>> \mathrm{d}x = dec.gamma_upper(a, x); mx = mpm.gamma_upper(a, x); gx = gmp.gamma_upper(a, x)
        >>> fx = fpm.gamma_upper(a, x); ax = apm.gamma_upper(a, x)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
        dec:  2.584340953098516615016740283565404650582E+0
        mpm:  2.584340953098516615016740283565404650582e+0
        gmp:  2.584340953098516615016740283565404650582E+00
        fpm:  2.58434095309852E+00
        apm:  2.584340953098516615016740283565404651198e+0 (4.411e-35%)


    An example with complex input:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; a= '10 + 3j'; z = '3 + 2j'
        >>> \mathrm{d}z = dec.gamma_upper(a, z); mz = mpm.gamma_upper(a, z); gz = gmp.gamma_upper(a, z)
        >>> fz = fpm.gamma_upper(a, z); az = apm.gamma_upper(a, z)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
        dec: 1.9750505254998015902E+5              + 1.1284570922907013455E+5j
        mpm: 1.9750505254998015902e+5              + 1.1284570922907013455e+5j
        gmp: 1.9750505254998015902E+05             + 1.1284570922907013455E+05j
        fpm: 1.97505052549980E+05                  + 1.12845709229070E+05j
        apm: 1.9750505254998015902e+5 (5.621e-20%) + 1.1284570922907013455e+5 (9.838e-20%)j





|newpage|

.. _rst_mpm_gamma_tricomi: 

Tricomi's entire incomplete gamma function: `\gamma^*(a,x)`
-------------------------------------------------------------------------------

.. method:: ctxflint.gamma_tricomi(a, z, len)


Returns Tricomi's entire incomplete gamma function `\gamma^*(a,x)`.

See also: Flint :cite:p:`FlintFun01`, Flint :cite:p:`FlintFun02`.

This routine returns Tricomi's incomplete gamma function `\gamma^*`, defined as

.. math :: \gamma^*(a,x)=e^{-x} \frac{M(1,a+1,x)}{\Gamma(a+1)}

Special cases are `\gamma^*(0,x)=1, \gamma^*(a,0)=1/\Gamma(a+1)`, and `\gamma^*(-n,x)=x^n`, if `-n` is a negative integer. Otherwise there are the following relations to the other incomplete functions:

.. math :: \gamma^*(a,x)=\frac{x^{-a}}{\Gamma(a)}\gamma(a,x)=x^{-a} P(a,x).




An example with real input:

.. code-block:: pycon

    >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
    >>> mpm.dps = 40; a= 10; x = 30
    >>> \mathrm{d}x = dec.gamma_tricomi(a, x); mx = mpm.gamma_tricomi(a, x); gx = gmp.gamma_tricomi(a, x)
    >>> fx = fpm.gamma_tricomi(a, x); ax = apm.gamma_tricomi(a, x)
    >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
    dec:  1.693496720095407516508168391232985587748E-15
    mpm:  1.693496720095407516508168391232985587748e-15
    gmp:  1.693496720095407516508168391232985587748E-15
    fpm:  1.69349672009541E-15
    apm:  1.693496720095407516508168391232985587748e-15 (4.214e-39%)


An example with complex input:

.. code-block:: pycon

    >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
    >>> mpm.dps = 20; a= '10 + 3j'; z = '3 + 2j'
    >>> \mathrm{d}z = dec.gamma_tricomi(a, z); mz = mpm.gamma_tricomi(a, z); gz = gmp.gamma_tricomi(a, z)
    >>> fz = fpm.gamma_tricomi(a, z); az = apm.gamma_tricomi(a, z)
    >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
    dec: -2.6190844813399921279E-8               - 1.3081710985777839884E-8j
    mpm: -2.6190844813399921279e-8               - 1.3081710985777839884e-8j
    gmp: -2.6190844813399921279E-08              - 1.3081710985777839884E-08j
    fpm: -2.61908448133999E-08                   - 1.30817109857778E-08j
    apm: -2.6190844813399921279e-8 (-1.446e-18%) - 1.3081710985777839884e-8 (-2.75e-18%)j





|newpage|

.. _rst_mpm_gamma_derivative: 

Derivative of the incomplete gamma function
-------------------------------------------------------------------------------

.. method:: ctx.gamma_p_prime(a, z)



Returns the partial derivative with respect to `x` of the incomplete gamma function `P(a,x)`:

The partial derivative with respect to `x` of the incomplete gamma function `P(a,x)` is defined as:

.. math :: \frac{\partial}{\partial x}P(a,x) = \frac{e^{-x} x^{a-1}}{\Gamma(a)}.




An example with real input:

.. code-block:: pycon

    >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
    >>> mpm.dps = 40; a= 10; x = 30
    >>> \mathrm{d}x = dec.gamma_derivative(a, x); mx = mpm.gamma_derivative(a, x); gx = gmp.gamma_derivative(a, x)
    >>> fx = fpm.gamma_derivative(a, x); ax = apm.gamma_derivative(a, x)
    >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax])
    dec:  5.075674958545005421862828639020146738895E-6
    mpm:  5.075674958545005421862828639020146738895e-6
    gmp:  5.075674958545005421862828639020146738895E-06
    fpm:  5.07567495854500E-06
    apm:  5.075674958545005421862828639020146738895e-6 (8.628e-40%)


An example with complex input:

.. code-block:: pycon

    >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
    >>> mpm.dps = 20; a= '10 + 3j'; z = '3 + 2j'
    >>> \mathrm{d}z = dec.gamma_derivative(a, z); mz = mpm.gamma_derivative(a, z); gz = gmp.gamma_derivative(a, z)
    >>> fz = fpm.gamma_derivative(a, z); az = apm.gamma_derivative(a, z)
    >>> mpm.show([\mathrm{d}z, mz, gz, fz, az],  aligned=True)
    dec: 3.6415328970281122640E-3              + 1.2712795456433263145E-3j
    mpm: 3.6415328970281122640e-3              + 1.2712795456433263145e-3j
    gmp: 3.6415328970281122640E-03             + 1.2712795456433263145E-03j
    fpm: 3.64153289702811E-03                  + 1.27127954564333E-03j
    apm: 3.6415328970281122640e-3 (2.272e-19%) + 1.2712795456433263145e-3 (5.856e-19%)j



    


.. _rst_mpm_real_gamma_p_inv: 

Inverse of the real lower normalised incomplete gamma function, `P^{-1}(a, q)`
----------------------------------------------------------------------------------------

.. method:: ctx.real_gamma_p_inv(a, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Note: math53.incGammaPInv(a, p)

    Returns `P^{-1}(a,p)`, the functional inverse of the real lower normalized incomplete gamma function, i.e. the function calculates `x` with `P(a,x) = p` where `a>0` and  `0<p<1`.

    See also   BoostMath :cite:p:`BoostFun02`,  Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun02`, NIST :cite:p:`DLMFun01`, :cite:t:`Ehrhardt2018` (3.5.2.4).


    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_gamma_p_inv(a, prob); mx = mpm.real_gamma_p_inv(a, prob)
        >>> ix = ipm.real_gamma_p_inv(a, prob); fx = fpm.real_gamma_p_inv(a, prob)
        >>> gx = gmp.real_gamma_p_inv(a, prob); ax = apm.real_gamma_p_inv(a, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  1.182065312732400158230548049644312582083E+1
        mpm:  1.182065312732400158230548049644312582083e+1
        ipm:  1.182065312732400158230548049644312582083e+1 (7.769e-40%)
        fpm:  1.18206531273240E+01
        gmp:  1.182065312732400158230548049644312582083E+01
        apm:  1.182065312732400158230548049644312582083e+1 (7.769e-40%)





.. _rst_mpm_real_gamma_q_inv: 

Inverse of the real upper normalised incomplete gamma function, `Q^{-1}(a, q)`
-----------------------------------------------------------------------------------------

.. method:: ctx.real_gamma_q_inv(a, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Note: math53.incGammaQInv(a, q)


    Returns `Q^{-1}(a,q)`, the functional inverse of the real upper normalized incomplete gamma function, i.e. the function calculates `x` with `Q(a,x) = q` where `a>0` and  `0<q<1`.

    See also   BoostMath :cite:p:`BoostFun02`,  Wikipedia :cite:p:`WikipediaFun01`, MathWorld :cite:p:`WolframFun02`, NIST :cite:p:`DLMFun01`, :cite:t:`Ehrhardt2018` (3.5.2.4).



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_gamma_q_inv(a, prob); mx = mpm.real_gamma_q_inv(a, prob)
        >>> ix = ipm.real_gamma_q_inv(a, prob); fx = fpm.real_gamma_q_inv(a, prob)
        >>> gx = gmp.real_gamma_q_inv(a, prob); ax = apm.real_gamma_q_inv(a, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  8.499407282754637944300146456267086376957E+0
        mpm:  8.499407282754637944300146456267086376957e+0
        ipm:  8.499407282754637944300146456267086376957e+0 (1.08e-39%)
        fpm:  8.49940728275464E+00
        gmp:  8.499407282754637944300146456267086376957E+00
        apm:  8.499407282754637944300146456267086376957e+0 (1.08e-39%)








.. _rst_mpm_real_gamma_p_inva: 

Inverse (on parameter `a`) of the real lower normalised incomplete gamma function
---------------------------------------------------------------------------------------------------

.. method:: ctx.real_gamma_p_inva(x, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Note: math53.incGammaPInva(x, p)

    Returns the functional inverse (on parameter a) of the lower normalized incomplete gamma function `P(a,x)`, i.e. the function calculates `a` with `P(a,x) = p` where `x>0` and  `0<p<1`.

    See also  BoostMath :cite:p:`BoostFun02`,  Wikipedia :cite:p:`WikipediaFun01`, NIST :cite:p:`DLMFun01`

    .. code-block:: python

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_gamma_p_inva(x, prob); mx = mpm.real_gamma_p_inva(x, prob)
        >>> ix = ipm.real_gamma_p_inva(x, prob); fx = fpm.real_gamma_p_inva(x, prob)
        >>> gx = gmp.real_gamma_p_inva(x, prob); ax = apm.real_gamma_p_inva(x, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  9.091223780657490024395740214633198685411E+0
        mpm:  9.091223780657490024395740214633198685411e+0
        ipm:  9.091223780657490024395740214633198685411e+0 (1.01e-39%)
        fpm:  9.09122378065749E+00
        gmp:  9.091223780657490024395740214633198685411E+00
        apm:  9.091223780657490024395740214633198685411e+0 (1.01e-39%)






.. _rst_mpm_real_gamma_q_inva: 

Inverse (on parameter `a`) of the real upper normalised incomplete gamma function
-----------------------------------------------------------------------------------------

.. method:: ctx.real_gamma_q_inva(x, q)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.

    Note: math53.incGammaQInva(x, p)


    Returns the functional inverse (on parameter a) of the upper normalized incomplete gamma function `Q(a,x)`, i.e. the function calculates `a` with `Q(a,x) = q` where `x>0` and  `0<q<1`.

    See also  BoostMath :cite:p:`BoostFun02`,  Wikipedia :cite:p:`WikipediaFun01`, NIST :cite:p:`DLMFun01`


    .. code-block:: pycon


        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; x = '10.4'; prob = '0.7'
        >>> \mathrm{d}x = dec.real_gamma_q_inva(x, prob); mx = mpm.real_gamma_q_inva(x, prob)
        >>> ix = ipm.real_gamma_q_inva(x, prob); fx = fpm.real_gamma_q_inva(x, prob)
        >>> gx = gmp.real_gamma_q_inva(x, prob); ax = apm.real_gamma_q_inva(x, prob)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  1.246374758284686223602899788651972294825E+1
        mpm:  1.246374758284686223602899788651972294825e+1
        ipm:  1.246374758284686223602899788651972294825e+1 (7.368e-40%)
        fpm:  1.24637475828469E+01
        gmp:  1.246374758284686201648128189845010638237E+01
        apm:  1.246374758284686223602899788651972294825e+1 (7.368e-40%)





