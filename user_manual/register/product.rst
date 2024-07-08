Insurance Products
^^^^^^^^^^^^^^^^^^

The register of insurance products contains all insurance products in the health insurance scheme. There may be several insurance products available for distribution/selling in a territory, e.g. one basic product and one or several supplemental insurance products. The insurance products may at the different levels. For example that basic insurance product may be at the national level whereas the supplemental insurance products may be at the regional level. Administration of the register of insurance products is restricted to users with the system role of Scheme Administrator or with a role including an access to Administratiom/Products.

.. contents:: Table of Contents

Pre-conditions
===============

An insurance product may only be added or thereafter edited, after the approval of the management of the scheme administration.

Navigation
==========

All functionality for use with the administration of insurance products can be found under the main menu ``Administration``, sub menu ``Products``.

.. _image4:
.. figure:: /img/user_manual/image4.png
  :align: center

  `Navigation Products`

Product Control Page
====================

Clicking on the sub menu ``Products`` redirects the current user to the ``Product Control Page``.

.. _image5:
.. figure:: /img/user_manual/image5.png
  :align: center

  `Product Control Page`

The ``Product Control Page`` is the central point for administration of insurance products. By having access to this page, it is possible to add, edit, duplicate and search. The panel is divided into four panels. (:numref:`image5`)

Search Panel
------------

The search panel allows a user to select specific criteria to minimise the search results. In the case of Products the following search options are available, which can be used alone, or in combination with each other.

Product Code
  Type in the beginning of; or the full ``Product Code``; to search for products with a ``Product Code``, which starts with or matches completely, the typed text.

Product Name
  Type in the beginning of; or the full ``Product Name`` to search for products with a ``Product Name``, which starts with or matches completely, the typed text.

Date From
  Type in a date; or use the Date Selector Button, to search for products with a ``Date From``, which is on or is greater than the date typed/selected. *Note: To clear the date entry box; use the mouse to highlight the full date and then press the space key.*

Date To
  Type in a date; or use the Date Selector Button, to search for products with a ``Date To``, which is on or is greater than the date typed/selected. *Note: To clear the date entry box; use the mouse to highlight the full date and then press the space key.*

Region
  Select the ``Region`` from the list of regions by clicking on the arrow on the right of the selector to select products from a specific region.
  
  .. note::
    The list will only be filled with the regions assigned to the current logged in user and with the option National. All nationwide products and all regional products relating to the selected region will be found. If no district is selected then also all district products for districts belonging to the selected region will be found.

District
  Select the ``District`` from the list of districts by clicking on the arrow on the right of the selector to select products from a specific district. 

  .. note::
    The list will be only filled with the districts belonging to the selected region. All nationwide products, all regional products relating to the selected region and all district products for the selected district will be found.

Show Historical Values
  Click on ``Show Historical Values`` to see historical records matching the selected criteria. Historical records are displayed in the result in grey to clearly define them from current records (:numref:`image7`).

  .. _image7:
  .. figure:: /img/user_manual/image9.png
    :align: center

    `Historical records - Result Panel`

Search Button
  Once the criteria have been entered, use the search button to filter the records, the results will appear in the result panel.

Result Panel
------------

The result panel displays a list of all products found, matching the selected criteria in the search panel. The currently hovered record is highlighted in grey (:numref:`image8`). The leftmost record contains a hyperlink which if clicked, redirects the user to the actual record for detailed viewing if it is a historical record or editing if it is the current record.

.. _image8:
.. figure:: /img/user_manual/image10.png
  :align: center

  `Result Panel`

 
Information Panel
-----------------

The Information Panel is used to display messages back to the user. Messages will occur once a product has been added, updated or deleted or if there was an error at any time during the process of these actions.

Product Page
=============

Data Entry
-----------

.. _image10:
.. image:: /img/user_manual/image12.png
  :align: center

General
""""""""

Product Code
  Enter the product code for the product. Mandatory, 8 characters.

Product Name
  Enter product name for the product. Mandatory, 100 characters maximum.

Region
  Select the region in which the product will be used, from the list by clicking on the arrow on the right hand side of the lookup. The option National means that the insurance product is nationwide and it is not constraint to a specific region. 
  
  .. note::
    The list will only be filled with the regions assigned to the current logged in user.` Mandatory.

District
  Select the district in which the product will be used, from the list by clicking on the arrow on the right hand side of the lookup.
  
  .. note::
    The list will only be filled with the districts assigned to the selected region and assigned to the current logged in user.

Maximum of Members
  Enter the maximal number of members of a household/group for the product.

Threshold Members
  Enter the threshold number of members in product for which the lump sum is valid.

Insurance Period
  Enter duration of the period in months, in which a policy with the product will be valid. Mandatory.

Administration Period
  Enter duration of the administration period in months. The administration period is added to the enrolment date/renewal date for determination of the policy start date.

Recurrence
  Enter duration of the period in months after which registration fee/lump sum is applied again for a renewal. The period starts with the expiry date of the policy to be renewed.

Date From
  Type in the date to provide the date for which underwriting for the insurance product can be done from. ``Date From`` determines the earliest date from which underwriting can be done. Mandatory.

Date To
  Type in the date or use the Date Selector Button to provide the date until which underwriting can be done to. Mandatory.

Conversion
  Select from the list of products, a reference to the product which replaces the current product in case of renewal after the ``Date to``. 
  
  .. note::
    Selecting the current product will prevent the record from saving, and cause a message to be displayed in the Information Panel.

Account Code Remuneration
  Enter the account code of the insurance product used in the accounting software for remuneration of the product. 25 characters maximum.

Account Code Contribution
  Enter the account code of the insurance product used in the accounting software for paid contributions. 25 characters maximum.


Contribution Plan
""""""""""""""""""

.. figure:: /img/user_manual/products_contribution_tab.png
  :align: center

  `Contribution Plan Tab`

Lump Sum
  Enter the lump sum contribution (an amount paid irrespective of the number of members up to a threshold) to be paid by a household/group for the product. If the lump sum is zero no lump sum is applied irrespective of the threshold members. Decimal up to two digits.

Contribution Adult
  Enter the contribution to be paid for each adult (on top of the threshold number of members). Decimal up to two digits.

Contribution Child
  Enter the contribution to be paid for each child (on top of the threshold number of members). Decimal up to two digits.

Max Instalments
  Enter maximal number of instalments in which contributions for a policy may be paid. Mandatory.

Registration Lump Sum
  Enter the lump sum (for a household/group) for registration fee to be paid at the first enrolment of the household/group. Registration fee is not paid for renewals of policies.

Assembly Lump Sum
  Enter the lump sum (for a household/group) for additional assembly fee to be paid both at the first enrolment and renewals of policies.

Registration Fee
  Enter the registration fee per member of a household/group. If registration lump sum is non zero, registration fee is not considered. Registration fee is not paid for renewals of policies.

Assembly Fee
  Enter the assembly fee per member of a household/group. If assembly lump sum is non zero, assembly fee is not considered. Assembly fee is paid both at the first enrolment and renewals of policies.

Enrolment Discount percentage
  Enter the enrolment discount percentage for the insurance product. The discount percentage is applied on the total contributions calculated for a policy underwritten earlier than ``Enrolment disc. period`` months before the start date of the corresponding cycle.

Enrolment Discount Period
  Enter the enrolment discount period of the insurance product in months.

Renewal Discount Percentage
  Enter the renewal discount percentage for the insurance product. The discount percentage is applied on the total contributions calculated for a policy renewed earlier than ``renewal disc. period`` months before the start date of the corresponding cycle.

Renewal Discount Period
  Enter the renewal discount period of the insurance product in months.

Grace Period Payment
  Enter duration of the period in months, in which a policy has a grace period (not fully paid up) before it is suspended. Mandatory, although it is by default and can be left at zero.

Grace Period Enrolment
  Enter duration of the period in months after the starting date of a cycle (including this starting date), in which underwriting of a policy will still be associated with this cycle.

Grace Period Renewal
  Enter duration of the period in months after the starting date of a cycle (including this starting date), in which renewing of a policy will still be associated with this cycle.


Covered Medical Items
""""""""""""""""""""""

.. figure:: /img/user_manual/products_medical_items_tab.png
  :align: center

  `Medical Items Tab`

List all items covered in this product. You can add new items by clicking on ``+ Add Items``. To edit items, simply click on the pen icon at the start of each row, change the values and click on the floppy disk icon at the start of the row. Changes are only effective once the product is saved using the ``Save`` button at the bottom right of the screen.

Actions
  Using the pen you can edit the row to edit its values, the bin will remove this item from the product and the floppy disk will finish the edition of the row (But the product still need to be saved to apply changes).

Code
  Displays the code for the medical item

Name
  Displays the name of the medical item

Type
  Displays the type of the medical item

Package
  Displays the packaging of the medical item

Price
  Displays the default price of the medical item

Limit
  Indicates the type of limitation of coverage for the medical item. This may be adjusted per medical item, select between Co-Insurance and Fixed amount. Co-insurance means coverage of a specific percentage of the price of the medical item by policies of the insurance product. Fixed amount means coverage up the specified limit. Co-insurance is the default value. Limit O is used for claims having the type of visit Other, Limit R is used for claims having the type of visit Referral and Limit E is used for claims having the type of visit Emergency.

Origin
  Indicates where the price for remuneration of the item comes from. This may be adjusted per item, the options are: 
  
  * **Schema Price**: It takes the price from price list of a claiming health facility
  * **Provider Price**: It takes the price from the claim
  * **Relative Price** taken from a claim and relative price, the nominal value of which is taken from the price list and the actual value of which is determined backwards according to available funds and volume of claimed items and medical items in a period. [R] is the default value.

Adult
  Indicates the limitation for adults. If the type of limitation is a co-insurance then the value is the percentage of the price covered by policies of the insurance product for adults. If the type of limitation is a fixed limit the value is an amount up to which price of the item is covered for adults by policies of the insurance product. Default is 100%. Adult O is for Other, Adult R is for Referral and Adult E is for Emergency claims according to the type of visit (Visit Type).

Child
  Indicates the limitation for children. If the type of limitation is a co-insurance then the value is the percentage of the price covered for children by policies of the insurance product. If the type of limitation is a fixed limit the value is an amount up to which price of the item is covered for children by policies of the insurance product. Default is 100%. Child O is for Other, Child R is for Referral and Child E is for Emergency claims according to the type of visit (Visit Type).

No Adult
  It indicates the maximal number of provisions of the medical item during the insurance period for an adult.

No Child
  It indicates the maximal number of provisions of the medical item during the insurance period for an child.

Waiting Period Adult
  Indicates waiting period in months (after the effective date of a policy) for an adult.

Waiting Period Child
  Indicates waiting period in months (after the effective date of a policy) for a child.

Ceiling Adult
  It indicates whether the medical item is excluded from comparison against ceilings defined in the insurance product for adults. Default is that the medical item is not excluded from comparisons with ceilings. 
  
  * **Hospital** means exclusion only for provision of in-patient care
  * **Non-hospital** means exclusion only for out-patient care
  * **Both** means exclusion both for in-patient and out-patient care  

Ceiling Child
  It indicates whether the medical item is excluded from comparison against ceilings defined in the insurance product for children. Default is that the medical item is not excluded from comparisons with ceilings. 

  * **Hospital** means exclusion only for provision of in-patient care
  * **Non-hospital** means exclusion only for out-patient care
  * **Both** means exclusion both for in-patient and out-patient care

Covered Medical Services
""""""""""""""""""""""""

.. figure:: /img/user_manual/products_medical_services_tab.png
  :align: center

  `Medical Services Tab`


List all services covered in this product. You can add new services by clicking on ``+ Add Items``. To edit services, simply click on the pen icon at the start of each row, change the values and click on the floppy disk icon at the start of the row. Changes are only effective once the product is saved using the ``Save`` button at the bottom right of the screen.

Code
  Displays the code of the medical item

Name
  Displays the name of the medical item

Type
  Displays the type of the medical item (Curative or Preventive)

Package
  Displays the packaging of the medical Item

Price
  Displays the default price of the medical item

Limit
  Indicates the type of limitation of coverage for the medical service. This may be adjusted per medical service, select between Co-Insurance and Fixed amount. Co-insurance means coverage of a specific percentage of the price of the medical service by policies of the insurance product. Fixed amount means coverage up the specified limit. Co-insurance is the default value. Limit O is used for claims having the type of visit Other, Limit R is used for claims having the type of visit Referral and Limit E is used for claims having the type of visit Emergency.

Origin
  It indicates where the price for remuneration of the item, comes from: This may be adjusted per medical item, the options are: [P] Price taken from the price list of a claiming health facility, [O] Price taken from a claim and [R] Relative price, the nominal value of which is taken from the price list and the actual value of which is determined backwards according to available funds and the volume of claimed services and medical items in a period. [R] is the default value.

Adult
  It indicates the limitation for adults. If the type of limitation is a co-insurance then the value is the percentage of the price covered for adults by policies of the insurance product. If the type of limitation is a fixed limit the value is an amount up to which price of the item is covered for adults by policies of the insurance product. Default is 100%. Adult O is for Other, Adult R is for Referral and Adult E is for Emergency claims according to the type of visit (Visit Type).

Child
  It indicates the limitation for children. If the type of limitation is a co-insurance then the value is the percentage of the price covered for children by policies of the insurance product. If the type of limitation is a fixed limit the value is an amount up to which price of the service is covered for children by policies of the insurance product. Default is 100%. Child O is for Other, Child R is for Referral and Child E is for Emergency claims according to the type of visit (Visit Type).

No Adult
  It indicates the maximal number of provisions of the medical item during the insurance period for an adult.

No Child
  It indicates the maximal number of provisions of the medical item during the insurance period for a child.

Waiting Period Adult
  It indicates waiting period in months (after the effective date of a policy) for an adult.

Waiting Period Child
  It indicates waiting period in months (after effective date of a policy) for a child.

Ceiling Adult
  It indicates whether the medical service is excluded from comparison against ceilings defined in the insurance product for adults. Default is that the medical service is not excluded from comparisons with ceilings. 
  
  * **Hospital** means exclusion only for provision of in-patient care
  * **Non-hospital** means exclusion only for out-patient care
  * **Both** means exclusion both for in-patient and out-patient care  

Ceiling Child
  It indicates whether the medical service is excluded from comparison against ceilings defined in the insurance product for children. Default is that the medical service is not excluded from comparisons with ceilings. 

  * **Hospital** means exclusion only for provision of in-patient care
  * **Non-hospital** means exclusion only for out-patient care
  * **Both** means exclusion both for in-patient and out-patient care

Deductibles and Ceilings
""""""""""""""""""""""""

.. figure:: /img/user_manual/products_deductibles_tab.png
  :align: center

  `Deductibles & Ceilings Tab`

.. note::
    It is possible to specify only one of the following ceilings –per Treatment, per Insuree or per Policy. If ceilings per category of claims are specified together with ceilings per Treatment, per Insuree or per Policy than evaluation of claims may be dependent under special circumstances on the order of claimed medical services/items in a claim.`

Ceiling Discrimination
  Specify whether Hospital and Non-Hospital care should be determined according to the type of health facility (select ``Based on Health Facility Type``) that provided health care or according to the type of health care (select ``Based on Claim Type``) acquired from a claim. In the first case all health care provided in hospitals (defined in the field ``HF Level`` in the register of Health Facilities) is accounted for ``Hospital Ceilings/Deductibles`` and for calculation of relative prices for the ``Hospital`` part. It means that if claimed health care was provided out-patient in a hospital, it is considered for calculation of ceilings/deductibles and for calculation of relative prices as hospital care. In the second case only in-patient care (determined from a claim when a patient spent at least one night in a health facility) is accounted for ``Hospital Ceilings/Deductibles`` and for calculation of relative prices for hospital part. Other health care including out-patient care provided in hospitals is accounted for ``Non hospital Ceilings/Deductibles`` and also such health care is used for calculation of relative prices for non-hospital part. Mandatory

Split Ceilings & Deductibles
  Wether you would like to split ceilings & deductibles for Hospitals/Non-Hospitals or not.

Ceiling Type
  Specify wether the deductibles and ceilings are per insuree, treatment or policy.

  Treatment
    Deductibles and Ceilings for treatments may be entered for general care (``Hospitals and Non-hospitals``) or for hospital care (``Hospitals``) only and/or for non-hospital care (``Non-Hospitals``) only. An amount may be set, indicating the value that a patient should cover within his/her own means, before a policy of the insurance product comes into effect (``Deductibles``) or the ceiling (maximum amount covered) within a policy of the insurance product (``Ceilings``) for a treatment (the treatment is identified health care claimed in one claim)

  Insuree
    Deductibles and Ceilings for an insuree may be entered for general care (``Hospitals and Non-hospitals``) or for hospital care (Hospitals) only and/or for non-hospital care (``Non-Hospitals``) only. An amount may be set, indicating the value that an insuree should cover within his/her own means, before a policy of the insurance product comes into effect (``Deductibles``) or the ceiling (maximum amount covered) within a policy of the insurance product (``Ceilings``) for an insuree for the whole insurance period.

  Policy
    Deductibles and Ceilings for a policy may be entered for general care (``Hospitals and Non-hospitals``) or for hospital care (``Hospitals``) only and/or for non-hospital care (Non-Hospitals) only. An amount may be set, indicating the value that policyholders should cover within their own means, before a policy of the insurance product comes into effect (``Deductibles``) or the ceiling (maximum amount covered) for the policy (all members of a family/group) of the insurance product (``Ceilings``) for the whole insurance period.

Extra Member Ceiling
  Additional (extra) ceiling for a policy may be entered for general care (``Hospitals`` and ``Non-hospitals``) or for hospital care (``Hospitals``) only and/or for non-hospital care (``Non-Hospital`` s ) only per a member of a family/group above ``Threshold Members``.

Maximum Ceiling
  Maximal ceiling for a policy may be entered for general care (``Hospitals`` and ``Non-hospitals``) or for hospital care (``Hospitals``) only and/or for non-hospital care (``Non-Hospitals``) only if extra ceilings are applied for members of a family/group above ``Threshold Members``.


Ceilings Table
  Maximal amount of coverage can be specified for claims according to the category of a claim. The options are claims of the category ``Consultations``, ``Surgery``, ``Delivery``, ``Antenatal care``, ``Hospitalizations``, and ``Visits``. The category of claim is determined according to the procedure described with ``Number``.


Number
  Maximal number of covered claims per an insuree during the whole insurance period according to the category of a claim. The options are claims of the category ``Consultations``, ``Surgery``, ``Delivery`` and ``Antenatal care``. Maximal numbers may be also specified for Hospitalizations (in-patient stays) and (out-patient visits) ``Visits``. The claim category is determined as follows:

  .. note::
    +-----------------------------------------------------------------------+
    | If at least one service of the category *Surgery* is given in the     |
    | claim it is of category *Surgery*                                     |
    |                                                                       |
    | otherwise                                                             |
    |                                                                       |
    | if at least one service of the category *Delivery* is given in the    |
    | claim it is of category *Delivery*                                    |
    |                                                                       |
    | otherwise                                                             |
    |                                                                       |
    | if at least one service of the category *Antenatal care* is given in  |
    | the claim it is of category *Antenatal care*                          |
    |                                                                       |
    | otherwise                                                             |
    |                                                                       |
    | if the claim is a hospital one the claim it is of category            |
    | *Hospitalization*                                                     |
    |                                                                       |
    | otherwise                                                             |
    |                                                                       |
    | if at least one service of the category *Consultation* is given in    |
    | the claim it is of category *Consultation*                            |
    |                                                                       |
    | otherwise                                                             |
    |                                                                       |
    | the claim is of the category *Visit*                                  |
    +-----------------------------------------------------------------------+

.. _product_distribution:

Pooling Management
""""""""""""""""""

Start Cycles (1 to 4)
  If one or more starting dates (a day and a month) of a cycle are specified then the insurance product is considered as the insurance product with fixed enrolment dates. In this case, activation of underwritten and renewed policies is accomplished always on fixed dates during a year. Maximum four cycle dates can be specified.

Distribution Type
  Wether the system has to calculate relative prices for general health care (**Enabled**) or for (non-)hospital care (**Split**). This system is disabled if the user selects **Disabled**.

Distribution Periods
  Select from the list of distribution periods (**NONE, Monthly, Quarterly, Yearly**), the period that is to be used for calculation of the actual value of relative prices for the insurance product.

Relative Pricing Table
  Distribution periods may be entered for general care (``Hospitals`` and ``Non-hospitals``), or for hospital care (``Hospitals``) only and/or for non-hospital care (``Non-Hospitals``) only. Percentages should be entered to indicate the distribution over the periods as per the product description. Enter to each field an appropriate percentage of paid contributions for policies of the insurance product allocated proportionally to corresponding calendar period. It means, for example, that in case of the distribution **Monthly** we put in each slot percentage of paid contributions of the insurance product that are allocated to the corresponding month and that is to be used for calculation of relative prices.

  It is not required to enter a value in each period, zero values are accepted. Once all the percentage values have been entered, click on the button OK to submit the values to the respective grid. Clicking on the button ``Cancel`` will cancel the action closing the popup and cancelling the change in the distribution.

Saving
------

Once all mandatory data is entered, clicking on the ``Save`` button will save the record. The user will be re-directed back to the `Product Control Page <#product-control-page>`__, with the newly saved record displayed and selected in the result panel. A message confirming that the product has been saved will appear on the Information Panel.

**Mandatory data**

  If mandatory data is not entered at the time the user clicks the ``Save`` button, a message will appear in the Information Panel, and the data field will take the focus (by an asterisk on the right of the corresponding data field).

**Cancel**

  By clicking on the ``Cancel`` button, the user will be re-directed to the `Product Control Page <#product-control-page>`__.

Adding a Product
================

Click on the ``Add`` button to re-direct to the `Product Page <#claim-administrators-administration>`__\ .

When the page opens all entry fields are empty. See the `Product Page <#claim-administrators-administration>`__ information on the data entry and mandatory fields.

Editing a Product
=================

Click on the ``Edit`` button to re-direct to the `ProductPage <#claim-administrators-administration>`__\ .

The page will open with the current information loaded into the data entry fields. See the `Product Page <#claim-administrators-administration>`__ for information on the data entry and mandatory fields

Deleting a Product
==================

Because of potential problems with synchronization of data between off-line and on-line version, it is not possible delete insurance products currently.
