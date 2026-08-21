

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|

Polylogarithm, and related functions
===============================================================================




Polylogarithm of integer order, `\mathrm{Li}_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.polylog_i(n, x)


    Returns the polylogarithm  of integer order `n`, `\displaystyle \mathrm{Li}_n(x) = \sum_{k=1}^{\infty} \frac{x^k}{k^n}, \quad n \in \mathbb{Z}, |x|<1 \,`, or its analytic continuation; for `n>0`, `x>1` the real part of `\mathrm{Li}_n(x)` is returned.

    See also   Wikipedia :cite:p:`WikipediaFun173`, MathWorld :cite:p:`WolframFun173`, NIST :cite:p:`DLMFun173`, :cite:t:`Ehrhardt2018` (3.6.11).



    Returns the polylogarithm function of integer order `n`.

    This function returns the polylogarithm function of integer order `n`

    .. math :: \text{Li}_n(z)=\sum_{k=1}^\infty \frac{z^{k}}{k^n}, \quad n \in  \mathbb{Z},  |z|<1.

    or its analytic continuation; for `n>0` there is the arguments restriction `x\leq 1`.




    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Polylog(2, 0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Polylog(2, '0.1')
        ereal('5.3518479027559984754E-1')












Fermi-Dirac integrals of integer order, `F_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.fermi_dirac_i(n, x)


    Returns the Fermi-Dirac integral of integer order `n`, `\displaystyle F_s(x) = \frac{1}{\Gamma(n+1)} \int_0^{\infty} \frac{t^n}{e^{t-x}+1} = -\text{Li}_{n+1}(-e^x) \,`.

    See also:  Wikipedia :cite:p:`WikipediaFun173c`, MathWorld :cite:p:`WolframFun173c`, :cite:t:`Ehrhardt2018` (3.6.8.2).




    This function returns the complete Fermi-Dirac integrals `F_n(x)` of integer order. They are defined for real orders `s>-1` by

    .. math :: F_s(x)=\frac{1}{\Gamma(s+1)} \int_0^\infty \frac{t^s}{e^{t-x}+1} \mathrm{d}t

    and by analytic continuation for `s \leq -1` using polylogarithms

    .. math :: F_s(x)=-\text{Li}_{s+1}(-e^x).



    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.FermiDirac(2,5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.FermiDirac(2,'51')
        ereal('5.3518479027559984754E-1')







Fermi-Dirac integral `F_{-1/2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.fermi_dirac_m05(x)

    Returns the Fermi-Dirac integral `F_{-1/2}(x)`. See also:  Wikipedia :cite:p:`WikipediaFun173c`, MathWorld :cite:p:`WolframFun173c`, :cite:t:`Ehrhardt2018` (3.6.8.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.FermiDiracm05(2,5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.FermiDiracm05('5.1')
        ereal('5.3518479027559984754E-1')







Fermi-Dirac integral `F_{1/2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.fermi_dirac_p05(x)

    Returns the Fermi-Dirac integral `F_{1/2}(x)`. See also:  Wikipedia :cite:p:`WikipediaFun173c`, MathWorld :cite:p:`WolframFun173c`, :cite:t:`Ehrhardt2018` (3.6.8.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.FermiDiracp05(2,5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.FermiDiracp05('5.1')
        ereal('5.3518479027559984754E-1')








Fermi-Dirac integral `F_{3/2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.fermi_dirac_p15(x)

    Returns the Fermi-Dirac integral `F_{3/2}(x)`. See also:  Wikipedia :cite:p:`WikipediaFun173c`, MathWorld :cite:p:`WolframFun173c`, :cite:t:`Ehrhardt2018` (3.6.8.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.FermiDiracp15(2,5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.FermiDiracp15('5.1')
        ereal('5.3518479027559984754E-1')







Fermi-Dirac integral `F_{5/2}(x)`
-------------------------------------------------------------------------------

.. method:: math53.fermi_dirac_p25(x, s)

    Returns the Fermi-Dirac integral `F_{5/2}(x)`. See also:  Wikipedia :cite:p:`WikipediaFun173c`, MathWorld :cite:p:`WolframFun173c`, :cite:t:`Ehrhardt2018` (3.6.8.3).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.FermiDiracp25(2,5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.FermiDiracp25('5.1')
        ereal('5.3518479027559984754E-1')



        


Inverse tangent integral, `\mathrm{Ti}_2(x)`
-------------------------------------------------------------------------------

.. method:: math53.tangent_int_2(x)

    Returns the  inverse tangent integral `\displaystyle \mathrm{Ti}_2(x)  =  \int_0^x  \frac{\arctan(t)}{t} \, \mathrm{d}t`.

    See also:  Wikipedia :cite:p:`WikipediaFun173a`, MathWorld :cite:p:`WolframFun173a`, :cite:t:`Ehrhardt2018` (3.6.16).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.TangentInt2(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.TangentInt2('0.1')
        ereal('5.3518479027559984754E-1')








Lobachevsky's log-cos integral, `L(x)`
-------------------------------------------------------------------------------

.. method:: math53.lobachevsky_c(x)

    Returns Lobachevsky's log-cos integral `\displaystyle L(x) = \int_0^x \log|\cos(t)| \, \mathrm{d}t`. See also: :cite:t:`Ehrhardt2018` (3.6.18).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LobachevskyC(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LobachevskyC('0.1')
        ereal('5.3518479027559984754E-1')







Lobachevsky's log-sin integral, `\Lambda(x)`
-------------------------------------------------------------------------------

.. method:: math53.lobachevsky_s(x, s)

    Returns Lobachevsky's log-sin integral `\displaystyle \Lambda(x) = \int_0^x \log|2\sin(t)| \, \mathrm{d}t`. See also: :cite:t:`Ehrhardt2018` (3.6.19).


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LobachevskyS(0.5)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LobachevskyS('0.1')
        ereal('5.3518479027559984754E-1')











Debye functions, `\mathrm{D}_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.debye(n,x)

    Returns the Debye function `\displaystyle \mathrm{D}_n(x) = \frac{n}{x^n} \int_0^x \frac{t^n}{e^t-1} \, \mathrm{d}t,  \quad n>0, x \ge 0`.

    See also:  Wikipedia :cite:p:`WikipediaFun323`, MathWorld :cite:p:`WolframFun323`, :cite:t:`Abramowitz1970` section 27.1,  :cite:t:`Ehrhardt2018` (3.10.6),  :cite:t:`Dubinov2008`.


    This routine returns the Debye functions

    .. math:: \text{D}_n(x) = \frac{n}{x^n} \int_0^x \frac{t^n}{e^t-1} \mathrm{d}t \quad (n>0, x \geq 0).


    .. math:: \text{D}_n^{(1)}(x) = \int_0^x \frac{t^n}{e^t-1} \mathrm{d}t = n! \zeta(n+1)  - n! Z_{n+1}(z) .


    .. math:: \text{D}_n^{(2)}(x) = \int_x^{\infty} \frac{t^n}{e^t-1} \mathrm{d}t = n! Z_{n+1}(z).


    .. math:: \text{D}^{(2)}_n(x) = \Gamma(n+1)\zeta(n+1) - \text{D}^{(1)}_n(x).


    .. math:: \text{D}^{(1)}_n(x) = n! \zeta(n+1) - \text{D}^{(2)}_n(x).


    .. math:: Z_{n+1}(z)=\sum _{k=0}^{n}\mathrm{Li} _{n-k+1}(e^{-z}){z^{k} \over k!} \quad (n=1,2,3,\ldots ).



    In terms of the incomplete zeta functions or "Debye functions" (Abramowitz & Stegun 1972, § 27.1):

    .. math:: Z_{n}(z)={1 \over (n-1)!}\int _{z}^{\infty }{t^{n-1} \over e^{t}-1}\mathrm{d}t\qquad (n=1,2,3,\ldots ),

    the polylogarithm Lin(z) for positive integer n may be expressed as the finite sum (Wood 1992, § 16):

    .. math:: \mathrm {Li} _{n}(e^{\mu })=\sum _{k=0}^{n-1}Z_{n-k}(-\mu ){\mu ^{k} \over k!}\qquad (n=1,2,3,\ldots ).

    A remarkably similar expression relates the "Debye functions" Zn(z) to the polylogarithm:

    .. math:: Z_{n}(z)=\sum _{k=0}^{n-1}\mathrm{Li}_{n-k}(e^{-z}){z^{k} \over k!}\qquad (n=1,2,3,\ldots ).





    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.Debye(1,3)
        ereal('5.2359877559829887307E-1')
        >>> ereal.Debye(2,13)
        ereal('5.3518479027559984754E-1')







Transport integral, `\mathrm{J}_n(x)`
-------------------------------------------------------------------------------

.. method:: math53.transport_jn(n,x)

    Returns the transport function `\displaystyle \mathrm{J}_n(x) =\int_0^x \frac{t^n e^t}{(e^t-1)^2} \, \mathrm{d}t,  \quad n \ge 2, x \ge 0`.

    See also: :cite:t:`Ehrhardt2018` (3.10.24).

    A.J. MacLeod, The numerical computation of transport integrals, 1992, Computer Physics Communications,
    69, pp. 229-234, https://doi.org/10.1016/0010-4655(92)90162-R,


    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.TransportJn(2,3)
        ereal('5.2359877559829887307E-1')
        >>> ereal.TransportJn(4,13)
        ereal('5.3518479027559984754E-1')







