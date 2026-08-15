


.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />







|newpage|



Flint/Power series and Taylor arithmetic
===============================================================================

The computation of high derivatives of a function is often considered to be a tedious and
error-prone task which is the reason why there exist almost no numerical methods making
use of higher derivatives. Only the Taylor series method for the approximate solution
of ordinary differential equations is sometimes mentioned in textbooks. However, this
method is usually discarded immediately because it is considered to be far too expensive.
Higher derivatives often occur also in remainder terms of various numerical approximation
methods such as Taylor expansion, interpolation, numerical integration and the like.

In this section we show that the computation of such higher derivatives is indeed
very easy and efficient and that even unknown intermediate values which often appear in
remainder terms can be handled almost trivially by the use of interval arithmetic. Here  
the combination of automatic differentiation and interval arithmetic has a strong effect
of synergy: Computing high derivatives efficiently and enclosing unknown intermediate points in intervals results in methods of totally new quality. This combination makes it
possible to estimate remainder terms rigorously and thus to derive proofs automatically on
a computer which were not possible earlier or which were at least much more complicated.





Taylor Arithmetic
-------------------------------------------------------------------------------

Assume that `f :\mathbb{R} \rightarrow \mathbb{R}` is an analytic function. Then `f`
can be expanded in a Taylor series around a point `x_0`

.. math::  f(x) = \sum_{k=0}^{\infty} \frac{f^{(k)}(x_0)}{k!}(x-x_0)^k  = \sum_{k=0}^{\infty} (f)_k(x-x_0)^k

where `f^{(k)}(x_0)` denotes the `k^{\text{th}}` derivative of `f` at the point of expansion `x = x_0` and `(f)_k` denotes the `k^{\text{th}}` Taylor coefficient.

When implementing automatic differentiation it is more convenient to work with the Taylor coefficients rather than directly with the derivatives. The resulting system of arithmetic operations and
elementary functions is therefore called Taylor arithmetic.

Here are a few examples:



Borel transform of power series
-------------------------------------------------------------------------------

.. method:: poly.BorelTransform(Q, A, n)

   Computes the Borel transform of the input polynomial, mapping  `\sum_{k} a_k x^k` to `\sum_{k} (a_k k!) x^k`.



Inverse Borel transform of power series
-------------------------------------------------------------------------------

.. method:: poly.InvBorelTransform(Q, A, n)

   Computes the inverse Borel transform of the input polynomial, mapping  `\sum_{k} a_k x^k` to `\sum_{k} (a_k/k!) x^k`.




Sum of power series
-------------------------------------------------------------------------------

.. method:: poly.PlusSeries(C, A, B, n)

   Sets C to the sum of A and B, truncated to length len n.




Difference of power series
-------------------------------------------------------------------------------

.. method:: poly.MinusSeries(C, A, B, n)

   Sets C to the difference of A and B, truncated to length len n.



Product of power series
-------------------------------------------------------------------------------

.. method:: poly.TimesSeries(C, A, B, n)

   Sets C to the product of A and B, truncated to length len n.



Quotient of power series
-------------------------------------------------------------------------------

.. method:: poly.DivSeries(Q, A, B, n)

   Sets Q to the power series quotient A divided by B, truncated to length n.



Inverse of power series
-------------------------------------------------------------------------------

.. method:: poly.InvSeries(Q, A, n)

   Sets Q to the power series inverse of A, truncated to length n.



Composition of power series
-------------------------------------------------------------------------------

.. method:: poly.ComposeSeries(Q, A, n)

   Sets res to the power series composition `h(x) = f(g(x))` truncated to order `O(x^n)` where `f` is given by poly1 and `g` is given by poly2, respectively using Horner's rule, the Brent-Kung baby step-giant step algorithm, and an automatic choice between the two algorithms.



Reversion of power series
-------------------------------------------------------------------------------

.. method:: poly.RevertSeries(Q, A, n)

   Sets `h` to the power series reversion of `f`, i.e. the expansion of the compositional inverse function `f^{-1}(x)`, truncated to order `O(x^n)`, using respectively Lagrange inversion, Newton iteration, fast Lagrange inversion, and a default algorithm choice. We require that the constant term in `f` is exactly zero and that the linear term is nonzero. The underscore methods assume that flen is at least 2, and do not support aliasing.








