

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Polygamma, and related functions
===============================================================================




Pentagamma function `\psi'''(x)`
-------------------------------------------------------------------------------

.. method:: math53.pentagamma(x) 

    Returns the pentagamma function `\psi'''(x), \quad x \ne 0, -1, -2, \ldots` The function returns the Hurwitz zeta value `6\zeta(4,x)` if `x` is positive; for `x<0` it returns `\psi'''(x) = -2\pi^4\left(1+ 4\cot^2(\pi x)+3\cot^4(\pi x)\right) - 6\zeta(4,1-x)`.

    See also   Wikipedia :cite:p:`WikipediaFun83`, MathWorld :cite:p:`WolframFun83`, NIST :cite:p:`DLMFun83`,  BoostMath :cite:p:`BoostFun83`, :cite:t:`Ehrhardt2018` (3.5.6.5).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Pentagamma(7)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Pentagamma('4.51')
        ereal('5.3518479027559984754E-1')






Tetragamma function, `\psi''(x)`
-------------------------------------------------------------------------------

.. method:: math53.tetragamma(x) 

    Returns the tetragamma function `\psi''(x), \quad x \ne 0, -1, -2, \ldots` The function returns the Hurwitz zeta value `-2\zeta(3,x)` if `x` is positive; for `x<0` it returns `\psi''(x) = -2\pi^3 \cot(\pi x)\left(1+\cot^2(\pi x)\right) - 2\zeta(3,1-x)`.

    See also   Wikipedia :cite:p:`WikipediaFun83`, MathWorld :cite:p:`WolframFun83`, NIST :cite:p:`DLMFun83`,  BoostMath :cite:p:`BoostFun83`, :cite:t:`Ehrhardt2018` (3.5.6.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Tetragamma(7)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Tetragamma('4.51')
        ereal('5.3518479027559984754E-1')






Auxiliary function `\psi^{*}(x)`
-------------------------------------------------------------------------------

.. method:: math53.psistar(x)  

    Returns `\psi^{*}(x) = \psi(x) - \log(x), x > 0`. The function is useful when computing differences of `\psi` functions, because it can avoid cancellation for larger `x` values. See also :cite:t:`Ehrhardt2018` (3.5.6.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.PsiStar(7)
        ereal('5.2359877559829887307E-1')
        >>> ereal.PsiStar('4.51')
        ereal('5.3518479027559984754E-1')








Inverse digamma function `\psi^{-1}(y)`
-------------------------------------------------------------------------------

.. method:: math53.psi_inv(y)

    Returns `\psi^{-1}(y)`, the functional inverse of of the digamma function, i.e. it returns `x` with `\psi(x) = y`.

    See also  Wikipedia :cite:p:`WikipediaFun125`, MathWorld :cite:p:`WolframFun125`, NIST :cite:p:`DLMFun83`,  BoostMath :cite:p:`BoostFun125`, :cite:t:`Ehrhardt2018` (3.5.6.7).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.PsiInv(7.1)
        ereal('5.2359877559829887307E-1')
        >>> ereal.PsiInv('4.51')
        ereal('5.3518479027559984754E-1')






Bateman function `G(x)`
-------------------------------------------------------------------------------

.. method:: math53.bateman_g(x)

    Returns the Bateman function `G(x) = \psi((x+1)/2) - \psi(x/2); x \ne 0,-1,-2,\ldots` See also :cite:t:`Ehrhardt2018` (3.5.6.8).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BatemanG(7.1)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BatemanG('4.51')
        ereal('5.3518479027559984754E-1')





