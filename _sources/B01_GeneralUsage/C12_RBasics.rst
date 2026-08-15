






.. |newpage| raw:: latex

   \newpage


.. |begin_flushleft| raw:: latex

   \begin{flushleft}


.. |end_flushleft| raw:: latex

   \end{flushleft}


.. |vspace| raw:: html

   <br />



|newpage|


A quick look at R, RStudio and Rpy2
===============================================



Installing R, RStudio, and the reticulate package
-----------------------------------------------------------------

Here is an overview of using Python from R:

https://rstudio.github.io/reticulate/

https://rstudio.github.io/reticulate/articles/calling_python.html

https://blog.rstudio.com/2018/10/09/rstudio-1-2-preview-reticulated-python/


https://www.business-science.io/code-tools/2019/02/06/python-in-rstudio-ide.html



.. code-block:: text

    In Umgebungsvariablen -> Systemvariablen

    add item

    R_HOME -> C:\Program Files\R\R-4.4.2






Installing additional R packges
-------------------------------------------------------

The following packages are recommended:

.. code-block:: rout

    > install.packages("reticulate")

    > install.packages("svglite")

    > install.packages("devEMF")

    > install.packages("tidyverse")

    > install.packages("GGally")




Using the python command line in the  RStudio console
-------------------------------------------------------


To be able to use Python from R, R needs to know the full path to the Python interpreter. This is set in Tools|Global Options...|Python. On Windows, the path could look like "C:/Python38/python.exe".

To start the reticulate package, use

.. code-block:: rout

    > library(reticulate)
    > reticulate::repl_python()   # switch on Python console




.. code-block:: pycon

    Python 3.6.3 (/Users/dietrichhadler/opt/anaconda3/bin/python)
    Reticulate 1.10 REPL -- A Python interpreter in R.
    >>> from xlcalcnet import *
    >>> mp.dps = 60
    >>> p = mp.pi()
    >>> r = 3*p
    >>> s = sqrt(r)
    >>> print("p: ", p)
    p:  3.1415926535897932384626433832795028841971693993751058209749445923078164
    >>> print("s: ", s)
    s:  3.0699801238394654654386548746677945821221293132529234536092078633942877
    >>> quit  # return to R console


.. code-block:: rout

    > p1 = py$p
    > p1
    3.1415926535897932384626433832795028841971693993751058209749445923078164


##########Example in python ##############



.. code-block:: pycon

    >>> from decimal import *
    >>> getcontext().prec = 28
    >>> Decimal(1) / Decimal(7)
    Decimal('0.1428571428571428571428571429')
    >>> a = Decimal(1) / Decimal(7)
    >>> b = a.sqrt()
    >>> b
    Decimal('0.3779644730092272272145165363')
    >>> c = a * b
    >>> c
    Decimal('0.05399492471560388960207379092')
    >>> d = exp(c)
    >>> d
    Decimal('1.055479245284142221355982839')
    >>> quit


.. code-block:: rout

    > a1 = py$a
    > a1
    0.1428571428571428571428571429



This shows how to use xlcalcnet:
    
.. code-block:: rout

    > library(reticulate)
    > use_python("C:\\Python313", required = TRUE)
    > xr = 3  # a number which will be referenced from Python
    > reticulate::repl_python()   # switch on Python console


.. code-block:: pycon

    Python 3.13.3 (C:/Python313/python.exe)
    Reticulate 1.41.0.1 REPL -- A Python interpreter in R.
    Enter 'exit' or 'quit' to exit the REPL and return to R.
    >>> from xlcalcnet import *
    >>> gui.setdps(50)
    >>> ds = dpm.sqrt(2)
    >>> ds
    Decimal('1.4142135623730950488016887242096980785696718753769')
    >>> r.xr  # accessing the xr variable which was set in the R console
    3.0
    >>> quit  # return to R console


.. code-block:: rout

    >  print (py$ds)
    0.045111761078870897297999831657494801135877181969858627156053




########## Begin Example for xlcalcnet ##############

.. code-block:: pycon

    > library(reticulate)
    > use_python("C:\\Python313", required = TRUE)
    > xr = 3  # a number which will be referenced from Python
    > reticulate::repl_python()   # switch on Python console
    >>> from xlcalcnet.mpclasses import mp4
    >>> mp4.setdps(60)
    >>> mp4any = mp4.mprf()
    >>> x1 = mp4any.pi()
    >>> x1
    mprf_t('3.141592653589793238462643383279502884197169399375105820974944E+00')
    >>> x3 = mp4any.exp(x1)
    >>> x3
    mprf_t('2.314069263277926900572908636794854738026610624260021199344506E+01')


########## End Example for xlcalcnet ##############










Using the python editor line in the  RStudio editor panel
-------------------------------------------------------------


.. code-block:: r

    library(reticulate)
    use_python("C:\\Python313", required = TRUE)
    py_config()
    source_python("testmpmath.py")
    p1 = py$p
    s1 = py$s
    print("py$p: ")
    print(py$p)
    print("py$s: ")
    print(py$s)
    print(py$dbl_p, digits = 15)
    print(py$dbl_s, digits = 15)
    print(py$str_p)


This is the code contained in the file "testmpmath.py".

.. code-block:: python

    from xlcalcnet import mp
    mp.dps = 160
    p = mp.pi()
    r = 3*p
    s = mp.sqrt(r)
    print("p: ", p)
    print("s: ", s)
    dbl_p = float(p)
    dbl_s = float(s)
    str_p = str(p)





