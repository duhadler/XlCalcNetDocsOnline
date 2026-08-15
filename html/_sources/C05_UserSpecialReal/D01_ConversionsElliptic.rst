

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Conversions of parameters of elliptic functions
===============================================================================






Elliptic nome `q(k)` (DAMath)
-------------------------------------------------------------------------------

.. method:: math53.elliptic_nome(z)

    Returns the elliptic nome  `q(k)` as a function of the modulus `|k| < 1`:. See also Wikipedia :cite:p:`WikipediaFun1001`,  MathWorld :cite:p:`WolframFun1001`, :cite:t:`Ehrhardt2018` (3.2.8).

    .. math:: q(k)=\exp \left(-\pi \frac{K'(k)}{K(k)} \right)


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticNome(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticNome('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticNome(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticNome('0.51')
        Gpr('5.3518479027559984754E-1')





Elliptic modulus `k(q)` (DAMath)
-------------------------------------------------------------------------------

.. method:: math53.elliptic_modulus(q)

    Returns the elliptic modulus k. as a function of the nome `|q|` \le 1.  See also MathWorld :cite:p:`WolframFun1004`, :cite:t:`Ehrhardt2018` (3.2.9).The modulus `k` is often used as argument of elliptic integrals and Jacobi elliptic functions, the nome `q` is used with Jacobi theta functions. `k(q)` is explicitly given by

    .. math ::  k(q) = \frac{\theta_2^2(q)}{\theta_3^2(q)}.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.EllipticModulus(0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.EllipticModulus('0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.EllipticModulus(0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.EllipticModulus('0.51')
        Gpr('5.3518479027559984754E-1')







Jacobi amplitude, `\mathrm{am}(x, k)` (DAMath)
-------------------------------------------------------------------------------

.. method:: math53.jacobi_amplitude(x, k)

    Returns the Jacobi amplitude function `\mathrm{am}(x, k)` for a given modulus `k`. This is the inverse function of Legendre’s elliptic function of the first kind: `\mathrm{am}(F(x, k), k) = x`. When `|k| < 1, \mathrm{am}(x, k)` is a monotone quasi-periodic function NIST :cite:p:`DLMFun1002`, 22.16.2: `\mathrm{am}(x + 2K(k), k) = \mathrm{am}(x, k) + \pi`, with the special case `\mathrm{am}(x, 0) = x`. When `|k| > 1, \mathrm{am}(x, k)` is periodic with period `4K(1/k)/k`, and if `|k| = 1`, then it is equal to the Gudermannian function `\mathrm{am}(x, \pm1) = \mathrm{gd}(x)`.

    See also  MathWorld :cite:p:`WolframFun1002`, NIST :cite:p:`DLMFun1002`, :cite:t:`Ehrhardt2018` (3.2.10).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiAmplitude(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiAmplitude(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiAmplitude(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiAmplitude(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')





