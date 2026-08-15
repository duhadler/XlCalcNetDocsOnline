


.. |newpage| raw:: latex

   \newpage





|newpage|


General and user interface functions
==================================================





Starting the socket server
--------------------------------------------------------------------------------


.. method:: gui.socketserver()

Describe the start of the socket server


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.socketserver()



Starting the output monitor
--------------------------------------------------------------------------------


.. method:: gui.outputmonitor()

Describe the start of the output monitor


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.outputmonitor()






Starting an additional instance of the IDE
--------------------------------------------------------------------------------


.. method:: gui.tinyide()

Describe the start an additional instance of the IDE


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.tinyide(x)






Starting the gallery of plots
--------------------------------------------------------------------------------



.. method:: gui.plot2d()

Describe the start of the gallery of plots


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.plot2d(x)






Starting the interactive 3D wpf plots
--------------------------------------------------------------------------------


.. method:: gui.plot3d()

Describe the start of Interactive 3D Wpf plots


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.plot3d(x)





Starting the data viewer
--------------------------------------------------------------------------------


.. method:: gui.dataviewer()

Describe the start of data viewer


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.dataviewer(x)





Starting IDLE
--------------------------------------------------------------------------------



.. method:: gui.idle()

Describe the setup and use of IDLE


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.idle(x)




Functions related to folders
--------------------------------------------------------------------------------

There are several functions related to folders


.. method:: gui.get_local_appdata()

Return the current user's local Application Data folder


    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.get_local_appdata()




.. method:: gui.get_local_appdata_xlcalcnet()

Return the current user's local AppData/XlCalcNetIDE folder

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.get_local_appdata_xlcalcnet()



.. method:: gui.get_my_documents()

Return the current user's local AppData/XlCalcNetIDE folder

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.get_my_documents()




Information about installation status of supporting python packages
--------------------------------------------------------------------------------


.. method:: gui.info()

Support for Matplotlib output in a separate process

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.info()


.. method:: gui.has_gpm()

Returns True if gmpy2 is installed

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.has_gpm()


.. method:: gui.has_apm()

Returns True if python-flint is installed

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.has_apm()



.. method:: gui.has_xlcalcnet2()

Returns True if xlcalcnet2 is installed

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.has_xlcalcnet2()







Information about context lists, and setting global precision
--------------------------------------------------------------------------------


.. property:: gui.ctxlistreal

Returns a list of all available numerical contexts supporting real data types

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.ctxlistreal



.. property:: gui.ctxlistcplx

Returns a list of all available numerical contexts supporting complex data types

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.ctxlistcomplex



.. method:: gui.setdps(dps)

Sets the decimal precision for all multiprecision data types

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> dps = 50
        >>> gui.setdps(dps)



Calling the socketserver from Python
--------------------------------------------------------------------------------


Describe calling the socketserver from Python


.. code-block:: pycon

    >>> import socket

    >>> host = socket.gethostname()
    >>> port = 11958  # socket server port number
    >>> client_socket = socket.socket()  # instantiate
    >>> client_socket.connect((host, port))  # connect to the server

    >>> client_socket.send(SnippetToSend.encode())  # send message
    >>> DataReceived = client_socket.recv(1024).decode()  # receive response
    >>> print('Received from server: ' + DataReceived)  # show in terminal

    >>> client_socket.close()  # close the connection



Support for running interactive Matplotlib output in a separate process
--------------------------------------------------------------------------------

There is support for Matplotlib output in a separate process

See also: https://matplotlib.org/stable/users/explain/figure/interactive.html#default-ui

.. property:: gui.plot(fig, file, fname)

Support for Matplotlib output in a separate process

    .. code-block:: pycon

        >>> from xlcalcnet import gui
        >>> gui.plot(fig, file, fname)


