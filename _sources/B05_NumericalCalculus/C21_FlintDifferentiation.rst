


.. |newpage| raw:: latex

   \newpage


.. |br| raw:: html

   <br />





|newpage|



Flint/Verified numerical differentiation
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






Finding "all" real roots within a finite interval
-------------------------------------------------------------------------------

.. method:: Apr.RealRoots(a, b, c)


Returns the roots.




Taylor Polynomial: rigorous error bounds of `f(x)-T_n(x)`
-------------------------------------------------------------------------------

That is, the error introduced when `f(x)` is approximated by its Taylor polynomial of degree `n` is precisely the last term of the Taylor polynomial of degree `n+1`, but with the derivative evaluated at some point `\xi` between `a` and `x`.

.. math::  f(x)-T_n(x) :=  \frac{f^{(n+1)}(\xi)}{(n+1)!} (x-a)^{(n+1)}.


See also: https://brilliant.org/wiki/taylor-series-error-bounds/




Chebyshev interpolation polynomials:  rigorous error bounds of `|f(x) - P_n(x)|`
--------------------------------------------------------------------------------------

Using Chebychev interpolation, an approximation of a function `f(x)` in the interval `[a, b]` by a polynomial `P_n(x)` is given by

.. math:: P_n(x) = \sum_{i=0}^{n} \frac{f(x_i)}{w_i(x-x_i)} \bigg/  \sum_{i=0}^{n} \frac{1}{w_i(x-x_i)}, \text{ where}

.. math:: x_i = \frac{b+a}{2} +  \frac{b-a}{2} \cos \left ( \frac{(2i - 1)\pi}{2(n+1)} \right ), \quad \text{and}  \quad w_i = \prod_{j=0, j\ne i}^{n}(x_i - x_j)



Note that for `a=-1, b=1`, the `x_i` are the roots of a Chebychev polynomial of the first kind. Then for `x \in [a, b]`

.. math:: |f(x) - P_n(x)| \le \left( \frac{b-a}{2} \right )^{n+1} \frac{\text{max}_{x \in [a, b]}|f^{(n+1)}(x)|}{2^n (n+1)!}




Trapezoidal rule and related quadratures: approximate error bounds
-------------------------------------------------------------------------------

.. math::     \int_a^b  f(x) \mathrm{d} x = h \sum_{j=a/h}^{b/h} f(jh) - \frac{h}{2} [f(a)+f(b)] - \sum_{i=1}^m \frac{h^{2i}B_{2i}}{(2i)!} \left[ D^{2i-1}f(b) -  D^{2i-1}f(a) \right] + E(h,m), \quad \text{where}

.. math::  E(h,m) = \frac{(a-b) B_{2m+2} D^{2m+2} f(\xi)}{(2m+2)!} h^{2m+2}, \quad \text{where } \xi \in (a,b).

See also:  Wikipedia :cite:p:`WikipediaAlg34`, :cite:t:`Bailey2006`.



A number of quadrature algorithms which work well in practice are obtained  on transforming the integral of `F(x)` on `[-1,1]` to an integral of `f(t)=F(g(t)) g'(t)` on `(-\infty, \infty)`, via the change of variable `x = g(t)`. We then have, for `h>0`,

.. math::  \int_{-1}^1 F(x) \mathrm{d} x = \int_{-\infty}^{\infty} F(g(t)) g'(t) \mathrm{d} t = h \sum_{j=-\infty}^{\infty} w_j F(x_j) + E(h),

where `x_j = g(hj)` and `w_j = g'(hj)`. Using `g(t):=\tanh(t)` gives rise to the *tanh quadrature*. Using `g(t):=\text{erf}(t)` gives rise to the *erf quadrature*. Using `g(t):=\tanh(\sinh(t))` gives rise to the *tanh-sinh quadrature*.

For integrand functions to be integrated on `(-\infty, \infty)` one can use `g(t):=\sinh(t)` or  `g(t):=\sinh(\pi/2 \cdot \sinh(t))` or `g(t):=\sinh(\sinh(t))`.

An estimate of the error of the approximation can be obtained as

.. math::  E_2(h,m) = h (-1)^{m-1} \left( \frac{h}{2\pi} \right)^{2m} \sum_{j=a/h}^{b/h} D^{2m} f(jh), \quad \text{where}

.. math::  D^2 f(t) = F(g(t)) g'''(t) + F'(g(t)) [3g'(t)g''(t)] + F''(g(t)) [g'(t)]^3

Additional information in Okayama 2013a.






