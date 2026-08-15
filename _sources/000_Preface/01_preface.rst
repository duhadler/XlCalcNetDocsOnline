





.. |vspace| raw:: html

   <br />

 



.. only:: html

    .. tip::

       To get to the index, click here: :ref:`genindex` (unlike other Sphinx themes, Read the Docs does not 
       provide a separate Index button). Alternatively, try the "Search docs" box in the upper left corner. 
       If you can't see such a box, move the mouse curser over the menu tree, and use the mouse wheel to 
       move the menu tree up and down. As an example, type "gamma" in the search box. This will return not 
       only the entry for the gamma function, but also a list of all occurrences of the word "gamma" in 
       this documentation.




Preface
=========================================



.. only:: html


    XlCalcNet is a Python  library focussing on the calculation of statistical distributions in arbitrary 
    precision. It uses the mpmath library (see http://mpmath.org)  as its computational backend, and 
    is expected to work on all Python configurations on Windows, macOS and Linux which can run mpmath.

    XlCalcNet is part of a group of three related Python libraries. The other two are XlCalcNet (a 
    **m**\ ulti\ **p**\ recision mathematical **fun**\ ction **lab**\ oratory, see 
    https://github.com/duhadler/xlcalcnet) 
    and **fpfunlab** (a **f**\ ixed **p**\ recision mathematical **fun**\ ction **lab**\ oratory, see 
    https://github.com/duhadler/fpfunlab). 
    While XlCalcNet has only mpmath as a dependency, it can use XlCalcNet and **fpfunlab** to speed up 
    calculations both in double precision and in arbitrary precision considerably.

    The three libraries together provide a toolset for investigating the speed and accuracy of the evaluation 
    of mathematical functions in a systematic fashion, since XlCalcNet supports function evaluation with 
    guaranteed (rigorous) error bounds, **fpfunlab** focusses on speed using algorithms optimized for double 
    precision computing, and XlCalcNet takes a middle-of-the-road approach.

    XlCalcNet is intended to be used together with existing software for numerical computing, in particular 
    the Python libraries NumPy, SciPy and Matplotlib, but also recent versions of RStudio and R.
    
    Examples for how to do this are given in the introduction, and comparisons of speed and accuracy of 
    existing numerical software are given in the documentation of many functions. 
