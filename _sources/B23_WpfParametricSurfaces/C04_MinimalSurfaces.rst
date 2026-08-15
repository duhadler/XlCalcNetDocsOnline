

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />









|newpage|




Minimal surfaces
==============================================



Helicoid
-------------------------------------


See also: https://mathworld.wolfram.com/Helicoid.html

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



|TestHelicoid_a| `\quad` |TestHelicoid_b|

.. |TestHelicoid_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestHelicoid_a.3D.xml.jpg
   :width: 30 %

.. |TestHelicoid_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestHelicoid_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Helicoid (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Helicoid (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).




.. code-block:: csharp

    double a = 1;
    x = u * Math.Cos(v);
    z = u * Math.Sin(v);
    y = v;



References

Gray, A. Modern Differential Geometry of Curves and Surfaces with Mathematica, 2nd ed. Boca Raton, FL: CRC Press, pp. 449 and 644, 1997.






|newpage|


Bours minimal surface
------------------------------------------------


See also: https://mathworld.wolfram.com/BoursMinimalSurface.html

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



.. code-block:: csharp

    double sv = Math.Sin(v);
    double s2v = Math.Sin(2*v);
    double c32u = Math.Cos(1.5*v);
    double cv = Math.Cos(v);
    double c2v = Math.Cos(2*v);
    double u2 = 0.5*u*u;
    double u32 = (4/3)* Math.Sqrt(u*u*u);
    x = u * cv - u2 * c2v;
    y = -u * sv - u2 * s2v;
    z = u32 * c32u;



|TestBour_a| `\quad` |TestBour_b|

.. |TestBour_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestBour_a.3D.xml.jpg
   :width: 30 %

.. |TestBour_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestBour_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Bours Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Bours Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|


Catalan minimal surface
--------------------------------------------------


See also: https://mathworld.wolfram.com/CatalanMinimalSurface.html

See also: https://en.wikipedia.org/wiki/Catalan%27s_minimal_surface

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.


.. code-block:: csharp

    x = u - u * u * u / 3 + u * v * v;
    y = u * u - v * v;
    z = v - v * v * v / 3 + v * u * u;




|TestCatalan_a| `\quad` |TestCatalan_b|

.. |TestCatalan_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestCatalan_a.3D.xml.jpg
   :width: 30 %

.. |TestCatalan_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestCatalan_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Catalan Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Catalan Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|newpage|






Ennepers first minimal surface
-------------------------------------------------------


See also: https://mathworld.wolfram.com/EnnepersMinimalSurface.html

See also: https://en.wikipedia.org/wiki/Enneper_surface

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



.. code-block:: csharp

    x = u - u * u * u / 3 + u * v * v;
    y = u * u - v * v;
    z = v - v * v * v / 3 + v * u * u;




|TestEnneper_a| `\quad` |TestEnneper_b|

.. |TestEnneper_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestEnneper_a.3D.xml.jpg
   :width: 30 %

.. |TestEnneper_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestEnneper_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Ennepers Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Ennepers Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Enneper second minimal surface
------------------------------------------------------


See also: https://mathcurve.com/surfaces.gb/enneper/enneper.shtml


See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



.. code-block:: csharp

    double n = 2;
    double a = 1;
                
    Complex i = Complex.ImaginaryOne;
    Complex w = new Complex(u, v);
    Complex w2nm1 = Complex.Pow(w, 2*n-1)/(2*n-1);
    Complex wn = Complex.Pow(w, n);
    x = a * (w - w2nm1).Real;
    y = a * (-i*(w + w2nm1)).Real;
    z = 2 * a * (wn/n).Real;



|TestEnneper2_a| `\quad` |TestEnneper2_b|

.. |TestEnneper2_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestEnneper2_a.3D.xml.jpg
   :width: 30 %

.. |TestEnneper2_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestEnneper2_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Ennepers Minimal Surface2 (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Ennepers Minimal Surface2 (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Hennebergs minimal surface
------------------------------------------------


See also: https://mathworld.wolfram.com/HennebergsMinimalSurface.html

See also: https://en.wikipedia.org/wiki/Henneberg_surface

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



.. code-block:: csharp

    double sv = Math.Sin(v);
    double s3v = Math.Sin(3*v);
    double cv = Math.Cos(v);
    double c2v = Math.Cos(2*v);
    double c3v = Math.Cos(3*v);
    double shu = Math.Sinh(u);
    double ch2u = Math.Cosh(2*u);
    double sh3u = Math.Sinh(3*u);
    x = 2*shu * cv - (2.0/3.0)*sh3u * c3v;
    y = 2*shu * sv + (2.0/3.0)*sh3u * s3v;
    z = 2*ch2u * c2v;



|TestHenneberg_a| `\quad` |TestHenneberg_b|

.. |TestHenneberg_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestHenneberg_a.3D.xml.jpg
   :width: 30 %

.. |TestHenneberg_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestHenneberg_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Hennebergs Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Hennebergs Minimal Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|newpage|


Scherk’s first minimal surface
-------------------------------------------------


See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.

See also https://mathcurve.com/surfaces.gb/scherk/scherk.shtml
See also  :cite:t:`Krivoshapko2015`, p. 431



.. code-block:: csharp

    var a = 1 / Math.PI;
    var x = u;
    var z = v;
    var y = a * Math.Log(Math.Cos(v / a) / Math.Cos(u / a));
    z = -z;




|TestScherk1_a| `\quad` |TestScherk1_b|

.. |TestScherk1_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestScherk1_a.3D.xml.jpg
   :width: 30 %

.. |TestScherk1_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestScherk1_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Scherk’s first minimal surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Scherk’s first minimal surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).




|newpage|


Scherk’s second minimal surface
--------------------------------------------------


See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.

See also https://mathworld.wolfram.com/ScherksMinimalSurfaces.html

See also  :cite:t:`Krivoshapko2015`, p. 442



.. code-block:: csharp

    var t = v;
    var r = u;
    var r2 = r * r;
    var ct = Math.Cos(t);
    var st = Math.Sin(t);
    var x = Math.Log((1 + r2 + 2 * r * ct) / (1 + r2 - 2 * r * ct));
    var y = Math.Log((1 + r2 - 2 * r * st) / (1 + r2 + 2 * r * st));
    var z = 2 * Math.Atan((2 * r2 * Math.Sin(2 * t)) / (r2 * r2 - 1));
    y = -y;






|TestScherk2_a| `\quad` |TestScherk2_b|

.. |TestScherk2_a| image:: ../_static/ParametricSurfaces/RuledMinimal/TestScherk2_a.3D.xml.jpg
   :width: 30 %

.. |TestScherk2_b| image:: ../_static/ParametricSurfaces/RuledMinimal/TestScherk2_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Scherk’s second minimal surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Scherk’s second minimal surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|


Richmond minimal surface
-------------------------------------------------------------------------


// See also: http://www.3d-meier.de/tut3/Seite250.html  // Richmond Surface III
// See also: https://en.wikipedia.org/wiki/Richmond_surface



.. code-block:: csharp

    var n = 2.0;
    var u2s = Math.Pow(u, 2 * n + 1) / (4 * n + 2);
    var x = -Math.Cos(v) / (2 * u) - u2s * Math.Cos(-(2 * n + 1) * v);
    var y = -Math.Sin(v) / (2 * u) + u2s * Math.Sin(-(2 * n + 1) * v);
    var z = Math.Pow(u, n) * Math.Cos(n * v) / n;





|TestRichmond_a| `\quad` |TestRichmond_b| `\quad` |TestRichmond_c|

.. |TestRichmond_a| image:: ../_static/ParametricSurfaces/RuledMinimal/11a_TestRichmond.3D.xml.jpg
   :width: 30 %

.. |TestRichmond_b| image:: ../_static/ParametricSurfaces/RuledMinimal/11b_TestRichmond.3D.xml.jpg
   :width: 30 %

.. |TestRichmond_c| image:: ../_static/ParametricSurfaces/RuledMinimal/11c_TestRichmond.3D.xml.jpg
   :width: 30 %



**Left figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



|TestRichmond_d| `\quad` |TestRichmond_e| `\quad` |TestRichmond_f|

.. |TestRichmond_d| image:: ../_static/ParametricSurfaces/RuledMinimal/11d_TestRichmond.3D.xml.jpg
   :width: 30 %

.. |TestRichmond_e| image:: ../_static/ParametricSurfaces/RuledMinimal/11e_TestRichmond.3D.xml.jpg
   :width: 30 %

.. |TestRichmond_f| image:: ../_static/ParametricSurfaces/RuledMinimal/11f_TestRichmond.3D.xml.jpg
   :width: 30 %



**Left figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Generalized Ennneper surfaces
-------------------------------------------------------------------------



// See also: http://www.3d-meier.de/tut3/Seite247.html  // Wavy Enneper Surface



.. code-block:: csharp

    var s = 2.0;
    var u2s = Math.Pow(u, 2 * s - 1) / (2 * s - 1);
    var x = u * Math.Cos(v) - u2s * Math.Cos((2 * s - 1) * v);
    var y = -u * Math.Sin(v) - u2s * Math.Sin((2 * s - 1) * v);
    var z = 2 * Math.Pow(u, s) * Math.Cos(s * v) / s;





|TestGenEnneper_b| `\quad` |TestGenEnneper_c| `\quad` |TestGenEnneper_d|

.. |TestGenEnneper_b| image:: ../_static/ParametricSurfaces/RuledMinimal/12b_TestGenEnneper.3D.xml.jpg
   :width: 30 %

.. |TestGenEnneper_c| image:: ../_static/ParametricSurfaces/RuledMinimal/12c_TestGenEnneper.3D.xml.jpg
   :width: 30 %

.. |TestGenEnneper_d| image:: ../_static/ParametricSurfaces/RuledMinimal/12d_TestGenEnneper.3D.xml.jpg
   :width: 30 %



**Left figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Richmond minimal surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



|TestGenEnneper_e| `\quad` |TestGenEnneper_f| `\quad` |TestGenEnneper_g|

.. |TestGenEnneper_e| image:: ../_static/ParametricSurfaces/RuledMinimal/12e_TestGenEnneper.3D.xml.jpg
   :width: 30 %

.. |TestGenEnneper_f| image:: ../_static/ParametricSurfaces/RuledMinimal/12f_TestGenEnneper.3D.xml.jpg
   :width: 30 %

.. |TestGenEnneper_g| image:: ../_static/ParametricSurfaces/RuledMinimal/12g_TestGenEnneper.3D.xml.jpg
   :width: 30 %



**Left figure**: Generalized Ennneper surface  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Generalized Ennneper surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Generalized Ennneper surface  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





