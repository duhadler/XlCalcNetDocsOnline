

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Neville theta functions
===============================================================================



Neville `\theta_s(x,k)`
-------------------------------------------------------------------------------

.. method:: math53.neville_theta_s(x, k)

    Returns the Neville theta function `\displaystyle \theta_s(x,k) = \frac{2K(k)}{\pi} \frac{\theta_1(v,q(k))}{\theta'_1(0,q(k))}, \quad v = \frac{\pi x}{2K(k)}, |k| \le  1`, and `q(k)` is the elliptic nome.

    See also: Wikipedia :cite:p:`WikipediaFun170a`, MathWorld :cite:p:`WolframFun170s`, :cite:t:`Ehrhardt2018` (3.2.15.1).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.NevilleThetaS(1.5, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.NevilleThetaS(1.5, '0.51')
        ereal('5.3518479027559984754E-1')







Neville `\theta_c(x,k)`
-------------------------------------------------------------------------------

.. method:: math53.neville_theta_c(x, k)

    Returns the Neville theta function `\displaystyle \theta_c(x,k) = \frac{\theta_2(v,q(k))}{\theta_2(0,q(k))}, \quad v = \frac{\pi x}{2K(k)}, |k| \le  1`, and `q(k)` is the elliptic nome.

    See also: Wikipedia :cite:p:`WikipediaFun170a`, MathWorld :cite:p:`WolframFun170c`, :cite:t:`Ehrhardt2018` (3.2.15.2).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.NevilleThetaC(1.5, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.NevilleThetaC(1.5, '0.51')
        ereal('5.3518479027559984754E-1')







Neville `\theta_d(x,k)`
-------------------------------------------------------------------------------

.. method:: math53.neville_theta_d(x, k)

    Returns the Neville theta function `\displaystyle \theta_d(x,k) = \frac{\theta_3(v,q(k))}{\theta_3(0,q(k))}, \quad v = \frac{\pi x}{2K(k)}, |k| \le  1`, and `q(k)` is the elliptic nome.

    See also: Wikipedia :cite:p:`WikipediaFun170a`, MathWorld :cite:p:`WolframFun170d`, :cite:t:`Ehrhardt2018` (3.2.15.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.NevilleThetaD(1.5, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.NevilleThetaD(1.5, '0.51')
        ereal('5.3518479027559984754E-1')







Neville `\theta_n(x,k)`
-------------------------------------------------------------------------------

.. method:: math53.neville_theta_n(x, k)

    Returns the Neville theta function `\displaystyle \theta_n(x,k) = \frac{\theta_4(v,q(k))}{\theta_4(0,q(k))}, \quad v = \frac{\pi x}{2K(k)}, |k| \le  1`, and `q(k)` is the elliptic nome.

    See also: Wikipedia :cite:p:`WikipediaFun170a`, MathWorld :cite:p:`WolframFun170n`, :cite:t:`Ehrhardt2018` (3.2.15.4).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.NevilleThetaN(1.5, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.NevilleThetaN(1.5, '0.51')
        ereal('5.3518479027559984754E-1')






