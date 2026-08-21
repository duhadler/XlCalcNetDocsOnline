

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

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcSN(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcSN(0.8, '0.51')
        ereal('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arccn}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arccn(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arccn}(x, k)` for `|x| < 1` if `k \le 1`, and `x^2 > 1 - 1/k^2` if `k > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018`  (3.2.12.2).

    .. math::  \mathrm{arccn}(x, k) = F(\mathrm{arccos}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcCN(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcCN(0.8, '0.51')
        ereal('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arcdn}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcdn(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcdn}(x, k)` for `0 \le x \le 1` and `k^2 + x^2 > 1` if `|k| < 1`; and `|x| \le 1` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018`  (3.2.12.3).

    .. math:: \mathrm{arcdn}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1-x^2}{k^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcDN(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcDN(0.8, '0.51')
        ereal('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arccd}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arccd(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arccd}(x, k)` for `|x| \le 1` if `|k| < 1`; and `|x| \ge 1` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.4).

    .. math:: \mathrm{arccd}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1-x^2}{1-k^2 x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcCD(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcCD(0.8, '0.51')
        ereal('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arcsd}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcsd(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcsd}(x, k)` for `x \in \mathbb{R}` if `|k| \ge 1` and `|x| < 1/\sqrt{1 - k^2}` otherwise. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018`  (3.2.12.5).

    .. math:: \mathrm{arcsd}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{x^2}{1+k^2 x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcSD(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcSD(0.8, '0.51')
        ereal('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arcnd}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcnd(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcnd}(x, k)` for `x \ge 1` and `x^2 \le k^2/(1 - k^2)` if `|k| < 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.6).

    .. math:: \mathrm{arcnd}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{x^2-1}{k^2 x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcND(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcND(0.8, '0.51')
        ereal('5.3518479027559984754E-1')






Inverse Jacobi elliptic function `\mathrm{arcdc}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcdc(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcdc}(x, k)` for `|x| \ge 1` if `|k| < 1`; and `|x| \le 1` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.7).

    .. math:: \mathrm{arcdc}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1-x^2-1}{k^2 - x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcDC(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcDC(0.8, '0.51')
        ereal('5.3518479027559984754E-1')







Inverse Jacobi elliptic function `\mathrm{arcnc}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcnc(x, k)

    Returns the inverse Jacobi elliptic function  `\mathrm{arcnc}(x, k)` for `x \ge 1`, and `x^2 \le k^2/(k^2 - 1)` for `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.8).

    .. math:: \mathrm{arcnc}(x, k) = F(\mathrm{arcsec}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcNC(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcNC(0.8, '0.51')
        ereal('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arcsc}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcsc(x, k)

    Returns the inverse Jacobi elliptic function  `\mathrm{arcsc}(x, k)` for `x \in \mathbb{R}` if `|k| \le 1` and `|x| \le 1/\sqrt{
    k^2 - 1}` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.9).

    .. math:: \mathrm{arcsc}(x, k) = F(\mathrm{arctan}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcSC(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcSC(0.8, '0.51')
        ereal('5.3518479027559984754E-1')









Inverse Jacobi elliptic function `\mathrm{arcns}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcns(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcns}(x, k)` for `|x| \ge 1` if `|k| < 1` and `|x| \ge |k|` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.10).

    .. math:: \mathrm{arcns}(x, k) = F(\mathrm{arccsc}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcNS(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcNS(0.8, '0.51')
        ereal('5.3518479027559984754E-1')









Inverse Jacobi elliptic function `\mathrm{arcds}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobi_arcds(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arcds}(x, k)` for `x \in \mathbb{R}` if `|k| > 1` and `|x| \ge \sqrt{ 1 - k^2}` if `|k| < 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.11).

    .. math:: \mathrm{arcds}(x, k) = F\left(\mathrm{arcsin}\left(\sqrt{\frac{1}{k^2 + x^2}} \right), k \right).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcDS(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcDS(0.8, '0.51')
        ereal('5.3518479027559984754E-1')








Inverse Jacobi elliptic function `\mathrm{arccs}(x, k)`
-------------------------------------------------------------------------------

.. method:: math53.jacobiArcCS(x, k)

    Returns the inverse Jacobi elliptic function `\mathrm{arccs}(x, k)` for `x \in \mathbb{R}` if `|k| < 1` and `|x| \ge \sqrt{k^2 - 1}` if `|k| > 1`. See also NIST :cite:p:`DLMFun155`, :cite:t:`Ehrhardt2018` (3.2.12.12).

    .. math:: \mathrm{arccs}(x, k) = F(\mathrm{arccot}(x), k).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.JacobiArcCS(0.8, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.JacobiArcCS(0.8, '0.51')
        ereal('5.3518479027559984754E-1')







