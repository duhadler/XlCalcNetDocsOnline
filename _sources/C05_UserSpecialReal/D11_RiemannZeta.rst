

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Riemann zeta, and related functions
===============================================================================




Riemann `\zeta(n)` for integer arguments
-------------------------------------------------------------------------------

.. method:: math53.zeta_i(n)

    Returns the Riemann zeta function `\zeta(n)` for integer arguments `n \ne 1`. For
    `n > 63` the result is `1`, for `0 \le n \le 63` the value is taken from a table, otherwise the Bernoulli
    numbers are used: `\zeta(n) = B_{1-n}/(n - 1)` for `n < 0`.

    See also   Wikipedia :cite:p:`WikipediaFun171`, MathWorld :cite:p:`WolframFun171`, NIST :cite:p:`DLMFun171`,  BoostMath :cite:p:`BoostFun171`, :cite:t:`Ehrhardt2018` (3.6.1.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ZetaInt(5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ZetaInt('51')
        ereal('5.3518479027559984754E-1')




        


Riemann `\zeta(1+x)`
-------------------------------------------------------------------------------

.. method:: math53.zeta1p(x) 

    Returns the Riemann zeta function `\zeta(1+x)` for `x \ne 0`. Normally used with `|x| \ll 1` for increased accuracy near the pole of `\zeta(s)` at `s = 1`.

    See also   Wikipedia :cite:p:`WikipediaFun171`, MathWorld :cite:p:`WolframFun171`, NIST :cite:p:`DLMFun171`,  BoostMath :cite:p:`BoostFun171`, :cite:t:`Ehrhardt2018` (3.6.1.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Zeta1p(0.004)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Zeta1p('0.0001')
        ereal('5.3518479027559984754E-1')








Dirichlet eta function for integer argument,  `\eta(n)`
-------------------------------------------------------------------------------

.. method:: math53.dirichlet_eta_i(n) 

    Returns the Riemann zeta function `\eta(n)` for integer arguments. For
    `n > 64` the result is `1`, for `0 \le n \le 64` the value is taken from a table, otherwise for `n<0` the Bernoulli
    numbers are used: `\eta(n) = (2^{1-n}-1) B_{1-n}/(1-n)`.

    See also: MathWorld :cite:p:`WolframFun1008`, :cite:t:`Ehrhardt2018` (3.6.3.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.DirichletEtaInt(5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.DirichletEtaInt('51')
        ereal('5.3518479027559984754E-1')








Inverse of the Riemann prime counting function, `R^{-1}(x)`
-------------------------------------------------------------------------------

.. method:: math53.riemann_r_inv(x)

    Returns the functional inverse of the Riemann prime counting function, i.e. `R(R^{-1}(x))= x`, for `x \ge 1.125`.

    See also :cite:t:`Ehrhardt2018` (3.10.21).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.RiemannRInv(44)
        ereal('5.2359877559829887307E-1')
        >>> ereal.RiemannRInv(4440.4)
        ereal('5.3518479027559984754E-1')






Rogers-Ramanujan continued fraction
-------------------------------------------------------------------------------

.. method:: math53.rogers_ramanujan_cf(q)

    Returns `\displaystyle R(q) = \frac{q^{1/5}}{1+} \frac{q}{1+} \frac{q^2}{1+} \frac{q^3}{1+} \frac{q^5}{1+}`, the Rogers-Ramanujan continued fraction, for `|q| < 1`.

    See also :cite:t:`Ehrhardt2018` (3.10.22).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.RogersRamanujanCF(0.44)
        ereal('5.2359877559829887307E-1')
        >>> ereal.RogersRamanujanCF(0.14404)
        ereal('5.3518479027559984754E-1')






q-Pochhammer Euler function, `(q)_{\infty}`
-------------------------------------------------------------------------------

.. method:: math53.euler_q(n,x) 

    Returns `\displaystyle \phi(q) = (q)_{\infty} = \prod_{k=1}^{\infty} \left(1-q^k\right)`, the q-Pochhammer Euler function, for `-1 \le q \le 1`.

    See also: MathWorld :cite:p:`WolframFun1031`,  Wikipedia :cite:p:`WikipediaFun1031`, :cite:t:`Ehrhardt2018` (3.10.19).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.EulerQ(-0.4)
        ereal('5.2359877559829887307E-1')
        >>> ereal.EulerQ(0.4)
        ereal('5.3518479027559984754E-1')




