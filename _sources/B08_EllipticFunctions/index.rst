




************************************************************************
Elliptic functions and related
************************************************************************



Elliptic functions historically comprise the elliptic integrals and their inverses, and originate from the problem of computing the arc length of an ellipse. From a more modern point of view, an elliptic function is defined as a doubly periodic function, i.e. a function which satisfies

.. math ::

    f(z + 2 \omega_1) = f(z + 2 \omega_2) = f(z)

for some half-periods `\omega_1, \omega_2` with `\mathrm{Im}[\omega_1 / \omega_2] > 0`. The canonical elliptic functions are the Jacobi elliptic functions. More broadly, this section includes  quasi-doubly periodic functions (such as the Jacobi theta functions) and other functions useful in the study of elliptic functions.

Many different conventions for the arguments of elliptic functions are in use. It is even standard to use different parameterizations for different functions in the same text or software. The usual parameters are the elliptic nome `q` or `\bar{q} = q^2` (see Wikipedia :cite:p:`WikipediaFun1001`, MathWorld :cite:p:`WolframFun1001`), which usually must satisfy `|q| < 1`; the elliptic parameter `m` (an arbitrary complex number, see MathWorld :cite:p:`WolframFun1003`); the elliptic modulus `k` (an arbitrary complex number, see MathWorld :cite:p:`WolframFun1004`.); and the half-period ratio `\tau` (see Wikipedia :cite:p:`WikipediaFun1005`, MathWorld :cite:p:`WolframFun1005`.), which usually must satisfy `\mathrm{Im}[\tau] > 0`.

In the context of Weierstrass elliptic functions, we also have the lattice roots `e_1, e_2, e_3`, which are the roots of the polynomial `4z^3 - g_2 z - g_3`, where `g_2` and `g_3` are the lattice invariants.

These quantities can be expressed in terms of each other using the following relations:

.. math :: m = k^2 = \frac{e_3 - e_2}{e_1 - e_2}

.. math :: \tau(m) = i \frac{K(1-m)}{K(m)}

.. math :: q(\tau) = e^{i \pi \tau}

.. math ::  \bar{q}(\tau) = q^2(\tau) = e^{2 i \pi \tau}


.. math:: q(k)=\exp \left(-\pi \frac{K'(k)}{K(k)} \right)

.. math ::  k(q) = \frac{\theta_2^2(q)}{\theta_3^2(q)},

where `K(\cdot)` denotes the complete elliptic integral of the first kind (Legendre), and `\theta_i(q)` denote the Jacobi theta functions.



See also Wikipedia :cite:p:`WikipediaFun155`, Wikipedia :cite:p:`WikipediaFun155a`, MathWorld :cite:p:`WolframFun155`, MathWorld :cite:p:`WolframFun155a`, NIST :cite:p:`DLMFun155`. 






.. toctree ::
   :maxdepth: 5


   C01_CarlsonIntegrals.rst

   C02_MathematicaIntegrals.rst

   C03_LegendreIntegrals.rst

   C04_JacobiEllipticFunctions.rst

   C05_JacobiThetafunctions.rst

   C06_WeierstrassConversions.rst

   C07_WeierstrassTau.rst

   C08_ModularFormsTau.rst


