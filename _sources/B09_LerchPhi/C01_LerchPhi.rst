

.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />




|newpage|


Lerch’s transcendent and Lerch’s zeta
===============================================================================


.. _rst_mpm_lerchphi: 

Lerch's transcendent, `\Phi(x,s,a)`
-------------------------------------------------------------------------------

.. method:: ctx.lerch_phi(s, z, a)

    where ``ctx`` is ``math53`` or ``ctxflint``.

    Returns the Lerch transcendent `\Phi(z, s, a)`. See also  Wikipedia :cite:p:`WikipediaFun1007`, MathWorld :cite:p:`WolframFun1007`, NIST :cite:p:`DLMFun1007`, :cite:t:`Ehrhardt2018` (3.6.10), Flint :cite:p:`FlintFun1007`,  Mpmath :cite:p:`MpmathFun1007`.  
    
    
    The function is defined for `|z| < 1` and `\Re{a} > 0` by

    .. math ::  \Phi(z,s,a) = \sum_{k=0}^{\infty} \frac{z^k}{(a+k)^s}

    and generally by the recurrence `\Phi(z,s,a) = z \Phi(z,s,a+1) + a^{-s}` along with the integral representation valid for `\Re{a} > 0`

    .. math :: \Phi(z,s,a) = \frac{1}{2 a^s} +  \int_0^{\infty} \frac{z^t}{(a+t)^s} \mathrm{d}t -  2 \int_0^{\infty} \frac{\sin(t \log z - s  \mathrm{arctan}(t/a)}{(a^2 + t^2)^{s/2} (e^{2 \pi t}-1)} \mathrm{d}t.


    The Amath implementation requires `x \le 1, s \ge -1, a \ge 0`. We have also `\Phi(x,0,a) = 1/(1-x)` and `\Phi(x,s,0) = \text{Li}_s(x)`.

    

See also: https://fredrikj.net/blog/2022/02/computing-the-lerch-transcendent/



    |01_0a_TestLerchPhiFlint_0_re| `\quad` |01_0b_TestLerchPhiFlint_0_im| `\quad` |01_0c_TestLerchPhiFlint_0_abs|

    .. |01_0a_TestLerchPhiFlint_0_re| image:: ../_static/ExplicitSurfaces/CplxLerch/01_0a_TestLerchPhiFlint_0_re.3D.xml.jpg
       :width: 30 %

    .. |01_0b_TestLerchPhiFlint_0_im| image:: ../_static/ExplicitSurfaces/CplxLerch/01_0b_TestLerchPhiFlint_0_im.3D.xml.jpg
       :width: 30 %

    .. |01_0c_TestLerchPhiFlint_0_abs| image:: ../_static/ExplicitSurfaces/CplxLerch/01_0c_TestLerchPhiFlint_0_abs.3D.xml.jpg
       :width: 30 %


    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.





    |01_1a_TestLerchPhiFlint_1_re| `\quad` |01_1b_TestLerchPhiFlint_1_im| `\quad` |01_1c_TestLerchPhiFlint_1_abs|

    .. |01_1a_TestLerchPhiFlint_1_re| image:: ../_static/ExplicitSurfaces/CplxLerch/01_1a_TestLerchPhiFlint_1_re.3D.xml.jpg
       :width: 30 %

    .. |01_1b_TestLerchPhiFlint_1_im| image:: ../_static/ExplicitSurfaces/CplxLerch/01_1b_TestLerchPhiFlint_1_im.3D.xml.jpg
       :width: 30 %

    .. |01_1c_TestLerchPhiFlint_1_abs| image:: ../_static/ExplicitSurfaces/CplxLerch/01_1c_TestLerchPhiFlint_1_abs.3D.xml.jpg
       :width: 30 %


   

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.






    |01_2a_TestLerchPhiFlint_2_re| `\quad` |01_2b_TestLerchPhiFlint_2_im| `\quad` |01_2c_TestLerchPhiFlint_2_abs|

    .. |01_2a_TestLerchPhiFlint_2_re| image:: ../_static/ExplicitSurfaces/CplxLerch/01_2a_TestLerchPhiFlint_2_re.3D.xml.jpg
       :width: 30 %

    .. |01_2b_TestLerchPhiFlint_2_im| image:: ../_static/ExplicitSurfaces/CplxLerch/01_2b_TestLerchPhiFlint_2_im.3D.xml.jpg
       :width: 30 %

    .. |01_2c_TestLerchPhiFlint_2_abs| image:: ../_static/ExplicitSurfaces/CplxLerch/01_2c_TestLerchPhiFlint_2_abs.3D.xml.jpg
       :width: 30 %

   

    **3D wpf plot**: real part (left figure), imaginary part (middle figure) and absolute value with color-coded phase (right figure) of the complex sine function `z = \sin(x + iy)`, with `-6 \le x \le 6` (blue axis), `-6 \le y \le 6` (red axis), `-10 \le z \le 10` (green axis). Function values are :ref:`loglog-transformed <rst_mpm_loglog_transformation>`.










    An example in Python

    .. code-block:: pycon

        >>> from xlcalcnet import ereal
        >>> ereal.LerchPhi(2,5, 0.5, 3)
        ereal('5.2359877559829887307E-1')
        >>> ereal.LerchPhi('5.1', 0.5, 3)
        ereal('5.3518479027559984754E-1')





    An example with real input, `x=1` (same result as Hurwitz zeta):

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '1.0'; s = '2.5'; a = '3.0'
        >>> \mathrm{d}x = dec.lerchphi(x, s, a); mx = mpm.lerchphi(x, s, a); gx = gmp.lerchphi(x, s, a)
        >>> fx = fpm.lerchphi(x, s, a); ax = apm.lerchphi(x, s, a)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 1.647105619542802986565586028223998768018E-1
        mpm: 1.647105619542802986565586028223998768018e-1
        gmp: 1.647105619542802986565586028223998768018E-01
        fpm: 1.64710561954280E-01
        apm: 1.647105619542802986565586028223998768018e-1 (1.742e-39%)


    An example with real input, `x<1, s \geq 0, a>0` (real result for real `x, s, a`):

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 40; x = '-11.5'; s = '2.5'; a = '7'
        >>> \mathrm{d}x = dec.lerchphi(x, s, a); mx = mpm.lerchphi(x, s, a); gx = gmp.lerchphi(x, s, a)
        >>> fx = fpm.lerchphi(x, s, a); ax = apm.lerchphi(x, s, a)
        >>> mpm.show([\mathrm{d}x, mx, gx, fx, ax], aligned=True)
        dec: 8.683791984836949848109532607614130875396E-4
        mpm: 8.683791984836949848109532607614130875396e-4
        gmp: 8.683791984836949848109532607614130875396E-04
        fpm: 8.68379198483695E-04
        apm: 8.683791984836949848109532607614130875396e-4 (4.518e-39%)


    An example with real input, complex result because `x>1` :

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '11.5'; s = '2.5'; a = '7'
        >>> \mathrm{d}z = dec.lerchphi(z, s, a); mz = mpm.lerchphi(z, s, a); gz = gmp.lerchphi(z, s, a)
        >>> fz = fpm.lerchphi(z, s, a); az = apm.lerchphi(z, s, a)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -1.1467900536878642113E-3               - 3.3910941716939727021E-7j
        mpm: -1.1467900536878642113e-3               - 3.3910941716939727021e-7j
        gmp: -1.1467900536878642113E-03              - 3.3910941716939727021E-07j
        fpm: -1.14679005368786E-03                   - 3.39109417169397E-07j
        apm: -1.1467900536878642113e-3 (-3.607e-19%) - 3.3910941716939727021e-7 (-2.263e-18%)j


    An example with complex input for `z` and `s`, but integer `a`:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; z = '11.0 + 2.0j'; s = '12.0 + 3.0j'; a = '7'
        >>> \mathrm{d}z = dec.lerchphi(z, s, a); mz = mpm.lerchphi(z, s, a); gz = gmp.lerchphi(z, s, a)
        >>> fz = fpm.lerchphi(z, s, a); az = apm.lerchphi(z, s, a)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: -1.3719753001137308013E-10              - 4.4570178228236195866E-12j
        mpm: -1.3719753001137308013e-10              - 4.4570178228236195866e-12j
        gmp: -1.3719753001137308013E-10              - 4.4570178228236195866E-12j
        fpm: -1.37197530011373E-10                   - 4.45701782282362E-12j
        apm: -1.3719752964740320417e-10 (-0.002002%) - 4.4570185825924147934e-12 (-0.06162%)j




    Evaluation works for complex arguments for  `z`, `s`, `a`, and `|z| \ge 1`, currently only for ``mpm``:

    .. code-block:: pycon

        >>> mpm.lerchphi(1+2j, 3-j, 4+2j)
        (0.002025009957009908600539469 + 0.003327897536813558807438089j)
        >>> mpm.lerchphi(-2,2,-2.5)
        -12.28676272353094275265944
        >>> mpm.lerchphi(10,10,10)
        (-4.462130727102185701817349e-11 - 1.575172198981096218823481e-12j)
        >>> mpm.lerchphi(10,10,-10.5)
        (112658784011940.5605789002 - 498113185.5756221777743631j)


|newpage|

.. _rst_mpm_lerchzeta: 

Lerch's zeta
-------------------------------------------------------------------------------


.. method:: ctxflint.lerch_zeta(lambda1, alpha, s)



    Returns the lerch zeta function.  See also  Wikipedia :cite:p:`WikipediaFun1007`, :cite:t:`Apostol1951`, :cite:t:`Ferreira2004`.

    The Lerch zeta function is given by

    .. math:: L(\lambda_1 ,\alpha ,s)=\sum _{n=0}^{\infty }{\frac {e^{2\pi i\lambda n}}{(n+\alpha )^{s}}}.


    The Lerch zeta function is related to the Lerch transcendent by

    .. math::  L(\lambda_1 ,\alpha ,s) = \,\Phi (e^{2\pi i\lambda_1 },s,\alpha ).



    For `\lambda_1` rational, `L(\lambda_1 ,\alpha ,s)` may be expressed as a finite sum over the Hurwitz zeta-function. Suppose `\lambda_1 =\frac {p}{q}` with `p,q \in \mathbb {Z}`  and `q>0`. Then `z=\omega =e^{2\pi i{\frac {p}{q}}}` and `\omega ^{q}=1`.

    .. math :: L(\lambda_1 ,\alpha ,s) = \Phi (\omega ,s,\alpha )=\sum _{n=0}^{\infty }{\frac {\omega ^{n}}{(n+\alpha )^{s}}} = \sum _{m=0}^{q-1}\omega ^{m}q^{-s}\zeta \left(s,{\frac {m+\alpha }{q}} \right)



    An example with complex input for `\lambda_1` and `s`, but integer `\alpha`:

    .. code-block:: pycon

        >>> from xlcalcnet import dec, mpm, gmp, fpm, apm
        >>> mpm.dps = 20; lambda1 = '1.0 + 0.5j'; s = '1.0 + 0.5j'; alpha = '1'
        >>> \mathrm{d}z = dec.lerch_zeta(lambda1, alpha, s); mz = mpm.lerch_zeta(lambda1, alpha, s)
        >>> gz = gmp.lerch_zeta(lambda1, alpha, s)
        >>> fz = fpm.lerch_zeta(lambda1, alpha, s); az = apm.lerch_zeta(lambda1, alpha, s)
        >>> mpm.show([\mathrm{d}z, mz, gz, fz, az], aligned=True)
        dec: 1.0208691797881172335E+0              - 7.6777982868597598415E-3j
        mpm: 1.0208691797881172335e+0              - 7.6777982868597598415e-3j
        gmp: 1.0208691797881172335E+00             - 7.6777982868597598415E-03j
        fpm: 1.02086917978812E+00                  - 7.67779828685976E-03j
        apm: 1.0208691797881172333e+0 (5.128e-17%) - 7.6777982868597598352e-3 (-4.862e-16%)j



