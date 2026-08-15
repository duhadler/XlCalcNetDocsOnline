





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


.. py:currentmodule:: dist





Introduction to random variables and distributions
========================================================



Elementary symbolic algebra of random variables
-------------------------------------------------------------------------------

See also https://en.wikipedia.org/wiki/Algebra_of_random_variables.

Considering two random variables `X` and `Y` the following algebraic operations are possible:

Addition: `Z=X+Y=Y+X`.

Subtraction: `Z=X-Y=-Y+X`.

Multiplication: `Z=XY=YX`.

Division: `Z=X/Y=X\cdot (1/Y)=(1/Y)\cdot X`.

In all cases, the variable `Z` resulting from each operation is also a random variable. All commutative and associative properties of conventional algebraic operations are also valid for random variables. If any of the random variables is replaced by a deterministic variable or by a constant value, all the previous properties remain valid.



Simple tranformations, results for pdf and cdf: see :cite:t:`Rinne2008`, page 217.



This is a summary of some transformations:

|spacingstart|

.. _table_some_transforms:
.. table:: Some transformations

        +---------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
        | Transformation                                          | pdf                                                         |cdf                                                                                  |
        | `Y = g(X)`                                              | `f_Y(y)`                                                    |`F_Y(y)`                                                                             |
        +=========================================================+=============================================================+=====================================================================================+
        |`{\displaystyle Y = a + bX ;                             |`{\displaystyle =\frac{1}{|b|} f_X \left(                    |`{\displaystyle =\begin{cases}                                                       |
        |\quad a, x \in \mathbb{R}; b \ne 0 }.`                   |\frac{y-a}{b}  \right)}.`                                    |F_X \left(\frac{y-a}{b}\right) & \text{for }b>0,\\                                   |
        |                                                         |                                                             |1-F_X \left(\frac{y-a}{b}\right)  & \text{for }b<0. \end{cases}}`                    |
        +---------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
        |`{\displaystyle Y = X^r ; \quad r \in \mathbb{N},        |`{\displaystyle =\frac{1}{r} y^{\frac{1}{r}-1} f_X \left(    |`{\displaystyle =F_X \left(\sqrt[r]{y}\right). }`                                    |
        |x \in \mathbb{R} }.`                                     |\sqrt[r]{y}  \right)}.`                                      |                                                                                     |
        +---------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
        |`{\displaystyle Y = aX^k; \quad a, k \in                 |`{\displaystyle =\frac{1}{|ka|} \left(\frac{y}{a}\right)^    |`{\displaystyle =\begin{cases}                                                       |
        |\mathbb{R}\setminus \{0\}; \quad  x>0 }.`                |{\frac{1}{k}-1} f_X \left(                                   |F_X \left(\sqrt[k]{\frac{y}{a}}\right) & \text{for }a>0,\\                           |
        |                                                         |\sqrt[k]{\frac{y}{a}}  \right)}`                             |1-F_X \left(\sqrt[k]{\frac{y}{a}}\right)  & \text{for }a<0. \end{cases}}`            |
        +---------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
        |`{\displaystyle Y = a\sqrt[k]{X}; \quad a, k \in         |`{\displaystyle =\frac{k}{|a|} \left(\frac{y}{a}\right)^     |`{\displaystyle =\begin{cases}                                                       |
        |\mathbb{R}\setminus \{0\}; \quad  x>0 }.`                |{k-1} f_X \left( \left[                                      |F_X \left( \left[\frac{y}{a}  \right]^k \right) & \text{for }a>0,\\                  |
        |                                                         |\frac{y}{a}  \right]^k \right) }`                            |1-F_X \left( \left[\frac{y}{a}  \right]^k \right)  & \text{for }a<0. \end{cases}}`   |
        +---------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------+
        |`{\displaystyle Y = a/X; \quad a \in                     |`{\displaystyle =\frac{|a|}{y^2}                             |`{\displaystyle =\begin{cases}                                                       |
        |\mathbb{R}\setminus \{0\}; \quad  x>0 }.`                |f_X \left(                                                   |F_X \left( \frac{a}{y} \right) & \text{for }a>0,\\                                   |
        |                                                         |\frac{a}{y} \right) }`                                       |1-F_X \left( \frac{a}{y} \right)  & \text{for }a<0. \end{cases}}`                    |
        +---------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------+



|spacingend|

Please see the above Table. :ref:`table_linear_transform`.

For more detailed result: see :cite:t:`Rinne2008`, p. 218-219.





|newpage|

Linear transformations of random variables
-----------------------------------------------------------------


All distributions have location (`L`) and Scale (`S`) parameters along with any other parameters needed. The distributions are given in standard forms  where `L=0` and `S=1`. The nonstandard forms can be obtained for the various functions using the following transformations:


|spacingstart|

.. _table_linear_transform:
.. table:: The linear transformation

        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | Function                                                | Transformation                                                                              |                 
        +=========================================================+=============================================================================================+
        | random variates                                         | `\text{rnd}_X(L,S) = L + S \cdot \text{rnd}X(0,1)`                                          |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulative distribution function                        | `\text{cdf}_X(x;L,S) = \text{cdf}_X \left(\frac{x-L}{S};0,1\right)`                         |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | probability density function                            | `\text{pdf}_X(x;L,S) = \frac{1}{S} \cdot \text{pdf}_X \left(\frac{x-L}{S};0,1\right)`       |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | quantile function                                       | `\text{qtf}_X(q;L,S) =  L + S \cdot \text{qtf}_X(q;0,1)`                                    |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | probability sparsity function                           | `\text{psf}_X(q;L,S) =  S \cdot \text{psf}_X(q;0,1)`                                        |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | hazard function                                         | `\text{hf}_X(x;L,S) =  \frac{1}{S} \cdot \text{hf}_X \left(\frac{x-L}{S};0,1\right)`        |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulative hazard function                              | `\text{chf}_X(x;L,S) = \text{chf}_X \left(\frac{x-L}{S};0,1\right)`                         |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | survival function                                       | `\text{sf}_X(x;L,S) = \text{sf}_X \left(\frac{x-L}{S};0,1\right)`                           |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | inverse survival function                               | `\text{isf}_X(p;L,S) =  L + S \cdot \text{isf}_X(p;0,1)`                                    |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | moment generating function                              | `M_X(t;L,S) = e^{t \cdot L} \cdot M_X(t \cdot S;0,1)`                                       |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | characteristic function                                 | `C_X(t;L,S) = e^{it \cdot L} \cdot C_X(t \cdot S;0,1)`                                      |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulant generating function                            | `K_X(t;L,S) = t \cdot L + K_X(t \cdot S;0,1)`                                               |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | differential entropy                                    | `\text{h}_X(L,S) = \text{h}_X(0,1) + \log(S)`                                               |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | mean                                                    | `\mu_X(1;L,S) =  L + S \cdot \mu_X(1;0,1)`                                                  |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | central moments                                         | `\mu_X(r;L,S) =  S^r \cdot \mu_X(r;0,1); r>1`                                               |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulants                                               | `\kappa_X(r;L,S) =  S^r \cdot \kappa_X(r;0,1); r>1`                                         |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+

|spacingend|

Please see the above Table. :ref:`table_linear_transform`.

For more detailed result: see :cite:t:`Rinne2008`, p. 218-219.


**Examples**


*   Standard normal distribution



*   Ch-squared distribution with different scales












|newpage|

Random variables having mixture distributions
-----------------------------------------------------------------


A random variable follows a mixture distribution if its cumulative distribution function (and the probability density function if it exists) can be expressed as a convex combination (i.e. a weighted sum, with non-negative weights `w_i` that sum to 1) of other distribution functions and density functions. The individual distributions that are combined to form the mixture distribution are called the mixture components, and the probabilities (or weights) associated with each component are called the mixture weights `w_i`. See also Wikipedia :cite:p:`WikipediaDef31`.



|spacingstart|

.. _table_mixture:
.. table:: The mixture distribution

        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | Function                                                | Transformation                                                                              |                 
        +=========================================================+=============================================================================================+
        | random variates                                         | see text below                                                                              |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulative distribution function                        | `\text{cdf}_Z(x) = \sum_{i=1}^k w_i \cdot \text{cdf}_{X_i}(x)`                              |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | probability density function                            | `\text{pdf}_Z(x) = \sum_{i=1}^k w_i \cdot \text{pdf}_{X_i}(x)`                              |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | probability mass function                               | `\text{pmf}_Z(x) = \sum_{i=1}^k w_i \cdot \text{pmf}_{X_i}(x)`                              |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | survival function                                       | `\text{sf}_Z(x) = \sum_{i=1}^k w_i \cdot \text{sf}_{X_i}(x)`                                |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | moment generating function                              | `M_Z(t) = \sum_{i=1}^k w_i \cdot M_{X_i}(t)`                                                |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | characteristic function                                 | `C_Z(t) = \sum_{i=1}^k w_i \cdot C_{X_i}(t)`                                                |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | raw moments                                             | `\mu'_Z(r) = \sum_{i=1}^k w_i \cdot \mu'_{X_i}(x)`                                          |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+

|spacingend|

Please see the above Table. :ref:`table_mixture`.


The cumulants and the central moments can be calculated from the raw moments.

The cumulant generating function can be calculated from the moment generating function.


**Examples**



*   Skellam: poisson with same rate back to back


*   Laplace: exponential with same rate back to back


*   Asymmetric Laplace: exponential with different rates back to back


*   Hyperexponential distribution









|newpage|

Linear combinations of independent random variables
-----------------------------------------------------------------


Suppose `Z` is the sum of `n` independent random variables `X_{1},\dots ,X_{n}` each with probability mass functions `f_{X_{i}}(x)`. Then `Z=\sum _{i=1}^{n}{X_{i}}` is distributed as the convolution of the distributions of the `X_{i}`.

See also: Wikipedia :cite:p:`WikipediaDef32`. 

In cases where there are no known expressions in terms of other, readily computed distributions, the distribution of  `Z` can be calculated using the characteristic functions of the `X_i`, as shown in the table below.


|spacingstart|

.. _table_sums_rv:
.. table:: The sums of random variables


        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | Function                                                | Transformation                                                                              |                 
        +=========================================================+=============================================================================================+
        | random variates                                         | `\text{rnd}_Z() = \sum_{i=1}^k a_i \cdot \text{rnd}_{X_i}()`                                |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | moment generating function                              | `M_Z(t) = \prod_{i=1}^k M_{X_i}(a_i \cdot t)`                                               |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | characteristic function                                 | `C_Z(t) = \prod_{i=1}^k C_{X_i}(a_i \cdot t)`                                               |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulant generating function                            | `K_Z(t) = \sum_{i=1}^k K_{X_i}(a_i \cdot t)`                                                |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulants                                               | `\kappa_Z(r) = \sum_{i=1}^k a_i^r \cdot \kappa_{X_i}(r)`                                    |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+

|spacingend|

Please see the above Table. :ref:`table_sums_rv`.


The raw moments and central moments are calculated from the cumulants.

The pmf, pdf and cdf are calculated by methods 1-3.

The qtf is started via the cumulants (Cornish-Fisher), followed by Newton iterations.

The pmf-vector is calculated via discrete convolution.









|newpage|

The log-transform of continuous random variables
-----------------------------------------------------------------


A random variable `X` has a log-transform `Y` (which also is a random variable), if `\text{cdf}_X(x) = \text{cdf}_Y \left(\log(x)\right)`, in other words if `\log(X) \sim Y` (where `\sim` means "is distributed as"). 
The transformation is only useful if the domain of `X` is `(a, b)` with `0 \le a < b \le \infty` (otherwise the domain of `Y` would be extended into the complex plane).
It is only implemented for continuous distributions.

The pdf, cdf, sf, qtf and isf of `X` and `Y` can be expressed in terms of each other, as shown below, together with the remarkable fact that the characteristic function of `Y` can be expressed in terms of the raw moments of `X` (this assumes that the raw moments of `X` are available in a form which allows to replace the discrete index variable `r` with the continuous complex variable `it`).


|spacingstart|

.. _table_logtransform:
.. table:: The logarithmic transformation of a variable

        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | Function                                                | Transformation                                                                              |                 
        +=========================================================+=============================================================================================+
        | random variates                                         | `\text{rnd}_Y() = \log(\text{rnd}_X())`                                                     |
        +                                                         +---------------------------------------------------------------------------------------------+
        |                                                         | `\text{rnd}_X() = \exp(\text{rnd}_Y())`                                                     |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | probability density function                            | `\text{pdf}_Y(t) = \text{pdf}_X \left(\exp(t)\right) \cdot \exp(t)`                         |
        +                                                         +---------------------------------------------------------------------------------------------+
        |                                                         | `\text{pdf}_X(u) = \text{pdf}_Y \left(\log(u)\right) \cdot \frac{1}{u}`                     |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | cumulative distribution function                        | `\text{cdf}_Y(t) = \text{cdf}_X \left(\exp(t)\right)`                                       |
        +                                                         +---------------------------------------------------------------------------------------------+
        |                                                         | `\text{cdf}_X(u) = \text{cdf}_Y \left(\log(u)\right)`                                       |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | survival function                                       | `\text{sf}_Y(t) = \text{sf}_X \left(\exp(t)\right)`                                         |
        +                                                         +---------------------------------------------------------------------------------------------+
        |                                                         | `\text{cdf}_X(u) = \text{cdf}_Y \left(\log(u)\right)`                                       |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | quantile function                                       | `\text{qtf}_Y(q) = \exp \left( \text{qtf}_X \right)`                                        |
        +                                                         +---------------------------------------------------------------------------------------------+
        |                                                         | `\text{qtf}_X(q) = \log \left( \text{qtf}_Y \right)`                                        |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        | inverse survival function                               | `\text{isf}_Y(q) = \exp \left( \text{isf}_X \right)`                                        |
        +                                                         +---------------------------------------------------------------------------------------------+
        |                                                         | `\text{isf}_X(q) = \log \left( \text{isf}_Y \right)`                                        |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+
        |characteristic function of `Y` and raw moments of `X`    | `C_Y(t) = \mu'_X(it)`                                                                       |
        +---------------------------------------------------------+---------------------------------------------------------------------------------------------+



|spacingend|

Please see the above Table. :ref:`table_logtransform`.


One of the major features of the log-transform is its ability to express the distribution of the product of variables `X_i` as the sum of their log-transforms `Y_i`.


**Examples**

*   Lognormal distribution


X: Lognormal

Y: Standard normal



*   Beta distribution 







