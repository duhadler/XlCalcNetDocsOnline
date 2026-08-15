

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Modified Bessel functions of integer order
===============================================================================



Modified Bessel function of the 1st kind, order `0, I_{0}(x)`
-------------------------------------------------------------------------------

.. method:: math53.bessel_i0(x)

    Returns I0(x), the modified Bessel function of the 1st kind, order zero. See also Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun86`, NIST :cite:p:`DLMFun86`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.1).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselI0(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselI0('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselI0(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselI0('0.51')
        Gpr('5.3518479027559984754E-1')






Modified Bessel function of the 1st kind, order `1, I_{1}(x)`
-------------------------------------------------------------------------------

.. method:: math53.bessel_i1(x)

    Returns I1(x), the modified Bessel function of the 1st kind, order one. See also Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun86`, NIST :cite:p:`DLMFun86`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselI1(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselI1('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselI1(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselI1('0.51')
        Gpr('5.3518479027559984754E-1')






Modified Bessel function of the 1st kind, integer order `n, I_{n}(x)`
-------------------------------------------------------------------------------

.. method:: math53.damath_bessel_in(x)

    Returns I_n(x), the modified Bessel function of the 1st kind, order n. See also Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun86`, NIST :cite:p:`DLMFun86`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.5).

    .. math:: I_{\nu}\left(z\right)=(\tfrac{1}{2}z)^{\nu}\sum_{k=0}^{\infty}\frac{(\tfrac{1}{4}z^{2})^{k}}{k!\Gamma\left(\nu+k+1\right)}.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselIn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselIn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselIn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselIn(3, '0.51')
        Gpr('5.3518479027559984754E-1')






Modified Bessel function of the 2nd kind, order 0, `K_{0}(x)`
-------------------------------------------------------------------------------

.. method:: math53.bessel_k0(x)

    Returns K0(x), the modified Bessel function of the 2nd kind, order zero, x>0.  See also  Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun87`, NIST :cite:p:`DLMFun87`,  BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.6).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselK0(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselK0('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselK0(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselK0('0.51')
        Gpr('5.3518479027559984754E-1')






Modified Bessel function of the 2nd kind, order `1, K_{1}(x)`
-------------------------------------------------------------------------------

.. method:: math53.bessel_k1(x)

    Returns K1(x), the modified Bessel function of the 2nd kind, order one, x>0.  See also  Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun87`, NIST :cite:p:`DLMFun87`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.8).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselK1(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselK1('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselK1(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselK1('0.51')
        Gpr('5.3518479027559984754E-1')






Modified Bessel function of the 2nd kind, integer order `n, K_{n}(x)`
-------------------------------------------------------------------------------

.. method:: math53.bessel_kn(x)

    Returns K_n(x), the modified Bessel function of the 2nd kind, order n, x > 0.  See also  Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun87`, NIST :cite:p:`DLMFun87`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.10).

    .. math::
       :nowrap:

       \begin{eqnarray}
        K_{n}\left(z\right) & = & \tfrac{1}{2}(\tfrac{1}{2}z)^{-n}\sum_{k=0}^{n-1}\frac{(n-k-1)!}{k!}(-\tfrac{1}{4}z^{2})^{k}+(-1)^{n+1}\log\left(\tfrac{1}{2}z\right)I_{n}\left(z\right) \\
        & + & (-1)^{n}\tfrac{1}{2}(\tfrac{1}{2}z)^{n}\sum_{k=0}^{\infty}\left(\psi\left(k+1\right)+\psi\left(n+k+1\right)\right)\frac{(\tfrac{1}{4}z^{2})^{k}}{k!(n+k)!} \nonumber 
       \end{eqnarray}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselKn(3, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselKn(3, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselKn(3, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselKn(3, '0.51')
        Gpr('5.3518479027559984754E-1')





Exponentially scaled modified Bessel function of the 1st kind, order `0, I_{0,e}(x)`
---------------------------------------------------------------------------------------

.. method:: math53.bessel_i0e(x)

    Returns I0(x)*exp(-`|x|`), the exponentially scaled modified Bessel function of the 1st kind, order zero. See also Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun86`, NIST :cite:p:`DLMFun86`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselI0e(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselI0e('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselI0e(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselI0e('0.51')
        Gpr('5.3518479027559984754E-1')





Exponentially scaled modified Bessel function of the 1st kind, order `1, I_{1,e}(x)`
-----------------------------------------------------------------------------------------

.. method:: math53.bessel_i1e(x)

    Returns I1(x)*exp(-`|x|`), the exponentially scaled modified Bessel function of the 1st kind, order one. See also Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun86`, NIST :cite:p:`DLMFun86`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselI1e(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselI1e('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselI1e(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselI1e('0.51')
        Gpr('5.3518479027559984754E-1')





Exponentially scaled modified Bessel function of the 2nd kind, order 0, `K_{0,e}(x)`
-----------------------------------------------------------------------------------------

.. method:: math53.bessel_k0e(x)

    Returns K0(x)*exp(x),    the exponentially scaled modified Bessel function of the 2nd kind, order zero, x>0. See also  Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun87`, NIST :cite:p:`DLMFun87`,  BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.7).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselK0e(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselK0e('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselK0e(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselK0e('0.51')
        Gpr('5.3518479027559984754E-1')




Exponentially scaled modified Bessel function of the 2nd kind, order `1, K_{1,e}(x)`
------------------------------------------------------------------------------------------

.. method:: math53.bessel_k1e(x)

    Returns K1(x)*exp(x),    the exponentially scaled modified Bessel function of the 2nd kind, order one, x>0.  See also  Wikipedia :cite:p:`WikipediaFun86`, MathWorld :cite:p:`WolframFun87`, NIST :cite:p:`DLMFun87`, BoostMath :cite:p:`BoostFun86`, :cite:t:`Ehrhardt2018` (3.1.2.9).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.BesselK1e(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.BesselK1e('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.BesselK1e(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.BesselK1e('0.51')
        Gpr('5.3518479027559984754E-1')

