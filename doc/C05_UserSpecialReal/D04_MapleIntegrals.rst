

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Maple style elliptic integrals
===============================================================================


Complete integral of the 1st kind, `\mathrm{EllipticK}(k)`
-------------------------------------------------------------------------------

.. method:: math53.ellipticK(k)

    Returns the complete elliptic integral of the first kind K(k) and the real part if `|k| > 1`. See also Maplesoft :cite:p:`Maplesoft101`, :cite:t:`Ehrhardt2018` (3.2.4.1).

    .. math:: \mathrm{EllipticK}(k) = \int_0^{1} \frac{\mathrm{d}t}{\sqrt{(1-t^2)(1-k^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticK(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticK('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticK(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticK('0.51')
        Gpr('5.3518479027559984754E-1')






Complete integral of the 1st kind for imaginary modulus, `\mathrm{EllipticKim}(k)`
----------------------------------------------------------------------------------------

.. method:: math53.ellipticKim(k)

    Returns the complete elliptic integral of the first kind for the imaginary modulus `ik` with `k \in \mathbb{R}`. See also Maplesoft :cite:p:`Maplesoft101`, :cite:t:`Ehrhardt2018` (3.2.4.2).

    .. math:: \mathrm{EllipticKim}(k) = \int_0^{1} \frac{\mathrm{d}t}{\sqrt{(1-t^2)(1+k^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticKim(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticKim('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticKim(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticKim('0.51')
        Gpr('5.3518479027559984754E-1')






Complementary complete integral of the 1st kind, `\mathrm{EllipticCK}(k) = K'(k)`
-----------------------------------------------------------------------------------------------

.. method:: math53.ellipticCK(k)

    Returns the complementary complete elliptic integral of the first kind with `k \ne 0`. See also Maplesoft :cite:p:`Maplesoft101`, :cite:t:`Ehrhardt2018` (3.2.4.3), :cite:t:`Ehrhardt2018` (4.2.28).

    .. math:: \mathrm{EllipticCK}(k) = \mathrm{EllipticK}(k_c) = \int_0^{1} \frac{\mathrm{d}t}{\sqrt{(1-t^2)(1-k_c^2 t^2)}}


    Note: the complex version is called Ellck(z) in Amath.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticCK(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticCK('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticCK(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticCK('0.51')
        Gpr('5.3518479027559984754E-1')






Complete integral of the 2nd kind, `\mathrm{EllipticEC}(k)`
-------------------------------------------------------------------------------

.. method:: math53.ellipticEC(k)

    Returns the complete elliptic integral of the second kind `E(k)` and the real part if `|k| > 1`. See also Maplesoft :cite:p:`Maplesoft102`, :cite:t:`Ehrhardt2018` (3.2.4.4).

    .. math:: \mathrm{EllipticEC}(k) = \int_0^{1} \frac{\sqrt{(1-k^2 t^2)}}{\sqrt{(1-t^2)}} \mathrm{d}t


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticEC(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticEC('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticEC(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticEC('0.51')
        Gpr('5.3518479027559984754E-1')







Complete integral of the 2nd kind for imaginary modulus, `\mathrm{EllipticECim}(k)`
----------------------------------------------------------------------------------------

.. method:: math53.ellipticECim(k)

    Returns the complete elliptic integral of the second kind for the imaginary modulus `ik` with `k \in \mathbb{R}`. See also Maplesoft :cite:p:`Maplesoft102`, :cite:t:`Ehrhardt2018` (3.2.4.5).

    .. math:: \mathrm{EllipticECim}(k) = E(ik) = \int_0^{1} \frac{\sqrt{(1+k^2 t^2)}}{\sqrt{(1-t^2)}} \mathrm{d}t


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticECim(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticECim('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticECim(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticECim('0.51')
        Gpr('5.3518479027559984754E-1')







Complementary complete integral of the 2nd kind, `\mathrm{EllipticCE}(k)`
-------------------------------------------------------------------------------

.. method:: math53.ellipticCE(k)

    Returns the complementary complete elliptic integral of the second kind. See also Maplesoft :cite:p:`Maplesoft102`, :cite:t:`Ehrhardt2018` (3.2.4.6).

    .. math:: \mathrm{EllipticEC}(k) = \mathrm{EllipticEC}(k_c) = \int_0^{1} \frac{\sqrt{(1-k_c^2 t^2)}}{\sqrt{(1-t^2)}} \mathrm{d}t


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticCE(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticCE('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticCE(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticCE('0.51')
        Gpr('5.3518479027559984754E-1')







Complete integral of the 3rd kind, `\mathrm{EllipticPiC}(\nu, k)`
-------------------------------------------------------------------------------

.. method:: math53.ellipticPiC(nu, k)

    Returns the complete elliptic integral of the third kind with `|k| \ne 1, \nu \ne 1` (or its real part if `|k| > 1`). See also Maplesoft :cite:p:`Maplesoft103`, :cite:t:`Ehrhardt2018` (3.2.4.7).

    .. math:: \mathrm{EllipticPiC}(\nu, k) = \int_0^{1} \frac{\mathrm{d}t}{(1-\nu t^2)\sqrt{(1-t^2)(1-k^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticPiC(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticPiC(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticPiC(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticPiC(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')








Complete integral of the 3rd kind for imaginary modulus, `\mathrm{EllipticPiCim}(\nu, k)`
-----------------------------------------------------------------------------------------------

.. method:: math53.ellipticPiCim(nu, k)

    Returns the complementary complete elliptic integral of the third kind with `\nu \ne 1`. See also Maplesoft :cite:p:`Maplesoft102`, :cite:t:`Ehrhardt2018` (3.2.4.8).

    .. math:: \mathrm{EllipticPiCim}(\nu, k) = \mathrm{EllipticPiC}(\nu, k) = \int_0^{1} \frac{\mathrm{d}t}{(1-\nu t^2)\sqrt{(1-t^2)(1+k^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticPiCim(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticPiCim(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticPiCim(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticPiCim(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Complementary complete integral of the 3rd kind, `\mathrm{EllipticCPi}(\nu, k)`
---------------------------------------------------------------------------------------

.. method:: math53.ellipticCPi(nu, x)

    Returns the complementary complete elliptic integral of the third kind with `|k| \ne 0, \nu \ne 1`. See also Maplesoft :cite:p:`Maplesoft102`, :cite:t:`Ehrhardt2018` (3.2.4.9).

    .. math:: \mathrm{EllipticCPi}(\nu, k) = \mathrm{EllipticPiC}(\nu, k_c) = \int_0^{1} \frac{\mathrm{d}t}{(1-\nu t^2)\sqrt{(1-t^2)(1-k_c^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticCPi(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticCPi(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticCPi(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticCPi(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Incomplete integral of the 1st kind, `\mathrm{EllipticF}(z, k)`
-------------------------------------------------------------------------------

.. method:: math53.ellipticF(z, k)

    Returns the incomplete elliptic integral of the first kind with `|z| \le 1, |kz| \le 1`. See also Maplesoft :cite:p:`Maplesoft101`, :cite:t:`Ehrhardt2018` (3.2.4.10).

    .. math:: \mathrm{EllipticF}(z, k) = \int_0^{z} \frac{\mathrm{d}t}{\sqrt{(1-t^2)(1-k^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticF(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticF(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticF(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticF(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Incomplete integral of the 2nd kind, `\mathrm{EllipticE}(z, k)`
-------------------------------------------------------------------------------

.. method:: math53.ellipticE(z, k)

    Returns the incomplete elliptic integral of the second kind with `|z| \le 1, |kz| \le 1`. See also Maplesoft :cite:p:`Maplesoft102`, :cite:t:`Ehrhardt2018` (3.2.4.11).

    .. math:: \mathrm{EllipticE}(z, k) = \int_0^{z} \frac{\sqrt{(1-k^2 t^2)}}{\sqrt{(1-t^2)}} \mathrm{d}t


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticE(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticE(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticE(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticE(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Incomplete integral of the 3rd kind, `\mathrm{EllipticPi}(z, \nu, k)`
---------------------------------------------------------------------------------------

.. method:: math53.ellipticPi(z, nu, k)

    Returns the incomplete elliptic integral of the third kind with `|z| \le 1, |kz| \le 1`. See also Maplesoft :cite:p:`Maplesoft103`, :cite:t:`Ehrhardt2018` (3.2.4.12).

    .. math:: \mathrm{EllipticPi}(z, \nu, k) = \int_0^{z} \frac{\mathrm{d}t}{(1-\nu t^2)\sqrt{(1-t^2)(1-k_c^2 t^2)}}


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticPi(0.6, 0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticPi(0.6, 0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticPi(0.6, 0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticPi(0.6, 0.8, '0.51')
        Gpr('5.3518479027559984754E-1')





