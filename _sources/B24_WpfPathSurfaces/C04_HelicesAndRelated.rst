

.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|

Helices and related curves traced on cylinders, cones and spheres
=======================================================================



See also: https://en.wikipedia.org/wiki/Helix

See also: https://mathworld.wolfram.com/Helix.html

See also: https://mathcurve.com/courbes3d.gb/helice/helice.shtml

The helices are the curves the tangents of which form a constant angle a with respect to a fixed plane (P0), or a fixed direction d (orthogonal to (P0)).
Therefore, the notion of helix in mathematics is more connected to a mountain road with constant slope than to the helix of a boat!

Examples (note that the helices are described by their base or the surface on which they are traced):
    - the straight line (lines on a surface are therefore helices of this surface)
    - the cylindrical helix (base = circle)
    - the conical helix (traced on a vertical cone of revolution, base = logarithmic spiral)
    - the elliptic helix (base = ellipse)
    - the spherical helix (traced on a sphere, base = epicycloid)
    - the helix of the paraboloid (base = involute of a circle).
    - the helix of the one-sheeted hyperboloid (traced on the one-sheeted hyperboloid)
    - the striction line of the milk carton


NOTE: the item "H. Stop of y, v [STOP2]" determines the diameter of the helix.


|newpage|


Cylindrical helix
-------------------------------------------

See also: https://mathcurve.com/courbes3d.gb/helicecirculaire/helicecirculaire.shtml

The cylindrical helix can be defined as a helix traced on a vertical cylinder of revolution, or a rhumb line of this cylinder (i.e., in both cases, a curve forming a constant angle with respect to the axis of the cylinder), or a geodesic of this cylinder (in other words, a curve that becomes a line when the cylinder is developed) or a solenoid with linear bore.
Intrinsic characterization: constant curvature and torsion.

The radius of the helix is a, and its shift is  (it is the distance between two consecutive coils) and b is sometimes called reduced shift of the helix. The angle of the helix is the constant angle (equal to ) formed by its tangent with respect to any plane orthogonal to Oz. The helix is right-handed when e = 1 (it “goes up” counterclockwise and an observer located outside of it sees it going up from left to right) and left-handed when e = - 1 (it “goes up” clockwise).




An example in C\#

.. code-block:: csharp

    double a = 0.2;
    // double b = 1.0;
    double b = 0.2;
    var x = a * Math.Cos(t);
    var y = a * Math.Sin(t);
    var z = b * t;


Some text


|Path_SpiralCylindrical_a| `\quad` |PathD_SpiralCylindrical_a|

.. |Path_SpiralCylindrical_a| image:: ../_static/PathSurfaces/Helices/Path_SpiralCylindrical_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SpiralCylindrical_a| image:: ../_static/PathSurfaces/Helices/PathD_SpiralCylindrical_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Cylindrical helix. Perspective camera. 

**Right figure**: Cylindrical helix. Perspective camera. 






|newpage|


Conical helix based on Archimedes spiral (spiral of Pappus)
-------------------------------------------------------------------

See also: https://en.wikipedia.org/wiki/Conical_spiral

See also: https://mathworld.wolfram.com/ConicalSpiral.html

See also: https://mathcurve.com/courbes3d.gb/helicecirculaire/helicecirculaire.shtml

The conical helix can be defined as a helix traced on a cone of revolution (i.e. a curve forming a constant angle with respect to the axis of the cone), or a rhumb line of this cone (i.e. a curve forming a constant angle with the meridians); it is not a geodesic of the cone.
In concrete terms, we get a conical helix when we trace a path with constant slope on a cone placed vertically.

The projection on xOy is a logarithmic spiral (), which is also the locus of the intersection between the tangents and xOy; the curve obtained by developing the cone is also a logarithmic spiral.
As for all helices, it is a geodesic of the vertical cylinder based on the aforementioned spiral, projection of the curve on xOy.
The principal normal is always perpendicular to Oy.
The radii of curvature and torsion are proportional to z.
The helix is right-handed when  (it “goes up” clockwise) and left-handed when  (it “goes up” counterclockwise). 



An example in C\#

.. code-block:: csharp

    double a = 1.0;
    double phi = t * Math.PI;
    double rphi = a * phi;
    var x = (rphi * Math.Cos(phi));
    var y = (rphi * Math.Sin(phi));
    //var z = (0.2 * t);
    var z = (1.2 * t);


Some text


|Path_SpiralAConical_a| `\quad` |PathD_SpiralAConical_a|

.. |Path_SpiralAConical_a| image:: ../_static/PathSurfaces/Helices/Path_SpiralAConical_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SpiralAConical_a| image:: ../_static/PathSurfaces/Helices/PathD_SpiralAConical_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Conical helix based on Archimedes spiral. Perspective camera. 

**Right figure**: Conical helix based on Archimedes spiral. Perspective camera. 








|newpage|


Conical helix based on Fermat's spiral 
----------------------------------------------------

See also: https://en.wikipedia.org/wiki/Conical_spiral



Conical helix based on Fermat's spiral 



An example in C\#

.. code-block:: csharp

    double a = 1.0;
    double m = 0.2 / Math.PI;
    double phi = t * Math.PI;
    double rphi = a * Math.Sqrt(phi);
    var x = (rphi * Math.Cos(phi));
    var y = (rphi * Math.Sin(phi));
    var z = (m * rphi);



Some text


|Path_SpiralFConical_a| `\quad` |PathD_SpiralFConical_a|

.. |Path_SpiralFConical_a| image:: ../_static/PathSurfaces/Helices/Path_SpiralFConical_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SpiralFConical_a| image:: ../_static/PathSurfaces/Helices/PathD_SpiralFConical_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Conical helix based on Fermat's spiral. Perspective camera. 

**Right figure**: Conical helix based on Fermat's spiral. Perspective camera. 






|newpage|


Conical helix based on the logarithmic spiral  (Concho-Spiral)
---------------------------------------------------------------------

See also: https://mathworld.wolfram.com/Concho-Spiral.html


See also: https://en.wikipedia.org/wiki/Conchospiral




An example in C\#

.. code-block:: csharp

    double k = 0.1;
    double a = 1.0;
    double m = 0.2 / Math.PI;
    double phi = t * Math.PI;
    double rphi = a * Math.Exp(k * phi);
    var x = (rphi * Math.Cos(phi));
    var y = (rphi * Math.Sin(phi));
    var z = (m * rphi);



Some text


|Path_SpiralLConical_a| `\quad` |PathD_SpiralLConical_a|

.. |Path_SpiralLConical_a| image:: ../_static/PathSurfaces/Helices/Path_SpiralLConical_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SpiralLConical_a| image:: ../_static/PathSurfaces/Helices/PathD_SpiralLConical_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Conical helix based on the logarithmic spiral. Perspective camera. 

**Right figure**: Conical helix based on the logarithmic spiral. Perspective camera. 








|newpage|


Conical helix based on the hyperbolic spiral
----------------------------------------------------------

See also: https://mathcurve.com/courbes3d.gb/spiralehyperbolique/spiralehyperbolique.shtml

The hyperbolic conical spirals are the spirals traced on a cone of revolution that can be projected on the plane perpendicular to the axis onto a hyperbolic spiral with center the vertex of the cone.



An example in C\#

.. code-block:: csharp

    double a = 1.0;
    double m = 0.2 / Math.PI;
    double phi = t * Math.PI;
    double rphi = a / Math.Sqrt(phi);
    var x = (rphi * Math.Cos(phi));
    var y = (rphi * Math.Sin(phi));
    var z = (m * rphi);




Some text


|Path_SpiralHConical_a| `\quad` |PathD_SpiralHConical_a|

.. |Path_SpiralHConical_a| image:: ../_static/PathSurfaces/Helices/Path_SpiralHConical_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SpiralHConical_a| image:: ../_static/PathSurfaces/Helices/PathD_SpiralHConical_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Conical helix based on the hyperbolic spiral. Perspective camera. 

**Right figure**: Conical helix based on the hyperbolic spiral. Perspective camera. 








|newpage|

Rhumb line of the sphere
------------------------------------------------


See also: https://mathcurve.com/courbes3d.gb/loxodromie/sphereloxodromie.shtml

The rhumb lines of the sphere, associated to a given axis, are the curves that form a constant angle with the parallel (or the meridians).
Do not mistake the rhumb lines for the spherical helices, that form a constant angle with the equatorial plane, nor for the clelias.

The rhumb lines correspond to the straight lines in Mercator coordinates ; in other words, on the maps of the Earth that use the Mercator projection, the rhumb lines are represented by straight lines. The angle a that the images of the rhumb lines form on the map with respect to the horizontal is the same as the angle they form on the sphere with respect to the parallels.
If we know the geographic coordinates  and  of two points, the angle a associated to the shortest rhumb line joining these two points is obtained by the formula:  and the length is given by: .
The notion of rhumb line is opposed to that of geodesic, shortest path joining two points on the sphere, which is an arc of a great circle



An example in C\#

.. code-block:: csharp

    double R = 1.0;
    double alpha = 0.05;
    double k = Math.Tan(alpha);
    var x = R * Math.Cos(t) / Math.Cosh(k * t);
    var y = R * Math.Sin(t) / Math.Cosh(k * t);
    var z = R * Math.Tanh(k * t);



Some text


|Path_SphericalRhumbline_a| `\quad` |PathD_SphericalRhumbline_a|

.. |Path_SphericalRhumbline_a| image:: ../_static/PathSurfaces/Helices/Path_SphericalRhumbline_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SphericalRhumbline_a| image:: ../_static/PathSurfaces/Helices/PathD_SphericalRhumbline_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Rhumb line of the sphere. Perspective camera. 

**Right figure**: Rhumb line of the sphere. Perspective camera. 








|newpage|


Clelia
----------------------------------------

See also: https://mathcurve.com/courbes3d.gb/clelie/clelie.shtml

See also: https://en.wikipedia.org/wiki/Cl%C3%A9lie

The clelias are the loci of a point M on a meridian of a sphere rotating at constant speed w around the polar axis, the point M also moving at constant speed nw along this meridian.
Therefore, physically, we obtain a clelia when peeling an orange or when rewinding regularly a spherical wool ball.

When n is rational with numerator p and denominator q:

In this case, the curve is composed of 2p patterns, obtained from the base pattern by rotations of axis Oz and angles `2k \pi / n`  and `p + 2k \pi / n`  .

When p and q are odd, the curve is composed of p patterns, obtained from the base pattern by rotations of axis Oz and angles  `2k \pi / n` . 



An example in C\#

.. code-block:: csharp

    double R = 1.0;
    double n1 = 5.0 / 2.0;    // Example 1
    var x = R * Math.Cos(n1 * t) * Math.Cos(t);
    var y = R * Math.Cos(n1 * t) * Math.Sin(t);
    var z = R * Math.Sin(n1 * t);



Some text


|Path_SphericalClelia_a| `\quad` |PathD_SphericalClelia_a|

.. |Path_SphericalClelia_a| image:: ../_static/PathSurfaces/Helices/Path_SphericalClelia_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SphericalClelia_a| image:: ../_static/PathSurfaces/Helices/PathD_SphericalClelia_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Clelia. Perspective camera. 

**Right figure**: Clelia. Perspective camera. 






|newpage|


Spherical helix
------------------------------------


See also: https://mathworld.wolfram.com/SphericalSpiral.html


See also: https://mathworld.wolfram.com/SphericalHelix.html


See also: https://mathcurve.com/courbes3d.gb/helicespheric/helicespheric.shtml

A spherical cycloid is the locus of a point on a circle rolling without slipping on a fixed circle, the angle between the two circles remaining constant equal to ; here, a is the radius of the fixed circle,  that of the moving circle, and xOy the plane where lies the fixed circle.

When = 0, we get the hypocycloid, and when = , the epicycloid; apart from these two cases, the cycloid is traced on the sphere corresponding to both the base and the rolling circles, hence its name of spherical cycloid. The center W of this sphere is the point on Oz at height  and its radius is .
Therefore, the spherical cycloid is a roulette of the motion of a sphere over a sphere.



An example in C\#

.. code-block:: csharp

    double q = 5.0 / 2.0;    // Example 1
    //double q = 2.0 / 5.0;    // Example 2
    //double q = 1.0 / 5.0;    // Example 3
    double R = 1.0;
    double k = q / (q + 2);
    var x = R * (k * Math.Cos(t) * Math.Cos(k * t) + Math.Sin(t) * Math.Sin(k * t));
    var y = R * (k * Math.Sin(t) * Math.Cos(k * t) - Math.Cos(t) * Math.Sin(k * t));
    var z = R * Math.Sqrt(1 - k * k) * Math.Cos(k * t);



Some text


|Path_SphericalHelix_a| `\quad` |PathD_SphericalHelix_a|

.. |Path_SphericalHelix_a| image:: ../_static/PathSurfaces/Helices/Path_SphericalHelix_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SphericalHelix_a| image:: ../_static/PathSurfaces/Helices/PathD_SphericalHelix_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Spherical helix. Perspective camera. 

**Right figure**: Spherical helix. Perspective camera. 





|newpage|


Satellite curve
----------------------------------------------------------------------------------------------------

See also: https://mathcurve.com/courbes3d.gb/satellite/satellite.shtml

See also: https://mathcurve.com/courbes3d.gb/capareda/capareda.shtml


The satellite curves are the various trajectories of a point M on a given great circle of a sphere rotating around one of its axes, while M has a uniform motion along the circle.
These curves can also be seen as the trajectories of points on a circle in uniform rotation around an axis, this axis being itself in uniform rotation around an axis passing by the center of the circle.

The name of satellite curve comes from the fact that the trajectory, in the frame associated to the Earth, of a satellite in uniform circular rotation around the center of the Earth is such a curve: see for example this book (pages 177 to 181).

In the above parametrization, the sphere centered on O turns around Oz and the plane of the circle forms an angle  with respect to xOy; k is the ratio of the speed of rotation of M on the circle over the speed of rotation of the sphere around its axis.

Special cases of satellite curves include:
    - the clelias when the great circle meets the axis of rotation of the sphere ().
    - the spherical helices when  (in the second definition above, the circle rolls without slipping on a fixed circle); it is the case where the curve has cuspidal points. 



An example in C\#

.. code-block:: csharp

    double R = 1.0;
    //double alpha = 1 * Math.PI / 2;  // This corresponds to clelias
    double alpha = 3 * Math.PI / 4;
    double k = 3.0 / 4.0;
    //double k = -Math.Cos(alpha);  // This corresponds to spherical helices
    var x = R * (Math.Cos(alpha) * Math.Cos(t) * Math.Cos(k * t) - Math.Sin(t) * Math.Sin(k * t));
    var y = R * (Math.Cos(alpha) * Math.Sin(t) * Math.Cos(k * t) + Math.Cos(t) * Math.Sin(k * t));
    var z = R * Math.Sin(alpha) * Math.Cos(k * t);



Some text


|Path_SphericalSatellite_a| `\quad` |PathD_SphericalSatellite_a|

.. |Path_SphericalSatellite_a| image:: ../_static/PathSurfaces/Helices/Path_SphericalSatellite_a.3D.xml.jpg
   :width: 30 %

.. |PathD_SphericalSatellite_a| image:: ../_static/PathSurfaces/Helices/PathD_SphericalSatellite_a.3D.xml.jpg
   :width: 30 %




**Left figure**: Satellite curve. Perspective camera. 

**Right figure**: Satellite curve. Perspective camera. 








|newpage|


Seiffert's spiral
----------------------------------------------------------------------------------------------------

See also: https://en.wikipedia.org/wiki/Seiffert%27s_spiral

See also: https://mathworld.wolfram.com/SeiffertsSphericalSpiral.html



See also: https://en.wikipedia.org/wiki/Cylindrical_coordinate_system



The spherical curve obtained when moving along the surface of a sphere with constant speed, while maintaining a constant angular velocity with respect to a fixed diameter (Erdős 2000). This curve is given in cylindrical coordinates by the parametric equations



.. math:: r = sn(s,k),

.. math:: \theta = k s,

.. math:: z=cn(s,k),


where k is a positive constant and sn(s) and cn(s) are Jacobi elliptic functions (Whittaker and Watson 1990, pp. 527-528).

Erdős (2000) provides a derivation of the equations of this curve, as well as an analysis of its properties, including conditions for obtaining periodic orbits. 




Erdős, P. "Spiraling the Earth with C. G. J. Jacobi." Amer. J. Phys. 68, 888-895, 2000.

Seiffert. "Über eine neue geometrische Einführung in die Theorie der elliptischen Funktionen." Wissensch. Beiträge Jahresber. Städtischen Realschule zu Charlottenburg, Ostern. 1896.


Whittaker, E. T. and Watson, G. N. A Course in Modern Analysis, 4th ed. Cambridge, England: Cambridge University Press, 1990.

