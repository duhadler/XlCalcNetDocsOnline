



************************************************************************
Lerch's phi and related
************************************************************************


The Lerch transcendent generalizes various other functions:

The polygamma function (see :ref:`polygamma() <rst_mpm_polygamma>`) is given by

.. math ::   \psi^{(n)}(z) = (-1)^{n+1} n! \: \Phi(1, n+1, z).


The polylogarithm  (see :ref:`polylog() <rst_mpm_polylog>`) is given by

.. math :: \text{Li}_s(z) = z \Phi(z, s, 1)).


The Legendre chi function (see :ref:`legendre_chi() <rst_mpm_legendre_chi>`) is  given by

.. math ::  \chi _{n}(z)=2^{-n}z\Phi (z^{2},n,1/2).


The Hurwitz zeta function  (see :ref:`hurwitz() <rst_mpm_hurwitz>`) is given by

.. math :: \zeta(s,a) =  \Phi(1, s, a).


The Riemann zeta function (see :ref:`zeta() <rst_mpm_zeta>`) is given by

.. math ::  \zeta (s)=\Phi (1,s,1).


The Dirichlet eta function (see :ref:`dirichlet_eta() <rst_mpm_dirichlet_eta>`) is given by

.. math ::  \eta (s)=\Phi (-1,s,1).



Various identities include:

.. math ::  \Phi (z,s,a)=z^{n}\Phi (z,s,a+n)+\sum _{k=0}^{n-1}{\frac {z^{k}}{(k+a)^{s}}}



and


.. math ::  \Phi (z,s-1,a)=\left(a+z{\frac {\partial }{\partial z}}\right)\Phi (z,s,a)

and

.. math ::  \Phi (z,s+1,a)=-\,{\frac {1}{s}}{\frac {\partial }{\partial a}}\Phi (z,s,a).



**Implementation notes**

The current Amath implementation is restricted to real arguments `z \leq 1, s \geq -1, a \geq 0`.

The current ARB implementation is restricted to calls to the polylogarithm or the Hurwitz zeta function, i.e. it expects `s=0` for arbitrary `z` and `a`, or `z=1` for arbitrary `s` and `a`, or `a` a nonnegative integer for arbitrary `z` and `s`, and otherwise returns NAN.










.. toctree ::
    :maxdepth: 5


    C01_LerchPhi.rst

    C02_Polygamma.rst

    C03_Polylogarithm.rst

    C04_HurwitzZeta.rst

    C05_RiemannZeta.rst


