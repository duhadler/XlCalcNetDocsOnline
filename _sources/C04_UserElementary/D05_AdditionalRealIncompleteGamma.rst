

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Additional real incomplete gamma functions (real arguments only)
===============================================================================





.. _rst_mpm_real_gamma_tricomi: 

Tricomi's entire incomplete gamma function: `\gamma^*(a,x)`
-------------------------------------------------------------------------------

.. method:: ctx.real_gamma_tricomi(a, x)

    where ``ctx`` is ``math53``, ``ctxcpp``, ``ctxboost`` or ``ctxflint``.


    Returns Tricomi's entire incomplete gamma function `\gamma^*(a,x)`. See also  Wikipedia :cite:p:`WikipediaFun01`, NIST :cite:p:`DLMFun01`, Flint :cite:p:`FlintFun01`, :cite:t:`Ehrhardt2018` (3.5.2.3).

    The function is defined as

    .. math :: \gamma^*(a,x)=e^{-x} \frac{M(1,a+1,x)}{\Gamma(a+1)}

    Special cases are `\gamma^*(0,x)=1, \gamma^*(a,0)=1/\Gamma(a+1)`, and `\gamma^*(-n,x)=x^n`, if `-n` is a negative integer. Otherwise there are the following relations to the other incomplete functions:

    .. math :: \gamma^*(a,x)=\frac{x^{-a}}{\Gamma(a)}\gamma(a,x)=x^{-a} P(a,x).



    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, ipm, fpm, gmp, apm
        >>> mpm.dps = 40; a = '8.6'; x = '10.7'
        >>> \mathrm{d}x = dec.real_gamma_tricomi(a, x); mx = mpm.real_gamma_tricomi(a, x)
        >>> ix = ipm.real_gamma_tricomi(a, x); fx = fpm.real_gamma_tricomi(a, x)
        >>> gx = gmp.real_gamma_tricomi(a, x); ax = apm.real_gamma_tricomi(a, x)
        >>> mpm.show([\mathrm{d}x, mx, ix, fx, gx, ax])
        dec:  1.096843106816267235367401300868241431961E-9
        mpm:  1.096843106816267235367401300868241431962e-9
        ipm:  1.096843106816267235367401300868241431962e-9 (3.217e-38%)
        fpm:  1.09684310681627E-09
        gmp:  1.096843106816267235367401300868241431962E-09
        apm:  1.096843106816267235367401300868241431962e-9 (3.217e-38%)



        


Truncated exponential function, `e_n(x)` 
-------------------------------------------------------------------------------

.. method:: math53.expn(n,x)

    Returns `\displaystyle e_n(x) = \sum_{k=0}^n \frac{x^k}{k!} = \frac{\Gamma(n+1, x)}{\Gamma(n+1)} e^x`, the truncated exponential sum function, for `n>0`.

    See also: :cite:t:`Ehrhardt2018` (3.10.25).

    https://mathworld.wolfram.com/ExponentialSumFunction.html


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Expn(2,3)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Expn(4,13)
        ereal('5.3518479027559984754E-1')





Relative exponential, `\mathrm{exprel}_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.expreln(n,x) 

    Returns  `\displaystyle \mathrm{exprel}_n(x) = \frac{n!}{x^n} \left(e^x - \sum_{k=0}^{n-1} \frac{x^k}{k!} \right) = e^x x^{-n} \left(\Gamma(1+n) - n \Gamma(n,x) \right)  = {}_1F_1(1, 1+n, x)`.

    See also  :cite:t:`Ehrhardt2018` (3.10.10).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Expreln(3, 4)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Expreln(3, 12)
        ereal('5.3518479027559984754E-1')









