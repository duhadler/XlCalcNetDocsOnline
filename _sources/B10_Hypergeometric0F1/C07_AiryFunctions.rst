

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Airy functions
===============================================================================


Airy function `\mathrm{Ai}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.airy_ai(x, scaled=False)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the Airy function `\mathrm{Ai}(x)`, with `x \in \mathbb{C}`. 

    If *scaled* is *True*, then `\mathrm{Ai}(x) \exp(\sqrt{x} \cdot 2x/3)` is returned, except for a real ``ctx`` with `x \le 0` where just `\mathrm{Ai}(x)` is returned.  


    See also Wikipedia :cite:p:`WikipediaFun146`, MathWorld :cite:p:`WolframFun146`, MathWorld :cite:p:`WolframFun146a`, NIST :cite:p:`DLMFun146`, BoostMath :cite:p:`BoostFun146a`, :cite:t:`Ehrhardt2018` (3.1.7.1), Mpmath :cite:p:`MpmathFun146a`. 

    The function `\mathrm{Ai}(x)` can be defined as


    .. math::  \mathrm{Ai}(x) = \frac{1}{3^{2/3}\Gamma(2/3)} {}_0F_1\left(\frac{2}{3},\frac{x^3}{9}\right) - \frac{x}{3^{1/3}\Gamma(1/3)} {}_0F_1\left(\frac{4}{3},\frac{x^3}{9}\right).




    The :ref:`wpf figures <rst_wpf_complex_function>` below are showing the real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex function `z = \mathrm{Ai}(x + iy)` `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`. 



|02a_TestAiryAi_re| `\quad` |02b_TestAiryAi_im| `\quad` |02c_TestAiryAi_abs|

.. |02a_TestAiryAi_re| image:: ../_static/ExplicitSurfaces/Cplx0F1/02a_TestAiryAi_re.3D.xml.jpg
   :width: 30 %

.. |02b_TestAiryAi_im| image:: ../_static/ExplicitSurfaces/Cplx0F1/02b_TestAiryAi_im.3D.xml.jpg
   :width: 30 %

.. |02c_TestAiryAi_abs| image:: ../_static/ExplicitSurfaces/Cplx0F1/02c_TestAiryAi_abs.3D.xml.jpg
   :width: 30 %




The corresponding scaled function looks like this:



|03a_TestAiryAie_re| `\quad` |03b_TestAiryAie_im| `\quad` |03c_TestAiryAie_abs|

.. |03a_TestAiryAie_re| image:: ../_static/ExplicitSurfaces/Cplx0F1/03a_TestAiryAie_re.3D.xml.jpg
   :width: 30 %

.. |03b_TestAiryAie_im| image:: ../_static/ExplicitSurfaces/Cplx0F1/03b_TestAiryAie_im.3D.xml.jpg
   :width: 30 %

.. |03c_TestAiryAie_abs| image:: ../_static/ExplicitSurfaces/Cplx0F1/03c_TestAiryAie_abs.3D.xml.jpg
   :width: 30 %





An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import xreal
    >>> xreal.AiryAi(0.5)
    xreal('5.2359877559829887307E-1')
    >>> xreal.AiryAi('0.51')
    xreal('5.3518479027559984754E-1')


An example in Visual Basic 

.. code-block:: pycon

    >>> from xlcalcnet import Gpr
    >>> Gpr.AiryAi(0.5)
    Gpr('5.2359877559829887307E-1')
    >>> Gpr.AiryAi('0.51')
    Gpr('5.3518479027559984754E-1')






|newpage|


Airy function `\mathrm{Bi}(x)`
-------------------------------------------------------------------------------

.. method:: ctx.airy_bi(x, scaled=False)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.


    Returns the Airy function `\mathrm{Bi}(x)`, with `x \in \mathbb{C}`. 

    If *scaled* is *True*, then `\mathrm{Bi}(x) \exp(-|\Re (\sqrt{x} \cdot 2x/3)|)` is returned, except for a real ``ctx`` with `x \le 0` where just `\mathrm{Bi}(x)` is returned.  
    
    See also Wikipedia :cite:p:`WikipediaFun146`, MathWorld :cite:p:`WolframFun146`, MathWorld :cite:p:`WolframFun146b`, NIST :cite:p:`DLMFun146`, BoostMath :cite:p:`BoostFun146b`, :cite:t:`Ehrhardt2018` (3.1.7.2), Mpmath :cite:p:`MpmathFun146b`.

    The function `\mathrm{Bi}(x)` can be defined as



    .. math::  \mathrm{Bi}(x) = \frac{1}{3^{1/6}\Gamma(2/3)} {}_0F_1\left(\frac{2}{3},\frac{x^3}{9}\right) + \frac{3^{1/6} x}{\Gamma(1/3)} {}_0F_1\left(\frac{4}{3},\frac{x^3}{9}\right).



    The :ref:`wpf figures <rst_wpf_complex_function>` below are showing the real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex function `z = \mathrm{Bi}(x + iy)` with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`. 




|04a_TestAiryBi_re| `\quad` |04b_TestAiryBi_im| `\quad` |04c_TestAiryBi_abs|

.. |04a_TestAiryBi_re| image:: ../_static/ExplicitSurfaces/Cplx0F1/04a_TestAiryBi_re.3D.xml.jpg
   :width: 30 %

.. |04b_TestAiryBi_im| image:: ../_static/ExplicitSurfaces/Cplx0F1/04b_TestAiryBi_im.3D.xml.jpg
   :width: 30 %

.. |04c_TestAiryBi_abs| image:: ../_static/ExplicitSurfaces/Cplx0F1/04c_TestAiryBi_abs.3D.xml.jpg
   :width: 30 %




The corresponding scaled function looks like this:



|05a_TestAiryBie_re| `\quad` |05b_TestAiryBie_im| `\quad` |05c_TestAiryBie_abs|

.. |05a_TestAiryBie_re| image:: ../_static/ExplicitSurfaces/Cplx0F1/05a_TestAiryBie_re.3D.xml.jpg
   :width: 30 %

.. |05b_TestAiryBie_im| image:: ../_static/ExplicitSurfaces/Cplx0F1/05b_TestAiryBie_im.3D.xml.jpg
   :width: 30 %

.. |05c_TestAiryBie_abs| image:: ../_static/ExplicitSurfaces/Cplx0F1/05c_TestAiryBie_abs.3D.xml.jpg
   :width: 30 %





An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import xreal
    >>> xreal.AiryBi(0.5)
    xreal('5.2359877559829887307E-1')
    >>> xreal.AiryBi('0.51')
    xreal('5.3518479027559984754E-1')


An example in Visual Basic 

.. code-block:: pycon

    >>> from xlcalcnet import Gpr
    >>> Gpr.AiryBi(0.5)
    Gpr('5.2359877559829887307E-1')
    >>> Gpr.AiryBi('0.51')
    Gpr('5.3518479027559984754E-1')






|newpage|


First derivative of the Airy function `\mathrm{Ai}`, `\mathrm{Ai}'(x)`
------------------------------------------------------------------------------------------------------

.. method:: ctx.airy_ai_prime(x, scaled=False)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns `\mathrm{Ai}'(x)`, the first derivative (with respect to `x`) of the  Airy function `\mathrm{Ai}(x)`, with `x \in \mathbb{C}`.


    If *scaled* is *True*, then `\mathrm{Ai}'(x) \exp(\sqrt{x} \cdot 2x/3)` is returned, except for a real ``ctx`` with `x \le 0` where just `\mathrm{Ai}'(x)` is returned.  


    See also Wikipedia :cite:p:`WikipediaFun146`, MathWorld :cite:p:`WolframFun146`, MathWorld :cite:p:`WolframFun146c`, NIST :cite:p:`DLMFun146`, BoostMath :cite:p:`BoostFun146c`, :cite:t:`Ehrhardt2018` (3.1.7.3). 


    The function `\mathrm{Ai}'(x)` can be defined as


    .. math::  \mathrm{Ai}'(x) = \frac{x^2}{2 \cdot 3^{2/3}\Gamma(2/3)} {}_0F_1\left(\frac{5}{3},\frac{x^3}{9}\right) - \frac{1}{3^{1/3}\Gamma(1/3)} {}_0F_1\left(\frac{1}{3},\frac{x^3}{9}\right).



    The :ref:`wpf figures <rst_wpf_complex_function>` below are showing the real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex function `z = \mathrm{Ai}'(x + iy)` with `\nu=0` and  `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.






An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import xreal
    >>> xreal.AiryAiPrime(0.5)
    xreal('5.2359877559829887307E-1')
    >>> xreal.AiryAiPrime('0.51')
    xreal('5.3518479027559984754E-1')


An example in Visual Basic 

.. code-block:: pycon

    >>> from xlcalcnet import Gpr
    >>> Gpr.AiryAiPrime(0.5)
    Gpr('5.2359877559829887307E-1')
    >>> Gpr.AiryAiPrime('0.51')
    Gpr('5.3518479027559984754E-1')






|newpage|


First derivative of the Airy function `\mathrm{Bi}`, `\mathrm{Bi}'(x)`
-----------------------------------------------------------------------------------------------------

.. method:: ctx.airy_bi_prime(x, scaled=False)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.
    
    Returns `\mathrm{Bi}'(x)`, the first derivative (with respect to `x`) of the  Airy function `\mathrm{Bi}(x)`, with `x \in \mathbb{C}`.
    
    If *scaled* is *True*, then `\mathrm{Bi}'(x) \exp(-|\Re (\sqrt{x} \cdot 2x/3)|)` is returned, except for a real ``ctx`` with `x \le 0` where just `\mathrm{Bi}'(x)` is returned.  


    See also Wikipedia :cite:p:`WikipediaFun146`, MathWorld :cite:p:`WolframFun146`, MathWorld :cite:p:`WolframFun146d`, NIST :cite:p:`DLMFun146`, BoostMath :cite:p:`BoostFun146d`, :cite:t:`Ehrhardt2018` (3.1.7.4) and  (3.1.7.6). 

    The function can be defined as


    .. math::  \mathrm{Bi}'(x) = \frac{x^2}{2 \cdot 3^{1/6}\Gamma(2/3)} {}_0F_1\left(\frac{5}{3},\frac{x^3}{9}\right) + \frac{3^{1/6}}{\Gamma(1/3)} {}_0F_1\left(\frac{1}{3},\frac{x^3}{9}\right).


    The :ref:`wpf figures <rst_wpf_complex_function>` below are showing the real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex function `z = \mathrm{Bi}'(x + iy)` with `\nu=0` and  `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.





An example in Python

.. code-block:: pycon

    >>> from xlcalcnet import xreal
    >>> xreal.AiryAiPrime(0.5)
    xreal('5.2359877559829887307E-1')
    >>> xreal.AiryAiPrime('0.51')
    xreal('5.3518479027559984754E-1')


An example in Visual Basic 

.. code-block:: pycon

    >>> from xlcalcnet import Gpr
    >>> Gpr.AiryAiPrime(0.5)
    Gpr('5.2359877559829887307E-1')
    >>> Gpr.AiryAiPrime('0.51')
    Gpr('5.3518479027559984754E-1')





|newpage|


Real zeros `a_k` of the Airy function `\mathrm{Ai}`, `\mathrm{Ai}(a_k)=0`
-------------------------------------------------------------------------------------------

.. method:: ctx.airy_ai_zero(k)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the `k`-th zero of the Airy Ai-function.  See also MathWorld :cite:p:`WolframFun147a`, NIST :cite:p:`DLMFun146`, BoostMath :cite:p:`BoostFun146b`, BoostMath :cite:p:`BoostFun146d`, Mpmath :cite:p:`MpmathFun146c`.


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.AiryAiZero(5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.AiryAiZero(17)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.AiryAiZero(5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.AiryAiZero(17)
        Gpr('5.3518479027559984754E-1')







|newpage|


Real zeros `b_k` of the Airy function `\mathrm{Bi}`, `\mathrm{Bi}(b_k)=0`
-------------------------------------------------------------------------------------------

.. method:: ctx.airy_bi_zero(k)

    where ``ctx`` is ``math53``, ``ctxboost`` or ``ctxflint``.

    Returns the `k`-th zero of the Airy Bi-function. See also Wikipedia :cite:p:`WikipediaFun146`, NIST :cite:p:`DLMFun146`, MathWorld :cite:p:`WolframFun147b`, BoostMath :cite:p:`BoostFun147`, Mpmath :cite:p:`MpmathFun147`.  


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.AiryBiZero(5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.AiryBiZero(17)
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.AiryBiZero(5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.AiryBiZero(17)
        Gpr('5.3518479027559984754E-1')







