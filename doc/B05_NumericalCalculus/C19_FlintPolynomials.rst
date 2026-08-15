


.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />







|newpage|


Flint/Functions for polynomials
============================================================




Product of polynomials
-------------------------------------------------------------------------------

.. method:: poly.Times(C, A, B)

   Sets C to the product of A and B.



**Options FMPZ**

Sets res to the product of poly1 and poly2. Chooses an optimal algorithm from the choices below.


fmpz_poly_mul_classical(res, poly1, poly2)

Sets res to the product of poly1 and poly2, computed using the classical or schoolbook
method.


fmpz_poly_mul_karatsuba(res, poly1, poly2)

Sets res to the product of poly1 and poly2, computed using the Karatsuba algorithm.



fmpz_poly_mul_SS(res, poly1, poly2)

Sets res to the product of poly1 and poly2, computed using the Schönhage-Strassen algorithm.






**Options FMPQ**

Same as for FMPZ.


**Options Arb**


Sets C to the product of A and B. If the same variable is passed for A and B, sets C to the square of A. The default algorithm chooses the classical algorithm for short polynomials and the block algorithm for long polynomials.


arb_poly_mullow_classical(C, A, B)

The classical version uses a plain loop. This has good numerical stability but gets slow for large n.


arb_poly_mullow_block(C, A, B)

The block version decomposes the product into several subproducts which are computed exactly
over the integers. It first attempts to find an integer `c` such that `A(2^c x)` and  `B(2^c x)` have slowly varying coefficients, to reduce the number of blocks.

The scaling factor `c` is chosen in a quick, heuristic way by picking the first and last nonzero terms
in each polynomial. If the indices in `A` are `a_1,a_2`  and the log-2 magnitudes are `e_1,e_2`, and the
indices in  `B` are `b_1, b_2`  and the log-2 magnitudes are `f_1, f_2`, then we compute `c` as the weighted
arithmetic mean of the slopes, rounded to the nearest integer:

.. math ::  \left \lfloor  \frac{(e_2-e_1) + (f_1-f_2)}{(a_2-a_1) + (b_1-b_2)} + \frac{1}{2} \right \rfloor

This strategy is used because it is simple. It is not optimal in all cases, but will typically give good
performance when multiplying two power series with a similar decay rate.




**Options ACB**


Sets C to the product of A and B. If the same variable is passed for A and B, sets C to the square of A. The default algorithm chooses the classical algorithm for short polynomials and the block algorithm for long polynomials.


acb_poly_mullow_classical(C, A, B)

The classical version uses a plain loop. This has good numerical stability but gets slow for large n.


acb_poly_mullow_transpose(C, A, B)

The transpose version evaluates the product using four real polynomial multiplications (via
_arb_poly_mullow() ).



acb_poly_mullow_transpose_gauss(C, A, B)

The transpose_gauss version evaluates the product using three real polynomial multiplications.
This is almost always faster than transpose, but has worse numerical stability when the coefficients
vary in magnitude.









Quotient of polynomials
-------------------------------------------------------------------------------

.. method:: poly.Div(Q, A, B, n)

   Sets Q to the power series quotient A divided by B, truncated to length n.



Quotient and remainder of polynomials
-------------------------------------------------------------------------------

.. method:: poly.Divrem(Q, A, B, n)

   Sets Q to the power series quotient A divided by B, truncated to length n.


   

Taylor shift of polynomials
-------------------------------------------------------------------------------

.. method:: poly.TaylorShift(Q, A, B, n)

   Sets g to the Taylor shift `f(x+c)`, computed respectively using an optimized form of Horner's rule, divide-and-conquer, a single convolution, and an automatic choice between the three algorithms.




Composition of polynomials
-------------------------------------------------------------------------------

.. method:: poly.Compose(Q, A, n)

   Sets res to the composition `h(x) = f(g(x))` where `f`is given by poly1 and `g`is given by poly2, respectively using Horner's rule, divide-and-conquer, and an automatic choice between the two algorithms. The default algorithm also handles special-form input `g = ax^n+c` efficiently by performing a Taylor shift followed by a rescaling.




Evaluation of polynomials, same type
-------------------------------------------------------------------------------

.. method:: poly.Evaluate(Q, A, n)

   Sets `y = f(x)`, evaluated respectively using Horner's rule, rectangular splitting, and an automatic algorithm choice.



Evaluation of polynomials, complex number
-------------------------------------------------------------------------------

.. method:: poly.EvaluatePolyCplx(Q, A, n)

   Sets `y = f(x)`, where `x` is a complex number, evaluated respectively using Horner's rule, rectangular splitting, and an automatic algorithm choice.




Polynomial from roots
-------------------------------------------------------------------------------

.. method:: poly.ProductRoots(Q, A, n)

   Generates the polynomial `(x-x_0)(x-x_1)\cdots(x-x_{n-1})`.




Polynomial from roots, complex number
-------------------------------------------------------------------------------

.. method:: poly.ProductRootsCplx(Q, A, n)

Generates the polynomial

.. math ::

    \left(\prod_{i=0}^{rn-1} (x-r_i)\right) \left(\prod_{i=0}^{cn-1} (x-c_i)(x-\bar{c_i})\right)

having *rn* real roots given by the array *r* and having `2cn` complex roots
in conjugate pairs given by the length-*cn* array *c*.
Either *rn* or *cn* or both may be zero.

Note that only one representative from each complex conjugate pair
is supplied (unless a pair is supposed to
be repeated with higher multiplicity).
To construct a polynomial from complex roots where the conjugate pairs
have not been distinguished, use :func:`acb_poly_product_roots` instead.




Multipoint evaluation for polynomials
-------------------------------------------------------------------------------

.. method:: poly.EvaluateVec(Q, A, n)

   Evaluates the polynomial simultaneously at *n* given points




Multipoint evaluation for polynomials, fast
-------------------------------------------------------------------------------

.. method:: poly.EvaluateVecFast(Q, A, n)

   Evaluates the polynomial simultaneously at *n* given points, using fast multipoint evaluation.




Interpolation for polynomials, Newton
-------------------------------------------------------------------------------

.. method:: poly.InterpolateNewton(Q, A, n)

   Recovers the unique polynomial of length at most *n* that interpolates the given *x* and *y* values. This implementation first interpolates in the Newton basis and then converts back to the monomial basis.



Interpolation for polynomials, Lagrange
-------------------------------------------------------------------------------

.. method:: poly.InterpolateFast(Q, A, n)

   Recovers the unique polynomial of length at most *n* that interpolatesthe given *x* and *y* values, using fast Lagrange interpolation. The precomp function takes a precomputed product tree over the *x* values and a vector of interpolation weights as additional inputs.




Differentiation for polynomials
-------------------------------------------------------------------------------

.. method:: poly.Derivative(Q, A, n)

   Sets *res* to the derivative of *poly*..




Integral of polynomials
-------------------------------------------------------------------------------

.. method:: poly.Integral(Q, A, n)

   Sets *res* to the derivative of *poly*..



   
Roots of a polynomial, floating point input
-------------------------------------------------------------------------------


.. method:: poly.FindRoots(roots, poly, initial, maxiter)

See also:  Wikipedia :cite:p:`WikipediaAlg10`

Attempts to compute all the roots of the given nonzero polynomial poly using a working precision of prec bits. If n denotes the degree of poly, the function writes n approximate roots with rigorous error bounds to the preallocated array roots, and returns the number of roots that are isolated. If the return value equals the degree of the polynomial, then all roots have been found. If the return value is smaller, all the output intervals are guaranteed to contain roots, but it is possible that not all of the polynomial's roots are contained among them.

The roots are computed numerically by performing several steps with the Durand-Kerner method and terminating if the estimated accuracy of the roots approaches the working precision or if the number of steps exceeds maxiter, which can be set to zero in order to use a default value. Finally, the approximate roots are validated rigorously. Initial values for the iteration can be provided as the array initial. If initial is set to NULL, default values `(0.4 + 0.9i)k` are used.

The polynomial is assumed to be squarefree. If there are repeated roots, the iteration is likely to find them (with low numerical accuracy), but the error bounds will not converge as the precision increases.




**Examples**

.. code-block:: vbnet
    
    Sub DemoArbPolyRoots()
        Console.WriteLine("Hallo from DemoArbPolyEvaluation!")
        mp4.setdps(40)
        Dim n = 6

        Dim poly_roots = apm.poly_random(n)
        poly_roots.print("poly_roots: ")
        
        Dim polyA1 = poly_roots.product_roots(n)
        polyA1.print("polyA1 = poly_roots.product_roots(n): ")
        
        Dim polyA = acb.poly_t(polyA1)
        polyA.print("polyA = poly_roots.product_roots(n): ")
        
        Dim roots = polyA.find_roots()
        roots.print("Roots:  ")
        
        Dim polyD = polyA.evaluate_vec_iter(roots, n)
        polyD.print("polyD = polyA.evaluate_vec_iter(roots, n): ")
    End Sub




.. code-block:: none
    
    Hallo from DemoArbPolyEvaluation!
    path: i:\desktop\wingcc\nativecode\sqlite\
    path: i:\desktop\wingcc\nativecode\sqlite\
    poly_roots: from within
    0: [0.001251258888515884883096962454374079243280 +/- 6.48e-45]
    1: [0.5635853144932401193045734544284641742706 +/- 2.99e-41]
    2: [0.1933042390209662175770688463671831414104 +/- 4.93e-41]
    3: [0.8087405011139255917029800002637784928083 +/- 4.20e-41]
    4: [0.5850093081453902055244498114916495978832 +/- 2.45e-41]
    5: [0.4798730430005798686110551898309495300055 +/- 4.50e-41]

    polyA1 = poly_roots.product_roots(n): from within
    0: [3.094899455310173502210071410522478501255e-5 +/- 1.77e-44]
    1: [-0.02510497074893984414153663924404388497784 +/- 1.02e-41]
    2: [0.2978708452048342616573425892505397407958 +/- 1.13e-40]
    3: [-1.298821651131025425954068323001746314521 +/- 6.77e-40]
    4: [2.672304129648149494088931969437947807289 +/- 2.02e-40]
    5: [-2.631763664662617887603224264836399015621 +/- 2.83e-40]
    6: 1.000000000000000000000000000000000000000

    polyA = poly_roots.product_roots(n): from within
    0: ([3.094899455310173502210071410522478501255e-5 +/- 1.77e-44], 0)
    1: ([-0.02510497074893984414153663924404388497784 +/- 1.02e-41], 0)
    2: ([0.2978708452048342616573425892505397407958 +/- 1.13e-40], 0)
    3: ([-1.298821651131025425954068323001746314521 +/- 6.77e-40], 0)
    4: ([2.672304129648149494088931969437947807289 +/- 2.02e-40], 0)
    5: ([-2.631763664662617887603224264836399015621 +/- 2.83e-40], 0)
    6: (1.000000000000000000000000000000000000000, 0)

    Roots:  from within
    0: ([0.8087405011139255917029800002637784928041 +/- 2.19e-37], [+/- 2.19e-37])
    1: ([0.4798730430005798686110551898309495299879 +/- 1.28e-36], [+/- 1.28e-36])
    2: ([0.001251258888515884883096962454374079243280 +/- 7.59e-42], [+/- 7.40e-42])
    3: ([0.1933042390209662175770688463671831414107 +/- 8.71e-39], [+/- 8.70e-39])
    4: ([0.5635853144932401193045734544284641742436 +/- 9.17e-36], [+/- 9.17e-36])
    5: ([0.5850093081453902055244498114916495978745 +/- 8.49e-36], [+/- 8.49e-36])

    polyD = polyA.evaluate_vec_iter(roots, n): from within
    0: ([-1.185498500818795242001475227463269047063e-41 +/- 4.38e-37], [+/- 4.38e-37])
    1: ([8.631998540240873156890174233065883368686e-42 +/- 5.93e-37], [+/- 5.93e-37])
    2: ([+/- 2.16e-43], [+/- 1.86e-43])
    3: ([-2.858648867222626824684408349911428907812e-43 +/- 6.80e-40], [+/- 6.73e-40])
    4: ([7.6566948090708004755272584430961017413e-42 +/- 6.45e-36], [+/- 6.45e-36])
    5: ([1.42147716221109443674503128928929092357e-41 +/- 6.60e-36], [+/- 6.60e-36])
    6: (0, 0)


    

Root finding, integer input
-------------------------------------------------------------------------------


.. method:: poly.FmpzComplexRoots(roots, poly, flags)

Writes to roots all the real and complex roots of the polynomial poly, computed to prec accurate bits. The real roots are written first in ascending order (with the imaginary parts set exactly to zero). The following nonreal roots are written in arbitrary order, but with conjugate pairs grouped together (the root in the upper plane leading the root in the lower plane). The input polynomial must be squarefree. For a general polynomial, compute the squarefree part `f/gcd(f,f')` or do a full squarefree factorization to obtain the multiplicities of the roots:


.. code-block:: C

    fmpz_poly_factor_t fac;
    fmpz_poly_factor_init(fac);
    fmpz_poly_factor_squarefree(fac, poly);

    for (i = 0; i < fac->num; i++)
    {
        deg = fmpz_poly_degree(fac->p + i);
        flint_printf("%wd roots of multiplicity %wd\n", deg, fac->exp[i]);
        roots = _acb_vec_init(deg);
        arb_fmpz_poly_complex_roots(roots, fac->p + i, 0, prec);
        _acb_vec_clear(roots, deg);
    }

    fmpz_poly_factor_clear(fac);


All roots are refined to a relative accuracy of at least prec bits. The output values will generally
have higher actual precision, depending on the precision used internally by the algorithm.
This implementation should be adequate for general use, but it is not currently competitive with
state-of-the-art isolation methods for finding real roots alone.

The following flags are supported: Arb_FMPZ_POLY_ROOTS_VERBOSE




Examples: poly_roots.c
-------------------------------------------------------------------------------

This program finds the complex roots of an integer polynomial
by calling :func:`arb_fmpz_poly_complex_roots`, which in turn calls
:func:`acb_poly_find_roots` with increasing
precision until the roots certainly have been isolated.
The program takes the following arguments::

``poly_roots [-refine d] [-print d] <poly>``

Isolates all the complex roots of a polynomial with integer coefficients.

If ``-refine d`` is passed, the roots are refined to a relative tolerance
better than `10^-d`. By default, the roots are only computed to sufficient
accuracy to isolate them. The refinement is not currently done efficiently.

If ``-print d`` is passed, the computed roots are printed to ``d`` decimals.
By default, the roots are not printed.

The polynomial can be specified by passing the following as ``<poly>``:

.. code-block:: none

    a <n>          Easy polynomial 1 + 2x + ... + (n+1)x^n
    t <n>          Chebyshev polynomial T_n
    u <n>          Chebyshev polynomial U_n
    p <n>          Legendre polynomial P_n
    c <n>          Cyclotomic polynomial Phi_n
    s <n>          Swinnerton-Dyer polynomial S_n
    b <n>          Bernoulli polynomial B_n
    w <n>          Wilkinson polynomial W_n
    e <n>          Taylor series of exp(x) truncated to degree n
    m <n> <m>      The Mignotte-like polynomial x^n + (100x+1)^m, n > m
    coeffs <c0 c1 ... cn>        c0 + c1 x + ... + cn x^n


Concatenate to multiply polynomials, e.g.: 

``p 5 t 6 coeffs 1 2 3`` for `P_5(x) \cdot T_6(x) \cdot (1+2x+3x^2)`

This finds the roots of the Wilkinson polynomial with roots at the positive integers 1, 2, ..., 100:

.. code-block:: none

    > build/examples/poly_roots -print 15 w 100
    computing squarefree factorization...
    cpu/wall(s): 0.001 0.001
    roots with multiplicity 1
    searching for 100 roots, 100 deflated
    prec=32: 0 isolated roots | cpu/wall(s): 0.098 0.098
    prec=64: 0 isolated roots | cpu/wall(s): 0.247 0.247
    prec=128: 0 isolated roots | cpu/wall(s): 0.498 0.497
    prec=256: 0 isolated roots | cpu/wall(s): 0.713 0.713
    prec=512: 100 isolated roots | cpu/wall(s): 0.104 0.105
    done!
    [1.00000000000000 +/- 3e-20]
    [2.00000000000000 +/- 3e-19]
    [3.00000000000000 +/- 1e-19]
    [4.00000000000000 +/- 1e-19]
    [5.00000000000000 +/- 1e-19]
    ...
    [96.0000000000000 +/- 1e-17]
    [97.0000000000000 +/- 1e-17]
    [98.0000000000000 +/- 3e-17]
    [99.0000000000000 +/- 3e-17]
    [100.000000000000 +/- 3e-17]
    cpu/wall(s): 1.664 1.664

This finds the roots of a Bernoulli polynomial which has both real
and complex roots:

.. code-block:: none

    > build/examples/poly_roots -refine 100 -print 20 b 16
    computing squarefree factorization...
    cpu/wall(s): 0.001 0
    roots with multiplicity 1
    searching for 16 roots, 16 deflated
    prec=32: 16 isolated roots | cpu/wall(s): 0.006 0.006
    prec=64: 16 isolated roots | cpu/wall(s): 0.001 0.001
    prec=128: 16 isolated roots | cpu/wall(s): 0.001 0.001
    prec=256: 16 isolated roots | cpu/wall(s): 0.001 0.002
    prec=512: 16 isolated roots | cpu/wall(s): 0.002 0.001
    done!
    [-0.94308706466055783383 +/- 2.02e-21]
    [-0.75534059252067985752 +/- 2.70e-21]
    [-0.24999757119077421009 +/- 4.27e-21]
    [0.24999757152512726002 +/- 4.43e-21]
    [0.75000242847487273998 +/- 4.43e-21]
    [1.2499975711907742101 +/- 1.43e-20]
    [1.7553405925206798575 +/- 1.74e-20]
    [1.9430870646605578338 +/- 3.21e-20]
    [-0.99509334829256233279 +/- 9.42e-22] + [0.44547958157103608805 +/- 3.59e-21]*I
    [-0.99509334829256233279 +/- 9.42e-22] + [-0.44547958157103608805 +/- 3.59e-21]*I
    [1.9950933482925623328 +/- 1.10e-20] + [0.44547958157103608805 +/- 3.59e-21]*I
    [1.9950933482925623328 +/- 1.10e-20] + [-0.44547958157103608805 +/- 3.59e-21]*I
    [-0.92177327714429290564 +/- 4.68e-21] + [-1.0954360955079385542 +/- 1.71e-21]*I
    [-0.92177327714429290564 +/- 4.68e-21] + [1.0954360955079385542 +/- 1.71e-21]*I
    [1.9217732771442929056 +/- 3.54e-20] + [1.0954360955079385542 +/- 1.71e-21]*I
    [1.9217732771442929056 +/- 3.54e-20] + [-1.0954360955079385542 +/- 1.71e-21]*I
    cpu/wall(s): 0.011 0.012

Roots are automatically separated by multiplicity by performing an initial squarefree factorization:

.. code-block:: none

    > build/examples/poly_roots -print 5 p 5 p 5 t 7 coeffs 1 5 10 10 5 1
    computing squarefree factorization...
    cpu/wall(s): 0 0
    roots with multiplicity 1
    searching for 6 roots, 3 deflated
    prec=32: 3 isolated roots | cpu/wall(s): 0 0.001
    done!
    [-0.97493 +/- 2.10e-6]
    [-0.78183 +/- 1.49e-6]
    [-0.43388 +/- 3.75e-6]
    [0.43388 +/- 3.75e-6]
    [0.78183 +/- 1.49e-6]
    [0.97493 +/- 2.10e-6]
    roots with multiplicity 2
    searching for 4 roots, 2 deflated
    prec=32: 2 isolated roots | cpu/wall(s): 0 0
    done!
    [-0.90618 +/- 1.56e-7]
    [-0.53847 +/- 6.91e-7]
    [0.53847 +/- 6.91e-7]
    [0.90618 +/- 1.56e-7]
    roots with multiplicity 3
    searching for 1 roots, 0 deflated
    prec=32: 0 isolated roots | cpu/wall(s): 0 0
    done!
    0
    roots with multiplicity 5
    searching for 1 roots, 1 deflated
    prec=32: 1 isolated roots | cpu/wall(s): 0 0
    done!
    -1.0000
    cpu/wall(s): 0 0.001


    



Polynomial square-free (integers)
-------------------------------------------------------------------------------

.. method:: poly.IsSquarefree(res, poly1, poly2)

Returns whether the polynomial poly is square-free. A non-zero polynomial is defined to be square-free if it has no non-unit square factors. We also define the zero polynomial to be square-free. Returns 1 if the length of poly is at most 2. Returns whether the discriminant is zero for quadratic polynomials. Otherwise, returns whether the greatest common divisor of poly and its derivative has length 1.






Convert to monic polynomial (rational)
-------------------------------------------------------------------------------

.. method:: poly.MakeMonic(C, A)

   Sets res to the monic scalar multiple of poly whenever poly is non-zero. If poly is the zero polynomial, sets res to zero.




Test for monic polynomial (rational)
-------------------------------------------------------------------------------

.. method:: poly.IsMonic(polyA)

   Returns whether the polynomial poly is monic. The zero polynomial is not monic by definition.



Test for square-free polynomial (rational)
-------------------------------------------------------------------------------

.. method:: poly.IsSquarefree2(polyA)

   Returns whether the polynomial polyA is square-free. A non-zero polynomial is defined to be square-free if it has no non-unit square factors. We also define the zero polynomial to be square-free.




