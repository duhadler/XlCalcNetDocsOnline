

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Exponential integrals, and related functions
===============================================================================




Entire cosine integral `\mathrm{Cin}(x)`
-------------------------------------------------------------------------------

.. method:: math53.cin(z)

    Returns the entire cosine integral of  `\displaystyle \mathrm{Cin}(x) = \int_0^{x} \frac{1-\cos(t)}{t} \, \mathrm{d}t`.

    See also   Wikipedia :cite:p:`WikipediaFun178`, MathWorld :cite:p:`WolframFun178`, NIST :cite:p:`DLMFun178`, :cite:t:`Ehrhardt2018` (3.4.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Cin(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Cin('0.51')
        ereal('5.3518479027559984754E-1')







Entire hyperbolic cosine integral `\mathrm{Cinh}(x)`
-------------------------------------------------------------------------------

.. method:: math53.cinh(z)

    Returns the entire hyperbolic cosine integral `\displaystyle \mathrm{Cinh}(x) = \int_0^{x} \frac{\cosh(t)-1}{t} \, \mathrm{d}t`.

    See also   Wikipedia :cite:p:`WikipediaFun180`, MathWorld :cite:p:`WolframFun180`, NIST :cite:p:`DLMFun180`, :cite:t:`Ehrhardt2018` (3.4.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Cinh(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Cinh('0.51')
        ereal('5.3518479027559984754E-1')







Entire exponential integral `\displaystyle \mathrm{Ein}(x)`
-------------------------------------------------------------------------------

.. method:: math53.ein(x) 

    Returns the entire exponential integral `\displaystyle \mathrm{Ein}(x) = -\int_0^{x} \frac{1-e^{-t}}{t} \, \mathrm{d}t`.

    See also   Wikipedia :cite:p:`WikipediaFun180`, MathWorld :cite:p:`WolframFun180`, NIST :cite:p:`DLMFun180`, :cite:t:`Ehrhardt2018` (3.4.11).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Ein(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Ein('0.51')
        ereal('5.3518479027559984754E-1')







Scaled exponential integral `\mathrm{e1s}(x)`
-------------------------------------------------------------------------------

.. method:: math53.exp_integral_e1_scaled(z)

    Returns the scaled exponential integral `\mathrm{e1s}(x) = e ^{-x} E_1(x)` for `x \ne 0`.

    See also   Wikipedia :cite:p:`WikipediaFun175`, MathWorld :cite:p:`WolframFun175`, NIST :cite:p:`DLMFun175`,  BoostMath :cite:p:`BoostFun175`, :cite:t:`Ehrhardt2018` (3.4.6).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.E1s(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.E1s('0.51')
        ereal('5.3518479027559984754E-1')








Scaled exponential integral `\mathrm{eis}(x)`
-------------------------------------------------------------------------------

.. method:: math53.exp_integral_ei_scaled(x)

    Returns the scaled exponential integral `\mathrm{eis}(x) = e ^{-x} \mathrm{Ei}(x)` for `x \ne 0`.

    See also   Wikipedia :cite:p:`WikipediaFun175`, MathWorld :cite:p:`WolframFun175`, NIST :cite:p:`DLMFun175`,  BoostMath :cite:p:`BoostFun175`, :cite:t:`Ehrhardt2018` (3.4.8).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Eis(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Eis('0.51')
        ereal('5.3518479027559984754E-1')








Scaled exponential integral `\mathrm{eisx2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.eisx2(x)

    Returns the scaled exponential integral `\mathrm{eisx2}(x) = e ^{-x^2} \mathrm{Ei}(x^2)` for `x \ne 0`.

    See also   Wikipedia :cite:p:`WikipediaFun175`, MathWorld :cite:p:`WolframFun175`, NIST :cite:p:`DLMFun175`,  BoostMath :cite:p:`BoostFun175`, :cite:t:`Ehrhardt2018` (3.4.9).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Eisx2(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Eisx2('0.51')
        ereal('5.3518479027559984754E-1')









Inverse of the exponential integral, `\mathrm{Ei}^{-1}(x)`
-------------------------------------------------------------------------------

.. method:: math53.ei_inv(x) 

    Returns `\mathrm{Ei}^{-1}(x) = \log(\mathrm{li}^{-1}(x))`, the functional inverse of the exponential integral, i.e. `\mathrm{Ei}(\mathrm{Ei}^{-1}(x)) = x`.

    See also   Wikipedia :cite:p:`WikipediaFun175`, MathWorld :cite:p:`WolframFun175`, NIST :cite:p:`DLMFun175`,  BoostMath :cite:p:`BoostFun175`, :cite:t:`Ehrhardt2018` (3.4.10).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.EiInv(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.EiInv('0.51')
        ereal('5.3518479027559984754E-1')







Generalized exponential integral `E_p(p,x)`
-------------------------------------------------------------------------------

.. method:: math53.gei(p,x) 

    Returns the generalized exponential integral of real order `\displaystyle E_p(x) = \int_{1}^{\infty} \frac{e^{-xt}}{t^p} \, \mathrm{d}t = x^{p-1} \Gamma(1-p, x) = x^{p-1} Q(1-p, x) \Gamma(1-p)`.

    See also   Wikipedia :cite:p:`WikipediaFun175`, MathWorld :cite:p:`WolframFun176`, NIST :cite:p:`DLMFun176`,  BoostMath :cite:p:`BoostFun176`, :cite:t:`Ehrhardt2018` (3.4.13).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Gei(3.1, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Gei(3.1, '0.51')
        ereal('5.3518479027559984754E-1')








Exponential integral `\displaystyle \beta_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.eibeta(n,x)

    Returns the exponential integral  `\displaystyle \beta_n(x) = \int_{1}^{1} t^n e^{-xt} \, \mathrm{d}t = x^{-n-1}\left(\Gamma(n+1,-x)-\Gamma(n+1,x)\right), n \ge 0`. 

    See also  :cite:t:`Abramowitz1970` (5.1.6) and (5.1.47), and :cite:t:`Ehrhardt2018` (3.4.14).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Eibeta(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Eibeta(3, '0.51')
        ereal('5.3518479027559984754E-1')







Inverse of the logarithmic integral, `\mathrm{li}^{-1}(x)`
-------------------------------------------------------------------------------

.. method:: math53.log_integral_inv(x)

    Returns `\mathrm{li}^{-1}(x)`, the functional inverse of the logarithmic integral, i.e. `\mathrm{li}(\mathrm{li}^{-1}(x)) = x`.

    See also   Wikipedia :cite:p:`WikipediaFun177`, MathWorld :cite:p:`WolframFun177`, NIST :cite:p:`DLMFun177`, :cite:t:`Ehrhardt2018` (3.4.16).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LiInv(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LiInv('0.51')
        ereal('5.3518479027559984754E-1')





Shifted sine integral `\mathrm{si}(x) =  \mathrm{Si}(x) - \pi/2`
-------------------------------------------------------------------------------

.. method:: math53.shifted_sin_integral(x)

    Returns the shifted sine integral, `\mathrm{si}(x) =  \mathrm{Si}(x) - \pi/2`.

    See also   Wikipedia :cite:p:`WikipediaFun179`, MathWorld :cite:p:`WolframFun179`, NIST :cite:p:`DLMFun178`, :cite:t:`Ehrhardt2018` (3.4.19).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.ShiftedSi(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.ShiftedSi('0.51')
        ereal('5.3518479027559984754E-1')






