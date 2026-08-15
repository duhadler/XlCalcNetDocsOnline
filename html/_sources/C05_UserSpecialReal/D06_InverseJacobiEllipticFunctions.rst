

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Inverse Jacobi elliptic functions 
===============================================================================

The inverse Jacobi elliptic functions can be defined like the inverse trigonometric functions: e.g. if `\mathrm{sn}(y, k) = x` then `y = \mathrm{arcsn}(x, k)`; they are multivalued and their principal values are returned. The functions can be represented as elliptic integrals [30, §22.15(ii)] and they are computed with the incomplete elliptic integral `F(., k)` using the table from Abramowitz and Stegun [1, p.596].



Inverse Jacobi elliptic function `\mathrm{arcsn}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcsn(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcsn}(x, k)` for `|x| \le 1` and `|kx| \le 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.1).

    .. math::  \mathrm{arcsn}(x, k) = F(\mathrm{arcsin}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcSN(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcSN(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcSN(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcSN(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arccn}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arccn(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arccn}(x, k)` for `|x| < 1` if `k \le 1`, and `x^2 > 1 - 1/k^2` if `k > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018`  (3.2.12.2).

    .. math::  \mathrm{arccn}(x, k) = F(\mathrm{arccos}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcCN(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcCN(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcCN(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcCN(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arcdn}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcdn(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcdn}(x, k)` for `0 \le x \le 1` and `k^2 + x^2 > 1` if `|k| < 1`; and `|x| \le 1` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018`  (3.2.12.3).

    .. math:: \mathrm{arcdn}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1-x^2}{k^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcDN(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcDN(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcDN(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcDN(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arccd}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arccd(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arccd}(x, k)` for `|x| \le 1` if `|k| < 1`; and `|x| \ge 1` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.4).

    .. math:: \mathrm{arccd}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1-x^2}{1-k^2 x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcCD(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcCD(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcCD(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcCD(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arcsd}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcsd(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcsd}(x, k)` for `x \in \mathbb{R}` if `|k| \ge 1` and `|x| < 1/\sqrt{1 - k^2}` otherwise. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018`  (3.2.12.5).

    .. math:: \mathrm{arcsd}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{x^2}{1+k^2 x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcSD(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcSD(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcSD(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcSD(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arcnd}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcnd(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcnd}(x, k)` for `x \ge 1` and `x^2 \le k^2/(1 - k^2)` if `|k| < 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.6).

    .. math:: \mathrm{arcnd}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{x^2-1}{k^2 x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcND(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcND(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcND(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcND(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')





Inverse Jacobi elliptic function `\mathrm{arcdc}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcdc(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcdc}(x, k)` for `|x| \ge 1` if `|k| < 1`; and `|x| \le 1` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.7).

    .. math:: \mathrm{arcdc}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1-x^2-1}{k^2 - x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcDC(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcDC(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcDC(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcDC(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')






Inverse Jacobi elliptic function `\mathrm{arcnc}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcnc(x, k)

    Returns the inverse Jacobi elliptic function  `\mathrm{arcnc}(x, k)` for `x \ge 1`, and `x^2 \le k^2/(k^2 - 1)` for `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.8).

    .. math:: \mathrm{arcnc}(x, k) = F(\mathrm{arcsec}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcNC(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcNC(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcNC(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcNC(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arcsc}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcsc(x, k)

    Returns the inverse Jacobi elliptic function  `\mathrm{arcsc}(x, k)` for `x \in \mathbb{R}` if `|k| \le 1` and `|x| \le 1/\sqrt{
    k^2 - 1}` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.9).

    .. math:: \mathrm{arcsc}(x, k) = F(\mathrm{arctan}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcSC(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcSC(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcSC(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcSC(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arcns}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcns(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcns}(x, k)` for `|x| \ge 1` if `|k| < 1` and `|x| \ge |k|` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.10).

    .. math:: \mathrm{arcns}(x, k) = F(\mathrm{arccsc}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcNS(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcNS(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcNS(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcNS(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arcds}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcds(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcds}(x, k)` for `x \in \mathbb{R}` if `|k| > 1` and `|x| \ge \sqrt{ 1 - k^2}` if `|k| < 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.11).

    .. math:: \mathrm{arcds}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1}{k^2 + x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcDS(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcDS(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcDS(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcDS(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arccs}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobiArcCS(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arccs}(x, k)` for `x \in \mathbb{R}` if `|k| < 1` and `|x| \ge \sqrt{k^2 - 1}` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.12).

    .. math:: \mathrm{arccs}(x, k) = F(\mathrm{arccot}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import xreal
        >>> xreal.JacobiArcCS(0.8, 0.5)
        xreal('5.2359877559829887307E-1')
        >>> xreal.JacobiArcCS(0.8, '0.51')
        xreal('5.3518479027559984754E-1')


    An example in Visual Basic 

    .. code-block:: pycon

        >>> from xlcalcnet import Gpr
        >>> Gpr.JacobiArcCS(0.8, 0.5)
        Gpr('5.2359877559829887307E-1')
        >>> Gpr.JacobiArcCS(0.8, '0.51')
        Gpr('5.3518479027559984754E-1')






