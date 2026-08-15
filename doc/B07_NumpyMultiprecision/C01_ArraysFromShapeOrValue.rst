




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









Numpy array creation from shape or value
==============================================================================

Slicing: https://stackoverflow.com/questions/509211/how-slicing-in-python-works




Note: Logic functions are not supported with multiprecision numbers as arguments

Note: input and output should use sqlite, xlread, enumerate

https://numpy.org/doc/stable/reference/generated/numpy.ufunc.html

https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where

https://numpy.org/doc/stable/reference/generated/numpy.choose.html#numpy.choose

https://numpy.org/doc/stable/reference/generated/numpy.select.html




Some text

https://numpy.org/doc/stable/glossary.html

https://numpy.org/doc/stable/reference/routines.array-creation.html

https://numpy.org/doc/stable/reference/maskedarray.baseclass.html#maskedarray-baseclass

https://numpy.org/doc/stable/reference/routines.ma.html

https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-attributes

https://numpy.org/doc/stable/reference/arrays.ndarray.html#array-methods




Conversion from integer, float or complex array
----------------------------------------------------------------

.. method:: npm.t(ctx, matA)

    The following code prepares the example:


    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> np.set_printoptions(linewidth=200)


    The following code creates a 3 x 3 array of type ``int``, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> matA = npm.array([[1,2,3], [4,5,6], [7,8,9]])
        >>> for ctx in ctx_all: matB = npm.t(ctx, matA); print(ctx.name + ':\n', matB)
        fpm:
         [[1.0 2.0 3.0]
         [4.0 5.0 6.0]
         [7.0 8.0 9.0]]
        mpm:
         [[mpf('1.0') mpf('2.0') mpf('3.0')]
         [mpf('4.0') mpf('5.0') mpf('6.0')]
         [mpf('7.0') mpf('8.0') mpf('9.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('2.0', '2.0') mpi('3.0', '3.0')]
         [mpi('4.0', '4.0') mpi('5.0', '5.0') mpi('6.0', '6.0')]
         [mpi('7.0', '7.0') mpi('8.0', '8.0') mpi('9.0', '9.0')]]
        dpm:
         [[Decimal('1') Decimal('2') Decimal('3')]
         [Decimal('4') Decimal('5') Decimal('6')]
         [Decimal('7') Decimal('8') Decimal('9')]]
        qpm:
         [[Fraction(1, 1) Fraction(2, 1) Fraction(3, 1)]
         [Fraction(4, 1) Fraction(5, 1) Fraction(6, 1)]
         [Fraction(7, 1) Fraction(8, 1) Fraction(9, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('2.0') mpfr('3.0')]
         [mpfr('4.0') mpfr('5.0') mpfr('6.0')]
         [mpfr('7.0') mpfr('8.0') mpfr('9.0')]]
        apm:
         [[1.00000000000000 2.00000000000000 3.00000000000000]
         [4.00000000000000 5.00000000000000 6.00000000000000]
         [7.00000000000000 8.00000000000000 9.00000000000000]]



    The following code creates a 3 x 3 array of random numbers of type ``float``, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> matA = matA = np.random.rand(3, 3)
        >>> for ctx in ctx_all: matB = npm.t(ctx, matA); print(ctx.name + ':\n', matB)
        fpm:
         [[0.6744434515981312 0.666353085652467 0.8970294047839491]
         [0.7559940954369713 0.9865280985239889 0.028695855364054057]
         [0.4402755692990895 0.9833733214486032 0.8904861723663713]]
        mpm:
         [[mpf('0.67444345159813124') mpf('0.66635308565246698') mpf('0.8970294047839491')]
         [mpf('0.75599409543697127') mpf('0.98652809852398893') mpf('0.028695855364054057')]
         [mpf('0.44027556929908951') mpf('0.98337332144860323') mpf('0.89048617236637129')]]
        ipm:
         [[mpi('0.67444345159813113', '0.67444345159813124') mpi('0.66635308565246698', '0.66635308565246709') mpi('0.89702940478394899', '0.8970294047839491')]
         [mpi('0.75599409543697127', '0.75599409543697138') mpi('0.98652809852398882', '0.98652809852398893') mpi('0.028695855364054054', '0.028695855364054057')]
         [mpi('0.44027556929908945', '0.44027556929908951') mpi('0.98337332144860312', '0.98337332144860323') mpi('0.89048617236637129', '0.8904861723663714')]]
        dpm:
         [[Decimal('0.6744434515981312') Decimal('0.666353085652467') Decimal('0.8970294047839491')]
         [Decimal('0.7559940954369713') Decimal('0.9865280985239889') Decimal('0.028695855364054057')]
         [Decimal('0.4402755692990895') Decimal('0.9833733214486032') Decimal('0.8904861723663713')]]
        qpm:
         [[Fraction(6586361832013, 9765625000000) Fraction(666353085652467, 1000000000000000) Fraction(8970294047839491, 10000000000000000)]
         [Fraction(7559940954369713, 10000000000000000) Fraction(9865280985239889, 10000000000000000) Fraction(28695855364054057, 1000000000000000000)]
         [Fraction(880551138598179, 2000000000000000) Fraction(614608325905377, 625000000000000) Fraction(8904861723663713, 10000000000000000)]]
        gpm:
         [[mpfr('0.67444345159813124') mpfr('0.66635308565246698') mpfr('0.8970294047839491')]
         [mpfr('0.75599409543697127') mpfr('0.98652809852398893') mpfr('0.028695855364054057')]
         [mpfr('0.44027556929908951') mpfr('0.98337332144860323') mpfr('0.89048617236637129')]]
        apm:
         [[[0.674443451598131 +/- 2.39e-16] [0.666353085652467 +/- 1.31e-16] [0.897029404783949 +/- 1.20e-16]]
         [[0.755994095436971 +/- 3.81e-16] [0.986528098523989 +/- 2.95e-16] [0.0286958553640541 +/- 5.00e-17]]
         [[0.440275569299089 +/- 5.09e-16] [0.983373321448603 +/- 2.33e-16] [0.890486172366371 +/- 3.98e-16]]]



    The following code creates a 3 x 3 array of random numbers of type ``complex``, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> matA = np.random.rand(3, 3) + 1j * np.random.rand(3, 3)
        >>> for ctx in ctx_all: matB = npm.t(ctx, matA); print(ctx.name + ':\n', matB)
        fpm:
         [[(0.567473450482438+0.775861558716608j) (0.9943782344345623+0.32179023975050236j) (0.2756393413671573+0.20943264624284674j)]
         [(0.6170089420540226+0.5969465058491088j) (0.694950179213084+0.6070312637822132j) (0.13610785528289382+0.9081719699208725j)]
         [(0.09188433151601583+0.26259046235301586j) (0.2551946534651285+0.9279289657328522j) (0.7147838697585964+0.043110422866829756j)]]
        mpm:
         [[mpc(real='0.56747345048243802', imag='0.775861558716608') mpc(real='0.9943782344345623', imag='0.32179023975050236') mpc(real='0.27563934136715729', imag='0.20943264624284674')]
         [mpc(real='0.61700894205402257', imag='0.5969465058491088') mpc(real='0.694950179213084', imag='0.60703126378221317') mpc(real='0.13610785528289382', imag='0.90817196992087246')]
         [mpc(real='0.091884331516015827', imag='0.26259046235301586') mpc(real='0.25519465346512848', imag='0.92792896573285222') mpc(real='0.71478386975859642', imag='0.043110422866829756')]]
        ipm:
         [[iv.mpc(mpi('0.56747345048243802', '0.56747345048243802'), mpi('0.775861558716608', '0.775861558716608'))
          iv.mpc(mpi('0.9943782344345623', '0.9943782344345623'), mpi('0.32179023975050236', '0.32179023975050236'))
          iv.mpc(mpi('0.27563934136715729', '0.27563934136715729'), mpi('0.20943264624284674', '0.20943264624284674'))]
         [iv.mpc(mpi('0.61700894205402257', '0.61700894205402257'), mpi('0.5969465058491088', '0.5969465058491088'))
          iv.mpc(mpi('0.694950179213084', '0.694950179213084'), mpi('0.60703126378221317', '0.60703126378221317'))
          iv.mpc(mpi('0.13610785528289382', '0.13610785528289382'), mpi('0.90817196992087246', '0.90817196992087246'))]
         [iv.mpc(mpi('0.091884331516015827', '0.091884331516015827'), mpi('0.26259046235301586', '0.26259046235301586'))
          iv.mpc(mpi('0.25519465346512848', '0.25519465346512848'), mpi('0.92792896573285222', '0.92792896573285222'))
          iv.mpc(mpi('0.71478386975859642', '0.71478386975859642'), mpi('0.043110422866829756', '0.043110422866829756'))]]
        dpm:
         [[DecCplx('0.567473450482438 + 0.775861558716608j') DecCplx('0.9943782344345623 + 0.32179023975050236j') DecCplx('0.2756393413671573 + 0.20943264624284674j')]
         [DecCplx('0.6170089420540226 + 0.5969465058491088j') DecCplx('0.694950179213084 + 0.6070312637822132j') DecCplx('0.13610785528289382 + 0.9081719699208725j')]
         [DecCplx('0.09188433151601583 + 0.26259046235301586j') DecCplx('0.2551946534651285 + 0.9279289657328522j') DecCplx('0.7147838697585964 + 0.043110422866829756j')]]
        qpm:
         [[QCplx('283736725241219/500000000000000 + 12122836854947/15625000000000j') QCplx('9943782344345623/10000000000000000 + 8044755993762559/25000000000000000j')
          QCplx('2756393413671573/10000000000000000 + 10471632312142337/50000000000000000j')]
         [QCplx('3085044710270113/5000000000000000 + 373091566155693/625000000000000j') QCplx('173737544803271/250000000000000 + 1517578159455533/2500000000000000j')
          QCplx('6805392764144691/50000000000000000 + 363268787968349/400000000000000j')]
         [QCplx('9188433151601583/100000000000000000 + 13129523117650793/50000000000000000j') QCplx('510389306930257/2000000000000000 + 4639644828664261/5000000000000000j')
          QCplx('1786959674396491/2500000000000000 + 10777605716707439/250000000000000000j')]]
        gpm:
         [[mpc('0.56747345048243802+0.775861558716608j') mpc('0.9943782344345623+0.32179023975050236j') mpc('0.27563934136715729+0.20943264624284674j')]
         [mpc('0.61700894205402257+0.5969465058491088j') mpc('0.694950179213084+0.60703126378221317j') mpc('0.13610785528289382+0.90817196992087246j')]
         [mpc('0.091884331516015827+0.26259046235301586j') mpc('0.25519465346512848+0.92792896573285222j') mpc('0.71478386975859642+0.043110422866829756j')]]
        apm:
         [[[0.567473450482438 +/- 2.44e-17] + [0.775861558716608 +/- 1.89e-18]j [0.994378234434562 +/- 3.03e-16] + [0.321790239750502 +/- 3.61e-16]j
          [0.275639341367157 +/- 2.87e-16] + [0.209432646242847 +/- 2.58e-16]j]
         [[0.617008942054023 +/- 4.32e-16] + [0.596946505849109 +/- 2.01e-16]j [0.694950179213084 +/- 3.91e-18] + [0.607031263782213 +/- 1.71e-16]j
          [0.136107855282894 +/- 1.81e-16] + [0.908171969920872 +/- 4.58e-16]j]
         [[0.0918843315160158 +/- 2.70e-17] + [0.262590462353016 +/- 1.37e-16]j [0.255194653465128 +/- 4.85e-16] + [0.927928965732852 +/- 2.18e-16]j
          [0.714783869758596 +/- 4.25e-16] + [0.0431104228668298 +/- 4.38e-17]j]]



Ones on the diagonal and zeros elsewhere: numpy.eye
----------------------------------------------------------------

.. method:: npm.eye(N, M=None, k=0, dtype=<class 'float'>, order='C', *, device=None, like=None)

    Return a 2-D array with ones on the diagonal and zeros elsewhere.


    See https://numpy.org/doc/stable/reference/generated/numpy.eye.html#numpy.eye for details.


    The following code creates a 3 x (M=4) array with ones on the first upper (k=1) diagonal and zeros elsewhere, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.eye(N=3, M=4, k=1, dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [[0.0 1.0 0.0 0.0]
         [0.0 0.0 1.0 0.0]
         [0.0 0.0 0.0 1.0]]
        mpm:
         [[mpf('0.0') mpf('1.0') mpf('0.0') mpf('0.0')]
         [mpf('0.0') mpf('0.0') mpf('1.0') mpf('0.0')]
         [mpf('0.0') mpf('0.0') mpf('0.0') mpf('1.0')]]
        ipm:
         [[mpi('0.0', '0.0') mpi('1.0', '1.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]
         [mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('1.0', '1.0') mpi('0.0', '0.0')]
         [mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('1.0', '1.0')]]
        dpm:
         [[Decimal('0.0') Decimal('1.0') Decimal('0.0') Decimal('0.0')]
         [Decimal('0.0') Decimal('0.0') Decimal('1.0') Decimal('0.0')]
         [Decimal('0.0') Decimal('0.0') Decimal('0.0') Decimal('1.0')]]
        qpm:
         [[Fraction(0, 1) Fraction(1, 1) Fraction(0, 1) Fraction(0, 1)]
         [Fraction(0, 1) Fraction(0, 1) Fraction(1, 1) Fraction(0, 1)]
         [Fraction(0, 1) Fraction(0, 1) Fraction(0, 1) Fraction(1, 1)]]
        gpm:
         [[mpfr('0.0') mpfr('1.0') mpfr('0.0') mpfr('0.0')]
         [mpfr('0.0') mpfr('0.0') mpfr('1.0') mpfr('0.0')]
         [mpfr('0.0') mpfr('0.0') mpfr('0.0') mpfr('1.0')]]
        apm:
         [[0 1.00000000000000 0 0]
         [0 0 1.00000000000000 0]
         [0 0 0 1.00000000000000]]



Identity array: numpy.identity
----------------------------------------------------------------

.. method:: npm.identity(n, dtype=None, *, like=None)

    Return the identity array. The identity array is a square array with ones on the main diagonal.

    See https://numpy.org/doc/stable/reference/generated/numpy.identity.html#numpy.identity for details.


    The following code creates a 3 x 3 identity array, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.identity(n=3, dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [[1.0 0.0 0.0]
         [0.0 1.0 0.0]
         [0.0 0.0 1.0]]
        mpm:
         [[mpf('1.0') mpf('0.0') mpf('0.0')]
         [mpf('0.0') mpf('1.0') mpf('0.0')]
         [mpf('0.0') mpf('0.0') mpf('1.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]
         [mpi('0.0', '0.0') mpi('1.0', '1.0') mpi('0.0', '0.0')]
         [mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('1.0', '1.0')]]
        dpm:
         [[Decimal('1.0') Decimal('0.0') Decimal('0.0')]
         [Decimal('0.0') Decimal('1.0') Decimal('0.0')]
         [Decimal('0.0') Decimal('0.0') Decimal('1.0')]]
        qpm:
         [[Fraction(1, 1) Fraction(0, 1) Fraction(0, 1)]
         [Fraction(0, 1) Fraction(1, 1) Fraction(0, 1)]
         [Fraction(0, 1) Fraction(0, 1) Fraction(1, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('0.0') mpfr('0.0')]
         [mpfr('0.0') mpfr('1.0') mpfr('0.0')]
         [mpfr('0.0') mpfr('0.0') mpfr('1.0')]]
        apm:
         [[1.00000000000000 0 0]
         [0 1.00000000000000 0]
         [0 0 1.00000000000000]]




Array of ones: numpy.ones
----------------------------------------------------------------

.. method:: npm.ones(shape, dtype=None, order='C', *, device=None, like=None)

    Return a new array of given shape and type, filled with ones.

    See https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones for details.



    The following code creates a 1 x 3 array of ones, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.ones(shape=(3,), dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [1.0 1.0 1.0]
        mpm:
         [mpf('1.0') mpf('1.0') mpf('1.0')]
        ipm:
         [mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0')]
        dpm:
         [Decimal('1') Decimal('1') Decimal('1')]
        qpm:
         [Fraction(1, 1) Fraction(1, 1) Fraction(1, 1)]
        gpm:
         [mpfr('1.0') mpfr('1.0') mpfr('1.0')]
        apm:
         [1.00000000000000 1.00000000000000 1.00000000000000]





Array of ones: numpy.ones_like
----------------------------------------------------------------

.. method:: npm.ones_like(a, dtype=None, order='K', subok=True, shape=None, *, device=None)

    Return an array of ones with the same shape and type as a given array.

    See https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html#numpy.ones_like for details.



    The following code creates a 2 x 3 array of ones, based on another ndarray, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> x = np.arange(6); x = x.reshape((2, 3))
        >>> for ctx in ctx_all: matB = npm.ones_like(x, dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [[1.0 1.0 1.0]
         [1.0 1.0 1.0]]
        mpm:
         [[mpf('1.0') mpf('1.0') mpf('1.0')]
         [mpf('1.0') mpf('1.0') mpf('1.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0')]
         [mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0')]]
        dpm:
         [[Decimal('1') Decimal('1') Decimal('1')]
         [Decimal('1') Decimal('1') Decimal('1')]]
        qpm:
         [[Fraction(1, 1) Fraction(1, 1) Fraction(1, 1)]
         [Fraction(1, 1) Fraction(1, 1) Fraction(1, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('1.0') mpfr('1.0')]
         [mpfr('1.0') mpfr('1.0') mpfr('1.0')]]
        apm:
         [[1.00000000000000 1.00000000000000 1.00000000000000]
         [1.00000000000000 1.00000000000000 1.00000000000000]]





Array of zeros: numpy.zeros
----------------------------------------------------------------

.. method:: npm.zeros(shape, dtype=float, order='C', *, like=None)

    Return a new array of given shape and type, filled with zeros.


    See https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros for details.



    The following code creates a 1 x 3 array of zeros, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.zeros(shape=(3,), dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [1.0 1.0 1.0]
        mpm:
         [mpf('1.0') mpf('1.0') mpf('1.0')]
        ipm:
         [mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0')]
        dpm:
         [Decimal('1') Decimal('1') Decimal('1')]
        qpm:
         [Fraction(1, 1) Fraction(1, 1) Fraction(1, 1)]
        gpm:
         [mpfr('1.0') mpfr('1.0') mpfr('1.0')]
        apm:
         [1.00000000000000 1.00000000000000 1.00000000000000]






Array of zeros: numpy.zeros_like
----------------------------------------------------------------

.. method:: npm.zeros_like(a, dtype=None, order='K', subok=True, shape=None, *, device=None)

    Return an array of zeros with the same shape and type as a given array.

    See https://numpy.org/doc/stable/reference/generated/numpy.zeros_like.html#numpy.zeros_like for details.



    The following code creates a 2 x 3 array of zeros, based on another ndarray, and then converts it into arrays of the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> x = np.arange(6); x = x.reshape((2, 3))
        >>> for ctx in ctx_all: matB = npm.zeros_like(x, dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [[0.0 0.0 0.0]
         [0.0 0.0 0.0]]
        mpm:
         [[mpf('0.0') mpf('0.0') mpf('0.0')]
         [mpf('0.0') mpf('0.0') mpf('0.0')]]
        ipm:
         [[mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]
         [mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]]
        dpm:
         [[Decimal('0') Decimal('0') Decimal('0')]
         [Decimal('0') Decimal('0') Decimal('0')]]
        qpm:
         [[Fraction(0, 1) Fraction(0, 1) Fraction(0, 1)]
         [Fraction(0, 1) Fraction(0, 1) Fraction(0, 1)]]
        gpm:
         [[mpfr('0.0') mpfr('0.0') mpfr('0.0')]
         [mpfr('0.0') mpfr('0.0') mpfr('0.0')]]
        apm:
         [[0 0 0]
         [0 0 0]]






Array of constant: numpy.full
----------------------------------------------------------------

.. method:: npm.full(shape, fill_value, dtype=None, order='C', *, device=None, like=None)

    Return a new array of given shape and type, filled with fill_value.

    See https://numpy.org/doc/stable/reference/generated/numpy.full.html#numpy.full for details.


    The following code creates a 2 x 2 array of tens, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: matB = npm.full(shape=(2,2), fill_value=ctx.t(10)); print(ctx.name + ':\n', matB)
        fpm:
         [[10. 10.]
         [10. 10.]]
        mpm:
         [[mpf('10.0') mpf('10.0')]
         [mpf('10.0') mpf('10.0')]]
        ipm:
         [[mpi('10.0', '10.0') mpi('10.0', '10.0')]
         [mpi('10.0', '10.0') mpi('10.0', '10.0')]]
        dpm:
         [[Decimal('10') Decimal('10')]
         [Decimal('10') Decimal('10')]]
        qpm:
         [[Fraction(10, 1) Fraction(10, 1)]
         [Fraction(10, 1) Fraction(10, 1)]]
        gpm:
         [[mpfr('10.0') mpfr('10.0')]
         [mpfr('10.0') mpfr('10.0')]]
        apm:
         [[10.0000000000000 10.0000000000000]
         [10.0000000000000 10.0000000000000]]


    The following code creates a 2 x 2 array of ``+inf``, using the multiprecision type ``ctx`` in ``ctx_all``. Note that ``qpm`` is excluded, sine it does not support  ``inf``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_fp = [fpm, mpm, ipm, dpm, gpm, apm]
        >>> for ctx in ctx_fp: matB = npm.full(shape=(2,2), fill_value=ctx.inf); print(ctx.name + ':\n', matB)
        fpm:
         [[inf inf]
         [inf inf]]
        mpm:
         [[mpf('+inf') mpf('+inf')]
         [mpf('+inf') mpf('+inf')]]
        ipm:
         [[mpi('+inf', '+inf') mpi('+inf', '+inf')]
         [mpi('+inf', '+inf') mpi('+inf', '+inf')]]
        dpm:
         [[Decimal('Infinity') Decimal('Infinity')]
         [Decimal('Infinity') Decimal('Infinity')]]
        gpm:
         [[mpfr('inf') mpfr('inf')]
         [mpfr('inf') mpfr('inf')]]
        apm:
         [[[+/- inf] [+/- inf]]
         [[+/- inf] [+/- inf]]]


    The following code creates a 2 x 2 array of ``nan``, using the multiprecision type ``ctx`` in ``ctx_all``. Note that ``qpm`` is excluded, sine it does not support  ``nan``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_fp = [fpm, mpm, ipm, dpm, gpm, apm]
        >>> for ctx in ctx_fp: matB = npm.full(shape=(2,2), fill_value=ctx.nan); print(ctx.name + ':\n', matB)
        fpm:
         [[nan nan]
         [nan nan]]
        mpm:
         [[mpf('nan') mpf('nan')]
         [mpf('nan') mpf('nan')]]
        ipm:
         [[mpi('nan', 'nan') mpi('nan', 'nan')]
         [mpi('nan', 'nan') mpi('nan', 'nan')]]
        dpm:
         [[Decimal('NaN') Decimal('NaN')]
         [Decimal('NaN') Decimal('NaN')]]
        gpm:
         [[mpfr('nan') mpfr('nan')]
         [mpfr('nan') mpfr('nan')]]
        apm:
         [[nan nan]
         [nan nan]]







Array of constant: numpy.full_like
----------------------------------------------------------------

.. method:: npm.full_like(a, fill_value, dtype=None, order='K', subok=True, shape=None, *, device=None)

    Return a full array with the same shape and type as a given array.

    See https://numpy.org/doc/stable/reference/generated/numpy.full_like.html#numpy.full_like for details.


    The following code creates a 2 x 2 array of tens, using the multiprecision type ``ctx`` in ``ctx_all``:

    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> x = np.arange(6); x = x.reshape((2, 3))
        >>> for ctx in ctx_all: matB = npm.full_like(x, fill_value=10.0, dtype=ctx); print(ctx.name + ':\n', matB)
        fpm:
         [[10.0 10.0 10.0]
         [10.0 10.0 10.0]]
        mpm:
         [[mpf('10.0') mpf('10.0') mpf('10.0')]
         [mpf('10.0') mpf('10.0') mpf('10.0')]]
        ipm:
         [[mpi('10.0', '10.0') mpi('10.0', '10.0') mpi('10.0', '10.0')]
         [mpi('10.0', '10.0') mpi('10.0', '10.0') mpi('10.0', '10.0')]]
        dpm:
         [[Decimal('10') Decimal('10') Decimal('10')]
         [Decimal('10') Decimal('10') Decimal('10')]]
        qpm:
         [[Fraction(10, 1) Fraction(10, 1) Fraction(10, 1)]
         [Fraction(10, 1) Fraction(10, 1) Fraction(10, 1)]]
        gpm:
         [[mpfr('10.0') mpfr('10.0') mpfr('10.0')]
         [mpfr('10.0') mpfr('10.0') mpfr('10.0')]]
        apm:
         [[10.0000000000000 10.0000000000000 10.0000000000000]
         [10.0000000000000 10.0000000000000 10.0000000000000]]





Array with ones at and below the given diagonal and zeros elsewhere: numpy.tri
---------------------------------------------------------------------------------

.. method:: npm.tri(N, M=None, k=0, dtype=<class 'float'>, *, like=None)

    Create an array with ones at and below the given diagonal and zeros elsewhere.


    See https://numpy.org/doc/stable/reference/generated/numpy.tri.html#numpy.tri for details

    An array with ones at and below the given diagonal and zeros elsewhere.


    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: x = npm.tri(N=3, M=5, k=2, dtype=ctx); print(ctx.name + ':\n', x)
        fpm:
         [[1.0 1.0 1.0 0.0 0.0]
         [1.0 1.0 1.0 1.0 0.0]
         [1.0 1.0 1.0 1.0 1.0]]
        mpm:
         [[mpf('1.0') mpf('1.0') mpf('1.0') mpf('0.0') mpf('0.0')]
         [mpf('1.0') mpf('1.0') mpf('1.0') mpf('1.0') mpf('0.0')]
         [mpf('1.0') mpf('1.0') mpf('1.0') mpf('1.0') mpf('1.0')]]
        ipm:
         [[mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]
         [mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('0.0', '0.0')]
         [mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('1.0', '1.0')]]
        dpm:
         [[Decimal('1.0') Decimal('1.0') Decimal('1.0') Decimal('0.0') Decimal('0.0')]
         [Decimal('1.0') Decimal('1.0') Decimal('1.0') Decimal('1.0') Decimal('0.0')]
         [Decimal('1.0') Decimal('1.0') Decimal('1.0') Decimal('1.0') Decimal('1.0')]]
        qpm:
         [[Fraction(1, 1) Fraction(1, 1) Fraction(1, 1) Fraction(0, 1) Fraction(0, 1)]
         [Fraction(1, 1) Fraction(1, 1) Fraction(1, 1) Fraction(1, 1) Fraction(0, 1)]
         [Fraction(1, 1) Fraction(1, 1) Fraction(1, 1) Fraction(1, 1) Fraction(1, 1)]]
        gpm:
         [[mpfr('1.0') mpfr('1.0') mpfr('1.0') mpfr('0.0') mpfr('0.0')]
         [mpfr('1.0') mpfr('1.0') mpfr('1.0') mpfr('1.0') mpfr('0.0')]
         [mpfr('1.0') mpfr('1.0') mpfr('1.0') mpfr('1.0') mpfr('1.0')]]
        apm:
         [[1.00000000000000 1.00000000000000 1.00000000000000 0 0]
         [1.00000000000000 1.00000000000000 1.00000000000000 1.00000000000000 0]
         [1.00000000000000 1.00000000000000 1.00000000000000 1.00000000000000 1.00000000000000]]



    .. code-block:: pycon

        >>> from mpfunlab import fpm, mpm, ipm, dpm, qpm, gpm, apm, npm, np
        >>> ctx_all = [fpm, mpm, ipm, dpm, qpm, gpm, apm]
        >>> for ctx in ctx_all: x = npm.tri(N=3, M=5, k=-1, dtype=ctx); print(ctx.name + ':\n', x)
        fpm:
         [[0.0 0.0 0.0 0.0 0.0]
         [1.0 0.0 0.0 0.0 0.0]
         [1.0 1.0 0.0 0.0 0.0]]
        mpm:
         [[mpf('0.0') mpf('0.0') mpf('0.0') mpf('0.0') mpf('0.0')]
         [mpf('1.0') mpf('0.0') mpf('0.0') mpf('0.0') mpf('0.0')]
         [mpf('1.0') mpf('1.0') mpf('0.0') mpf('0.0') mpf('0.0')]]
        ipm:
         [[mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]
         [mpi('1.0', '1.0') mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]
         [mpi('1.0', '1.0') mpi('1.0', '1.0') mpi('0.0', '0.0') mpi('0.0', '0.0') mpi('0.0', '0.0')]]
        dpm:
         [[Decimal('0.0') Decimal('0.0') Decimal('0.0') Decimal('0.0') Decimal('0.0')]
         [Decimal('1.0') Decimal('0.0') Decimal('0.0') Decimal('0.0') Decimal('0.0')]
         [Decimal('1.0') Decimal('1.0') Decimal('0.0') Decimal('0.0') Decimal('0.0')]]
        qpm:
         [[Fraction(0, 1) Fraction(0, 1) Fraction(0, 1) Fraction(0, 1) Fraction(0, 1)]
         [Fraction(1, 1) Fraction(0, 1) Fraction(0, 1) Fraction(0, 1) Fraction(0, 1)]
         [Fraction(1, 1) Fraction(1, 1) Fraction(0, 1) Fraction(0, 1) Fraction(0, 1)]]
        gpm:
         [[mpfr('0.0') mpfr('0.0') mpfr('0.0') mpfr('0.0') mpfr('0.0')]
         [mpfr('1.0') mpfr('0.0') mpfr('0.0') mpfr('0.0') mpfr('0.0')]
         [mpfr('1.0') mpfr('1.0') mpfr('0.0') mpfr('0.0') mpfr('0.0')]]
        apm:
         [[0 0 0 0 0]
         [1.00000000000000 0 0 0 0]
         [1.00000000000000 1.00000000000000 0 0 0]]


