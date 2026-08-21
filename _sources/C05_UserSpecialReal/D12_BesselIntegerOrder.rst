

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





Bessel functions of integer order
===============================================================================




Bessel function of the 1st kind, order `0, J_{0}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.bessel_j0(x)

    where ``ctx`` is ``math53`` or ``ctxcpp``.

    Returns `J_0(x)`, the Bessel function of the 1st kind, order zero.  See also Wikipedia :cite:p:`WikipediaFun84`, MathWorld :cite:p:`WolframFun84`, NIST :cite:p:`DLMFun84`,  BoostMath :cite:p:`BoostFun84`,  :cite:t:`Ehrhardt2018`  (3.1.1.1).




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselJ0(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselJ0('0.51')
        ereal('5.3518479027559984754E-1')





Bessel function of the 1st kind, order `1, J_{1}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.bessel_j1(x)

    where ``ctx`` is ``math53`` or ``ctxcpp``.


    Returns `J_1(x)`, the Bessel function of the 1st kind, order one. See also Wikipedia :cite:p:`WikipediaFun84`, MathWorld :cite:p:`WolframFun84`, NIST :cite:p:`DLMFun84`,  BoostMath :cite:p:`BoostFun84`,  :cite:t:`Ehrhardt2018`  (3.1.1.1).



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselJ1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselJ1('0.51')
        ereal('5.3518479027559984754E-1')






Bessel function of the 1st kind, integer order `n, J_{n}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.bessel_jn(n, x)

    where ``ctx`` is ``math53`` or ``ctxcpp``.

    Returns `J_n(x)`, the Bessel function of the 1st kind, order `n`. See also Wikipedia :cite:p:`WikipediaFun84`, MathWorld :cite:p:`WolframFun84`, NIST :cite:p:`DLMFun84`,  BoostMath :cite:p:`BoostFun84`,  :cite:t:`Ehrhardt2018`  (3.1.1.1).



    .. math:: J_{n}(x)  = \left(\tfrac{1}{2}x\right)^{n}  \sum_{k=0}^\infty (-1)^k \frac{(x^2 / 4)^k}{k! \Gamma(n+k+1)}.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselJn(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselJn(3, '0.51')
        ereal('5.3518479027559984754E-1')






Bessel function of the 2nd kind, order `0, Y_{0}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.bessel_y0(x)

    where ``ctx`` is ``math53`` or ``ctxcpp``.

    Returns `Y_0(x)`, the Bessel function of the 2nd kind, order zero, `x>0`. See also Wikipedia :cite:p:`WikipediaFun85`, MathWorld :cite:p:`WolframFun85`, NIST :cite:p:`DLMFun85`,  BoostMath :cite:p:`BoostFun84`,  :cite:t:`Ehrhardt2018`  (3.1.1.1).



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselY0(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselY0('0.51')
        ereal('5.3518479027559984754E-1')






Bessel function of the 2nd kind, order `1, Y_{1}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.bessel_y1(x)

    where ``ctx`` is ``math53`` or ``ctxcpp``.

    Returns `Y_1(x)`, the Bessel function of the 2nd kind, order one, `x>0`.  See also Wikipedia :cite:p:`WikipediaFun85`, MathWorld :cite:p:`WolframFun85`, NIST :cite:p:`DLMFun85`,  BoostMath :cite:p:`BoostFun84`,  :cite:t:`Ehrhardt2018`  (3.1.1.1).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselY1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselY1('0.51')
        ereal('5.3518479027559984754E-1')








Bessel function of the 2nd kind, integer order `n, Y_{n}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.bessel_yn(x)

    where ``ctx`` is ``math53`` or ``ctxcpp``.

    Returns `Y_n(x)`, the Bessel function of the 2nd kind, order n, `x>0`.  See also Wikipedia :cite:p:`WikipediaFun85`, MathWorld :cite:p:`WolframFun85`, NIST :cite:p:`DLMFun85`,  BoostMath :cite:p:`BoostFun84`,  :cite:t:`Ehrhardt2018`  (3.1.1.1).


    .. math :: Y_{n}(z)=-{\frac {\left({\frac {z}{2}}\right)^{-n}}{\pi }}\sum _{k=0}^{n-1}{\frac {(n-k-1)!}{k!}}\left({\frac {z^{2}}{4}}\right)^{k}+{\frac {2}{\pi }}J_{n}(z)\log {\frac {z}{2}}-{\frac {\left({\frac {z}{2}}\right)^{n}}{\pi }}\sum _{k=0}^{\infty }(\psi (k+1)+\psi (n+k+1)){\frac {\left(-{\frac {z^{2}}{4}}\right)^{k}}{k!(n+k)!}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselYn(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselYn(3, '0.51')
        ereal('5.3518479027559984754E-1')


    An example in double precision (32 bit version of xlcalcnet)

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselYn(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselYn(3, '0.51')
        ereal('5.3518479027559984754E-1')





|newpage|


Bessel Lambda function, `\Lambda(\nu,x)`
-------------------------------------------------------------------------------

.. method:: math53.bessel_lambda(v,x)

    Returns the Bessel `\Lambda_{\nu}(x)` function, defined for `x, \nu \ge 0` as

    .. math:: \Lambda(\nu,x) = \Gamma(\nu+1) \frac{J_{\nu}(x)}{(x/2)^{\nu}}

    See also: :cite:t:`Ehrhardt2018` (3.1.3.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.BesselLambda(3, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.BesselLambda(3, '0.51')
        ereal('5.3518479027559984754E-1')






