

.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}


.. |spacingend| raw:: latex

   \end{spacing}



.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|

Read-only properties: information about a matrix
===============================================================================


Rows of a matrix
-------------------------------------------------------------------------------

.. method:: mat.Rows()



    Returns the number of rows of the matrix.


    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mpm.dps = 15;
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", "")
        >>> print("A.rows: ", A.rows)
        A.rows: 6





Columns of a matrix
-------------------------------------------------------------------------------

.. method:: mat.Cols()

    Returns the number of columns of the matrix.


    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mpm.dps = 15;
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", "")
        >>> print("A.cols: ", A.cols)
        A.cols: 4




Size of a matrix
-------------------------------------------------------------------------------

.. method:: mat.Size()

    Returns the size of the matrix.



    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> mpm.dps = 15;
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", "")
        >>> print("A.size: ", A.size)
        A.cols: 24





