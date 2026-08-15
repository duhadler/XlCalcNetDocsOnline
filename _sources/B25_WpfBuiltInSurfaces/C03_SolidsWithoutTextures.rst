

.. |newpage| raw:: latex

   \newpage




.. |cr| raw:: latex

   \hspace{0.0mm}









|newpage|



Builtin solids without support for textures
==============================================================



See also: https://mathworld.wolfram.com/topics/Prisms.html


See also: https://en.wikipedia.org/wiki/Prism_(geometry)

A prism is a polyhedron comprising an n-sided polygon base, a second base which is a translated copy (rigidly moved without rotation) of the first, and n other faces, necessarily all parallelograms, joining corresponding sides of the two bases. All cross-sections parallel to the bases are translations of the bases. Prisms are named after their bases, e.g. a prism with a pentagonal base is called a pentagonal prism.



Triangular Prism
-------------------------------------------------

A triangular prism or trigonal prism[1] is a prism with 2 triangular bases. If the edges pair with each triangle's vertex and if they are perpendicular to the base, it is a right triangular prism.

See also: https://mathworld.wolfram.com/TriangularPrism.html

See also: https://en.wikipedia.org/wiki/Triangular_prism


An example in C\#

.. code-block:: csharp

    var a = 0.50;
    var b = 0.50;
    var height = 1.0;
    var proc = BuiltIn.SetTriangularPrism(a, b, height, 0,0);




|cr|


|01a_PRISM_Triangular| `\quad` |01b_PRISM_Triangular_Tilted|

.. |01a_PRISM_Triangular| image:: ../_static/BuiltIn/WithoutTextures/01a_PRISM_Triangular.3D.xml.jpg
    :width: 30 %

.. |01b_PRISM_Triangular_Tilted| image:: ../_static/BuiltIn/WithoutTextures/01b_PRISM_Triangular_Tilted.3D.xml.jpg
    :width: 30 %



**Left figure**: Triangular Prism

**Right figure**: Triangular Prism, tilted








|newpage|

Square prism
-----------------------------------------

See also: https://mathworld.wolfram.com/Cube.html

See also: https://en.wikipedia.org/wiki/Cuboid

Cuboids have different types. A special case of a cuboid is a rectangular cuboid, with six rectangle faces and adjacent faces meeting at right angles. When all of the rectangular cuboid's edges are equal in length, it results in a cube, with six square faces and adjacent faces meeting at right angles.[1][3] Along with the rectangular cuboids, parallelepiped is a cuboid with six parallelogram. Rhombohedron is a cuboid with six rhombus faces. A square frustum is a frustum with a square base, but the rest of its faces are quadrilaterals.


An example in C\#

.. code-block:: csharp

    var a = 0.50;
    var b = 0.50;
    var height = 0.55;
    var proc = BuiltIn.SetSquarePrism(a, b, height, 0,0);



|cr|


|02a_PRISM_Square| `\quad` |02b_PRISM_Square_Tilted|

.. |02a_PRISM_Square| image:: ../_static/BuiltIn/WithoutTextures/02a_PRISM_Square.3D.xml.jpg
    :width: 30 %

.. |02b_PRISM_Square_Tilted| image:: ../_static/BuiltIn/WithoutTextures/02b_PRISM_Square_Tilted.3D.xml.jpg
    :width: 30 %



**Left figure**: Square prism

**Right figure**: Square Prism, tilted






|newpage|

Hexagonal prism
---------------------------------------

The hexagonal prism is a prism with hexagonal base. Prisms are polyhedrons; this polyhedron has 8 faces, 18 edges, and 12 vertices.

See also: https://mathworld.wolfram.com/HexagonalPrism.html

See also: https://en.wikipedia.org/wiki/Hexagonal_prism


An example in C\#

.. code-block:: csharp

    var a = 0.50;
    var b = 0.50;
    var height = 1.0;
    var proc = BuiltIn.SetHexagonalPrism(a, b, height, 0,0);



|cr|


|06a_PRISM_Hexagonal| `\quad` |06b_PRISM_Hexagonal_Tilted|

.. |06a_PRISM_Hexagonal| image:: ../_static/BuiltIn/WithoutTextures/06a_PRISM_Hexagonal.3D.xml.jpg
    :width: 30 %

.. |06b_PRISM_Hexagonal_Tilted| image:: ../_static/BuiltIn/WithoutTextures/06b_PRISM_Hexagonal_Tilted.3D.xml.jpg
    :width: 30 %



**Left figure**: Hexagonal prism

**Right figure**: Hexagonal prism, tilted







|newpage|

Octagonal prism
----------------------------------

The octagonal prism is a prism comprising eight rectangular sides joining two regular octagon caps. 

See also: https://mathworld.wolfram.com/OctagonalPrism.html

See also: https://en.wikipedia.org/wiki/Octagonal_prism


An example in C\#

.. code-block:: csharp

    var a = 0.50;
    var b = 0.50;
    var height = 1.0;
    var proc = BuiltIn.SetOctagonalPrism(a, b, height, 0,0);



|cr|


|06c_PRISM_Octagonal| `\quad` |06d_PRISM_Octagonal_Tilted|

.. |06c_PRISM_Octagonal| image:: ../_static/BuiltIn/WithoutTextures/06c_PRISM_Octagonal.3D.xml.jpg
    :width: 30 %

.. |06d_PRISM_Octagonal_Tilted| image:: ../_static/BuiltIn/WithoutTextures/06d_PRISM_Octagonal_Tilted.3D.xml.jpg
    :width: 30 %



**Left figure**: Hexagonal prism

**Right figure**: Hexagonal prism, tilted








|newpage|

Cylinder
------------------------------------------

A cylinder  is considered a prism with a circle as its base. The cylinder obtained by rotating a line segment about a fixed line that it is parallel to is a cylinder of revolution. A cylinder of revolution is a right circular cylinder.

See also: https://en.wikipedia.org/wiki/Cylinder

See also: https://en.wikipedia.org/wiki/Right_circular_cylinder


See also: https://mathworld.wolfram.com/Cylinder.html


An example in C\#

.. code-block:: csharp

    var numSides = 7;
    var a = 0.50;
    var b = 0.50;
    var height = 1.0;
    var proc = BuiltIn.SetCylinder(numSides, a, b, height, 0,0);


|cr|


|07a_Scatter_Cylinder| `\quad` |07b_Scatter_4_Cylinders|

.. |07a_Scatter_Cylinder| image:: ../_static/BuiltIn/WithoutTextures/07a_Scatter_Cylinder.3D.xml.jpg
    :width: 30 %

.. |07b_Scatter_4_Cylinders| image:: ../_static/BuiltIn/WithoutTextures/07b_Scatter_4_Cylinders.3D.xml.jpg
    :width: 30 %



**Left figure**: Cylinder

**Right figure**: 4 Cylinders





|newpage|

Cylinder, truncated by an inclined plane
---------------------------------------------------------

A cylinder  is considered a prism with a circle as its base. The cylinder obtained by rotating a line segment about a fixed line that it is parallel to is a cylinder of revolution. A cylinder of revolution is a right circular cylinder.

See also: https://en.wikipedia.org/wiki/Cylinder

See also: https://en.wikipedia.org/wiki/Right_circular_cylinder


See also: https://mathworld.wolfram.com/Cylinder.html



An example in C\#

.. code-block:: csharp

    var numSides = 7;
    var a = 0.50;
    var b = 0.50;
    var height = 1.0;
    var cutslope1 = -0.5;
    var cutslope2 = 0.5;
    var proc = BuiltIn.SetCylinder2CP(numSides, a, b, height, cutslope1, cutslope2);


|cr|


|08a_Scatter_Cylinder_cut_plane| `\quad` |08d_Scatter_Cylinder_cut_plane|

.. |08a_Scatter_Cylinder_cut_plane| image:: ../_static/BuiltIn/WithoutTextures/08a_Scatter_Cylinder_cut_plane.3D.xml.jpg
    :width: 30 %

.. |08d_Scatter_Cylinder_cut_plane| image:: ../_static/BuiltIn/WithoutTextures/08a_Scatter_Cylinder_cut_plane.3D.xml.jpg
    :width: 30 %



**Left figure**: Cylinder with inclined cut plane

**Right figure**: Cylinder with inclined cut plane







|newpage|


Pyramid
--------------------------------------

A pyramid is a polyhedron formed by connecting a polygonal base and a point, called the apex. Each base edge and apex form a triangle, called a lateral face. It is a conic solid with a polygonal base. Many types of pyramids can be found by determining the shape of bases, or cutting off the apex. 

See also: https://en.wikipedia.org/wiki/Pyramid_(geometry)

See also: https://mathworld.wolfram.com/Pyramid.html


An example in C\#

.. code-block:: csharp

    var numSides = 7;
    var a = 0.50;
    var b = 0.50;
    var height = 1.0;
    var proc = BuiltIn.SetPyramid(numSides, a, b, height);


|cr|


|09a_Scatter_Pyramid| 

.. |09a_Scatter_Pyramid| image:: ../_static/BuiltIn/WithoutTextures/09a_Scatter_Pyramid.3D.xml.jpg
    :width: 30 %



**Left figure**: Pyramid




|newpage|

Pyramid frustum
-----------------------------------

A frustum of a pyramid is the portion of the pyramid that lies between two parallel planes cutting the pyramid. In a truncated  pyramid, the truncation plane is not necessarily parallel to the pyramid's base (as in a frustum), i.e. it is inclined.

See also: https://en.wikipedia.org/wiki/Frustum

See also: https://mathworld.wolfram.com/PyramidalFrustum.html



An example in C\#

.. code-block:: csharp

    var numSides = 7;
    var a = 0.50;
    var b = 0.50;
    var height = 1.2;
    var cutheight = 0.8;
    var cutslope = 0.0;
    var proc = BuiltIn.SetFrustum(numSides, a, b, height, cutheight, cutslope);


|cr|


|02c_Scatter_Frustum|

.. |02c_Scatter_Frustum| image:: ../_static/BuiltIn/WithoutTextures/10a_Scatter_Frustum.3D.xml.jpg
    :width: 30 %


**Left figure**: Pyramid Frustum





|newpage|

Pyramid, truncated by an inclined plane
---------------------------------------------------

A frustum of a pyramid is the portion of the pyramid that lies between two parallel planes cutting the pyramid. In a truncated  pyramid, the truncation plane is not necessarily parallel to the pyramid's base (as in a frustum), i.e. it is inclined.

See also: https://en.wikipedia.org/wiki/Frustum

See also: https://mathworld.wolfram.com/PyramidalFrustum.html



An example in C\#

.. code-block:: csharp

    var numSides = 7;
    var a = 0.50;
    var b = 0.50;
    var height = 1.2;
    var cutheight = 0.8;
    var cutslope = 0.3;
    var proc = BuiltIn.SetFrustum(numSides, a, b, height, cutheight, cutslope);



|cr|


|02d_Scatter_Frustum_cut_plane|


.. |02d_Scatter_Frustum_cut_plane| image:: ../_static/BuiltIn/WithoutTextures/11a_Scatter_Frustum_cut_plane.3D.xml.jpg
    :width: 30 %



**Right figure**: Pyramid with inclined cut plane






|newpage|

Cone 
----------------------------------------

A cone is a three-dimensional geometric shape that tapers smoothly from a flat base (frequently, though not necessarily, circular) to a point called the apex or vertex. A cone with a polygonal base is called a pyramid.


See also: https://en.wikipedia.org/wiki/Cone

See also: https://mathworld.wolfram.com/Cone.html


An example in C\#

.. code-block:: csharp

    var numSides = 32;
    var a = 0.50;
    var b = 0.50;
    var height = 1.0;
    var proc = BuiltIn.SetCone(numSides, a, b, height);


|cr|


|12a_Scatter_Cone| 

.. |12a_Scatter_Cone| image:: ../_static/BuiltIn/WithoutTextures/12a_Scatter_Cone.3D.xml.jpg
    :width: 30 %



**Left figure**: Cone





|newpage|

Cone Frustum
-------------------------------------

A cone is a three-dimensional geometric shape that tapers smoothly from a flat base (frequently, though not necessarily, circular) to a point called the apex or vertex. A cone with a polygonal base is called a pyramid.


See also: https://en.wikipedia.org/wiki/Frustum

See also: https://mathworld.wolfram.com/ConicalFrustum.html



An example in C\#

.. code-block:: csharp

    var numSides = 32;
    var a = 0.50;
    var b = 0.50;
    var height = 1.2;
    var cutheight = 0.6;
    var cutslope = 0.0;
    var proc = BuiltIn.SetConeFrustum(numSides, a, b, height, cutheight, cutslope);




|cr|


|13a_Scatter_Cone_frustum|

.. |13a_Scatter_Cone_frustum| image:: ../_static/BuiltIn/WithoutTextures/13a_Scatter_Cone_frustum.3D.xml.jpg
    :width: 30 %




**Left figure**: Cone frustum





|newpage|

Cone, truncated by an inclined plane
------------------------------------------------

A cone is a three-dimensional geometric shape that tapers smoothly from a flat base (frequently, though not necessarily, circular) to a point called the apex or vertex. A cone with a polygonal base is called a pyramid.


See also: https://en.wikipedia.org/wiki/Frustum

See also: https://mathworld.wolfram.com/ConicalFrustum.html


An example in C\#

.. code-block:: csharp

    var numSides = 32;
    var a = 0.50;
    var b = 0.50;
    var height = 1.2;
    var cutheight = 0.6;
    var cutslope = 0.3;
    var proc = BuiltIn.SetConeFrustum(numSides, a, b, height, cutheight, cutslope);


|cr|


|14a_Scatter_Cone_frustum_cut_plane|


.. |14a_Scatter_Cone_frustum_cut_plane| image:: ../_static/BuiltIn/WithoutTextures/14a_Scatter_Cone_frustum_cut_plane.3D.xml.jpg
    :width: 30 %


**Right figure**: Cone, truncated by an inclined plane




