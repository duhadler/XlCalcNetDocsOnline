

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Hypergeometric pFq, and related functions
===============================================================================



        
Struve function `\mathbf{H}_0(x)`
-------------------------------------------------------------------------------

.. method:: math53.struve_h0(x)

    Returns the Struve function `H_0(x)`


    See also: :cite:t:`Ehrhardt2018` (3.1.9.1), Mpmath :cite:p:`MpmathFun1044`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.StruveH0(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.StruveH0('0.51')
        ereal('5.3518479027559984754E-1')








Struve function `\mathbf{H}_1(x)`
-------------------------------------------------------------------------------

.. method:: math53.struve_h1(x)

    Returns the Struve function `H_1(x)`

    See also: :cite:t:`Ehrhardt2018` (3.1.9.2), Mpmath :cite:p:`MpmathFun1044`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.StruveH1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.StruveH1('0.51')
        ereal('5.3518479027559984754E-1')






Struve function `\mathbf{L}_0(x)`
-------------------------------------------------------------------------------

.. method:: math53.struve_l0(x)

    Returns the Struve function `L_0(x)`

    See also: :cite:t:`Ehrhardt2018` (3.1.9.5). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.StruveL0(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.StruveL0('0.51')
        ereal('5.3518479027559984754E-1')







Struve function `\mathbf{L}_1(x)`
-------------------------------------------------------------------------------

.. method:: math53.struve_l1(x)

    Returns the Struve function `\mathbf{L}_1(x)`

    See also: :cite:t:`Ehrhardt2018` (3.1.9.6). 


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.StruveL1(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.StruveL1('0.51')
        ereal('5.3518479027559984754E-1')




