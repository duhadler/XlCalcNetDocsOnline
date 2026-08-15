

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Jacobi theta functions  at `x=0` for `0 \le q <1`
===============================================================================




Jacobi theta function `\theta'_1(q)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_theta1p(q)  

    Returns the Jacobi theta function `\theta'_1(q) = \partial\theta_1(x,q)/\partial x` at `x=0` for `0 \le q <1`. See also Wikipedia :cite:p:`WikipediaFun170`, MathWorld :cite:p:`WolframFun170`,  MathWorld :cite:p:`WolframFun170a`, NIST :cite:p:`DLMFun170`, :cite:t:`Ehrhardt2018` (3.2.14.1).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiTheta1p(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiTheta1p('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiTheta1p(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiTheta1p('0.51')
        Gpr('5.3518479027559984754E-1')







Jacobi theta function `\theta_2(q)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_theta02(q)  

    Returns the Jacobi theta function `\theta_2(q) = \theta_2(0,q)` for `0 \le q <1`. See also Wikipedia :cite:p:`WikipediaFun170`, MathWorld :cite:p:`WolframFun170`, NIST :cite:p:`DLMFun170`, :cite:t:`Ehrhardt2018` (3.2.14.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiTheta2(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiTheta2('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiTheta2(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiTheta2('0.51')
        Gpr('5.3518479027559984754E-1')






Jacobi theta function `\theta_3(q)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_theta03(q)  

    Returns the Jacobi theta function `\theta_3(q) = \theta_3(0,q)` for `0 \le q <1`. See also Wikipedia :cite:p:`WikipediaFun170`, MathWorld :cite:p:`WolframFun170`, NIST :cite:p:`DLMFun170`, :cite:t:`Ehrhardt2018` (3.2.14.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiTheta3(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiTheta3('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiTheta3(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiTheta3('0.51')
        Gpr('5.3518479027559984754E-1')







Jacobi theta function `\theta_4(q)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_theta04(q)  

    Returns the Jacobi theta function `\theta_4(q) = \theta_4(0,q)` for `-1 < q <1`. See also Wikipedia :cite:p:`WikipediaFun170`, MathWorld :cite:p:`WolframFun170`, NIST :cite:p:`DLMFun170`, :cite:t:`Ehrhardt2018` (3.2.14.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiTheta4(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiTheta4('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiTheta4(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiTheta4('0.51')
        Gpr('5.3518479027559984754E-1')



