

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}




|newpage|

Mpmath: Conversions of parameters of elliptic functions
===============================================================================



Elliptic functions historically comprise the elliptic integrals
and their inverses, and originate from the problem of computing the
arc length of an ellipse. From a more modern point of view,
an elliptic function is defined as a doubly periodic function, i.e.
a function which satisfies

.. math ::

    f(z + 2 \omega_1) = f(z + 2 \omega_2) = f(z)

for some half-periods `\omega_1, \omega_2` with `\mathrm{Im}[\omega_1 / \omega_2] > 0`. The canonical elliptic functions are the Jacobi elliptic functions. More broadly, this section includes  quasi-doubly periodic functions (such as the Jacobi theta functions) and other functions useful in the study of elliptic functions.

Many different conventions for the arguments of elliptic functions are in use. It is even standard to use different parameterizations for different functions in the same text or software. The usual parameters are the elliptic nome `q` or `\bar{q} = q^2`, which usually must satisfy `|q| < 1`; the elliptic parameter `m` (an arbitrary complex number); the elliptic modulus `k` (an arbitrary complex number); and the half-period ratio `\tau`, which usually must satisfy `\mathrm{Im}[\tau] > 0`.

In the context of Weierstrass elliptic functions, we also have the lattice roots `e_1, e_2, e_3`, which are the roots of the polynomial `4z^3 - g_2 z - g_3`, where `g_2` and `g_3` are the lattice invariants.

These quantities can be expressed in terms of each other using the following relations:

.. math :: m = k^2 = \frac{e_3 - e_2}{e_1 - e_2}

.. math :: \tau(m) = i \frac{K(1-m)}{K(m)}

.. math :: q(\tau) = e^{i \pi \tau}

.. math ::  \bar{q}(\tau) = q^2(\tau) = e^{2 i \pi \tau}

.. math ::  k(q) = \frac{\theta_2^2(q)}{\theta_3^2(q)},

where `K(\cdot)` denotes the complete elliptic integral of the first kind (Legendre), and `\theta_i(q)` denote the Jacobi theta functions.



For convenience, functions are provided to convert between the various parameters (:ref:`qfrom() <rst_mpm_qfrom>`, :ref:`mfrom() <rst_mpm_mfrom>`, :ref:`kfrom() <rst_mpm_kfrom>`, :ref:`taufrom() <rst_mpm_taufrom>`, :ref:`qbarfrom() <rst_mpm_qbarfrom>`).

See also Wikipedia :cite:p:`WikipediaFun155`, Wikipedia :cite:p:`WikipediaFun155a`, MathWorld :cite:p:`WolframFun155`, MathWorld :cite:p:`WolframFun155a`, NIST :cite:p:`DLMFun155`, Mpmath :cite:p:`MpmathFun155`, 






.. _rst_mpm_qfrom: 

Elliptic nome `q`: from `q, m, k, \tau, \bar{q}`
-------------------------------------------------------------------------------


.. method:: ctx.qfrom(**kwargs)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.



    Returns the elliptic nome q. See also Wikipedia :cite:p:`WikipediaFun1001`, MathWorld :cite:p:`WolframFun1001`, Mpmath :cite:p:`MpmathFun1001`


    This function computes the value of the elliptic nome `q(k)` as a function of the modulus `|k| < 1`:

    .. math:: q(k)=\exp \left(-\pi \frac{K'(k)}{K(k)} \right)


    Returns the elliptic nome `q`, given any of `q, m, k, \tau, \bar{q}`::


        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qfrom(q=0.25)
        0.25
        >>> qfrom(m=mfrom(q=0.25))
        0.25
        >>> qfrom(k=kfrom(q=0.25))
        0.25
        >>> qfrom(tau=taufrom(q=0.25))
        (0.25 + 0.0j)
        >>> qfrom(qbar=qbarfrom(q=0.25))
        0.25









.. _rst_mpm_qbarfrom: 

Number-theoretic nome `\bar q = q^2` (qbar): from `q, m, k, \tau, \bar{q}`
-------------------------------------------------------------------------------


.. method:: ctx.qbarfrom(**kwargs)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.



    Returns the number-theoretic nome qbar. See also MathWorld :cite:p:`WolframFun1001`, Mpmath :cite:p:`MpmathFun1002`

    Returns the number-theoretic nome `\bar q = q^2`, given any of
    `q, m, k, \tau, \bar{q}`::

        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> qbarfrom(qbar=0.25)
        0.25
        >>> qbarfrom(q=qfrom(qbar=0.25))
        0.25
        >>> qbarfrom(m=extraprec(20)(mfrom)(qbar=0.25))  # ill-conditioned
        0.25
        >>> qbarfrom(k=extraprec(20)(kfrom)(qbar=0.25))  # ill-conditioned
        0.25
        >>> qbarfrom(tau=taufrom(qbar=0.25))
        (0.25 + 0.0j)







.. _rst_mpm_mfrom: 

Elliptic parameter `m`: from `q, m, k, \tau, \bar{q}`
-------------------------------------------------------------------------------


.. method:: ctx.mfrom(**kwargs)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.


    Returns the elliptic parameter m.  See also MathWorld :cite:p:`WolframFun1003`, Mpmath :cite:p:`MpmathFun1003`




    Returns the elliptic parameter `m`, given any of
    `q, m, k, \tau, \bar{q}`::

        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> mfrom(m=0.25)
        0.25
        >>> mfrom(q=qfrom(m=0.25))
        0.25
        >>> mfrom(k=kfrom(m=0.25))
        0.25
        >>> mfrom(tau=taufrom(m=0.25))
        (0.25 + 0.0j)
        >>> mfrom(qbar=qbarfrom(m=0.25))
        0.25







.. _rst_mpm_kfrom: 

Elliptic modulus `k`: from `q, m, k, \tau, \bar{q}`
-----------------------------------------------------------------------------------------------


.. method:: ctx.kfrom(**kwargs)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.



    Returns the elliptic modulus k.  See also MathWorld :cite:p:`WolframFun1004`, Mpmath :cite:p:`MpmathFun1004`

    Returns the elliptic modulus `k`, given any of
    `q, m, k, \tau, \bar{q}`::

        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> kfrom(k=0.25)
        0.25
        >>> kfrom(m=mfrom(k=0.25))
        0.25
        >>> kfrom(q=qfrom(k=0.25))
        0.25
        >>> kfrom(tau=taufrom(k=0.25))
        (0.25 + 0.0j)
        >>> kfrom(qbar=qbarfrom(k=0.25))
        0.25






.. _rst_mpm_taufrom: 

Elliptic period ratio `\tau`: from `q, m, k, \tau, \bar{q}`
-------------------------------------------------------------------------------


.. method:: ctx.taufrom(**kwargs)

    where ``ctx`` is ``dec``, ``mpm``, ``fpm``, ``gmp`` or ``apm``.



    Returns the elliptic half-period ratio tau. See also Wikipedia :cite:p:`WikipediaFun1005`, MathWorld :cite:p:`WolframFun1005`, Mpmath :cite:p:`MpmathFun1005`

    Returns the elliptic half-period ratio `\tau`, given any of
    `q, m, k, \tau, \bar{q}`::

        >>> from xlcalcnet import *
        >>> mp.dps = 25; mp.pretty = True
        >>> taufrom(tau=0.5j)
        (0.0 + 0.5j)
        >>> taufrom(q=qfrom(tau=0.5j))
        (0.0 + 0.5j)
        >>> taufrom(m=mfrom(tau=0.5j))
        (0.0 + 0.5j)
        >>> taufrom(k=kfrom(tau=0.5j))
        (0.0 + 0.5j)
        >>> taufrom(qbar=qbarfrom(tau=0.5j))
        (0.0 + 0.5j)



