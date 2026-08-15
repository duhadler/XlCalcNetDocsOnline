

.. |spacingstart| raw:: latex

   \begin{spacing}{1.5}


.. |spacingend| raw:: latex

   \end{spacing}



.. |newpage| raw:: latex

   \newpage



.. |br| raw:: html

   <br />





|newpage|

Accessing and setting parts of a matrix
===============================================================================


Getting and setting a matrix coefficient
-------------------------------------------------------------------------------

Individual coefficients of a matrix `A` are accessed using the ``A[row,col]`` syntax. Note that indexing starts at 0, so that the coefficient in the `4^{\text{th}}` row and `2^{\text{nd}}` column is accessed as ``A[3,1]``.  Examples:

.. code-block:: pycon

    >>> from xlcalcnet import *
    >>> ctx = mp14.drf()
    >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
    A: 
    11,  12,  13,  14, 
    21,  22,  23,  24, 
    31,  32,  33,  34, 
    41,  42,  43,  44, 
    51,  52,  53,  54, 
    61,  62,  63,  64, 

    >>> # gets the coefficient in row number 3 and column number 1
    >>> print("A[3,1]: ", A[3,1])
    A[3,1]:  42

    >>> # sets the coefficient in row number 1 and column number 2 to the value of 99.
    >>> A[1,2] = 99; A.show("A")
    matA: 
    11,  12,  13,  14, 
    21,  22,  99,  24, 
    31,  32,  33,  34, 
    41,  42,  43,  44, 
    51,  52,  53,  54, 
    61,  62,  63,  64, 




Getting and setting a matrix row
-------------------------------------------------------------------------------

.. method:: mat.GetRow(i)

    Gets the `i^{\text{th}}` row.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets row number 2 (i.e. the 3rd row from the top)
        >>> r1 = A.row(2); r1.show("r1")
        r1: 
        31,  32,  33,  34, 



.. method:: mat.SetRow(i, matB)

    Sets the `i^{\text{th}}` row to *matB*.


    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the content of row number 5 to the content of row number 2
        >>> A.set_row(5, A.row(2)); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        31,  32,  33,  34, 





Getting and setting a matrix column
-------------------------------------------------------------------------------

.. method:: mat.GetCol(j)

    Gets the `j^{\text{th}}` column.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets column number 1 (i.e. the 2nd column from the left)
        >>> c1 = A.col(1); c1.show("c1")
        c1: 
        12, 
        22, 
        32, 
        42, 
        52, 
        62, 


.. method:: mat.SetCol(j, matB)

    Sets the `j^{\text{th}}` column to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the content of column number 3 to the content of column number 1
        >>> A.set_col(3, A.col(1)); A.show("A")
        A: 
        11,  12,  13,  12, 
        21,  22,  23,  22, 
        31,  32,  33,  32, 
        41,  42,  43,  42, 
        51,  52,  53,  52, 
        61,  62,  63,  62, 






Getting and setting a block
-------------------------------------------------------------------------------

.. method:: mat.GetBlock(i, j, p, q)

    Gets a block of the matrix, starting at row `i` and column `j`, with `p` row elements and `q` column elements.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets a block, beginning at A[1, 1], stretching to A[1+3, 1+2]
        >>> b1 = A.block(1, 1, 3, 2); b1.show("b1")
        b1: 
        22,  23, 
        32,  33, 
        42,  43, 



.. method:: mat.SetBlock(i, j, p, q, matB)

    Sets a block of the matrix to *matB*, starting at row `i` and column `j`, with `p` row elements and `q` column elements.

    .. code-block:: pycon

            >>> # continued from above
            >>> # sets b1 into a block, beginning at A[0, 0], stretching to A[0+3, 0+2]
            >>> A.set_block(0, 0, 3, 2, b1); ; A.show("A")
            A: 
            22,  23,  13,  14, 
            32,  33,  23,  24, 
            42,  43,  33,  34, 
            41,  42,  43,  44, 
            51,  52,  53,  54, 
            61,  62,  63,  64, 






Getting and setting a block in the top left corner
-------------------------------------------------------------------------------

.. method:: mat.GetTopLeftCorner(p, q)

    Gets the `p` by `q` top left corner of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the `3` by `2` block top left corner
        >>> b1 = A.top_left_corner(3, 2); b1.show("b1")
        b1: 
        11,  12, 
        21,  22, 
        31,  32, 



.. method:: mat.SetTopLeftCorner(p, q, matB)

    Sets the `p` by `q` top left corner of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the `3` by `2` top left corner to the `3` by `2` bottom left corner
        >>> A.set_top_left_corner(3, 2, A.bottom_left_corner(3, 2)); A.show("A")
        A: 
        41,  42,  13,  14, 
        51,  52,  23,  24, 
        61,  62,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 





Getting and setting a block in the bottom left corner
-------------------------------------------------------------------------------

.. method:: mat.GetBottomLeftCorner(p, q)

    Gets the `p` by `q` bottom left corner of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the `3` by `2` bottom left corner
        >>> b1 = A.bottom_left_corner(3, 2); b1.show("b1")"
        b1:
        41,  42, 
        51,  52, 
        61,  62, 



.. method:: mat.SetBottomLeftCorner(p, q, matB)

    Sets the `p` by `q` bottom left corner of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the `3` by `2` bottom left corner to the `3` by `2` top left corner
        >>> A.set_bottom_left_corner(3, 2, A.top_left_corner(3, 2)); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        11,  12,  43,  44, 
        21,  22,  53,  54, 
        31,  32,  63,  64, 






Getting and setting a block in the top right corner
-------------------------------------------------------------------------------

.. method:: mat.GetTopRightCorner(p, q)

    Gets the `p` by `q` top right corner of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the `3` by `2` top right corner
        >>> b1 = A.top_right_corner(3, 2); b1.show("b1")
        b1: 
        13,  14, 
        23,  24, 
        33,  34, 



.. method:: mat.SetTopRightCorner(p, q, matB)

    Sets the `p` by `q` top right corner of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the `3` by `2` top right corner to the `3` by `2` bottom right corner
        >>> A.set_top_right_corner(3, 2, A.bottom_right_corner(3, 2)); A.show("A")
        A: 
        11,  12,  43,  44, 
        21,  22,  53,  54, 
        31,  32,  63,  64, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 




Getting and setting a block in the bottom right corner
-------------------------------------------------------------------------------

.. method:: mat.GetBottomRightCorner(p,q)

    Gets the `p` by `q` bottom right corner of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the `3` by `2` top right corner
        >>> b1 = A.bottom_right_corner(3, 2); b1.show("b1")
        b1: 
        43,  44, 
        53,  54, 
        63,  64, 



.. method:: mat.SetBottomRightCorner(p,q, matB)

    Sets the `p` by `q` bottom right corner of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the `3` by `2` top right corner to the `3` by `2` bottom right corner
        >>> A.set_bottom_right_corner(3, 2, A.top_right_corner(3, 2)); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  13,  14, 
        51,  52,  23,  24, 
        61,  62,  33,  34, 






Getting and setting a block containing the first q rows
-------------------------------------------------------------------------------

.. method:: mat.GetTopRows(q)

    Gets the top `q` rows of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the 2 top rows
        >>> b1 = A.top_rows(2); b1.show("b1")
        b1: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 




.. method:: mat.SetTopRows(q, matB)

    Sets the top `q` rows of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the 2 top rows to the 2 bottom rows
        >>> A.set_top_rows(2, A.bottom_rows(2)); A.show("A")
        A: 
        51,  52,  53,  54, 
        61,  62,  63,  64, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 




Getting and setting a block containing the last q rows
-------------------------------------------------------------------------------

.. method:: mat.GetBottomRows(q)

    Gets the bottom `q` rows of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the 2 bottom rows
        >>> b1 = A.bottom_rows(2); b1.show("b1")
        b1: 
        51,  52,  53,  54, 
        61,  62,  63,  64, 



.. method:: mat.SetBottomRows(q, matB)

    Sets the bottom `q` rows of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the 2 bottom rows to the 2 top rows
        >>> A.set_bottom_rows(2, A.top_rows(2)); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        11,  12,  13,  14, 
        21,  22,  23,  24, 




Getting and setting a block containing the first p columns
-------------------------------------------------------------------------------

.. method:: mat.GetLeftCols(p)

    Gets the first `p` (leftmost) columns of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the first 2 (leftmost) columns
        >>> b1 = A.left_cols(2); b1.show("b1")
        b1: 
        11,  12, 
        21,  22, 
        31,  32, 
        41,  42, 
        51,  52, 
        61,  62, 



.. method:: mat.SetLeftCols(p, matB)

    Sets the first `p` (leftmost) columns of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the first 2 (leftmost) columns to the last 2 (rightmost) columns
        >>> A.set_left_cols(2, A.right_cols(2)); A.show("A")
        A: 
        13,  14,  13,  14, 
        23,  24,  23,  24, 
        33,  34,  33,  34, 
        43,  44,  43,  44, 
        53,  54,  53,  54, 
        63,  64,  63,  64, 




Getting and setting a block containing the last q columns
-------------------------------------------------------------------------------

.. method:: mat.GetRightCols(p)

    Gets the last `p` (rightmost) columns of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the last 2 (rightmost) columns
        >>> b1 = A.right_cols(2); b1.show("b1")
        b1: 
        13,  14, 
        23,  24, 
        33,  34, 
        43,  44, 
        53,  54, 
        63,  64, 



.. method:: mat.SetRightCols(p, matB)

    Sets the first `p` (rightmost) columns of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the last 2 (rightmost) columns to the first 2 (leftmost) columns
        >>> A.set_right_cols(2, A.left_cols(2)); A.show("A")
        A: 
        11,  12,  11,  12, 
        21,  22,  21,  22, 
        31,  32,  31,  32, 
        41,  42,  41,  42, 
        51,  52,  51,  52, 
        61,  62,  61,  62, 







Getting and setting a diagonal
-------------------------------------------------------------------------------

.. method:: mat.GetDiagonal(q=0)

    Gets the diagonal or a subdiagonal of the matrix.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets the first lower subdiagonal
        >>> b1 = A.diagonal(-1); b1.show("b1")
        b1 = A.diagonal(-1): 
        21, 
        32, 
        43, 
        54, 



.. method:: mat.SetDiagonal(q, matB)

    Sets the diagonal or a subdiagonal of the matrix to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets the diagonal to the first lower subdiagonal
        >>> A.set_diagonal(0, b1); A.show("A")
        A: 
        21,  12,  13,  14, 
        21,  32,  23,  24, 
        31,  32,  43,  34, 
        41,  42,  43,  54, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 




Getting and setting middle rows
-------------------------------------------------------------------------------

.. method:: mat.GetMiddleRows(p, q)

    Gets a block containing `q` rows of the matrix, starting at row `p`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets a block containing 2 rows, starting at row 1
        >>> b1 = A.middle_rows(1, 2); b1.show("b1")
        b1: 
        21,  22,  23,  24, 
        31,  32,  33,  34, 




.. method:: mat.SetMiddleRows(p, q, matB)

    Sets a block containing `q` rows of the matrix to *matB*, starting at row `p`.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets a block containing 2 rows, starting at row 3, to b1
        >>> A.set_middle_rows(3, 2, b1); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        61,  62,  63,  64, 





Getting and setting middle columns
-------------------------------------------------------------------------------

.. method:: mat.GetMiddleCols(p, q)

    Gets a block containing `q` columns of the matrix, starting at column `p`.

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x4", ""); A.show("A")
        A: 
        11,  12,  13,  14, 
        21,  22,  23,  24, 
        31,  32,  33,  34, 
        41,  42,  43,  44, 
        51,  52,  53,  54, 
        61,  62,  63,  64, 

        >>> # gets a block containing 2 columns, starting at column 0
        >>> b1 = A.middle_cols(0, 2); b1.show("b1")
        b1: 
        11,  12, 
        21,  22, 
        31,  32, 
        41,  42, 
        51,  52, 
        61,  62, 



.. method:: mat.SetMiddleCols(p, q, matB)

    Sets a block containing `q` columns of the matrix to *matB*, starting at column `p`.

    .. code-block:: pycon

        >>> # continued from above
        >>> # sets a block containing 2 columns, starting at column 1, to b1
        >>> A.set_middle_cols(1, 2, b1); A.show("A")
        A: 
        11,  11,  12,  14, 
        21,  21,  22,  24, 
        31,  31,  32,  34, 
        41,  41,  42,  44, 
        51,  51,  52,  54, 
        61,  61,  62,  64, 







Getting and setting the lower triangle
-------------------------------------------------------------------------------

.. method:: mat.GetLowerTriangle()

    Gets the lower triangle (including the diagonal).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> # gets the lower triangle (including the diagonal)
        >>> b1 = A.lower_triangle(); b1.show("b1")
        b1: 
        11,  0,  0,  0,  0,  0, 
        21, 22,  0,  0,  0,  0, 
        31, 32, 33,  0,  0,  0, 
        41, 42, 43, 44,  0,  0, 
        51, 52, 53, 54, 55,  0, 
        61, 62, 63, 64, 65, 66, 




.. method:: mat.SetLowerTriangle(matB)

    Sets the lower triangle (including the diagonal)  to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # read and display another matrix, B
        >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
        B: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 

        >>> # sets the lower triangle (including the diagonal) of A to B
        >>> A.set_lower_triangle(B); A.show("A")
        A: 
        911,  12,  13,  14,  15,  16, 
        921, 922,  23,  24,  25,  26, 
        931, 932, 933,  34,  35,  36, 
        941, 942, 943, 944,  45,  46, 
        951, 952, 953, 954, 955,  56, 
        961, 962, 963, 964, 965, 966, 






Getting and setting the upper triangle
-------------------------------------------------------------------------------

.. method:: mat.GetUpperTriangle()

    Gets the lower triangle (including the diagonal).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> # gets the upper triangle (including the diagonal)
        >>> b1 = A.upper_triangle(); b1.show("b1")
        b1: 
        11, 12, 13, 14, 15, 16, 
         0, 22, 23, 24, 25, 26, 
         0,  0, 33, 34, 35, 36, 
         0,  0,  0, 44, 45, 46, 
         0,  0,  0,  0, 55, 56, 
         0,  0,  0,  0,  0, 66, 



.. method:: mat.SetUpperTriangle(matB)

    Sets the lower triangle (including the diagonal)  to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # read and display another matrix, B
        >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
        B: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 

        >>> # sets the upper triangle (including the diagonal) of A to B
        >>> A.set_upper_triangle(B); A.show("A")
        A: 
        911, 912, 913, 914, 915, 916, 
         21, 922, 923, 924, 925, 926, 
         31,  32, 933, 934, 935, 936, 
         41,  42,  43, 944, 945, 946, 
         51,  52,  53,  54, 955, 956, 
         61,  62,  63,  64,  65, 966, 




Getting and setting the strictly lower triangle
-------------------------------------------------------------------------------

.. method:: mat.GetStrictlyLowerTriangle()

    Gets the strictly lower triangle (without the diagonal).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> # gets the strictly lower triangle (without the diagonal)
        >>> b1 = A.strictly_lower_triangle(); b1.show("b1")
        b1: 
         0,  0,  0,  0,  0,  0, 
        21,  0,  0,  0,  0,  0, 
        31, 32,  0,  0,  0,  0, 
        41, 42, 43,  0,  0,  0, 
        51, 52, 53, 54,  0,  0, 
        61, 62, 63, 64, 65,  0, 


.. method:: mat.SetStrictlyLowerTriangle(matB)

    Sets the strictly lower triangle (without the diagonal)  to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # read and display another matrix, B
        >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
        B: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 

        >>> # sets the strictly lower triangle (without the diagonal) of A to B
        >>> A.set_strictly_lower_triangle(B); A.show("A")
        A: 
         11,  12,  13,  14,  15,  16, 
        921,  22,  23,  24,  25,  26, 
        931, 932,  33,  34,  35,  36, 
        941, 942, 943,  44,  45,  46, 
        951, 952, 953, 954,  55,  56, 
        961, 962, 963, 964, 965,  66, 









Getting and setting the strictly upper triangle
-------------------------------------------------------------------------------

.. method:: mat.GetStrictlyUpperTriangle()

    Gets the strictly upper triangle (without the diagonal).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> # gets the strictly upper triangle (without the diagonal)
        >>> b1 = A.strictly_upper_triangle(); b1.show("b1")
        b1: 
         0, 12, 13, 14, 15, 16, 
         0,  0, 23, 24, 25, 26, 
         0,  0,  0, 34, 35, 36, 
         0,  0,  0,  0, 45, 46, 
         0,  0,  0,  0,  0, 56, 
         0,  0,  0,  0,  0,  0, 




.. method:: mat.SetStrictlyUpperTriangle(matB)

    Sets the strictly upper triangle (without the diagonal)  to *matB*: ``set_strictly_upper_triangle(matB)``.

    .. code-block:: pycon

        >>> # continued from above
        >>> # read and display another matrix, B
        >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
        B: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 

        >>> # sets the strictly upper triangle (without the diagonal) of A to B
        >>> A.set_strictly_upper_triangle(B); A.show("A")
        A: 
         11, 912, 913, 914, 915, 916, 
         21,  22, 923, 924, 925, 926, 
         31,  32,  33, 934, 935, 936, 
         41,  42,  43,  44, 945, 946, 
         51,  52,  53,  54,  55, 956, 
         61,  62,  63,  64,  65,  66, 




Getting and setting the unit lower triangle
-------------------------------------------------------------------------------

.. method:: mat.GetUnitLowerTriangle()

    Gets the unit lower triangle (returning 1s for the diagonal).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> # gets the unit lower triangle (without the diagonal)
        >>> b1 = A.unit_lower_triangle(); b1.show("b1")
        b1: 
         1,  0,  0,  0,  0,  0, 
        21,  1,  0,  0,  0,  0, 
        31, 32,  1,  0,  0,  0, 
        41, 42, 43,  1,  0,  0, 
        51, 52, 53, 54,  1,  0, 
        61, 62, 63, 64, 65,  1, 



.. method:: mat.SetUnitLowerTriangle(matB)

    Sets the unit lower triangle (without changing the diagonal)  to *matB*.

    .. code-block:: pycon

        >>> # continued from above
        >>> # read and display another matrix, B
        >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
        B: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 

        >>> # sets the unit lower triangle (without the diagonal) of A to B
        >>> A.set_unit_lower_triangle(B); A.show("A")
        A: 
         11,  12,  13,  14,  15,  16, 
        921,  22,  23,  24,  25,  26, 
        931, 932,  33,  34,  35,  36, 
        941, 942, 943,  44,  45,  46, 
        951, 952, 953, 954,  55,  56, 
        961, 962, 963, 964, 965,  66, 





Getting and setting the unit upper triangle
-------------------------------------------------------------------------------

.. method:: mat.GetUnitUpperTriangle()

    Gets the unit upper triangle (returning 1s for the diagonal).

    .. code-block:: pycon

        >>> from xlcalcnet import *
        >>> ctx = mp14.drf()
        >>> A = ctx.read_from_sqlite(mp14.dbpath(), "DecTableA6x6", ""); A.show("A")
        A: 
        11, 12, 13, 14, 15, 16, 
        21, 22, 23, 24, 25, 26, 
        31, 32, 33, 34, 35, 36, 
        41, 42, 43, 44, 45, 46, 
        51, 52, 53, 54, 55, 56, 
        61, 62, 63, 64, 65, 66, 

        >>> # gets the unit upper triangle (without the diagonal)
        >>> b1 = A.unit_upper_triangle(); b1.show("b1")
        b1: 
         1, 12, 13, 14, 15, 16, 
         0,  1, 23, 24, 25, 26, 
         0,  0,  1, 34, 35, 36, 
         0,  0,  0,  1, 45, 46, 
         0,  0,  0,  0,  1, 56, 
         0,  0,  0,  0,  0,  1, 




.. method:: mat.SetUnitUpperTriangle(matB)

    Sets the unit upper triangle (without changing the diagonal)  to *matB*.

    .. code-block:: pycon

        >>> # read and display another matrix, B
        >>> B = ctx.read_from_sqlite(mp14.dbpath(), "DecTableB6x6", ""); B.show("B")
        B: 
        911, 912, 913, 914, 915, 916, 
        921, 922, 923, 924, 925, 926, 
        931, 932, 933, 934, 935, 936, 
        941, 942, 943, 944, 945, 946, 
        951, 952, 953, 954, 955, 956, 
        961, 962, 963, 964, 965, 966, 

        >>> # sets the unit upper triangle (without the diagonal) of A to B
        >>> A.set_unit_upper_triangle(B); A.show("A")
        A: 
         11, 912, 913, 914, 915, 916, 
         21,  22, 923, 924, 925, 926, 
         31,  32,  33, 934, 935, 936, 
         41,  42,  43,  44, 945, 946, 
         51,  52,  53,  54,  55, 956, 
         61,  62,  63,  64,  65,  66, 





