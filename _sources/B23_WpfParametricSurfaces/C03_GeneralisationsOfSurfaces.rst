

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />








|newpage|




Generalisations of common surfaces
==============================================



Parametric Surfaces: `x=f(u,v),` `y=g(u,v),` `z=h(u,v)`



Ellipsoid
-------------------------------------------------


    The parametric equations of an ellipsoid can be written as 


.. math:: x(u, v) = a \cos(u) \sin(v),

.. math:: y(u, v) = b \sin(u) \sin(v),

.. math:: z(u, v) = r \sin(t),

for `u \in [0, 2 \pi)` and `v \in [0, \pi]`.


See also: http://paulbourke.net/geometry/spherical/
See also: https://mathcurve.com/surfaces.gb/lame/lame.shtml
See also: https://mathworld.wolfram.com/Ellipsoid.html        

See also  :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`.

    

.. code-block:: text

    var a = 1.0;
    var b = 2.0;
    var c = 3.0;
    var x = a * Math.Cos(u) * Math.Cos(v);
    var y = b * Math.Cos(u) * Math.Sin(v);
    var z = c * Math.Sin(u);



If the lengths of two axes of an ellipsoid are the same, the figure is called an ellipsoid of revolution or spheroid. Denote the equal semi-axes lengths of a spheroid `a=b`, call `a` the equatorial radius, and call the other semi-axis length the polar radius `c`. Then if `a>c`, the spheroid is called an oblate spheroid, and if `a<c`, the spheroid is called an prolate spheroid. If all three semi-axes lengths are the same so `a=b=c`, the ellipsoid is a sphere. 

|picEllipsoid_a| `\quad` |picEllipsoid_b|

.. |picEllipsoid_a| image:: ../_static/ParametricSurfaces/GenCommon/Ellipsoid_small.jpg
    :width: 30 %

.. |picEllipsoid_b| image:: ../_static/ParametricSurfaces/GenCommon/Ellipsoid_small.jpg
    :width: 30 %


**Left figure**: Ellipsoid

**Right figure**: Ellipsoid








|newpage|



Superellipsoid
------------------------------------------------------------


Superellipsoid is the name given to a family of shapes formed from the spherical product of two superquadratric curves. These shapes can be used to model a wide range of shapes including spheres, cylinders, and parallelepipeds as well as shapes in between. The parametric equations of an superellipsoid can be written as 


.. math:: x(u, v) =  \mathrm{sgn}(\cos(u)) \cdot |\cos(u)| ^{p1} \cdot \mathrm{sgn}(\cos(v)) \cdot |\cos(v)|^{p2},

.. math:: y(u, v) =  \mathrm{sgn}(\cos(u)) \cdot |\cos(u)| ^{p1} \cdot \mathrm{sgn}(\sin(v)) \cdot |\sin(v)|^{p2},

.. math:: z(u, v) = \mathrm{sgn}(\sin(u)) \cdot |\sin(u)|^{p1},

where `\displaystyle \frac{-\pi}{2} \le u  \le \frac{\pi}{2}`, `-\pi \le v  \le \pi`, and `0 < p1, p2 < \infty`.



.. code-block:: text

    double p1 = 2.0;
    double p2 = 3.8; 

    double u = u;
    double v = v;

    \cos(u) = Math.Cos(u);
    \cos(v) = Math.Cos(v);
    \sin(u) = Math.Sin(u);
    \sin(v) = Math.Sin(v);

    tmp  = Math.Sign(\cos(u)) * Math.Pow(Math.Abs(\cos(u)),p1);
    x = tmp * Math.Sign(\cos(v)) * Math.Pow(Math.Abs(\cos(v)),p2);
    y = -Math.Sign(\sin(u)) * Math.Pow(Math.Abs(\sin(u)),p1);
    z = tmp * Math.Sign(\sin(v)) * Math.Pow(Math.Abs(\sin(v)),p2);


See also: http://paulbourke.net/geometry/spherical/
See also: https://en.wikipedia.org/wiki/Superellipsoid
See also: https://mathcurve.com/surfaces.gb/lame/lame.shtml
See also: https://mathworld.wolfram.com/Ellipsoid.html        
See also: https://mathworld.wolfram.com/Superellipsoid.html      

See also  :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`.



|TestSuperEllipse_a| `\quad` |TestSuperEllipse_b|

.. |TestSuperEllipse_a| image:: ../_static/ParametricSurfaces/GenCommon/TestSuperEllipse_a.3D.xml.jpg
    :width: 30 %

.. |TestSuperEllipse_b| image:: ../_static/ParametricSurfaces/GenCommon/TestSuperEllipse_a.3D.xml.jpg
    :width: 30 %



**Left figure**: Superellipsoid

**Right figure**: Superellipsoid






|newpage|


Hexaedron
-------------------------------


See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



|TestHexaedron_a| `\quad` |TestHexaedron_b|

.. |TestHexaedron_a| image:: ../_static/ParametricSurfaces/GenCommon/TestHexaedron_a.3D.xml.jpg
   :width: 30 %

.. |TestHexaedron_b| image:: ../_static/ParametricSurfaces/GenCommon/TestHexaedron_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Hexaedron (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Hexaedron (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).


.. code-block:: csharp

    double cosu = Math.Cos(u);
    double sinu = Math.Sin(u);
    double cosv = Math.Cos(v);
    double sinv = Math.Sin(v);
    x = cosv * cosv * cosv * cosu * cosu * cosu;
    y = -sinu * sinu * sinu;
    z = sinv * sinv * sinv * cosu * cosu * cosu;







|newpage|


Super Toroid
------------------------


See also: http://paulbourke.net/geometry/toroidal/


|TestSuperToroid_a| `\quad` |TestSuperToroid_b|

.. |TestSuperToroid_a| image:: ../_static/ParametricSurfaces/GenCommon/TestSuperToroid_a.3D.xml.jpg
   :width: 30 %

.. |TestSuperToroid_b| image:: ../_static/ParametricSurfaces/GenCommon/TestSuperToroid_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Super Toroid (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Super Toroid (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).


.. code-block:: csharp

    double r0 = 1;
    double r1 = 0.3;
                
    double tmp;
    double ct1,ct2,st1,st2;
                
    double p1 = 2.0;
    double p2 = 3.8; 
    double t1 = u;
    double t2 = v;
                
    ct1 = Math.Cos(t1);
    ct2 = Math.Cos(t2);
    st1 = Math.Sin(t1);
    st2 = Math.Sin(t2);
                
    tmp  = r0 + r1 * Math.Sign(ct2) * Math.Pow(Math.Abs(ct2),p2);

    x = tmp * Math.Sign(ct1) * Math.Pow(Math.Abs(ct1),p1);
    y = -tmp * Math.Sign(st1) * Math.Pow(Math.Abs(st1),p1);
    z = r1 * Math.Sign(st2) * Math.Pow(Math.Abs(st2),p2);






|newpage|


Elliptic Helicoid
-----------------------------


See also: https://mathworld.wolfram.com/EllipticHelicoid.html


See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



|TestEllipticHelicoid_a| `\quad` |TestEllipticHelicoid_b|

.. |TestEllipticHelicoid_a| image:: ../_static/ParametricSurfaces/GenCommon/TestEllipticHelicoid_a.3D.xml.jpg
   :width: 30 %

.. |TestEllipticHelicoid_b| image:: ../_static/ParametricSurfaces/GenCommon/TestEllipticHelicoid_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Elliptic Helicoid (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Elliptic Helicoid (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



.. code-block:: csharp

    double a = 0.5;
    double b = 1.5;
    double c = 1;
    double su = Math.Sin(u);
    double cu = Math.Cos(u);
                
    x = a * v * cu;
    z = b * v * su;
    y = c * u;





|newpage|


Hyperbolic Helicoid
-----------------------------


See also: https://mathworld.wolfram.com/HyperbolicHelicoid.html

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



|TestHyperhelicoid_a| `\quad` |TestHyperhelicoid_b|

.. |TestHyperhelicoid_a| image:: ../_static/ParametricSurfaces/GenCommon/TestHyperhelicoid_a.3D.xml.jpg
   :width: 30 %

.. |TestHyperhelicoid_b| image:: ../_static/ParametricSurfaces/GenCommon/TestHyperhelicoid_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Hyperbolic Helicoid (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Hyperbolic Helicoid (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



.. code-block:: csharp

    x = (Math.Sinh(v) * Math.Cos(3 * u)) / (1 + Math.Cosh(u) * Math.Cosh(v));
    y = (Math.Cosh(v) * Math.Sinh(u)) / (1 + Math.Cosh(u) * Math.Cosh(v));
    z = (Math.Sinh(v) * Math.Sin(3 * u)) / (1 + Math.Cosh(u) * Math.Cosh(v));







Lemniscape
---------------------------------


See also: http://paulbourke.net/geometry/lemniscape/



.. code-block:: csharp

    var x = Math.Cos(v) * Math.Sqrt(Math.Abs(Math.Sin(2 * u))) * Math.Cos(u);
    var y = Math.Cos(v) * Math.Sqrt(Math.Abs(Math.Sin(2 * u))) * Math.Sin(u);
    var z = x * x - y * y + 2 * x * y * Math.Tan(v) * Math.Tan(v);




|TestLemnescate_a| `\quad` |TestLemnescate_b|

.. |TestLemnescate_a| image:: ../_static/ParametricSurfaces/Removal/TestLemnescate_a.3D.xml.jpg
   :width: 30 %

.. |TestLemnescate_b| image:: ../_static/ParametricSurfaces/Removal/TestLemnescate_a.3D.xml.jpg
   :width: 30 %


**Left figure**: Lemniscape (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Lemniscape (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|


Bohemian Dome
-------------------------------------------

See also: https://mathworld.wolfram.com/BohemianDome.html

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.


.. code-block:: csharp

    var a = 0.5;
    var b = 1.5;
    var c = 1;
    var su = Math.Sin(u);
    var sv = Math.Sin(v);
    var cu = Math.Cos(u);
    var cv = Math.Cos(v);

    var x = a * cu;
    var z = b * cv + a * su;
    var y = c * sv;





|TestBohemianDome_a| `\quad` |TestBohemianDome_b|

.. |TestBohemianDome_a| image:: ../_static/ParametricSurfaces/Removal/TestBohemianDome_a.3D.xml.jpg
   :width: 30 %

.. |TestBohemianDome_b| image:: ../_static/ParametricSurfaces/Removal/TestBohemianDome_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Bohemian Dome (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Bohemian Dome (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).














|newpage|


Dupin1 surface
-----------------------


See also: https://mathcurve.com/surfaces.gb/cycliddedupin/cyclidededupin.shtml

See also: https://en.wikipedia.org/wiki/Dupin_cyclide#Elliptic_cyclides


See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.


|picTestDupin1| `\quad` |picTestDupin2|

.. |picTestDupin1| image:: ../_static/ParametricSurfaces/GenCommon/TestDupin1.3D.xm.jpg
   :width: 30 %

.. |picTestDupin2| image:: ../_static/ParametricSurfaces/GenCommon/TestDupin1.3D.xml.jpg
   :width: 30 %



**Left figure**: Dupin1 Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Dupin1 Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



.. code-block:: csharp

    double a = 1.5;
    double b = 1.4;
    double c = Math.Sqrt(a*a-b*b);
    double d = b/2;
    double su = Math.Sin(u);
    double sv = Math.Sin(v);
    double cu = Math.Cos(u);
    double cv = Math.Cos(v);
    double den = a - c * cu * cv;
                
    x = (d * (c - a * cu * cv) + b*b * cu )   / den;
    y = -(b * su * (a - d * cv)) / den;
    z = (b * sv * (c * cu - d)) / den;






|newpage|


Dupin2 surface
-------------------------


See also: https://mathcurve.com/surfaces.gb/cycliddedupin/cyclidededupin.shtml

See also: https://en.wikipedia.org/wiki/Dupin_cyclide#Parabolic_cyclides

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.


|TestDupin2_a| `\quad` |TestDupin2_b|

.. |TestDupin2_a| image:: ../_static/ParametricSurfaces/GenCommon/TestDupin2_a.3D.xml.jpg
   :width: 30 %

.. |TestDupin2_b| image:: ../_static/ParametricSurfaces/GenCommon/TestDupin2_a.3D.xml.jpg
   :width: 30 %



**Left figure**: Dupin2 Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Dupin2 Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



.. code-block:: csharp

    double p = 2;
    double k = 0.7;
    double den = 1 + u*u + v*v;
    x = 0.5*p * (2*v*v + k*(1-u*u-v*v)) / den;
    z = p*u * (v*v+k) / den;
    y = p*v * (1+u*u-k) / den;







|newpage|


Dinis Surface (twisted pseudosphere)
------------------------------------------


See also: https://mathworld.wolfram.com/DinisSurface.html

See also  Wikipedia :cite:p:`Wikipedia2D101`,  MathWorld :cite:p:`Wolfram3D101`.



|picTestDini1| `\quad` |picTestDini2|

.. |picTestDini1| image:: ../_static/ParametricSurfaces/GenCommon/TestDini.3D.xm.jpg
   :width: 30 %

.. |picTestDini2| image:: ../_static/ParametricSurfaces/GenCommon/TestDini.3D.xml.jpg
   :width: 30 %


**Left figure**: Dinis Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Dinis Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).


.. code-block:: csharp

    double a = Math.Cos(u);
    double b = Math.Sin(u);
    double c = Math.Cos(v);
    double a2 = a * a;
    double a4 = a2 * a2;

    x = -(2.0 / 15.0) * a * (3 * c + b * (-30 + a4 * (90 - 60 * a2) + 5 * a * c));
    z = -(1.0 / 15.0) * b * b * (c * b * (3 - 48 * a4 + 5 * a * b * (1 - 16 * a4)) - 60);
    y = (2.0 / 15.0) * (3 + 5 * a * b) * Math.Sin(v);




**Left figure**: Dinis Surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Dinis Surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|newpage|



Plueckers conoid
-----------------------------


// See : https://mathworld.wolfram.com/PlueckersConoid.html
// See : Gray, p. 436
// See : https://en.wikipedia.org/wiki/Pl%C3%BCcker%27s_conoid


.. code-block:: csharp

    x = u * Math.Sqrt(1 - v*v);
    y = u*v;
    z = 1 - v*v;



|TestPluecker_a| `\quad` |TestPluecker_b| `\quad` |TestPluecker_c|

.. |TestPluecker_a| image:: ../_static/ParametricSurfaces/GenCommon/10a_TestPluecker.3D.xml.jpg
   :width: 30 %

.. |TestPluecker_b| image:: ../_static/ParametricSurfaces/GenCommon/10b_TestPluecker.3D.xml.jpg
   :width: 30 %

.. |TestPluecker_c| image:: ../_static/ParametricSurfaces/GenCommon/10c_TestPluecker.3D.xml.jpg
   :width: 30 %



**Left figure**: Plueckers Conoid (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Plueckers Conoid (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Plueckers Conoid (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



References

Gray, A. "Plücker's Conoid." Modern Differential Geometry of Curves and Surfaces with Mathematica, 2nd ed. Boca Raton, FL: CRC Press, pp. 435-437, 1997.











|newpage|


Umbilic Torus
----------------------------


// See also: http://www.3d-meier.de/tut3/Seite61.html  // Umbilic Torus



|TestUmbilicTorus|

.. |TestUmbilicTorus| image:: ../_static/ParametricSurfaces/GenCommon/11a_TestUmbilicTorus.3D.xml.jpg
   :width: 30 %


**Left figure**: Umbilic Torus (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|newpage|


Skidian's ruled surface
-----------------------------------


// See also: http://www.3d-meier.de/tut3/Seite227.html  // Skidan Ruled Surface
// See Krivoshapko, p. 499



|TestSkidan_a| `\quad` |TestSkidan_b| `\quad` |TestSkidan_c|

.. |TestSkidan_a| image:: ../_static/ParametricSurfaces/GenCommon/12a_TestSkidan.3D.xml.jpg
   :width: 30 %

.. |TestSkidan_b| image:: ../_static/ParametricSurfaces/GenCommon/12b_TestSkidan.3D.xml.jpg
   :width: 30 %

.. |TestSkidan_c| image:: ../_static/ParametricSurfaces/GenCommon/12c_TestSkidan.3D.xml.jpg
   :width: 30 %



**Left figure**: Skidian's ruled surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Skidian's ruled surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Skidian's ruled surface (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|


Umbrella surface
------------------------------------


// See also: http://www.3d-meier.de/tut3/Seite215.html  // Umbrella Surface
// See Krivoshapko, p. 507 - 509 
// See Krivoshapko, p. 513 - 515 
// See Krivoshapko, p. 521, 526, 530, 531, 533


|TestUmbrella|

.. |TestUmbrella| image:: ../_static/ParametricSurfaces/GenCommon/13a_TestUmbrella.3D.xml.jpg
   :width: 30 %


**Left figure**: Umbrella surface (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).







|newpage|


Cyclic surfaces (generalized torus)
---------------------------------------------


// See Krivoshapko, p. 376


|CyclicSurface_a| `\quad` |CyclicSurface_b| `\quad` |CyclicSurface_c|

.. |CyclicSurface_a| image:: ../_static/ParametricSurfaces/GenCommon/14a_CyclicSurface1.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_b| image:: ../_static/ParametricSurfaces/GenCommon/14b_CyclicSurface2.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_c| image:: ../_static/ParametricSurfaces/GenCommon/14c_CyclicSurface1.3D.xml.jpg
   :width: 30 %



**Left figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).




|CyclicSurface_d| `\quad` |CyclicSurface_e| `\quad` |CyclicSurface_f|

.. |CyclicSurface_d| image:: ../_static/ParametricSurfaces/GenCommon/14d_CyclicSurface2.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_e| image:: ../_static/ParametricSurfaces/GenCommon/14e_CyclicSurface2.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_f| image:: ../_static/ParametricSurfaces/GenCommon/14f_CyclicSurface2.3D.xml.jpg
   :width: 30 %



**Left figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).




|CyclicSurface_g| `\quad` |CyclicSurface_h| `\quad` |CyclicSurface_i|

.. |CyclicSurface_g| image:: ../_static/ParametricSurfaces/GenCommon/14g_CyclicSurface2.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_h| image:: ../_static/ParametricSurfaces/GenCommon/14h_CyclicSurface2.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_i| image:: ../_static/ParametricSurfaces/GenCommon/14i_CyclicSurface2.3D.xml.jpg
   :width: 30 %



**Left figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|CyclicSurface_j| `\quad` |CyclicSurface_k| `\quad` |CyclicSurface_l|

.. |CyclicSurface_j| image:: ../_static/ParametricSurfaces/GenCommon/14j_CyclicSurface2.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_k| image:: ../_static/ParametricSurfaces/GenCommon/14k_CyclicSurface2.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_l| image:: ../_static/ParametricSurfaces/GenCommon/14l_CyclicSurface3.3D.xml.jpg
   :width: 30 %



**Left figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).




|CyclicSurface_m| `\quad` |CyclicSurface_n|

.. |CyclicSurface_m| image:: ../_static/ParametricSurfaces/GenCommon/14m_CyclicSurface3.3D.xml.jpg
   :width: 30 %

.. |CyclicSurface_n| image:: ../_static/ParametricSurfaces/GenCommon/14n_CyclicSurface3.3D.xml.jpg
   :width: 30 %



**Left figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Cyclic surfaces (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).









|newpage|


Goursat surfaces 
-------------------------------------

// See : Krivoshapko (2015), p. 643
// See: https://mathworld.wolfram.com/GoursatsSurface.html
// See Gray 1997, p. 314)
// See: https://mathcurve.com/surfaces.gb/goursat/goursat.shtml




|TestGoursat_a| `\quad` |TestGoursat_b| `\quad` |TestGoursat_c|

.. |TestGoursat_a| image:: ../_static/ParametricSurfaces/GenCommon/15a_TestGoursat1.3D.xml.jpg
   :width: 30 %

.. |TestGoursat_b| image:: ../_static/ParametricSurfaces/GenCommon/15b_TestGoursat1.3D.xml.jpg
   :width: 30 %

.. |TestGoursat_c| image:: ../_static/ParametricSurfaces/GenCommon/15c_TestGoursat2.3D.xml.jpg
   :width: 30 %



**Left figure**: Goursat surfaces  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Goursat surfaces  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Goursat surfaces  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).



|TestGoursat_d| `\quad` |TestGoursat_e| `\quad` |TestGoursat_f|

.. |TestGoursat_d| image:: ../_static/ParametricSurfaces/GenCommon/15d_TestGoursat2.3D.xml.jpg
   :width: 30 %

.. |TestGoursat_e| image:: ../_static/ParametricSurfaces/GenCommon/15f_TestGoursat4.3D.xml.jpg
   :width: 30 %

.. |TestGoursat_f| image:: ../_static/ParametricSurfaces/GenCommon/15g_TestGoursat5.3D.xml.jpg
   :width: 30 %



**Left figure**: Goursat surfaces  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Goursat surfaces  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Goursat surfaces  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).






|newpage|


Cyclides triples
--------------------------------


// See : Krivoshapko (2015), p. 651



|CyclidesTriple_a| `\quad` |CyclidesTriple_b| `\quad` |CyclidesTriple_c|

.. |CyclidesTriple_a| image:: ../_static/ParametricSurfaces/GenCommon/16a_TestCyclidesTriple.3D.xml.jpg
   :width: 30 %

.. |CyclidesTriple_b| image:: ../_static/ParametricSurfaces/GenCommon/16b_TestCyclidesTriple.3D.xml.jpg
   :width: 30 %

.. |CyclidesTriple_c| image:: ../_static/ParametricSurfaces/GenCommon/16c_TestCyclidesTriple.3D.xml.jpg
   :width: 30 %



**Left figure**: Cyclides triples  (see also  Wikipedia :cite:p:`Wikipedia2D010`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Middle figure**: Cyclides triples  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).

**Right figure**: Cyclides triples  (see also  Wikipedia :cite:p:`Wikipedia2D011`, :cite:t:`Gray2006`,  :cite:t:`Krivoshapko2015`).





|newpage|


Ship Lamé
------------------------------


// See : Krivoshapko (2015), p. 671



|TestShipLame_a| `\quad` |TestShipLame_b|

.. |TestShipLame_a| image:: ../_static/ParametricSurfaces/GenCommon/17a_TestShipLame.3D.xml.jpg
   :width: 30 %

.. |TestShipLame_b| image:: ../_static/ParametricSurfaces/GenCommon/17b_TestShipLame.3D.xml.jpg
   :width: 30 %

