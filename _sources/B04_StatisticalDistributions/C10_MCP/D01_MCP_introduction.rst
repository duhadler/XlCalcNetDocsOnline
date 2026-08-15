

.. |newpage| raw:: latex

   \newpage


.. |cr| raw:: latex

   \hspace{0.0mm}





.. _rst_dist_mcp_overview: 


Overview and literature
-------------------------------------------------------------------------------

See also: :cite:t:`Hahn1971`, :cite:t:`Narula1978`, :cite:t:`Stoline1979`, :cite:t:`Tong1990`, :cite:t:`Genz2020`.



See also: :cite:t:`Bechhofer1988`

See also: :cite:t:`Genz2009`

See also: :cite:t:`Genz2020`

See also: :cite:t:`Hahn1971`

See also: :cite:t:`Narula1978`

See also: :cite:t:`Stoline1979`

See also: :cite:t:`Tong1990`

For tables see :cite:t:`Soong2001`.

For tables see :cite:t:`David1953`.

For tables see :cite:t:`David1972`.



An `n`-dimensional random variable `\textbf{X}` with mean vector `\boldsymbol{\mu}` and covariance matrix  `\boldsymbol{\Sigma}` is said to have a nonsingular multivariate normal distribution, in symbols `\boldsymbol{X}  \sim \mathcal{N}_n(\boldsymbol{\mu}, \boldsymbol{\Sigma})`, if  `\boldsymbol{\Sigma}` is positive definite, and the density function of `\textbf{X}` is of the form (see Tong 1990):


.. math:: f(\boldsymbol{x; \mu, \Sigma}) = \frac{1}{(2\pi)^{n/2}  \vert \boldsymbol{\Sigma} \vert ^{1/2}} e^{-Q_n(\boldsymbol{x; \mu, \Sigma})/2}, \quad \boldsymbol{x} \in \Re^n

where


.. math:: Q_n(\boldsymbol{x; \mu, \Sigma}) = (\boldsymbol{x - \mu})' \boldsymbol{\Sigma^{-1}} (\boldsymbol{x - \mu}).


The notion of cumulative distribution function (cdf) in one dimension can be extended to the multidimensional case, based on rectangular regions. We define the cdf  `F(\mathbf {x} )` of a random vector  `\mathbf {X}` as the probability that all components  `\mathbf {X}` are less than or equal to the corresponding values in the vector `\mathbf {x}`:

.. math::  F(\mathbf {x} )=\mathbb {P} (\mathbf {X} \leq \mathbf {x} ),\quad {\text{where }}\mathbf {X} \sim {\mathcal {N}}({\boldsymbol {\mu }},\,{\boldsymbol {\Sigma }}).


See also: Genz(2009), Bretz(2003).



Let `\boldsymbol{R} = (\rho_{ij})` be an `n \times n` symmetric matrix such that it is either positive definite or positive semidefinite and `\rho_{ii} = 1 (i=1,\ldots,n)`.
Let  `\textbf{Z} = (Z_1,\ldots,Z_{n})'` have an `\mathcal{N}_n(\boldsymbol{0}, \boldsymbol{R})` distribution, and let the univariate variable `S` be such that `S` is independent of `\boldsymbol{Z}`, and `\nu S^2` has a `\chi^2(\nu)` distribution. Then a natural generalization of the Student's `t` variable is


.. math:: \boldsymbol{t} = (t_1,\ldots,t_n)' = \left(\frac{Z_1}{S},\ldots,\frac{Z_n}{S}\right)' .


If `\boldsymbol{R}` is positive definite, then the density of `\boldsymbol{t}` (with correlation matrix `\boldsymbol{R}` and degrees of freedom `\nu`) is given by \citep{Tong_1990}:


.. math:: h(\boldsymbol{t; R}, \nu)= \frac{\Gamma((n+\nu)/2)}{(\nu \pi)^{n/2} \Gamma(\nu/2) \vert \boldsymbol{R}  \vert^{1/2}} \left(1+\frac{1}{\nu} \boldsymbol{t}' \boldsymbol{R}^{-1} \boldsymbol{t} \right)^{-(n+\nu)/2} , \quad \boldsymbol{t} \in \Re^n.



The notion of cumulative distribution function (cdf) in one dimension can be extended to the multidimensional case, based on rectangular regions. We define the cdf  `F(\mathbf {x} )` of a random vector  `\mathbf {X}` as the probability that all components  `\mathbf {X}` are less than or equal to the corresponding values in the vector `\mathbf {x}`:

.. math::  F(\mathbf {x} )=\mathbb {P} (\mathbf {X} \leq \mathbf {x} ),\quad {\text{where }}\mathbf {X} \sim {\mathcal {N}}({\boldsymbol {\mu }},\,{\boldsymbol {\Sigma }}).


See also: Genz(2009), Bretz(2003).







