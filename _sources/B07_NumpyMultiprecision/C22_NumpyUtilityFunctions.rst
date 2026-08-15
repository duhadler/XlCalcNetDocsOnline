




.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}



.. |spacingend| raw:: latex

   \end{spacing}







.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />








Summary and examples: Numpy utility functions
==========================================================



Exact mathematical constants
----------------------------------------------------------------

**ctx.zero**


Returns zero.

.. code-block:: python

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(repr(ctx.zero))
    0.0
    mpf('0.0')
    mpi('0.0', '0.0')
    Decimal('0')
    mpfr('0.0')
    arb('0')



**ctx.one**


Returns one.


.. code-block:: python

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(repr(ctx.one))
    1.0
    mpf('1.0')
    mpi('1.0', '1.0')
    Decimal('1')
    mpfr('1.0')
    arb('1.00')




**ctx.j**



Returns the imaginary unit.


.. code-block:: python

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(repr(ctx.j))
    1j
    mpc(real='0.0', imag='1.0')
    iv.mpc(mpi('0.0', '0.0'), mpi('1.0', '1.0'))
    DecCplx('0 + 1j')
    mpc('0.0+1.0j')
    acb('0 + 1.00j')




**ctx.inf**


Returns positive infinity.


.. code-block:: python

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(repr(ctx.inf))
    inf
    mpf('+inf')
    mpi('+inf', '+inf')
    Decimal('Infinity')
    mpfr('inf')
    arb('+inf')



**ctx.ninf**


Returns negative infinity.


.. code-block:: python

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(repr(ctx.ninf))
    -inf
    mpf('-inf')
    mpi('-inf', '-inf')
    Decimal('-Infinity')
    mpfr('-inf')
    arb('-inf')



**ctx.nan**


Returns Not-a-Number (NaN).


.. code-block:: python

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(repr(ctx.nan))
    nan
    mpf('nan')
    mpi('nan', 'nan')
    Decimal('NaN')
    mpfr('nan')
    arb('nan')












Complex components
----------------------------------------------------------------

**numpy.real**, **ctx.real**, **ctx.re**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.real.html#numpy.real

Return the real part of the complex argument.

.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.real(1 + 1j)
    1.0
    >>> a = np.array([1+2j, 3+4j, 5+6j])
    >>> np.real(a)
    array([1.,  3.,  5.])


From mpmath See also  Mpmath :cite:p:`MpmathFun914`.


Returns the real part of `x`, `\Re(x)`. :func:`~re`
converts a non-mpmath number to an mpmath number:

.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> mp.dps = 15; mp.pretty = False
    >>> x = 3
    >>> fp.re(x), mp.re(x), iv.re(x), dp.re(x), gp.re(x), ap.re(x)
    (3.0,
     mpf('3.0'),
     mpi('3.0', '3.0'),
     Decimal('3'),
     mpfr('3.0'),
     arb3_t('3.00000000000000'))

    >>> x = -1+4j
    >>> fp.re(x), mp.re(x), iv.re(x), dp.re(x), gp.re(x), ap.re(x)
    (-1.0,
     mpf('-1.0'),
     mpi('-1.0', '-1.0'),
     Decimal('-1'),
     mpfr('-1.0'),
     arb3_t('-1.00000000000000'))





**numpy.imag**, **ctx.imag**, **ctx.im**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.imag

Return the imaginary part of the complex argument.

.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.imag(1 + 1j)
    1.0
    >>> a = np.array([1+2j, 3+4j, 5+6j])
    >>> np.imag(a)
    array([2.,  4.,  6.])

From mpmath.  See also  Mpmath :cite:p:`MpmathFun915`.


Returns the imaginary part of `x`, `\Im(x)`. :func:`~im`
converts a non-mpmath number to an mpmath number:

.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> mp.dps = 15; mp.pretty = False
    >>> x = 3
    >>> fp.im(x), mp.im(x), iv.im(x), dp.im(x), gp.im(x), ap.im(x)
    (0.0, mpf('0.0'), mpi('0.0', '0.0'), Decimal('0'), mpfr('0.0'), arb3_t('0'))

    >>> x = -1+4j
    >>> fp.im(x), mp.im(x), iv.im(x), dp.im(x), gp.im(x), ap.im(x)
    (4.0,
     mpf('4.0'),
     mpi('4.0', '4.0'),
     Decimal('4.0'),
     mpfr('4.0'),
     arb3_t('4.00000000000000'))






**numpy.absolute**, **numpy.abs**, **ctx.fabs**

https://numpy.org/doc/stable/reference/generated/numpy.absolute.html

See also: https://numpy.org/doc/stable/reference/generated/numpy.fabs.html


Calculate the absolute  value of `x`, `|x|`, element-wise.

.. code-block:: pycon

    >>> x = np.array([-1.2, 1.2])
    >>> np.absolute(x)
    array([ 1.2,  1.2])
    >>> np.absolute(1.2 + 1j)
    1.5620499351813308

The abs function can be used as a shorthand for np.absolute on ndarrays.

.. code-block:: pycon

    >>> x = np.array([-1.2, 1.2])
    >>> abs(x)
    array([1.2, 1.2])

From mpmath. See also  Mpmath :cite:p:`MpmathFun912`.


.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> fp.fabs(3), mp.fabs(3), iv.fabs(3), dp.fabs(3), gp.fabs(3), ap.fabs(3)
    (3.0, mpf('3.0'), mpi('3.0', '3.0'), Decimal('3'), 3, 3)
    >>> fp.fabs(-3), mp.fabs(-3), iv.fabs(-3), dp.fabs(-3), gp.fabs(-3), ap.fabs(-3)
    (3.0, mpf('3.0'), mpi('3.0', '3.0'), Decimal('3'), 3, 3)
    >>> fp.fabs(3+4j), mp.fabs(3+4j), iv.fabs(3+4j), dp.fabs(3+4j), gp.fabs(3+4j), ap.fabs(3+4j)
    (5.0, mpf('5.0'), mpi('5.0', '5.0'), Decimal('5.0'), 5.0, 5.0)




**numpy.angle**, **ctx.angle**, **ctx.arg**, **ctx.phase**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.angle.html

Return the angle of the complex argument. Although the angle of the complex number 0 is undefined, numpy.angle(0) returns the value 0.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.angle([1.0, 1.0j, 1+1j])               # in radians
    array([ 0.        ,  1.57079633,  0.78539816]) # may vary
    >>> np.angle(1+1j, deg=True)                  # in degrees
    45.0

From mpmath. See also  Mpmath :cite:p:`MpmathFun916`.



Example:

.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> mp.dps = 15; mp.pretty = True
    >>> x = 3
    >>> fp.arg(x), mp.arg(x), iv.arg(x), dp.arg(x), gp.arg(x), ap.arg(x)
    (0.0, mpf('0.0'), mpi('0.0', '0.0'), Decimal('0.0'), mpfr('0.0'), arb3_t('0'))

    >>> x = 3+3j
    >>> fp.arg(x), mp.arg(x), iv.arg(x), dp.arg(x), gp.arg(x), ap.arg(x)
    (0.7853981633974483,
     mpf('0.78539816339744828'),
     mpi('0.78539816339744828', '0.78539816339744839'),
     Decimal('0.785398163397448'),
     mpfr('0.78539816339744828'),
     arb3_t('[0.785398163397448 +/- 3.35e-16]'))

    >>> x = 3j
    >>> fp.arg(x), mp.arg(x), iv.arg(x), dp.arg(x), gp.arg(x), ap.arg(x)
    (1.5707963267948966,
     mpf('1.5707963267948966'),
     mpi('1.5707963267948966', '1.5707963267948968'),
     Decimal('1.5707963267949'),
     mpfr('1.5707963267948966'),
     arb3_t('[1.57079632679490 +/- 3.56e-15]'))

    >>> x = -3
    >>> fp.arg(x), mp.arg(x), iv.arg(x), dp.arg(x), gp.arg(x), ap.arg(x)
    (3.141592653589793,
     mpf('3.1415926535897931'),
     mpi('3.1415926535897931', '3.1415926535897936'),
     Decimal('3.14159265358979'),
     mpfr('3.1415926535897931'),
     arb3_t('[3.14159265358979 +/- 3.34e-15]'))


The angle is defined to satisfy `-\pi < \arg(x) \le \pi` and
with the sign convention that a nonnegative imaginary part
results in a nonnegative argument.

The value returned by :func:`~arg` is an ``mpf`` instance.







**numpy.sign**, **ctx.sign**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.sign.html

Returns an element-wise indication of the sign of a number.

The sign function returns -1 if x < 0, 0 if x==0, 1 if x > 0. nan is returned for nan inputs.

For complex inputs, the sign function returns sign(x.real) + 0j if x.real != 0 else sign(x.imag) + 0j.

complex(nan, 0) is returned for complex nan inputs.

.. code-block:: pycon

    >>> np.sign([-5., 4.5])
    array([-1.,  1.])
    >>> np.sign(0)
    0
    >>> np.sign(5-2j)
    (1+0j)


From mpmath. See also  Mpmath :cite:p:`MpmathFun913`.



Returns the sign of `x`, defined as `\mathrm{sign}(x) = x / |x|`
(with the special case `\mathrm{sign}(0) = 0`):


.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> mp.dps = 15; mp.pretty = False
    >>> x = 10
    >>> fp.sign(x), mp.sign(x), iv.sign(x), dp.sign(x), gp.sign(x), ap.sign(x)
    (1.0,
     mpf('1.0'),
     mpi('1.0', '1.0'),
     Decimal('1'),
     1,
     arb3_t('1.00000000000000'))

    >>> x = -10
    >>> fp.sign(x), mp.sign(x), iv.sign(x), dp.sign(x), gp.sign(x), ap.sign(x)
    (-1.0,
     mpf('-1.0'),
     mpi('-1.0', '-1.0'),
     Decimal('-1'),
     -1,
     arb3_t('-1.00000000000000'))

    >>> x = 0
    >>> fp.sign(x), mp.sign(x), iv.sign(x), dp.sign(x), gp.sign(x), ap.sign(x)
    (0.0, mpf('0.0'), mpi('-1.0', '-1.0'), Decimal('0'), 0, arb3_t('0'))


Note that the sign function is also defined for complex numbers,
for which it gives the projection onto the unit circle:

.. code-block:: pycon

    >>> mp.dps = 15; mp.pretty = True
    >>> x = 1+1j
    >>> fp.sign(x), mp.sign(x), iv.sign(x), dp.sign(x), gp.sign(x), ap.sign(x)
    ((0.7071067811865475+0.7071067811865475j),
     mpc(real='0.70710678118654746', imag='0.70710678118654746'),
     iv.mpc(mpi('0.7071067811703', '0.7071067811994'), mpi('0.7071067811703', '0.7071067811994')),
     DecCplx('0.707106781186547 + 0.707106781186547j'),
     mpc('0.70710678118654746+0.70710678118654746j'),
     acb3_t('[0.707106781186548 +/- 6.50e-16] + [0.707106781186548 +/- 6.50e-16]j'))






**numpy.conjugate**, **numpy.conj**

https://numpy.org/doc/stable/reference/generated/numpy.conj.html

Return the complex conjugate, element-wise.

The complex conjugate of a complex number is obtained by changing the sign of its imaginary part.

.. code-block:: pycon

    >>> np.conjugate(1+2j)
    (1-2j)

    >>> x = np.eye(2) + 1j * np.eye(2)
    >>> np.conjugate(x)
    array([[ 1.-1.j,  0.-0.j],
           [ 0.-0.j,  1.-1.j]])


From mpmath. See also  Mpmath :cite:p:`MpmathFun917`.



!!! Error in iv with complex input !!!



Returns the complex conjugate of `x`, `\overline{x}`. Unlike
``x.conjugate()``, :func:`~im` converts `x` to a mpmath number:

Example:

.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> mp.dps = 15; mp.pretty = True
    >>> x = 3
    >>> fp.conj(x), mp.conj(x), iv.conj(x), dp.conj(x), gp.conj(x), ap.conj(x)
    (3.0,
     mpf('3.0'),
     mpi('3.0', '3.0'),
     Decimal('3'),
     mpfr('3.0'),
     arb3_t('3.00000000000000'))

    >>> x = -1+4j
    >>> fp.conj(x), mp.conj(x), dp.conj(x), gp.conj(x), ap.conj(x)
    ((-1-4j),
     mpc(real='-1.0', imag='-4.0'),
     DecCplx('-1 - 4.0j'),
     mpc('-1.0-4.0j'),
     acb3_t('-1.00000000000000 - 4.00000000000000j'))







Array contents
----------------------------------------------------------------


**numpy.isfinite**, **ctx.isfinite**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isfinite.html

Test element-wise for finiteness (not infinity and not Not a Number). The result is returned as a boolean array. Not a Number, positive infinity and negative infinity are considered to be non-finite.

NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). This means that Not a Number is not equivalent to infinity. Also that positive infinity is not equivalent to negative infinity. But infinity is equivalent to positive infinity. Errors result if the second argument is also supplied when x is a scalar input, or if first and second arguments have different shapes.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isfinite(1)
    True
    >>> np.isfinite(0)
    True
    >>> np.isfinite(np.nan)
    False
    >>> np.isfinite(np.inf)
    False
    >>> np.isfinite(np.NINF)
    False
    >>> np.isfinite([np.log(-1.),1.,np.log(0)])
    array([False,  True, False])

    >>> x = np.array([-np.inf, 0., np.inf])
    >>> y = np.array([2, 2, 2])
    >>> np.isfinite(x, y)
    array([0, 1, 0])
    >>> y
    array([0, 1, 0])


From mpmath. See also  Mpmath :cite:p:`MpmathFun930`.

Return *True* if *x* is a finite number, i.e. neither an infinity or a NaN.

Example:

.. code-block:: pycon

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(ctx.ctx.isfinite(ctx.inf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(ctx.ninf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(ctx.nan), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(3), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(3+4j), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(ctx.mpc(3,ctx.nan)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(ctx.mpc(ctx.nan,3)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(ctx.mpc(3,ctx.inf)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ctx.isfinite(ctx.mpc(ctx.inf,3)), end=', ')
    False, False, False, False, False, False, 




**numpy.isinf**, **ctx.isinf**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isinf

Test element-wise for positive or negative infinity.

Returns a boolean array of the same shape as x, True where ``x == +/-inf``, otherwise False. NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). Errors result if the second argument is supplied when the first argument is a scalar, or if the first and second arguments have different shapes.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isinf(np.inf)
    True
    >>> np.isinf(np.nan)
    False
    >>> np.isinf(np.NINF)
    True
    >>> np.isinf([np.inf, -np.inf, 1.0, np.nan])
    array([ True,  True, False, False])

    >>> x = np.array([-np.inf, 0., np.inf])
    >>> y = np.array([2, 2, 2])
    >>> np.isinf(x, y)
    array([1, 0, 1])
    >>> y
    array([1, 0, 1])


From mpmath. See also  Mpmath :cite:p:`MpmathFun926`.


Return *True* if the absolute value of *x* is infinite; otherwise return *False*.



Example:

.. code-block:: pycon

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(ctx.isinf(ctx.inf), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isinf(ctx.ninf), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isinf(ctx.nan), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isinf(3), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isinf(3+4j), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isinf(ctx.mpc(3,ctx.nan)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isinf(ctx.mpc(ctx.nan,3)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isinf(ctx.mpc(3,ctx.inf)), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isinf(ctx.mpc(ctx.inf,3)), end=', ')
    True, True, True, True, True, True, 








**numpy.isnan**, **ctx.isnan**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isnan.html#numpy.isnan

Test element-wise for NaN and return result as a boolean array. NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). This means that Not a Number is not equivalent to infinity.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isnan(np.nan)
    True
    >>> np.isnan(np.inf)
    False
    >>> np.isnan([np.log(-1.),1.,np.log(0)])
    array([ True, False, False])


From mpmath. See also  Mpmath :cite:p:`MpmathFun928`.



Return *True* if *x* is a NaN (not-a-number), or for a complex number, whether either the real or complex part is NaN;
otherwise return *False*:

Example:

.. code-block:: pycon


    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(ctx.isnan(ctx.nan), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isnan(ctx.inf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnan(ctx.ninf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnan(3), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnan(3+4j), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnan(ctx.mpc(3,ctx.inf)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnan(ctx.mpc(ctx.inf,3)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnan(ctx.mpc(3,ctx.nan)), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isnan(ctx.mpc(ctx.nan,3)), end=', ')
    True, True, True, True, True, True, 







**numpy.isnat**, **ctx.isnat**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isnat.html#numpy.isnat

Test element-wise for NaT (not a time) and return result as a boolean array.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isnat(np.datetime64("NaT"))
    True
    >>> np.isnat(np.datetime64("2016-01-01"))
    False
    >>> np.isnat(np.array(["NaT", "2016-01-01"], dtype="datetime64[ns]"))
    array([ True, False])




**numpy.isneginf**, **ctx.isneginf**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isneginf.html#numpy.isneginf

Test element-wise for negative infinity, return result as bool array. NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). Errors result if the second argument is also supplied when x is a scalar input, if first and second arguments have different shapes, or if the first argument has complex values.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isneginf(np.NINF)
    True
    >>> np.isneginf(np.inf)
    False
    >>> np.isneginf(np.PINF)
    False
    >>> np.isneginf([-np.inf, 0., np.inf])
    array([ True, False, False])

    >>> x = np.array([-np.inf, 0., np.inf])
    >>> y = np.array([2, 2, 2])
    >>> np.isneginf(x, y)
    array([1, 0, 0])
    >>> y
    array([1, 0, 0])





**numpy.isposinf**, **ctx.isposinf**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isposinf.html#numpy.isposinf

Test element-wise for positive infinity, return result as bool array. NumPy uses the IEEE Standard for Binary Floating-Point for Arithmetic (IEEE 754). Errors result if the second argument is also supplied when x is a scalar input, if first and second arguments have different shapes, or if the first argument has complex values.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isposinf(np.PINF)
    True
    >>> np.isposinf(np.inf)
    True
    >>> np.isposinf(np.NINF)
    False
    >>> np.isposinf([-np.inf, 0., np.inf])
    array([False, False,  True])

    >>> x = np.array([-np.inf, 0., np.inf])
    >>> y = np.array([2, 2, 2])
    >>> np.isposinf(x, y)
    array([0, 0, 1])
    >>> y
    array([0, 0, 1])





**ctx.isint(x, gaussian=False)**

From mpmath. See also  Mpmath :cite:p:`MpmathFun931`.

Return *True* if *x* is integer-valued; otherwise return *False*:

Example:

.. code-block:: pycon

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(ctx.isint(ctx.inf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isint(ctx.ninf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isint(ctx.nan), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isint(3), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isint(3+0j), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isint(3+4j), end=', ')
    False, False, False, False, False, False, 



Optionally, Gaussian integers can be checked for::

    >>> isint(3+2j, gaussian=True)
    True




**ctx.isnormal(x)**

From mpmath. . See also  Mpmath :cite:p:`MpmathFun929`.


Determine whether *x* is "normal" in the sense of floating-point
representation; that is, return *False* if *x* is zero, an
infinity or NaN; otherwise return *True*. 

By extension, a complex number *x* is considered "normal" if its magnitude is normal:

.. code-block:: pycon


    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(ctx.isnormal(ctx.nan), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnormal(ctx.inf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnormal(ctx.ninf), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnormal(0), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnormal(3), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isnormal(3+4j), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.isnormal(ctx.mpc(3,ctx.inf)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnormal(ctx.mpc(ctx.inf,3)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnormal(ctx.mpc(3,ctx.nan)), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.isnormal(ctx.mpc(ctx.nan,3)), end=', ')
    False, False, False, False, False, False, 









Array type testing
----------------------------------------------------------------


**numpy.iscomplex**, **ctx.iscomplex**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.iscomplex.html#numpy.iscomplex

Returns a bool array, where True if input element is complex. What is tested is whether the input has a non-zero imaginary part, not if the input type is complex.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.iscomplex([1+1j, 1+0j, 4.5, 3, 2, 2j])
    array([ True, False, False, False, False,  True])





**numpy.iscomplexobj**, **ctx.iscomplexobj**, **ctx.ismpc**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.iscomplexobj.html#numpy.iscomplexobj

Check for a complex type or an array of complex numbers. The type of the input is checked, not the value. Even if the input has an imaginary part equal to zero, iscomplexobj evaluates to True.



.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.iscomplexobj(1)
    False
    np.iscomplexobj(1+0j)
    True
    np.iscomplexobj([3, 1+0j, True])
    True



From mpmath:

Returns *True* if *x* is an instance of ``ctx.mpc``; otherwise returns *False*.


Example:

.. code-block:: pycon

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(ctx.ismpc(ctx.inf), end=', ')
    False, False, False, False, False, False,

    >>> for ctx in ctxall: print(ctx.ismpc(ctx.ninf), end=', ')
    False, False, False, False, False, False,

    >>> for ctx in ctxall: print(ctx.ismpc(ctx.nan), end=', ')
    False, False, False, False, False, False,

    >>> for ctx in ctxall: print(ctx.ismpc(ctx.one), end=', ')
    False, False, False, False, False, False,

    >>> for ctx in ctxall: print(ctx.ismpc(1.0), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ismpc(ctx.j), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.ismpc(1j), end=', ')
    True, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ismpc(ctx.mpc(3,ctx.inf)), end=', ')
    True, True, True, True, True, True, 










**numpy.isreal**, **ctx.isreal**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isreal.html#numpy.isreal

Returns a bool array, where True if input element is real. If element has complex type with zero complex part, the return value for that element is True. This function may behave unexpectedly for string or object arrays (see examples)


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j], dtype=complex)
    >>> np.isreal(a)
    array([False,  True,  True,  True,  True, False])

The function does not work on string arrays.

.. code-block:: pycon

    >>> a = np.array([2j, "a"], dtype="U")
    >>> np.isreal(a)  # Warns about non-elementwise comparison
    False

Returns True for all elements in input array of dtype=object even if any of the elements is complex.

.. code-block:: pycon

    >>> a = np.array([1, "2", 3+4j], dtype=object)
    >>> np.isreal(a)
    array([ True,  True,  True])

``isreal`` should not be used with object arrays

.. code-block:: pycon

    >>> a = np.array([1+2j, 2+1j], dtype=object)
    >>> np.isreal(a)
    array([ True,  True])





**numpy.isrealobj**, **ctx.isrealobj**, **ctx.ismpf**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isrealobj.html#numpy.isrealobj

Return True if x is a not complex type or an array of complex numbers. The type of the input is checked, not the value. So even if the input has an imaginary part equal to zero, ``isrealobj`` evaluates to False if the data type is complex. The function is only meant for arrays with numerical values but it accepts all other objects. Since it assumes array input, the return value of other objects may be True.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isrealobj('A string')
    True
    >>> np.isrealobj(False)
    True
    >>> np.isrealobj(None)
    True

    >>> np.isrealobj(1)
    True
    >>> np.isrealobj(1+0j)
    False
    >>> np.isrealobj([3, 1+0j, True])
    False



From mpmath:

Returns *True* if *x* is an instance of ``ctx.mpf``; otherwise returns *False*.


Example:

.. code-block:: pycon

    >>> from mpfunlab import fpm, mpm, ipm, dec, gmp, apm; ctxall = [fpm, mpm, ipm, dec, gmp, apm]
    >>> for ctx in ctxall: print(ctx.ismpf(ctx.inf), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.ismpf(ctx.ninf), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.ismpf(ctx.nan), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.ismpf(ctx.one), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in ctxall: print(ctx.ismpf(1.0), end=', ')
    True, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ismpf(ctx.j), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ismpf(1j), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in ctxall: print(ctx.ismpf(ctx.mpc(3,ctx.inf)), end=', ')
    False, False, False, False, False, False,











**numpy.isscalar**, **ctx.isscalar**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isscalar.html#numpy.isscalar

Returns True if the type of element is a scalar type. In most cases ``np.ndim(x) == 0`` should be used instead of this function, as that will also return true for 0d arrays. 


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isscalar(3.1)
    True
    >>> np.isscalar(np.array(3.1))
    False
    >>> np.isscalar([3.1])
    False
    >>> np.isscalar(False)
    True
    >>> np.isscalar('numpy')
    True

NumPy supports PEP 3141 numbers:

.. code-block:: pycon

    >>> from fractions import Fraction
    >>> np.isscalar(Fraction(5, 17))
    True
    >>> from numbers import Number
    >>> np.isscalar(Number())
    True









Using tolerances
----------------------------------------------------------------




**numpy.allclose**, **ctx.allclose**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.allclose.html#numpy.allclose

Returns True if two arrays are element-wise equal within a tolerance.

The tolerance values are positive, typically very small numbers. The relative difference (rtol * abs(b)) and the absolute difference atol are added together to compare against the absolute difference between a and b.

NaNs are treated as equal if they are in the same place and if ``equal_nan=True``. Infs are treated as equal if they are in the same place and of the same sign in both arrays.

If the following equation is element-wise True, then allclose returns True.

absolute(a - b) <= (atol + rtol * absolute(b))

The above equation is not symmetric in a and b, so that ``allclose(a, b)`` might be different from ``allclose(b, a)`` in some rare cases.

The comparison of a and b uses standard broadcasting, which means that a and b need not have the same shape in order for ``allclose(a, b)`` to evaluate to True. The same is true for equal but not array_equal.

allclose is not defined for non-numeric data types. bool is considered a numeric data-type for this purpose.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.allclose([1e10,1e-7], [1.00001e10,1e-8])
    False
    >>> np.allclose([1e10,1e-8], [1.00001e10,1e-9])
    True
    >>> np.allclose([1e10,1e-8], [1.0001e10,1e-9])
    False
    >>> np.allclose([1.0, np.nan], [1.0, np.nan])
    False
    >>> np.allclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)
    True





**numpy.isclose**, **ctx.isclose**, **ctx.almosteq(s, t, rel_eps=None, abs_eps=None)**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.isclose.html#numpy.isclose

Returns a boolean array where two arrays are element-wise equal within a tolerance.

The tolerance values are positive, typically very small numbers. The relative difference (rtol * abs(b)) and the absolute difference atol are added together to compare against the absolute difference between a and b.

For finite values, isclose uses the following equation to test whether two floating point values are equivalent.

absolute(a - b) <= (atol + rtol * absolute(b))

Unlike the built-in math.isclose, the above equation is not symmetric in a and b – it assumes b is the reference value – so that isclose(a, b) might be different from isclose(b, a). Furthermore, the default value of atol is not zero, and is used to determine what small values should be considered close to zero. The default value is appropriate for expected values of order unity: if the expected values are significantly smaller than one, it can result in false positives. atol should be carefully selected for the use case at hand. A zero value for atol will result in False if either a or b is zero.

isclose is not defined for non-numeric data types. bool is considered a numeric data-type for this purpose.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.isclose([1e10,1e-7], [1.00001e10,1e-8])
    array([ True, False])
    >>> np.isclose([1e10,1e-8], [1.00001e10,1e-9])
    array([ True, True])
    >>> np.isclose([1e10,1e-8], [1.0001e10,1e-9])
    array([False,  True])

    >>> np.isclose([1.0, np.nan], [1.0, np.nan])
    array([ True, False])
    >>> np.isclose([1.0, np.nan], [1.0, np.nan], equal_nan=True)
    array([ True, True])

    >>> np.isclose([1e-8, 1e-7], [0.0, 0.0])
    array([ True, False])
    >>> np.isclose([1e-100, 1e-7], [0.0, 0.0], atol=0.0)
    array([False, False])
    >>> np.isclose([1e-10, 1e-10], [1e-20, 0.0])
    array([ True,  True])
    >>> np.isclose([1e-10, 1e-10], [1e-20, 0.999999e-10], atol=0.0)
    array([False,  True])


From mpmath. See also  Mpmath :cite:p:`MpmathFun925`.

Determine whether the difference between `s` and `t` is smaller
than a given epsilon, either relatively or absolutely.

Both a maximum relative difference and a maximum difference
('epsilons') may be specified. The absolute difference is
defined as `|s-t|` and the relative difference is defined
as `|s-t|/\max(|s|, |t|)`.

If only one epsilon is given, both are set to the same value.
If none is given, both epsilons are set to `2^{-p+m}` where
`p` is the current working precision and `m` is a small
integer. The default setting typically allows :func:`~almosteq`
to be used to check for mathematical equality
in the presence of small rounding errors.

**Examples**


.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> mp.dps = 15; mp.pretty = False
    >>> s = 3.141592653589793; t = 3.141592653589790
    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.almosteq(s, t), end=', ')
    True, True, True, True, True, True,

    >>> s = 3.141592653589793; t = 3.141592653589700
    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.almosteq(s, t), end=', ')
    False, False, False, False, False, False, 

    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.almosteq(s, t, 1e-10), end=', ')
    True, True, True, True, True, True,  

    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.almosteq(1e-20, 2e-20), end=', ')
    True, True, True, True, True, True, 

    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(ctx.almosteq(1e-20, 2e-20, rel_eps=0, abs_eps=0), end=', ')
    False, False, False, False, False, False, 




     

Clipping (limiting) the values in an array.
----------------------------------------------------------------



**numpy.clip**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.clip.html

Clip (limit) the values in an array.

Given an interval, values outside the interval are clipped to the interval edges. For example, if an interval of ``[0, 1]`` is specified, values smaller than 0 become 0, and values larger than 1 become 1.

Equivalent to but faster than ``np.minimum(a_max, np.maximum(a, a_min))``.


No check is performed to ensure ``a_min < a_max``.

When a_min is greater than a_max, ``clip`` returns an array in which all values are equal to a_max, as shown in the second example.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> np.clip(a, 1, 8)
    array([1, 1, 2, 3, 4, 5, 6, 7, 8, 8])
    >>> np.clip(a, 8, 1)
    array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    >>> np.clip(a, 3, 6, out=a)
    array([3, 3, 3, 3, 4, 5, 6, 6, 6, 6])
    >>> a
    array([3, 3, 3, 3, 4, 5, 6, 6, 6, 6])
    >>> a = np.arange(10)
    >>> a
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> np.clip(a, [3, 4, 1, 1, 1, 4, 4, 4, 4, 4], 8)
    array([3, 4, 2, 3, 4, 5, 6, 7, 8, 8])



**numpy.real_if_close**

For a detailed description of parameters and return values see: 

https://numpy.org/doc/stable/reference/generated/numpy.real_if_close.html

If input is complex with all imaginary parts close to zero, return real parts.

"Close to zero" is defined as tol * (machine epsilon of the type for a).

Machine epsilon varies from machine to machine and between data types but Python floats on most platforms have a machine epsilon equal to 2.2204460492503131e-16. You can use ‘np.finfo(float).eps’ to print out the machine epsilon for floats.


.. code-block:: pycon

    >>> import numpy as np; from mpfunlab import mpm, dpm
    >>> np.finfo(float).eps
    2.2204460492503131e-16 # may vary

    >>> np.real_if_close([2.1 + 4e-14j, 5.2 + 3e-15j], tol=1000)
    array([2.1, 5.2])
    >>> np.real_if_close([2.1 + 4e-13j, 5.2 + 3e-15j], tol=1000)
    array([2.1+4.e-13j, 5.2 + 3e-15j])





**ctx.chop(x, tol=None)**

 See also  Mpmath :cite:p:`MpmathFun924`.



!!! iv context does not accept lists: NotImplementedError !!!

!!! dp, gp and ap contexts do not accept lists: return None !!!


Chops off small real or imaginary parts, or converts
numbers close to zero to exact zeros. The input can be a
single number or an iterable:

Example:

.. code-block:: pycon

    >>> from mpfunlab import mp, iv, fp, dp, gp, ap
    >>> mp.dps = 15; mp.pretty = False

    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(repr(ctx.chop(1e-10, tol = 1e-11)))
    1e-10
    mpf('1.0e-10')
    mpi('1.0e-10', '1.0e-10')
    Decimal('1E-10')
    mpfr('1e-10')
    arb3_t('[1.00000000000000e-10 +/- 3.66e-27]')

    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(repr(ctx.chop(1e-10, tol = 1e-9)))
    0.0
    mpf('0.0')
    mpi('0.0', '0.0')
    Decimal('0')
    mpfr('0.0')
    arb3_t('0')

    >>> for ctx in [fp, mp, iv, dp, gp, ap]: print(repr(ctx.chop(5+1e-10j, tol = 1e-9)))
    5.0
    mpf('5.0')
    mpi('5.0', '5.0')
    Decimal('5')
    mpfr('5.0')
    arb3_t('5.00000000000000')

    >>> for ctx in [mp, fp, dp, gp, ap]: print(ctx.chop([1.0, 1e-20, 3+1e-18j, -4, 2]))
    [mpf('1.0'), mpf('0.0'), mpf('3.0'), mpf('-4.0'), mpf('2.0')]
    [1.0, 0.0, 3.0, -4.0, 2.0]

    None
    None
    None


The tolerance defaults to ``100*eps``.









