




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








Numpy mathematical functions: Matrix and vector products
==============================================================================




Dot product: numpy.dot
-------------------------------------------------------------------------------------------

.. method:: npm.dot(a, b, out=None)

    Compute the Dot product of two arrays. .


    See https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot for details.

    Dot product of two arrays. Specifically,

    If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).

    If both a and b are 2-D arrays, it is matrix multiplication, but using matmul or a @ b is preferred.

    If either a or b is 0-D (scalar), it is equivalent to multiply and using numpy.multiply(a, b) or a * b is preferred.

    If a is an N-D array and b is a 1-D array, it is a sum product over the last axis of a and b.

    If a is an N-D array and b is an M-D array (where M>=2), it is a sum product over the last axis of a and the second-to-last axis of b:


    .. code-block:: pycon

        >>> np.dot(3, 4)
        12

    Neither argument is complex-conjugated:

    .. code-block:: pycon

        np.dot([2j, 3j], [2j, 3j])
        (-13+0j)

    For 2-D arrays it is the matrix product:

    .. code-block:: pycon

        a = [[1, 0], [0, 1]]
        b = [[4, 1], [2, 2]]
        np.dot(a, b)
        array([[4, 1],
               [2, 2]])

        a = np.arange(3*4*5*6).reshape((3,4,5,6))
        b = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
        np.dot(a, b)[2,3,2,1,2,2]
        499128
        sum(a[2,3,2,:] * b[1,2,:,2])
        499128







Dot product of two vectors: numpy.vdot
-------------------------------------------------------------------------------------------

.. method:: npm.vdot(a, b, /)

    Return the dot product of two vectors.


    See https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot for details.


    The vdot(a, b) function handles complex numbers differently than dot(a, b). If the first argument is complex the complex conjugate of the first argument is used for the calculation of the dot product.

    Note that vdot handles multidimensional arrays differently than dot: it does not perform a matrix product, but flattens input arguments to 1-D vectors first. Consequently, it should only be used for vectors.


    .. code-block:: pycon

        >>> a = np.array([1+2j,3+4j])
        >>> b = np.array([5+6j,7+8j])
        >>> np.vdot(a, b)
        (70-8j)
        >>> np.vdot(b, a)
        (70+8j)

    Note that higher-dimensional arrays are flattened!

    .. code-block:: pycon

        >>> a = np.array([[1, 4], [5, 6]])
        >>> b = np.array([[4, 1], [2, 2]])
        >>> np.vdot(a, b)
        30
        >>> np.vdot(b, a)
        30
        1*4 + 4*1 + 5*2 + 6*2
        30





Inner product of two arrays: numpy.inner
-------------------------------------------------------------------------------------------

.. method:: npm.inner(a, b, /)

    Return the inner product of two arrays.


    See https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner for details.



    Ordinary inner product of vectors for 1-D arrays (without complex conjugation), in higher dimensions a sum product over the last axes.

    For vectors (1-D arrays) it computes the ordinary inner-product:

    .. code-block:: python

        np.inner(a, b) = sum(a[:]*b[:])

    More generally, if ndim(a) = r > 0 and ndim(b) = s > 0:

    .. code-block:: python

        np.inner(a, b) = np.tensordot(a, b, axes=(-1,-1))

    or explicitly:

    .. code-block:: python

        np.inner(a, b)[i0,...,ir-2,j0,...,js-2]
             = sum(a[i0,...,ir-2,:]*b[j0,...,js-2,:])

    In addition a or b may be scalars, in which case:

    .. code-block:: python

        np.inner(a,b) = a*b


    Ordinary inner product for vectors:

    .. code-block:: pycon

        >>> a = np.array([1,2,3])
        >>> b = np.array([0,1,0])
        >>> np.inner(a, b)
        2

    Some multidimensional examples:

    .. code-block:: pycon

        >>> a = np.arange(24).reshape((2,3,4))
        >>> b = np.arange(4)
        >>> c = np.inner(a, b)
        >>> c.shape
        (2, 3)
        >>> c
        array([[ 14,  38,  62],
               [ 86, 110, 134]])

        >>> a = np.arange(2).reshape((1,1,2))
        >>> b = np.arange(6).reshape((3,2))
        >>> c = np.inner(a, b)
        >>> c.shape
        (1, 1, 3)
        >>> c
        array([[[1, 3, 5]]])

    An example where b is a scalar:

    .. code-block:: pycon

        >>> np.inner(np.eye(2), 7)
        array([[7., 0.],
               [0., 7.]])






Outer product of two vectors: numpy.outer
-------------------------------------------------------------------------------------------

.. method:: npm.outer(a, b, out=None)

    Compute the outer product of two vectors.


    See https://numpy.org/doc/stable/reference/generated/numpy.outer.html#numpy.outer for details.



    Given two vectors a and b of length M and N, repsectively, the outer product [1] is:

    .. code-block:: python

        [[a_0*b_0  a_0*b_1 ... a_0*b_{N-1} ]
         [a_1*b_0    .
         [ ...          .
         [a_{M-1}*b_0            a_{M-1}*b_{N-1} ]]

    Make a (very coarse) grid for computing a Mandelbrot set:

    .. code-block:: pycon

        >>> rl = np.outer(np.ones((5,)), np.linspace(-2, 2, 5))
        >>> rl
        array([[-2., -1.,  0.,  1.,  2.],
               [-2., -1.,  0.,  1.,  2.],
               [-2., -1.,  0.,  1.,  2.],
               [-2., -1.,  0.,  1.,  2.],
               [-2., -1.,  0.,  1.,  2.]])
        >>> im = np.outer(1j*np.linspace(2, -2, 5), np.ones((5,)))
        >>> im
        array([[0.+2.j, 0.+2.j, 0.+2.j, 0.+2.j, 0.+2.j],
               [0.+1.j, 0.+1.j, 0.+1.j, 0.+1.j, 0.+1.j],
               [0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j, 0.+0.j],
               [0.-1.j, 0.-1.j, 0.-1.j, 0.-1.j, 0.-1.j],
               [0.-2.j, 0.-2.j, 0.-2.j, 0.-2.j, 0.-2.j]])
        >>> grid = rl + im
        >>> grid
        array([[-2.+2.j, -1.+2.j,  0.+2.j,  1.+2.j,  2.+2.j],
               [-2.+1.j, -1.+1.j,  0.+1.j,  1.+1.j,  2.+1.j],
               [-2.+0.j, -1.+0.j,  0.+0.j,  1.+0.j,  2.+0.j],
               [-2.-1.j, -1.-1.j,  0.-1.j,  1.-1.j,  2.-1.j],
               [-2.-2.j, -1.-2.j,  0.-2.j,  1.-2.j,  2.-2.j]])

    An example using a “vector” of letters:

    .. code-block:: pycon

        >>> x = np.array(['a', 'b', 'c'], dtype=object)
        >>> np.outer(x, [1, 2, 3])
        array([['a', 'aa', 'aaa'],
               ['b', 'bb', 'bbb'],
               ['c', 'cc', 'ccc']], dtype=object)






Matrix product of two arrays: numpy.matmul
---------------------------------------------------------------------------------

.. method:: npm.matmul(x1, x2, /, out=None, *, casting='same_kind', order='K', dtype=None, subok=True)

    Matrix product of two arrays. 


    See https://numpy.org/doc/stable/reference/generated/numpy.matmul.html#numpy.matmul for details.


    The behavior depends on the arguments in the following way.

    * If both arguments are 2-D they are multiplied like conventional matrices.

    * If either argument is N-D, N > 2, it is treated as a stack of matrices residing in the last two indexes and broadcast accordingly.

    * If the first argument is 1-D, it is promoted to a matrix by prepending a 1 to its dimensions. After matrix multiplication the prepended 1 is removed.

    * If the second argument is 1-D, it is promoted to a matrix by appending a 1 to its dimensions. After matrix multiplication the appended 1 is removed.

    ``matmul`` differs from ``dot`` in two important ways:

    * Multiplication by scalars is not allowed, use ``*`` instead.

    * Stacks of matrices are broadcast together as if the matrices were elements, respecting the signature ``(n,k),(k,m)->(n,m)``:

    .. code-block:: pycon

        >>> a = np.ones([9, 5, 7, 4])
        >>> c = np.ones([9, 5, 4, 3])
        >>> np.dot(a, c).shape
        (9, 5, 7, 9, 5, 3)
        >>> np.matmul(a, c).shape
        (9, 5, 7, 3)
        >>> # n is 7, k is 4, m is 3

    The matmul function implements the semantics of the ``@`` operator introduced in Python 3.5 following PEP 465.

    For 2-D arrays it is the matrix product:

    .. code-block:: pycon

        >>> a = np.array([[1, 0], [0, 1]])
        >>> b = np.array([[4, 1], [2, 2]])
        >>> np.matmul(a, b)
        array([[4, 1],
               [2, 2]])

    For 2-D mixed with 1-D, the result is the usual.

    .. code-block:: pycon

        >>> a = np.array([[1, 0], [0, 1]])
        >>> b = np.array([1, 2])
        >>> np.matmul(a, b)
        array([1, 2])
        >>> np.matmul(b, a)
        array([1, 2])

    Broadcasting is conventional for stacks of arrays

    .. code-block:: pycon

        >>> a = np.arange(2 * 2 * 4).reshape((2, 2, 4))
        >>> b = np.arange(2 * 2 * 4).reshape((2, 4, 2))
        >>> np.matmul(a,b).shape
        (2, 2, 2)
        >>> np.matmul(a, b)[0, 1, 1]
        98
        >>> sum(a[0, 1, :] * b[0 , :, 1])
        98

    Vector, vector returns the scalar inner product, but neither argument is complex-conjugated:

    .. code-block:: pycon

        >>> np.matmul([2j, 3j], [2j, 3j])
        (-13+0j)

    Scalar multiplication raises an error.

    .. code-block:: pycon

        >>> np.matmul([1,2], 3)
        Traceback (most recent call last):
        ...
        ValueError: matmul: Input operand 1 does not have enough dimensions ...

    The ``@`` operator can be used as a shorthand for ``np.matmul`` on ndarrays.

    .. code-block:: pycon

        >>> x1 = np.array([2j, 3j])
        x2 = np.array([2j, 3j])
        >>> x1 @ x2
        (-13+0j)








Tensor dot product: numpy.matmul
----------------------------------------------------------------------------

.. method:: npm.tensordot(a, b, axes=2)

    Compute tensor dot product along specified axes.


    See https://numpy.org/doc/stable/reference/generated/numpy.tensordot.html#numpy.tensordot for details.


    Given two tensors, a and b, and an array_like object containing two array_like objects, (a_axes, b_axes), sum the products of a’s and b’s elements (components) over the axes specified by a_axes and b_axes. The third argument can be a single non-negative integer_like scalar, N; if it is such, then the last N dimensions of a and the first N dimensions of b are summed over.

    Three common use cases are:

    * ``axes = 0`` : tensor product `a \otimes b`

    * ``axes = 1`` : tensor dot product  `a \cdot b`

    * ``axes = 2`` : (default) tensor double contraction  `a : b`

    When axes is integer_like, the sequence for evaluation will be: first the -Nth axis in a and 0th axis in b, and the -1th axis in a and Nth axis in b last.

    When there is more than one axis to sum over - and they are not the last (first) axes of a (b) - the argument axes should consist of two sequences of the same length, with the first axis to sum over given first in both sequences, the second axis second, and so forth.

    The shape of the result consists of the non-contracted axes of the first tensor, followed by the non-contracted axes of the second.


    A "traditional" example:

    .. code-block:: pycon

        >>> a = np.arange(60.).reshape(3,4,5)
        >>> b = np.arange(24.).reshape(4,3,2)
        >>> c = np.tensordot(a,b, axes=([1,0],[0,1]))
        >>> c.shape
        (5, 2)
        >>> c
        array([[4400., 4730.],
               [4532., 4874.],
               [4664., 5018.],
               [4796., 5162.],
               [4928., 5306.]])
        >>> # A slower but equivalent way of computing the same...
        >>> d = np.zeros((5,2))
        >>> for i in range(5):
          for j in range(2):
            for k in range(3):
              for n in range(4):
                d[i,j] += a[k,n,i] * b[n,k,j]
        >>> c == d
        array([[ True,  True],
               [ True,  True],
               [ True,  True],
               [ True,  True],
               [ True,  True]])

    An extended example taking advantage of the overloading of ``+`` and ``*`` :

    .. code-block:: pycon

        >>> a = np.array(range(1, 9))
        >>> a.shape = (2, 2, 2)
        >>> A = np.array(('a', 'b', 'c', 'd'), dtype=object)
        A.shape = (2, 2)
        >>> a; A
        array([[[1, 2],
                [3, 4]],
               [[5, 6],
                [7, 8]]])
        array([['a', 'b'],
               ['c', 'd']], dtype=object)

        >>> np.tensordot(a, A) # third argument default is 2 for double-contraction
        array(['abbcccdddd', 'aaaaabbbbbbcccccccdddddddd'], dtype=object)

        >>> np.tensordot(a, A, 1)
        array([[['acc', 'bdd'],
                ['aaacccc', 'bbbdddd']],
               [['aaaaacccccc', 'bbbbbdddddd'],
                ['aaaaaaacccccccc', 'bbbbbbbdddddddd']]], dtype=object)

        >>> np.tensordot(a, A, 0) # tensor product (result too long to incl.)
        array([[[[['a', 'b'],
                  ['c', 'd']],
                  ...
        >>> np.tensordot(a, A, (0, 1))
        array([[['abbbbb', 'cddddd'],
                ['aabbbbbb', 'ccdddddd']],
               [['aaabbbbbbb', 'cccddddddd'],
                ['aaaabbbbbbbb', 'ccccdddddddd']]], dtype=object)

        >>> np.tensordot(a, A, (2, 1))
        array([[['abb', 'cdd'],
                ['aaabbbb', 'cccdddd']],
               [['aaaaabbbbbb', 'cccccdddddd'],
                ['aaaaaaabbbbbbbb', 'cccccccdddddddd']]], dtype=object)

        >>> np.tensordot(a, A, ((0, 1), (0, 1)))
        array(['abbbcccccddddddd', 'aabbbbccccccdddddddd'], dtype=object)

        >>> np.tensordot(a, A, ((2, 1), (1, 0)))
        array(['acccbbdddd', 'aaaaacccccccbbbbbbdddddddd'], dtype=object)






Einstein summation: numpy.einsum
----------------------------------------------------------------------

.. method:: npm.einsum(subscripts, *operands, out=None, dtype=None, order='K', casting='safe', optimize=False)

    Evaluates the Einstein summation convention on the operands.


    See https://numpy.org/doc/stable/reference/generated/numpy.einsum.html#numpy.einsum for details.



    Using the Einstein summation convention, many common multi-dimensional, linear algebraic array operations can be represented in a simple fashion. In implicit mode einsum computes these values.

    In explicit mode, einsum provides further flexibility to compute other array operations that might not be considered classical Einstein summation operations, by disabling, or forcing summation over specified subscript labels.

    Typically a ‘greedy’ algorithm is applied which empirical tests have shown returns the optimal path in the majority of cases. In some cases ‘optimal’ will return the superlative path through a more expensive, exhaustive search. For iterative calculations it may be advisable to calculate the optimal path once and reuse that path by supplying it as an argument. An example is given below.

    See numpy.einsum_path for more details.


    .. code-block:: pycon

        >>> a = np.arange(25).reshape(5,5)
        >>> b = np.arange(5)
        >>> c = np.arange(6).reshape(2,3)

    Trace of a matrix:

    .. code-block:: pycon

        >>> np.einsum('ii', a)
        60
        >>> np.einsum(a, [0,0])
        60
        >>> np.trace(a)
        60

    Extract the diagonal (requires explicit form):

    .. code-block:: pycon

        >>> np.einsum('ii->i', a)
        array([ 0,  6, 12, 18, 24])
        >>> np.einsum(a, [0,0], [0])
        array([ 0,  6, 12, 18, 24])
        >>> np.diag(a)
        array([ 0,  6, 12, 18, 24])

    Sum over an axis (requires explicit form):

    .. code-block:: pycon

        >>> np.einsum('ij->i', a)
        array([ 10,  35,  60,  85, 110])
        >>> np.einsum(a, [0,1], [0])
        array([ 10,  35,  60,  85, 110])
        >>> np.sum(a, axis=1)
        array([ 10,  35,  60,  85, 110])

    For higher dimensional arrays summing a single axis can be done with ellipsis:

    .. code-block:: pycon

        >>> np.einsum('...j->...', a)
        array([ 10,  35,  60,  85, 110])
        >>> np.einsum(a, [Ellipsis,1], [Ellipsis])
        array([ 10,  35,  60,  85, 110])








Kronecker product: numpy.kron
-------------------------------------------------------------------

.. method:: npm.kron(a, b)

    Kronecker product of two arrays. 


    **numpy.kron**

    https://numpy.org/doc/stable/reference/generated/numpy.kron.html#numpy.kron

    Computes the Kronecker product, a composite array made of blocks of the second array scaled by the first.

    The function assumes that the number of dimensions of a and b are the same, if necessary prepending the smallest with ones. If a.shape = (r0,r1,..,rN) and b.shape = (s0,s1,...,sN), the Kronecker product has shape (r0*s0, r1*s1, ..., rN*SN). The elements are products of elements from a and b, organized explicitly by:

    .. code-block:: python

        kron(a,b)[k0,k1,...,kN] = a[i0,i1,...,iN] * b[j0,j1,...,jN]

    where:

    .. code-block:: python

        kt = it * st + jt,  t = 0,...,N

    In the common 2-D case (N=1), the block structure can be visualized:

    .. code-block:: python

        [[ a[0,0]*b,   a[0,1]*b,  ... , a[0,-1]*b  ],
         [  ...                              ...   ],
         [ a[-1,0]*b,  a[-1,1]*b, ... , a[-1,-1]*b ]]


    Further examples:

    .. code-block:: pycon

        >>> np.kron([1,10,100], [5,6,7])
        array([  5,   6,   7, ..., 500, 600, 700])
        >>> np.kron([5,6,7], [1,10,100])
        array([  5,  50, 500, ...,   7,  70, 700])

        >>> np.kron(np.eye(2), np.ones((2,2)))
        array([[1.,  1.,  0.,  0.],
               [1.,  1.,  0.,  0.],
               [0.,  0.,  1.,  1.],
               [0.,  0.,  1.,  1.]])

        >>> a = np.arange(100).reshape((2,5,2,5))
        >>> b = np.arange(24).reshape((2,3,4))
        >>> c = np.kron(a,b)
        >>> c.shape
        (2, 10, 6, 20)
        >>> I = (1,3,0,2)
        >>> J = (0,2,1)
        >>> J1 = (0,) + J             # extend to ndim=4
        >>> S1 = (1,) + b.shape
        >>> K = tuple(np.array(I) * np.array(S1) + np.array(J1))
        c[K] == a[I]*b[J]
        True





Discrete, linear convolution: numpy.convolve
-----------------------------------------------------------------------

.. method:: npm.convolve(a, v, mode='full')

    Returns the discrete, linear convolution of two one-dimensional sequences.


    For a detailed description of parameters and return values see: 

    https://numpy.org/doc/stable/reference/generated/numpy.convolve.html

    See also: Wikipedia, “Convolution”, https://en.wikipedia.org/wiki/Convolution


    Returns the discrete, linear convolution of two one-dimensional sequences.

    The convolution operator is often seen in signal processing, where it models the effect of a linear time-invariant system on a signal [1]. In probability theory, the sum of two independent random variables is distributed according to the convolution of their individual distributions.

    If v is longer than a, the arrays are swapped before computation.

    The discrete convolution operation is defined as

    .. math:: (a * v)_n = \sum_{m=-\infty}^{\infty} a_m v_{n-m}

    It can be shown that a convolution `x(t) * y(t)` in time/space is equivalent to the multiplication `X(f) Y(f)` in the Fourier domain, after appropriate padding (padding is necessary to prevent circular convolution). Since multiplication is more efficient (faster) than convolution, the function ``scipy.signal.fftconvolve`` exploits the FFT to calculate the convolution of large data-sets.


    Note how the convolution operator flips the second array before “sliding” the two across one another:

    .. code-block:: pycon

        >>> import numpy as np; from mpfunlab import mpm, dpm
        >>> np.convolve([1, 2, 3], [0, 1, 0.5])
        array([0. , 1. , 2.5, 4. , 1.5])

    Only return the middle values of the convolution. Contains boundary effects, where zeros are taken into account:

    .. code-block:: pycon

        >>> np.convolve([1,2,3],[0,1,0.5], 'same')
        array([1. ,  2.5,  4. ])

    The two arrays are of the same length, so there is only one position where they completely overlap:

    .. code-block:: pycon

        >>> np.convolve([1,2,3],[0,1,0.5], 'valid')
        array([2.5])





