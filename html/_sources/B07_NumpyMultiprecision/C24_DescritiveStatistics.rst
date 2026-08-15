




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









|newpage|

Numerical transformations and descriptive statistics
===============================================================================



Centering of a matrix
-------------------------------------------------------------------------------

.. method:: mat.centered(res, data, population, opt)

    Returns the centered version of the matrix


    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> ctx = mp14.drf(); mp14.setdps(15)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> B = A.centered(); B.show("B")
        B: 
        -25, -25, -25, -25, -25, -25, 
        -15, -15, -15, -15, -15, -15, 
         -5,  -5,  -5,  -5,  -5,  -5, 
          5,   5,   5,   5,   5,   5, 
         15,  15,  15,  15,  15,  15, 
         25,  25,  25,  25,  25,  25, 

        >>> B = A.variance(); B.show("B")
        B: 
        350, 350, 350, 350, 350, 350, 


        >>> B = A.stdev(); B.show("B")




Standardization of a matrix
-------------------------------------------------------------------------------

.. method:: mat.standardized(res, data, population, opt)

    Returns the standardized version of the matrix


    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> ctx = mp14.drf(); mp14.setdps(5)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> B = A.standardized(); B.show("B")
        B: 
         -1.336,  -1.336,  -1.336,  -1.336,  -1.336,  -1.336, 
        -0.8017, -0.8017, -0.8017, -0.8017, -0.8017, -0.8017, 
        -0.2672, -0.2672, -0.2672, -0.2672, -0.2672, -0.2672, 
         0.2672,  0.2672,  0.2672,  0.2672,  0.2672,  0.2672, 
         0.8017,  0.8017,  0.8017,  0.8017,  0.8017,  0.8017, 
          1.336,   1.336,   1.336,   1.336,   1.336,   1.336, 


        >>> C = B.variance(); C.show("C")
        C: 
        0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 0.9996, 





See also: https://en.m.wikipedia.org/wiki/Quantile

Hyndman, 1996.

The quantile functions are not working:

https://numpy.org/doc/stable/reference/generated/numpy.ptp.html#numpy.ptp

https://numpy.org/doc/stable/reference/generated/numpy.percentile.html#numpy.percentile

https://numpy.org/doc/stable/reference/generated/numpy.nanpercentile.html#numpy.nanpercentile

https://numpy.org/doc/stable/reference/generated/numpy.quantile.html#numpy.quantile

https://numpy.org/doc/stable/reference/generated/numpy.nanquantile.html#numpy.nanquantile



The correlation functions are not working:

https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html#numpy.corrcoef

https://numpy.org/doc/stable/reference/generated/numpy.correlate.html#numpy.correlate

https://numpy.org/doc/stable/reference/generated/numpy.cov.html#numpy.cov







See also Eigen :cite:p:`EigenMat101`.




Trace
-------------------------------------------------------------------------------

.. method:: mat.trace()

    Returns the trace of the matrix. See also: Wikipedia :cite:p:`WikipediaMat10`.

    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> Res = A.trace(); Res.show("Res")

        !!! MISSING !!!




Squared Norm
-------------------------------------------------------------------------------

.. method:: mat.squaredNorm(partialmode=full)

    Returns the squared norm of the matrix.


    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> Res = A.squaredNorm(); Res.show("Res")
        Res: 
         9526,  9964, 10414, 10876, 11350, 11836, 






Euclidian Norm
-------------------------------------------------------------------------------

.. method:: mat.Norm(partialmode=full)

    Returns the norm of the matrix.


    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> ctx = mp14.drf(); mp14.setdps(6)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> Res = A.Norm(); Res.show("Res")
        Res: 
        97.601, 99.820, 102.05, 104.29, 106.54, 108.79, 










Covariance matrix
-------------------------------------------------------------------------------

.. method:: mat.covariance_matrix(use_crossproduct=False)

    Returns the covariance matrix of the matrix. See also Wikipedia :cite:p:`WikipediaMat11`, Wikipedia :cite:p:`WikipediaMat12`.

    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> ctx = mp14.drf(); mp14.setdps(15)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> B = A.centered(); B.show("B")
        B: 
        -25, -25, -25, -25, -25, -25, 
        -15, -15, -15, -15, -15, -15, 
         -5,  -5,  -5,  -5,  -5,  -5, 
          5,   5,   5,   5,   5,   5, 
         15,  15,  15,  15,  15,  15, 
         25,  25,  25,  25,  25,  25, 

        >>> C = (B.T * B)/(B.cols-1); C.show("C")
        C: 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 

        >>> D = A.covariance(); D.show("D")
        D: 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 
        350, 350, 350, 350, 350, 350, 




Correlation matrix
-------------------------------------------------------------------------------

.. method:: mat.correlation(use_crossproduct=False)

    Returns the correlation matrix of matrix ?matA. See also Wikipedia :cite:p:`WikipediaMat13`.


    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> ctx = mp14.drf(); mp14.setdps(6)
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> B = A.standardized(); B.show("B")
        B: 
         -1.3363,  -1.3363,  -1.3363,  -1.3363,  -1.3363,  -1.3363, 
        -0.80180, -0.80180, -0.80180, -0.80180, -0.80180, -0.80180, 
        -0.26727, -0.26727, -0.26727, -0.26727, -0.26727, -0.26727, 
         0.26727,  0.26727,  0.26727,  0.26727,  0.26727,  0.26727, 
         0.80180,  0.80180,  0.80180,  0.80180,  0.80180,  0.80180, 
          1.3363,   1.3363,   1.3363,   1.3363,   1.3363,   1.3363, 

        >>> C = (B.T * B)/(B.cols-1); C.show("C")
        C: 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 


        >>> D = A.correlation(); D.show("D")
        D: 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 
        1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 1.0000, 





Summary statistic
-------------------------------------------------------------------------------


.. method:: mat.summary(summary, data, population, opt)




    Sets *summary* to a matrix containing summary statistics  of *data*.


     ========================================  =================================================================
                  Constant                                Meaning
     ========================================  =================================================================
       ARB_STAT_COUNT                           1
       ARB_STAT_SUM                             4  = `\sum_0^10 7^e+11^f`
       ARB_STAT_MEAN                            4
       ARB_STAT_MIN                             13
       ARB_STAT_MEDIAN                          1
       ARB_STAT_MAX                             11
       ARB_STAT_AVERAGE_DEVIATION               2
       ARB_STAT_SUM_OF_SQUARES_OF_DEV           14
       ARB_STAT_SUM_OF_SQUARES                  8
       ARB_STAT_VARIANCE                        11
       ARB_STAT_STANDARD_DEVIATION              6
       ARB_STAT_SKEWNESS                        6
       ARB_STAT_KURTOSIS                        8
       ARB_STAT_TRIMMED_MEAN                    8
       ARB_STAT_HARMONIC_MEAN                   9
       ARB_STAT_GEOMETRIC_MEAN                  9
     ========================================  =================================================================



    .. code-block:: pycon

        >>> from arbeigenlab import mp14
        >>> mpm.dps = 40;
        >>> A = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableA4x4", "")
        >>> B = mp14.xrf().read_from_sqlite(mp14.dbpath(), "MpfrTableB4x4", "")







.. _rst_mpm_norm: 

Vector norm of a matrix 
-------------------------------------------------------------------------------

.. method:: ctx.norm(x, p=2)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.



    Gives the entrywise `p`-norm of an iterable *x*, i.e. the vector norm
    `\left(\sum_k |x_k|^p\right)^{1/p}`, for any given `1 \le p \le \infty`.

    Special cases:

    If *x* is not iterable, this just returns ``absmax(x)``.

    ``p=1`` gives the sum of absolute values.

    ``p=2`` is the standard Euclidean vector norm.

    ``p=inf`` gives the magnitude of the largest element.

    For *x* a matrix, ``p=2`` is the Frobenius norm.
    For operator matrix norms, use :func:`~mpmath.mnorm` instead.

    You can use the string 'inf' as well as float('inf') or mpf('inf')
    to specify the infinity norm.

    **Examples**

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> x = matrix([-10, 2, 100])
        >>> norm(x, 1)
        mpf('112.0')
        >>> norm(x, 2)
        mpf('100.5186549850325')
        >>> norm(x, inf)
        mpf('100.0')




.. _rst_mpm_mnorm: 

Matrix norm 
---------------------------------------------------------------------------------

.. method:: ctx.mnorm(A, p=1)

    where ``ctx`` is ``fpm``, ``mpm``, ``ipm``, ``dec``, ``gmp`` or ``apm``.


    Gives the matrix (operator) `p`-norm of A. Currently ``p=1`` and ``p=inf``
    are supported:

    ``p=1`` gives the 1-norm (maximal column sum)

    ``p=inf`` gives the `\infty`-norm (maximal row sum).
    You can use the string 'inf' as well as float('inf') or mpf('inf')

    ``p=2`` (not implemented) for a square matrix is the usual spectral
    matrix norm, i.e. the largest singular value.

    ``p='f'`` (or 'F', 'fro', 'Frobenius, 'frobenius') gives the
    Frobenius norm, which is the elementwise 2-norm. The Frobenius norm is an
    approximation of the spectral norm and satisfies

    .. math ::

        \frac{1}{\sqrt{\mathrm{rank}(A)}} \|A\|_F \le \|A\|_2 \le \|A\|_F

    The Frobenius norm lacks some mathematical properties that might
    be expected of a norm.

    For general elementwise `p`-norms, use :func:`~mpmath.norm` instead.

    **Examples**

        >>> from mpmath import *
        >>> mp.dps = 15; mp.pretty = False
        >>> A = matrix([[1, -1000], [100, 50]])
        >>> mnorm(A, 1)
        mpf('1050.0')
        >>> mnorm(A, inf)
        mpf('1001.0')
        >>> mnorm(A, 'F')
        mpf('1006.2310867787777')




