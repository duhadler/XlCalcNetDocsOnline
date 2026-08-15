

.. |newpage| raw:: latex

   \newpage



.. |cr| raw:: latex

   \hspace{0.0mm}








|newpage|


Platonic solids, and related solids
==============================================================

A Platonic solid is a convex, regular polyhedron in three-dimensional Euclidean space. Being a regular polyhedron means that the faces are congruent (identical in shape and size) regular polygons (all angles congruent and all edges congruent), and the same number of faces meet at each vertex.

See also: https://en.wikipedia.org/wiki/Platonic_solid

See also: https://mathworld.wolfram.com/PlatonicSolid.html

Augmentation is the operation of replacing the faces of a polyhedron with pyramids of height `h` (where `h` may be positive, zero, or negative) having the face as the base. Augmentation with `h=0` gives a triangulated version of the original solid. 

See also: https://mathworld.wolfram.com/Augmentation.html




Tetrahedron
------------------------------------------------------------------------------

A regular tetrahedron is a tetrahedron in which all four faces are equilateral triangles. In other words, all of its faces are the same size and shape (congruent) and all edges are the same length.

See also: https://en.wikipedia.org/wiki/Tetrahedron#Regular_tetrahedron

See also: https://mathworld.wolfram.com/RegularTetrahedron.html

See also: https://mathcurve.com/polyedres/tetraedre/tetraedre.shtml



An example in C\#

.. code-block:: csharp

    var proc = BuiltIn.SetTetrahedron();



|cr|


|01a_Scatter_Tetrahedron| 

.. |01a_Scatter_Tetrahedron| image:: ../_static/BuiltIn/PlatonicSolids/01a_Scatter_Tetrahedron.3D.xml.jpg
    :width: 30 %




**Left figure**: Tetrahedron






|newpage|

Cube
---------------------------------------


A cube is a three-dimensional solid object bounded by six square faces. It has twelve edges and eight vertices. It can be represented as a rectangular cuboid with six square faces, or a parallelepiped with equal edges.


See also: https://en.wikipedia.org/wiki/Cube

See also: https://mathworld.wolfram.com/Cube.html

See also: https://mathcurve.com/polyedres/cube/cube.shtml


An example in C\#

.. code-block:: csharp

    var proc = BuiltIn.SetCube();



|cr|


|02a_Scatter_Cube| 

.. |02a_Scatter_Cube| image:: ../_static/BuiltIn/PlatonicSolids/02a_Scatter_Cube.3D.xml.jpg
    :width: 30 %



**Left figure**: Cube







|newpage|

Octahedron
---------------------------------


A regular octahedron is an octahedron that is a regular polyhedron. All the faces of a regular octahedron are equilateral triangles of the same size, and exactly four triangles meet at each vertex. A regular octahedron is convex, meaning that for any two points within it, the line segment connecting them lies entirely within it. 


See also: https://en.wikipedia.org/wiki/Octahedron#Regular_octahedron

See also: https://mathworld.wolfram.com/RegularOctahedron.html

See also: https://mathcurve.com/polyedres/octaedre/octaedre.shtml



An example in C\#

.. code-block:: csharp

    var proc = BuiltIn.SetOctahedron();





|cr|


|03a_Scatter_Octahedron| 

.. |03a_Scatter_Octahedron| image:: ../_static/BuiltIn/PlatonicSolids/03a_Scatter_Octahedron.3D.xml.jpg
    :width: 30 %



**Left figure**: Octahedron





|newpage|

Dodecahedron
----------------------------------


A regular dodecahedron or pentagonal dodecahedron is a dodecahedron composed of regular pentagonal faces, three meeting at each vertex.

See also: https://en.wikipedia.org/wiki/Regular_dodecahedron

See also: https://mathworld.wolfram.com/RegularDodecahedron.html

See also: https://mathcurve.com/polyedres/dodecaedre/dodecaedre.shtml



An example in C\#

.. code-block:: csharp

    var proc = BuiltIn.SetDodecahedron();





|cr|


|04a_Scatter_Dodecahedron| 

.. |04a_Scatter_Dodecahedron| image:: ../_static/BuiltIn/PlatonicSolids/04a_Scatter_Dodecahedron.3D.xml.jpg
    :width: 30 %


**Left figure**: Dodecahedron







|newpage|

Icosahedron 
-----------------------------------


A regular icosahedron (or simply icosahedron) is a convex polyhedron that can be constructed from pentagonal antiprism by attaching two pentagonal pyramids with regular faces to each of its pentagonal faces, or by putting points onto the cube.

See also: https://en.wikipedia.org/wiki/Regular_icosahedron

See also: https://mathworld.wolfram.com/RegularIcosahedron.html

See also: https://mathcurve.com/polyedres/icosaedre/icosaedre.shtml



An example in C\#

.. code-block:: csharp

    var proc = BuiltIn.SetIcosahedron();



|cr|

|05a_Scatter_Icosahedron| 

.. |05a_Scatter_Icosahedron| image:: ../_static/BuiltIn/PlatonicSolids/05a_Scatter_Icosahedron.3D.xml.jpg
    :width: 30 %



**Left figure**: Icosahedron






|newpage|

Geodesic sphere
-----------------------------------------


A spherical polyhedron or spherical tiling is a tiling of the sphere in which the surface is divided or partitioned by great arcs into bounded regions called spherical polygons

See also: https://en.wikipedia.org/wiki/Geodesic_polyhedron

See also: https://en.wikipedia.org/wiki/Spherical_polyhedron



An example in C\#

.. code-block:: csharp

    var radius = 1.0;
    var numDiv = 1;
    var proc = BuiltIn.SetGeodesicSphere(radius, numDiv);


|cr|


|06a_Scatter_Geodesic_Sphere1| `\quad` |06b_Scatter_Geodesic_Sphere2| `\quad` |06c_Scatter_Geodesic_Sphere3|

.. |06a_Scatter_Geodesic_Sphere1| image:: ../_static/BuiltIn/PlatonicSolids/06a_Scatter_Geodesic_Sphere1.3D.xml.jpg
    :width: 30 %

.. |06b_Scatter_Geodesic_Sphere2| image:: ../_static/BuiltIn/PlatonicSolids/06b_Scatter_Geodesic_Sphere2.3D.xml.jpg
    :width: 30 %

.. |06c_Scatter_Geodesic_Sphere3| image:: ../_static/BuiltIn/PlatonicSolids/06c_Scatter_Geodesic_Sphere3.3D.xml.jpg
    :width: 30 %


|06d_Scatter_Geodesic_Sphere5| `\quad` |06e_Scatter_Geodesic_Sphere7| `\quad` |06f_Scatter_Geodesic_Sphere9|

.. |06d_Scatter_Geodesic_Sphere5| image:: ../_static/BuiltIn/PlatonicSolids/06d_Scatter_Geodesic_Sphere5.3D.xml.jpg
    :width: 30 %

.. |06e_Scatter_Geodesic_Sphere7| image:: ../_static/BuiltIn/PlatonicSolids/06e_Scatter_Geodesic_Sphere7.3D.xml.jpg
    :width: 30 %

.. |06f_Scatter_Geodesic_Sphere9| image:: ../_static/BuiltIn/PlatonicSolids/06f_Scatter_Geodesic_Sphere9.3D.xml.jpg
    :width: 30 %


**Left figure**: Geodesic sphere

**Middle figure**: Geodesic sphere

**Right figure**: Geodesic sphere





|newpage|




Augmented Octahedron
--------------------------------------------

Returns the augmented Octahedron.


An example in C\#

.. code-block:: csharp

    var starRadius = 3.0;
    var proc = BuiltIn.SetAugmentedOctahedron(starRadius );


|cr|


|07a_Scatter_Stell_Octahedron_a| `\quad` |07c_Scatter_Stell_Octahedron_c| `\quad` |07d_Scatter_Stell_Octahedron_d|

.. |07a_Scatter_Stell_Octahedron_a| image:: ../_static/BuiltIn/PlatonicSolids/07a_Scatter_Stell_Octahedron_a.3D.xml.jpg
    :width: 30 %

.. |07c_Scatter_Stell_Octahedron_c| image:: ../_static/BuiltIn/PlatonicSolids/07c_Scatter_Stell_Octahedron_c.3D.xml.jpg
    :width: 30 %

.. |07d_Scatter_Stell_Octahedron_d| image:: ../_static/BuiltIn/PlatonicSolids/07d_Scatter_Stell_Octahedron_d.3D.xml.jpg
    :width: 30 %



**Left figure**: Augmented Octahedron

**Middle figure**: Augmented Octahedron

**Right figure**: Augmented Octahedron







|newpage|



Augmented Dodecahedron
-------------------------------------------

Returns the augmented Dodecahedron.


An example in C\#

.. code-block:: csharp

    var starRadius = 6.0;
    var proc = BuiltIn.SetAugmentedDodecahedron(starRadius );


|cr|


|08a_Scatter_Stell_Dodecahedron_a| `\quad` |08c_Scatter_Stell_Dodecahedron_c| `\quad` |08d_Scatter_Stell_Dodecahedron_d|

.. |08a_Scatter_Stell_Dodecahedron_a| image:: ../_static/BuiltIn/PlatonicSolids/08a_Scatter_Stell_Dodecahedron_a.3D.xml.jpg
    :width: 30 %

.. |08c_Scatter_Stell_Dodecahedron_c| image:: ../_static/BuiltIn/PlatonicSolids/08c_Scatter_Stell_Dodecahedron_c.3D.xml.jpg
    :width: 30 %

.. |08d_Scatter_Stell_Dodecahedron_d| image:: ../_static/BuiltIn/PlatonicSolids/08d_Scatter_Stell_Dodecahedron_d.3D.xml.jpg
    :width: 30 %



**Left figure**: Augmented Dodecahedron

**Middle figure**: Augmented Dodecahedron

**Right figure**: Augmented Dodecahedron









|newpage|


Augmented Icosahedron
-------------------------------------------


Returns the augmented Dodecahedron.


An example in C\#

.. code-block:: csharp

    var starRadius = 2.0;
    var proc = BuiltIn.SetAugmentedIcosahedron(starRadius );



|cr|


|09a_Scatter_Stell_Icosahedron_a| `\quad` |09c_Scatter_Stell_Icosahedron_c| `\quad` |09d_Scatter_Stell_Icosahedron_d|

.. |09a_Scatter_Stell_Icosahedron_a| image:: ../_static/BuiltIn/PlatonicSolids/09a_Scatter_Stell_Icosahedron_a.3D.xml.jpg
    :width: 30 %

.. |09c_Scatter_Stell_Icosahedron_c| image:: ../_static/BuiltIn/PlatonicSolids/09c_Scatter_Stell_Icosahedron_c.3D.xml.jpg
    :width: 30 %

.. |09d_Scatter_Stell_Icosahedron_d| image:: ../_static/BuiltIn/PlatonicSolids/09d_Scatter_Stell_Icosahedron_d.3D.xml.jpg
    :width: 30 %



**Left figure**: Augmented Icosahedron

**Middle figure**: Augmented Icosahedron

**Right figure**: Augmented Icosahedron







|newpage|


Augmented Geodesic Sphere
-----------------------------------------


Returns augmented versions of the Geodesic.

See also: https://mathworld.wolfram.com/IcosahedronStellations.html


An example in C\#

.. code-block:: csharp

    var starRadius = 2.0;
    var numDiv = 2;
    var proc = BuiltIn.SetAugmentedGeodesic(starRadius, numDiv);



|cr|


|10b_Scatter_Stellate_geodesic_b| `\quad` |10c_Scatter_Stellate_geodesic_c| `\quad` |10d_Scatter_Stellate_geodesic_d|

.. |10b_Scatter_Stellate_geodesic_b| image:: ../_static/BuiltIn/PlatonicSolids/10b_Scatter_Stellate_geodesic_b.3D.xml.jpg
    :width: 30 %

.. |10c_Scatter_Stellate_geodesic_c| image:: ../_static/BuiltIn/PlatonicSolids/10c_Scatter_Stellate_geodesic_c.3D.xml.jpg
    :width: 30 %

.. |10d_Scatter_Stellate_geodesic_d| image:: ../_static/BuiltIn/PlatonicSolids/10d_Scatter_Stellate_geodesic_d.3D.xml.jpg
    :width: 30 %



**Left figure**: Augmented Geodesic Sphere

**Middle figure**: Augmented Geodesic Sphere

**Right figure**: Augmented Geodesic Sphere






|newpage|

Stella Octangula
----------------------------------------


The stella octangula is a polyhedron compound composed of a tetrahedron and its dual (a second tetrahedron rotated 180 degrees with respect to the first). The stella octangula is also (incorrectly) called the augmented tetrahedron, and is the only stellation of the octahedron.

It can be constructed from a regular octahedron by augmentation with `h = \sqrt{6}/3`.

See also: https://mathworld.wolfram.com/StellaOctangula.html

See also: https://en.wikipedia.org/wiki/Stellated_octahedron


An example in C\#

.. code-block:: csharp

    var starRadius = 2.0;
    var proc = BuiltIn.SetAugmentedOctahedron(starRadius );



|cr|



|Stella_Octangula|

.. |Stella_Octangula| image:: ../_static/BuiltIn/PlatonicSolids/11a_StellaOctangula.3D.3D.xml.jpg
    :width: 30 %



**Left figure**: Stella Octangula






|newpage|

Small stellated Dodecahedron
---------------------------------------


The small stellated dodecahedron is the Kepler-Poinsot polyhedra whose dual polyhedron is the great dodecahedron.

It can be constructed from a regular dodecahedron by augmentation with `h = \sqrt{(5 + 2\sqrt{5})/5 }`.


See also: https://mathworld.wolfram.com/SmallStellatedDodecahedron.html

See also: https://mathworld.wolfram.com/Augmentation.html

See also: https://en.wikipedia.org/wiki/Small_stellated_dodecahedron

See also: https://mathworld.wolfram.com/Kepler-PoinsotPolyhedron.html



An example in C\#

.. code-block:: csharp

    var starRadius = 6.0;
    var proc = BuiltIn.SetAugmentedDodecahedron(starRadius );



|cr|


|Small_stellated_Dodecahedron|

.. |Small_stellated_Dodecahedron| image:: ../_static/BuiltIn/PlatonicSolids/12a_SmallStellatedDodecahedron.3D.xml.jpg
    :width: 30 %



**Left figure**: Small stellated Dodecahedron





|newpage|

Great Dodecahedron
------------------------------------------

The great dodecahedron is the Kepler-Poinsot polyhedron whose dual is the small augmented dodecahedron. 

It can be constructed from a regular icosahedron by augmentation with `h = (\sqrt{3} (\sqrt{5}-3))/6`.



See also: https://mathworld.wolfram.com/GreatDodecahedron.html

See also: https://mathworld.wolfram.com/Augmentation.html

See also: https://en.wikipedia.org/wiki/Great_dodecahedron

See also: https://mathworld.wolfram.com/Kepler-PoinsotPolyhedron.html


An example in C\#

.. code-block:: csharp

    var starRadius = 0.25;
    var proc = BuiltIn.SetAugmentedIcosahedron(starRadius );



|cr|


|13a_GreatDodecahedron|

.. |13a_GreatDodecahedron| image:: ../_static/BuiltIn/PlatonicSolids/13a_GreatDodecahedron.3D.xml.jpg
    :width: 30 %



**Left figure**: Great Dodecahedron










|newpage|

Great stellated Dodecahedron
--------------------------------------------

The great augmented dodecahedron is one of the Kepler-Poinsot polyhedra. 

It can be constructed from a regular icosahedron by augmentation with `h = (\sqrt{3} (3+\sqrt{5}))/6`.


See also: https://mathworld.wolfram.com/GreatStellatedDodecahedron.html

See also: https://mathworld.wolfram.com/Augmentation.html

See also: https://en.wikipedia.org/wiki/Great_stellated_dodecahedron

See also: https://mathworld.wolfram.com/Kepler-PoinsotPolyhedron.html




An example in C\#

.. code-block:: csharp

    var starRadius = 2.0;
    var proc = BuiltIn.SetAugmentedIcosahedron(starRadius );




|cr|


|14a_GreatStellatedDodecahedron_a|

.. |14a_GreatStellatedDodecahedron_a| image:: ../_static/BuiltIn/PlatonicSolids/14a_GreatStellatedDodecahedron_a.3D.xml.jpg
    :width: 30 %



**Left figure**: Great stellated Dodecahedron







