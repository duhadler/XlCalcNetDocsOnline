

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />






|newpage|

Basic curves
==============================================================




Regular convex polygon
------------------------------------------------------------------------------------------

.. method:: User.RegularConvexPolygon(a, Resolution, AsPolar = false)

    A regular polygon is a polygon that is direct equiangular (all angles are equal in measure) and equilateral (all sides have the same length). Regular polygons may be either convex, star or skew. In the limit, a sequence of regular polygons with an increasing number of sides approximates a circle.

    .. math:: r = \frac{a}{\cos \left(t - \alpha/2 - \alpha \ \lfloor \theta/\alpha \rfloor \right)}, \quad \text{where } \alpha = \frac{2 \pi}{n}.

    .. math:: x(t) = r \cos(t)),

    .. math:: y(t) = r \sin(t).


    See also: https://en.wikipedia.org/wiki/Star_polygon

    See also: https://mathcurve.com/polyedres/regulier/polygoneregulier.shtml



    See also: https://mathcurve.com/courbes2d/goursat/goursat.shtml

    See also: https://mathcurve.com/courbes3d.gb/polygramme/polygramme.shtml

    See also: https://mathcurve.com/courbes3d.gb/billardcylindrique/billardcylindrique.shtml



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Regular_polygon_a| `\quad` |Regular_polygon_b| `\quad` |Regular_polygon_c|

    .. |Regular_polygon_a| image:: ../_static/ParametricCurves/BasicCurves/RegularConvexPolygon.*
       :width: 30 %

    .. |Regular_polygon_b| image:: ../_static/ParametricCurves/BasicCurves/RegularConvexPolygon.*
       :width: 30 %

    .. |Regular_polygon_c| image:: ../_static/ParametricCurves/BasicCurves/RegularConvexPolygon.*
       :width: 30 %





    **Left figure**: Regularpolygon


    **Middle figure**: Regularpolygon


    **Right figure**: Regularpolygon







|newpage|


Circle
------------------------------------------------------------------------------------------

.. method:: User.Circle(a, Resolution, AsPolar = false)


    A circle is the set of points in a plane that are equidistant from a given point `O`. The parametric equations for a circle of radius `a` can be given by 


    .. math:: x(t) = a \cos(t)),

    .. math:: y(t) = a \sin(t).


    See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram2D101`,  MathCurve :cite:p:`MathCurve2D101`.



    |Circle_a| `\quad` |Circle_b| `\quad` |Circle_c|

    .. |Circle_a| image:: ../_static/ParametricCurves/BasicCurves/Circle.*
       :width: 30 %

    .. |Circle_b| image:: ../_static/ParametricCurves/BasicCurves/Circle.*
       :width: 30 %

    .. |Circle_c| image:: ../_static/ParametricCurves/BasicCurves/Circle.*
       :width: 30 %



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    **Left figure**: Circle


    **Middle figure**: Circle


    **Right figure**: Circle




|newpage|


Ellipse
------------------------------------------------------------------------------------------

.. method:: User.Ellipse(a, Resolution, AsPolar = false)


    An ellipse is a plane curve surrounding two focal points, such that for all points on the curve, the sum of the two distances to the focal points is a constant. The parametric equations of a standard ellipse centered at the origin with width `2a` and height `2b` can be given by (with `0 \le t < 2\pi`):

    .. math:: x(t) = a \cos(t)),

    .. math:: y(t) = b \sin(t).

    Assuming `a \ge b`, the focal points are `(\pm \sqrt{a^2-b^2}, 0)`.


    See also  Wikipedia :cite:p:`Wikipedia2D102`,  MathWorld :cite:p:`Wolfram2D102`,  MathCurve :cite:p:`MathCurve2D102`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')



    |Ellipse_a| `\quad` |Ellipse_b| `\quad` |Ellipse_c|

    .. |Ellipse_a| image:: ../_static/ParametricCurves/BasicCurves/Ellipse.*
       :width: 30 %

    .. |Ellipse_b| image:: ../_static/ParametricCurves/BasicCurves/Ellipse.*
       :width: 30 %

    .. |Ellipse_c| image:: ../_static/ParametricCurves/BasicCurves/Ellipse.*
       :width: 30 %





    **Left figure**: Ellipse


    **Middle figure**: Ellipse


    **Right figure**: Ellipse





|newpage|


Parabola
-------------------------------------------------------------------------------

.. method:: User.Parabola(a, Resolution, AsPolar = false)

    A parabola is a plane curve which is mirror-symmetrical and is approximately U-shaped. It fits several superficially different mathematical descriptions, which can all be proved to define exactly the same curves. 

    The graph of a quadratic function `y = a x^2 + b x + c` (with `a \ne 0`) is a parabola with its axis parallel to the `y`-axis. Conversely, every such parabola is the graph of a quadratic function.

    The surface of revolution obtained by rotating a parabola about its axis of symmetry is called a paraboloid. 

    See also:  https://mathworld.wolfram.com/Parabola.html

    See also: https://en.wikipedia.org/wiki/Parabola


    In polar coordinates, the equation of a parabola with parameter a and center (0, 0) is given by `\displaystyle r(t) = - \frac{2a}{1 + \cos(t)}`. It can also be written parametrically as 

    .. math:: x(t) = a t^2,

    .. math:: y(t) = 2 a t.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Parabola_a| `\quad` |Parabola_b| `\quad` |Parabola_c|

    .. |Parabola_a| image:: ../_static/ParametricCurves/BasicCurves/Parabola.*
       :width: 30 %

    .. |Parabola_b| image:: ../_static/ParametricCurves/BasicCurves/Parabola.*
       :width: 30 %

    .. |Parabola_c| image:: ../_static/ParametricCurves/BasicCurves/Parabola.*
       :width: 30 %





    **Left figure**: Parabola


    **Middle figure**: Parabola


    **Right figure**: Parabola






|newpage|


Hyperbola
-------------------------------------------------------------------------------

.. method:: User.Hyperbola(a, Resolution, AsPolar = false)

    In polar coordinates, the equation of a hyperbola centered at the origin (i.e., with `x_0=y_0=0`) is `\displaystyle r2(t) = \frac{a^2 b^2}{b^2 \cos^2(t) - a^2 \sin^2(t)}`.

    Parametric equations for the right branch of a hyperbola are given by


    .. math:: x(t) = a \cosh(t),

    .. math:: y(t) = b \sinh(t),

    which ranges over the right branch of the hyperbola. 

    A parametric representation which ranges over both branches of the hyperbola is


    .. math:: x(t) = a \sec(t),

    .. math:: y(t) = b \tan(t),

    with `t \in (-\pi,\pi)` and discontinuities at `\pm \pi/2`.


    See also:  https://mathworld.wolfram.com/Hyperbola.html

    See also:  https://mathworld.wolfram.com/ConicSection.html



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Hyperbola_a| `\quad` |Hyperbola_b| `\quad` |Hyperbola_c|

    .. |Hyperbola_a| image:: ../_static/ParametricCurves/BasicCurves/Hyperbola.*
       :width: 30 %

    .. |Hyperbola_b| image:: ../_static/ParametricCurves/BasicCurves/Hyperbola.*
       :width: 30 %

    .. |Hyperbola_c| image:: ../_static/ParametricCurves/BasicCurves/Hyperbola.*
       :width: 30 %


    **Left figure**: Hyperbola

    **Middle figure**: Hyperbola

    **Right figure**: Hyperbola








|newpage|


Cycloid
-------------------------------------------------------------------------------

.. method:: User.Cycloid(a, Resolution, AsPolar = false)


    The cycloid is the locus of a point on the rim of a circle of radius a rolling along a straight line. If the cycloid has a cusp at the origin and its humps are oriented upward, its parametric equation is 


    .. math:: x(t) = a (t - \sin(t)),

    .. math:: y(t) = a (t - \cos(t)).



    See also  Wikipedia :cite:p:`Wikipedia2D103`,  MathWorld :cite:p:`Wolfram2D103`,  MathCurve :cite:p:`MathCurve2D103`.




    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Cycloid_a| `\quad` |Cycloid_b| `\quad` |Cycloid_c|

    .. |Cycloid_a| image:: ../_static/ParametricCurves/BasicCurves/Cycloid.*
       :width: 30 %

    .. |Cycloid_b| image:: ../_static/ParametricCurves/BasicCurves/Cycloid.*
       :width: 30 %

    .. |Cycloid_c| image:: ../_static/ParametricCurves/BasicCurves/Cycloid.*
       :width: 30 %





    **Left figure**: Cycloid


    **Middle figure**: Cycloid


    **Right figure**: Cycloid





|newpage|


Trochoid
-------------------------------------------------------------------------------

.. method:: User.Trochoid(a, Resolution, AsPolar = false)


    A trochoid is the locus of a point at a distance b from the center of a circle of radius a rolling on a fixed line. A trochoid has parametric equations 


    .. math:: x(t) = a t - b \sin(t),

    .. math:: y(t) = a t - b \cos(t)).

    If `b<a`, the trochoid is known as a curtate cycloid; if `b=a`, it is a cycloid; and if `b>a`, the curve is a prolate cycloid. 


    See also  Wikipedia :cite:p:`Wikipedia2D104`,  MathWorld :cite:p:`Wolfram2D104`,  MathCurve :cite:p:`MathCurve2D104`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')



    |Trochoid_a| `\quad` |Trochoid_b| `\quad` |Trochoid_c|

    .. |Trochoid_a| image:: ../_static/ParametricCurves/BasicCurves/Trochoid.*
       :width: 30 %

    .. |Trochoid_b| image:: ../_static/ParametricCurves/BasicCurves/Trochoid.*
       :width: 30 %

    .. |Trochoid_c| image:: ../_static/ParametricCurves/BasicCurves/Trochoid.*
       :width: 30 %





    **Left figure**: Trochoid


    **Middle figure**: Trochoid


    **Right figure**: Trochoid






|newpage|


Cardioid
--------------------------------------------------------------------


.. method:: User.Cardioid(a, Resolution, AsPolar = false)

    Returns the curve given by the polar equation 
    
    .. math:: r = a (1 - \cos (\theta)).

    See also:  Wikipedia :cite:p:`Wikipedia2D201`,  MathWorld :cite:p:`Wolfram2D201`


    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |picCardioid_p| `\quad` |picCardioid_c|

    .. |picCardioid_p| image:: ../_static/ParametricCurves/BasicCurves/Cardioid.*
       :width: 30%

    .. |picCardioid_c| image:: ../_static/ParametricCurves/BasicCurves/Cardioid.*
       :width: 30%




    **Left figure**: polar coordinates. **Right figure**: cartesian coordinates.






|newpage|


Limaçon curve
---------------------------------------------------------


.. method:: User.Limacon(AsPolar, Resolution, a, b)

    Returns the curve given by the polar equation 
    
    .. math:: r = b + a \cos (\theta).


    See also: see also  Wikipedia :cite:p:`Wikipedia2D202`,  MathWorld :cite:p:`Wolfram2D202`



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')





    |picLimacon_p| `\quad` |picLimacon_c|

    .. |picLimacon_p| image:: ../_static/ParametricCurves/BasicCurves/Limacon.*
       :width: 30%

    .. |picLimacon_c| image:: ../_static/ParametricCurves/BasicCurves/Limacon.*
       :width: 30%




    **Left figure**: polar coordinates. **Right figure**: cartesian coordinates.





|newpage|


Conchoid of de Sluze
--------------------------------------------------------


.. method:: User.ConchoidOfDeSluze(AsPolar, Resolution, a)

    Returns the curve given by the polar equation 

    .. math:: r = \sec(\theta) + a \cos (\theta).


    See also: see also  Wikipedia :cite:p:`Wikipedia2D204`,  MathWorld :cite:p:`Wolfram2D204`


    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Conchoid_of_de_Sluze_p_a| `\quad` |Conchoid_of_de_Sluze_c_a|

    .. |Conchoid_of_de_Sluze_p_a| image:: ../_static/ParametricCurves/BasicCurves/Conchoid_of_de_Sluze.*
       :width: 30%

    .. |Conchoid_of_de_Sluze_c_a| image:: ../_static/ParametricCurves/BasicCurves/Conchoid_of_de_Sluze.*
       :width: 30%



    **Left figure**: polar coordinates. **Right figure**: cartesian coordinates.









|newpage|


Freeth's Nephroid
--------------------------------------------------

.. method:: User.FreethNephroid(a, Resolution, AsPolar = false)

    The curve has the polar equation


    .. math:: r = a \left[1 + 2 \sin \left(\tfrac{1}{2} \theta \right) \right]



    See also: Wikipedia :cite:p:`Wikipedia2D206`,  MathWorld :cite:p:`Wolfram2D206`


    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Freeth_Nephroid_p_a| `\quad` |Freeth_Nephroid_c_a|

    .. |Freeth_Nephroid_p_a| image:: ../_static/ParametricCurves/BasicCurves/FreethNephroid.*
       :width: 30%

    .. |Freeth_Nephroid_c_a| image:: ../_static/ParametricCurves/BasicCurves/FreethNephroid.*
       :width: 30%



    **Left figure**: polar coordinates. **Right figure**: cartesian coordinates.





|newpage|


Strophoid
--------------------------------------------

.. method:: User.Strophoid(a, b, Resolution, AsPolar = false)

    The name strophoid means "belt with a twist". The polar form for a general strophoid is 

    .. math:: r = \frac{b \sin(a - 2 \theta)}{\sin(a - \theta)}


    See also: Wikipedia :cite:p:`Wikipedia2D207`,  MathWorld :cite:p:`Wolfram2D207`

    A special cases is the right strophoid with `a = \pi/2`.

    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')

    An example in C\#

    .. code-block:: csharp

        using User;
        Curve = User.Cardioid(a: 1, Resolution: 200, AsPolar: true);
        User.Chart2D.Show(Curve, Template = "PolarCurve", Title = "Cardioid");



    |Strophoid_p_a| `\quad` |Strophoid_c_a|

    .. |Strophoid_p_a| image:: ../_static/ParametricCurves/BasicCurves/Right_Strophoid.*
       :width: 30%

    .. |Strophoid_c_a| image:: ../_static/ParametricCurves/BasicCurves/Right_Strophoid.*
       :width: 30%


    **Left figure**: polar coordinates. **Right figure**: cartesian coordinates.








|newpage|


Cycloid of Ceva
-------------------------------------------

.. method:: User.CycloidOfCeva(a, Resolution, AsPolar = false)

A curve with the polar form

    .. math:: r = 1 + 2 \cos(2 \theta).



    See also: Wikipedia :cite:p:`Wikipedia2D208`,  MathWorld :cite:p:`Wolfram2D208`


    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Cycloid_of_Ceva_p_a| `\quad` |Cycloid_of_Ceva_c_a|

    .. |Cycloid_of_Ceva_p_a| image:: ../_static/ParametricCurves/BasicCurves/Cycloid_of_Ceva.*
       :width: 30%

    .. |Cycloid_of_Ceva_c_a| image:: ../_static/ParametricCurves/BasicCurves/Cycloid_of_Ceva.*
       :width: 30%



    **Left figure**: polar coordinates. **Right figure**: cartesian coordinates.











|newpage|


Lemniscate of Gerono
-------------------------------------------------------------------------------

.. method:: User.LemniscateOfGerono(a, Resolution, AsPolar = false)


    This curve is also known as Eight curve. It has parametric equations


    .. math:: x(t) = a \sin(t),

    .. math:: y(t) = x(t) \cos(t)).


    See also  Wikipedia :cite:p:`Wikipedia2D110`,  MathWorld :cite:p:`Wolfram2D110`, MathCurve :cite:p:`MathCurve2D110`.


    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')




    |Lemniscate_of_Gerono_a| `\quad` |Lemniscate_of_Gerono_b| `\quad` |Lemniscate_of_Gerono_c|

    .. |Lemniscate_of_Gerono_a| image:: ../_static/ParametricCurves/BasicCurves/Lemniscate_of_Gerono.*
       :width: 30 %

    .. |Lemniscate_of_Gerono_b| image:: ../_static/ParametricCurves/BasicCurves/Lemniscate_of_Gerono.*
       :width: 30 %

    .. |Lemniscate_of_Gerono_c| image:: ../_static/ParametricCurves/BasicCurves/Lemniscate_of_Gerono.*
       :width: 30 %





    **Left figure**: Lemniscate of Gerono


    **Middle figure**: Lemniscate of Gerono


    **Right figure**: Lemniscate of Gerono







|newpage|



Lemniscate of Bernoulli
-------------------------------------------------------------------------------

.. method:: User.LemniscateOfBernoulli(a, Resolution, AsPolar = false)


    The lemniscate of Bernoulli is a polar curve defined as the locus of points such that the the product of distances from two fixed points `(-a,0)` and `(a,0)`  is a constant `a^2`. It has parametric equations


    .. math:: x(t) = \frac{a \cos(t)}{1 + \sin^2(t)},

    .. math:: y(t) = x(t) \sin(t)).


    See also  Wikipedia :cite:p:`Wikipedia2D109`,  MathWorld :cite:p:`Wolfram2D109`, MathCurve :cite:p:`MathCurve2D109`.



    An example in Python

    .. code-block:: pycon

        >>> from mpfunlab import User
        >>> Curve = User.Cardioid(a = 1, Resolution = 200, AsPolar = true)
        >>> User.Chart2D.Show(Curve, Template = 'PolarCurve', Title = 'Cardioid')



    |Lemniscate_of_Bernoulli_a| `\quad` |Lemniscate_of_Bernoulli_b| `\quad` |Lemniscate_of_Bernoulli_c|

    .. |Lemniscate_of_Bernoulli_a| image:: ../_static/ParametricCurves/BasicCurves/Lemniscate_of_Bernoulli.*
       :width: 30 %

    .. |Lemniscate_of_Bernoulli_b| image:: ../_static/ParametricCurves/BasicCurves/Lemniscate_of_Bernoulli.*
       :width: 30 %

    .. |Lemniscate_of_Bernoulli_c| image:: ../_static/ParametricCurves/BasicCurves/Lemniscate_of_Bernoulli.*
       :width: 30 %





    **Left figure**: Lemniscate of Bernoulli


    **Middle figure**: Lemniscate of Bernoulli


    **Right figure**: Lemniscate of Bernoulli






