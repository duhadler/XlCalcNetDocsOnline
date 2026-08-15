

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Lemniscate functions
===============================================================================



Lemniscate sine function, `\mathrm{sinlemn}(x)` 
-------------------------------------------------------------------------------

.. method:: math53.sin_lemniscate(x)  

    Returns the lemniscate sine function  `\displaystyle \mathrm{sinlemn}(x) = \frac{\sqrt{2}}{2} \mathrm{sd}\left(x \sqrt{2}, \frac{\sqrt{2}}{2}\right)`, where `\mathrm{sd}(\cdot)` is a Jacobi elliptic function.

    See also: Wikipedia :cite:p:`WikipediaFun170l`, MathWorld :cite:p:`WolframFun170l`, :cite:t:`Ehrhardt2018` (3.2.16.1).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SinLemniscate(1.5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SinLemniscate(1.5, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SinLemniscate(1.5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SinLemniscate(1.5, '0.51')
        Gpr('5.3518479027559984754E-1')






Lemniscate cosine function, `\mathrm{coslemn}(x)` 
-------------------------------------------------------------------------------

.. method:: math53.cos_lemniscate(x)  

    Returns the lemniscate cosine function `\displaystyle \mathrm{coslemn}(x) = \mathrm{cn}\left(x \sqrt{2}, \frac{\sqrt{2}}{2}\right)`, where `\mathrm{cn}(\cdot)` is a Jacobi elliptic function.

    See also: Wikipedia :cite:p:`WikipediaFun170l`, MathWorld :cite:p:`WolframFun170l`, :cite:t:`Ehrhardt2018` (3.2.16.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.CosLemniscate(1.5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.CosLemniscate(1.5, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.CosLemniscate(1.5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.CosLemniscate(1.5, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse lemniscate cosine function, `\mathrm{arcsl}(x)` 
-------------------------------------------------------------------------------

.. method:: math53.acos_lemniscate(x)  

    Returns the inverse lemniscate cosine function `\displaystyle \mathrm{arcsl}(x) = \frac{1}{\sqrt{2}} \mathrm{arcsd}\left(x \sqrt{2}, \frac{\sqrt{2}}{2}\right),  |x| \le 1`, where `\mathrm{arcsd}(\cdot)` is an inverse Jacobi elliptic function.

    See also: Wikipedia :cite:p:`WikipediaFun170l`, MathWorld :cite:p:`WolframFun170l`, :cite:t:`Ehrhardt2018` (3.2.16.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.AcosLemniscate(1.5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.AcosLemniscate(1.5, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.AcosLemniscate(1.5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.AcosLemniscate(1.5, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse lemniscate sine function, `\mathrm{arccl}(x)` 
-------------------------------------------------------------------------------

.. method:: math53.asin_lemniscate(x)  

    Returns the inverse lemniscate sine function `\displaystyle \mathrm{arccl}(x) = \frac{1}{\sqrt{2}} \mathrm{arccn}\left(x \sqrt{2}, \frac{\sqrt{2}}{2}\right),  |x| \le 1`, where `\mathrm{arccn}(\cdot)` is an inverse Jacobi elliptic function.

    See also: Wikipedia :cite:p:`WikipediaFun170l`, MathWorld :cite:p:`WolframFun170l`, :cite:t:`Ehrhardt2018` (3.2.16.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.AsinLemniscate(1.5, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.AsinLemniscate(1.5, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.AsinLemniscate(1.5, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.AsinLemniscate(1.5, '0.51')
        Gpr('5.3518479027559984754E-1')






