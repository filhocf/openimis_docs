
How access data from the Data Warehouse
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  Data from the Data Warehouse can be accessed by means of an Excel file. As access to the Data Warehouse is protected, a user has to get from an administrator of AR-MIS URL of the Data Warehouse for remote access, a userid and a password. A userid may allow access to all data in the Data Warehouse or only to a subset of data corresponding to a specific region, to selected regions, to a specific district or to selected districts.


  The procedure of accessing of data is as follows (:ref:`image274`)

  .. _image274:
  .. figure:: /img / user_manual / image239.png
    :align: center

    `Accessing the Data Warehouse`

  1. Open an Excel file

  2. Click on the menu item **Data**

  3. Click on the sub-menu **From Other Sources**

  4. Click on the sub-menu **From Analysis Services**

  5. A dialog box appears for specification of logon data:

     a. Enter URL of the Data Warehouse into the field **Server Name**

     b. Select the option **Use the following user name and password**

     c. Enter your userid into the field **User Name**

     d. Enter your password into the field **Password**

     e. Click on **Finish**

  6. A box appears (**Select Database and Tables**) with the list of available cubes. Select one and click on **Finish**

  7. A box appears (**Save Data Connection File and Finish**).Check the box **Save passport in file** and click on **Finish**.

  8. A box appears (**Import Data**). Select whether cube should be accessed by a pivot table and / or chart and specify a placement of the pivot table. Click on **OK**.

  9. An area for the pivot table appears in the sheet with the **Pivot Table Field** area on the right (:ref:`image275`). Click on facts to be displayed and click or drag dimensions to appropriate sectors of the pivot table in the **Pivot Table Field** area.

    .. _image275:
    .. figure:: /img / user_manual / image240.png
       :align: center

       `Pivot Table in Excel`