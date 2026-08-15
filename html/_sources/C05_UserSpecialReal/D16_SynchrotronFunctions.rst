

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />






|newpage|

Synchrotron functions
==============================================================================================


First synchrotron function `F(x)`
-------------------------------------------------------------------------------

.. method:: math53.synchrotron_f(x)

    Returns the first synchrotron function `F(x)` for `x \ge 0`, `\displaystyle F(x) = x\int_x^{\infty} K_{5/3}(t) \mathrm{d}t.`

    See also: :cite:t:`Ehrhardt2018` (3.1.11.1). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SynchF(2.25)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SynchF(12.25)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SynchF(2.25)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SynchF(12.25)
        Gpr('5.3518479027559984754E-1')







Second synchrotron function `G(x)`
-------------------------------------------------------------------------------

.. method:: math53.synchrotron_g(x)

    Returns the second synchrotron function `G(x) = x K_{2/3}(x)` for `x \ge 0`.

    See also: :cite:t:`Ehrhardt2018` (3.1.11.2). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.SynchG(2.25)
        xreal('5.2359877559829887307E-1')
        >>> xreal.SynchG(12.25)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.SynchG(2.25)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.SynchG(12.25)
        Gpr('5.3518479027559984754E-1')




