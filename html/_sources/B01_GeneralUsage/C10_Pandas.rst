

.. |newpage| raw:: latex

   \newpage



.. |vspace| raw:: html

   <br />







|newpage|



A quick look at Pandas and Xlxswriter
=====================================================





Reading dataframes from ``*.xlsx`` files
-------------------------------------------------------

**pandas.read_excel**

See also: https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel

Read an Excel file into a pandas DataFrame.

Supports xls, xlsx, xlsm, xlsb, odf, ods and odt file extensions read from a local filesystem or URL. Supports an option to read a single sheet or a list of sheets.


Examples

The file can be read using the file name as string or an open file object:

.. code-block:: pycon

    >>> pd.read_excel('tmp.xlsx', index_col=0)  
           Name  Value
    0   string1      1
    1   string2      2
    2  #Comment      3

    >>> ppd.read_excel(open('tmp.xlsx', 'rb'),
                  sheet_name='Sheet3')  
       Unnamed: 0      Name  Value
    0           0   string1      1
    1           1   string2      2
    2           2  #Comment      3


Index and header can be specified via the index_col and header arguments

.. code-block:: pycon

    >>> ppd.read_excel('tmp.xlsx', index_col=None, header=None)
         0         1      2
    0  NaN      Name  Value
    1  0.0   string1      1
    2  1.0   string2      2
    3  2.0  #Comment      3


Column types are inferred but can be explicitly specified

.. code-block:: pycon

    >>> ppd.read_excel('tmp.xlsx', index_col=0, dtype={'Name': str, 'Value': float})
           Name  Value
    0   string1    1.0
    1   string2    2.0
    2  #Comment    3.0


True, False, and NA values, and thousands separators have defaults, but can be explicitly specified, too. Supply the values you would like as strings or lists of strings!

.. code-block:: pycon

    >>> ppd.read_excel('tmp.xlsx', index_col=0, na_values=['string1', 'string2'])  
           Name  Value
    0       NaN      1
    1       NaN      2
    2  #Comment      3


Comment lines in the excel input file can be skipped using the comment kwarg.

.. code-block:: pycon

    >>> pd.read_excel('tmp.xlsx', index_col=0, comment='#')  
          Name  Value
    0  string1    1.0
    1  string2    2.0
    2     None    NaN





**Reading Excel files using the ``ExcelFile`` class**

See also: https://pandas.pydata.org/docs/user_guide/io.html#reading-excel-files


To facilitate working with multiple sheets from the same file, the ``ExcelFile`` class can be used to wrap the file and can be passed into ``read_excel``. There will be a performance benefit for reading multiple sheets as the file is read into memory only once.

.. code-block:: python

    xlsx = pd.ExcelFile("path_to_file.xls")
    df = pd.read_excel(xlsx, "Sheet1")

The ``ExcelFile`` class can also be used as a context manager.

.. code-block:: python

    with pd.ExcelFile("path_to_file.xls") as xls:
        df1 = pd.read_excel(xls, "Sheet1")
        df2 = pd.read_excel(xls, "Sheet2")

The ``sheet_names`` property will generate a list of the sheet names in the file.

The primary use-case for an ``ExcelFile`` is parsing multiple sheets with different parameters:

.. code-block:: python

    data = {}
    # For when Sheet1's format differs from Sheet2
    with pd.ExcelFile("path_to_file.xls") as xls:
        data["Sheet1"] = pd.read_excel(xls, "Sheet1", index_col=None, na_values=["NA"])
        data["Sheet2"] = pd.read_excel(xls, "Sheet2", index_col=1)


Note that if the same parsing parameters are used for all sheets, a list of sheet names can simply be passed to read_excel with no loss in performance.

.. code-block:: python

    # using the ExcelFile class
    data = {}
    with pd.ExcelFile("path_to_file.xls") as xls:
        data["Sheet1"] = pd.read_excel(xls, "Sheet1", index_col=None, na_values=["NA"])
        data["Sheet2"] = pd.read_excel(xls, "Sheet2", index_col=None, na_values=["NA"])

    # equivalent using the read_excel function
    data = pd.read_excel(
        "path_to_file.xls", ["Sheet1", "Sheet2"], index_col=None, na_values=["NA"]
    )

ExcelFile can also be called with a xlrd.book.Book object as a parameter. This allows the user to control how the excel file is read. For example, sheets can be loaded on demand by calling xlrd.open_workbook() with on_demand=True.

.. code-block:: python

    import xlrd

    xlrd_book = xlrd.open_workbook("path_to_file.xls", on_demand=True)
    with pd.ExcelFile(xlrd_book) as xls:
        df1 = pd.read_excel(xls, "Sheet1")
        df2 = pd.read_excel(xls, "Sheet2")


**Specifying sheets**


* The second argument is sheet_name, not to be confused with ExcelFile.sheet_names.

* An ExcelFile’s attribute sheet_names provides access to a list of sheets.

* The arguments sheet_name allows specifying the sheet or sheets to read.

* The default value for sheet_name is 0, indicating to read the first sheet

* Pass a string to refer to the name of a particular sheet in the workbook.

* Pass an integer to refer to the index of a sheet. Indices follow Python convention, beginning at 0.

* Pass a list of either strings or integers, to return a dictionary of specified sheets.

* Pass a None to return a dictionary of all available sheets.


.. code-block:: python

    # Returns a DataFrame
    pd.read_excel("path_to_file.xls", "Sheet1", index_col=None, na_values=["NA"])


Using the sheet index:

.. code-block:: python

    # Returns a DataFrame
    pd.read_excel("path_to_file.xls", 0, index_col=None, na_values=["NA"])


Using all default values:

.. code-block:: python

    # Returns a DataFrame
    pd.read_excel("path_to_file.xls")


Using None to get all sheets:

.. code-block:: python

    # Returns a dictionary of DataFrames
    pd.read_excel("path_to_file.xls", sheet_name=None)

Using a list to get multiple sheets:

.. code-block:: python

    # Returns the 1st and 4th sheet, as a dictionary of DataFrames.
    pd.read_excel("path_to_file.xls", sheet_name=["Sheet1", 3])

``read_excel`` can read more than one sheet, by setting ``sheet_name`` to either a list of sheet names, a list of sheet positions, or ``None`` to read all sheets. Sheets can be specified by sheet index or sheet name, using an integer or string, respectively.


**Reading a MultiIndex**

read_excel can read a MultiIndex index, by passing a list of columns to index_col and a MultiIndex column by passing a list of rows to header. If either the index or columns have serialized level names those will be read in as well by specifying the rows/columns that make up the levels.

For example, to read in a MultiIndex index without names:

.. code-block:: pycon

    >>> df = pd.DataFrame(
        {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]},
        index=pd.MultiIndex.from_product([["a", "b"], ["c", "d"]]),
    )
    >>> df.to_excel("path_to_file.xlsx")
    >>> df = pd.read_excel("path_to_file.xlsx", index_col=[0, 1])
    >>> df
         a  b
    a c  1  5
      d  2  6
    b c  3  7
      d  4  8


If the index has level names, they will parsed as well, using the same parameters.

.. code-block:: pycon

    >>> df.index = df.index.set_names(["lvl1", "lvl2"])
    >>> df.to_excel("path_to_file.xlsx")
    >>> df = pd.read_excel("path_to_file.xlsx", index_col=[0, 1])
    >>> df
               a  b
    lvl1 lvl2      
    a    c     1  5
         d     2  6
    b    c     3  7
         d     4  8

If the source file has both MultiIndex index and columns, lists specifying each should be passed to index_col and header:

.. code-block:: pycon

    >>> df.columns = pd.MultiIndex.from_product([["a"], ["b", "d"]], names=["c1", "c2"])
    >>> df.to_excel("path_to_file.xlsx")
    >>> df = pd.read_excel("path_to_file.xlsx", index_col=[0, 1], header=[0, 1])
    >>> df

    c1         a   
    c2         b  d
    lvl1 lvl2      
    a    c     1  5
         d     2  6
    b    c     3  7
         d     4  8

Missing values in columns specified in index_col will be forward filled to allow roundtripping with to_excel for merged_cells=True. To avoid forward filling the missing values use set_index after reading the data instead of index_col.




**Parsing specific columns**

It is often the case that users will insert columns to do temporary computations in Excel and you may not want to read in those columns. ``read_excel`` takes a ``usecols`` keyword to allow you to specify a subset of columns to parse.

You can specify a comma-delimited set of Excel columns and ranges as a string:

.. code-block:: python

    pd.read_excel("path_to_file.xls", "Sheet1", usecols="A,C:E")

If ``usecols`` is a list of integers, then it is assumed to be the file column indices to be parsed.

.. code-block:: python

    pd.read_excel("path_to_file.xls", "Sheet1", usecols=[0, 2, 3])

Element order is ignored, so ``usecols=[0, 1]`` is the same as ``[1, 0]``.

If ``usecols`` is a list of strings, it is assumed that each string corresponds to a column name provided either by the user in ``names`` or inferred from the document header row(s). Those strings define which columns will be parsed:

.. code-block:: python

    pd.read_excel("path_to_file.xls", "Sheet1", usecols=["foo", "bar"])

Element order is ignored, so ``usecols=['baz', 'joe']`` is the same as ``['joe', 'baz']``.

If ``usecols`` is callable, the callable function will be evaluated against the column names, returning names where the callable function evaluates to ``True``.

.. code-block:: python

    pd.read_excel("path_to_file.xls", "Sheet1", usecols=lambda x: x.isalpha())




**Parsing dates**

Datetime-like values are normally automatically converted to the appropriate dtype when reading the excel file. But if you have a column of strings that look like dates (but are not actually formatted as dates in excel), you can use the parse_dates keyword to parse those strings to datetimes:


.. code-block:: python

    pd.read_excel("path_to_file.xls", "Sheet1", parse_dates=["date_strings"])

**Cell converters**

It is possible to transform the contents of Excel cells via the converters option. For instance, to convert a column to boolean:

.. code-block:: python

    pd.read_excel("path_to_file.xls", "Sheet1", converters={"MyBools": bool})


This options handles missing values and treats exceptions in the converters as missing data. Transformations are applied cell by cell rather than to the column as a whole, so the array dtype is not guaranteed. For instance, a column of integers with missing values cannot be transformed to an array with integer dtype, because NaN is strictly a float. You can manually mask missing data to recover integer dtype:

.. code-block:: python

    def cfun(x):
        return int(x) if x else -1

    pd.read_excel("path_to_file.xls", "Sheet1", converters={"MyInts": cfun})


**Dtype specifications**

As an alternative to converters, the type for an entire column can be specified using the dtype keyword, which takes a dictionary mapping column names to types. To interpret data with no type inference, use the type str or object.

.. code-block:: python

    pd.read_excel("path_to_file.xls", dtype={"MyInts": "int64", "MyText": str})







Writing a dataframe object to an ``*.xlsx`` file
-------------------------------------------------------

See also: https://pandas.pydata.org/docs/user_guide/io.html#writing-excel-files


To write a ``DataFrame`` object to a sheet of an Excel file, you can use the ``to_excel`` instance method. The arguments are largely the same as ``to_csv`` described above, the first argument being the name of the excel file, and the optional second argument the name of the sheet to which the ``DataFrame`` should be written. For example:

.. code-block:: python

    df.to_excel("path_to_file.xlsx", sheet_name="Sheet1")


Files with a ``.xlsx`` extension will be written using ``xlsxwriter`` (if available) or ``openpyxl``.

The ``DataFrame`` will be written in a way that tries to mimic the REPL output. The ``index_label`` will be placed in the second row instead of the first. You can place it in the first row by setting the ``merge_cells`` option in ``to_excel()`` to ``False``:

.. code-block:: python

    df.to_excel("path_to_file.xlsx", index_label="label", merge_cells=False)


In order to write separate ``DataFrames`` to separate sheets in a single Excel file, one can pass an ``ExcelWriter``.

.. code-block:: python

    with pd.ExcelWriter("path_to_file.xlsx") as writer:
        df1.to_excel(writer, sheet_name="Sheet1")
        df2.to_excel(writer, sheet_name="Sheet2")

When using the ``engine_kwargs`` parameter, pandas will pass these arguments to the engine. For this, it is important to know which function pandas is using internally.

* For the engine openpyxl, pandas is using ``openpyxl.Workbook()`` to create a new sheet and ``openpyxl.load_workbook()`` to append data to an existing sheet. The openpyxl engine writes to (.xlsx) and (.xlsm) files.

* For the engine xlsxwriter, pandas is using ``xlsxwriter.Workbook()`` to write to (.xlsx) files.

* For the engine odf, pandas is using ``odf.opendocument.OpenDocumentSpreadsheet()`` to write to (.ods) files.


**Style and formatting**

The look and feel of Excel worksheets created from pandas can be modified using the following parameters on the ``DataFrame``'s ``to_excel`` method.

* ``float_format`` : Format string for floating point numbers (default ``None``).

* ``freeze_panes`` : A tuple of two integers representing the bottommost row and rightmost column to freeze. Each of these parameters is one-based, so (1, 1) will freeze the first row and first column (default ``None``).

Using the Xlsxwriter engine provides many options for controlling the format of an Excel worksheet created with the ``to_excel`` method. Excellent examples can be found in the Xlsxwriter documentation here: https://xlsxwriter.readthedocs.io/working_with_pandas.html










Reading a dataframe from a ``*.csv`` file
-------------------------------------------------------

See also: https://pandas.pydata.org/docs/reference/api/pandas.read_table.html#pandas.read_table

Read general delimited file into DataFrame.

Also supports optionally iterating or breaking of the file into chunks.

.. code-block:: pycon

    >>> import pandas as pd
    >>> pd.read_table('data.csv') 
    >>> pd





Writing a dataframe to a ``*.csv`` file
-------------------------------------------------------

See also: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv


Create 'out.csv' containing 'df' without indices

.. code-block:: pycon

    df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                       'mask': ['red', 'purple'],
                       'weapon': ['sai', 'bo staff']})
    df.to_csv('out.csv', index=False)  


Create ‘out.zip’ containing ‘out.csv’

.. code-block:: pycon

    df.to_csv(index=False)
    'name,mask,weapon\nRaphael,red,sai\nDonatello,purple,bo staff\n'
    compression_opts = dict(method='zip',
                            archive_name='out.csv')  
    df.to_csv('out.zip', index=False,
              compression=compression_opts)  


To write a csv file to a new folder or nested folder you will first need to create it using either Pathlib or os:

.. code-block:: pycon

    from pathlib import Path  
    filepath = Path('folder/subfolder/out.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    df.to_csv(filepath)  

    import os  
    os.makedirs('folder/subfolder', exist_ok=True)  
    df.to_csv('folder/subfolder/out.csv')




Transforming data in a dataframe
-------------------------------------------------------


See also: https://pandas.pydata.org/docs/user_guide/10min.html#min


See also: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html



See also: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html


See also: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join




See also: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html


See also: https://pandas.pydata.org/docs/user_guide/10min.html#user-defined-functions







Xlsxwriter: creating files in the ``*.xlsx`` format
----------------------------------------------------------------



Note on usability by MS Office and Libreoffice.

Note on graphics formats: issues with  ``*.svg``  files.


See also: https://xlsxwriter.readthedocs.io/index.html

See also: https://github.com/jmcnamara/XlsxWriter

See also: https://pypi.org/project/XlsxWriter/



|newpage|



Python-docx: creating files in the ``*.docx`` format
----------------------------------------------------------------


See also: https://python-docx.readthedocs.io/en/latest/

See also: https://github.com/python-openxml/python-docx

See also: https://pypi.org/project/python-docx/



|newpage|



Python-pptx: creating files in the ``*.pptx`` format
----------------------------------------------------------------


See also: https://python-pptx.readthedocs.io/en/latest/

See also: https://github.com/scanny/python-pptx

See also: https://pypi.org/project/python-pptx/









