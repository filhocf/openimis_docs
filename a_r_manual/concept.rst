Analytic and reporting user manual
==================================

  The Analytic and Reporting component of the Insurance Management Information System (AR-IMIS) provides managerial data for management of health insurance schemes supported by IMIS, allows easy and speedy analysis of these data with the objective to reveal causes of different phenomena encountered in supported health insurance schemes. Provided data allow also monitoring of developments within supported health insurance schemes and identification of potential errors in operational data.


Concept of AR-IMIS
^^^^^^^^^^^^^^^^^^

  The concept of AR-IMIS is based on populating of the Data Warehouse with aggregate data from the operational database of IMIS. This populating is done automatically and regularly (usually once a week) from the operational database by Extract, Transformation and Loading process (ETL). Within this process data from the operational database are aggregated and stored in the Data Warehouse in conformance with multidimensional data model (:ref:`image271`).

  .. _image271:
  .. figure:: /img / user_manual / image236.png
    :align: center

    `Concept of AR-IMIS`

  This model is suitable for analysis of data. Questions like “What is the number of newly covered insurees by an insurance product at during a calendar period and who were of an age, a gender, lived in a location and were cared for by a Enrolment officer? Data in the multidimensional Data Warehouse are presented by a suitable front-end tool. Currently AR-IMIS uses MS Excel as the front-end presentation tool. An Excel file is remotely connected to the Data Warehouse and data are stored in the Excel file in the form of so called pivot tables. The multidimensional model is based on the notion of facts and dimensions. The facts (indicators) are what we are interested in. For example, a fact may number of insured persons, number of active policies, number of submitted claims etc. Facts can be looked at from different angles-for example from the point of view of age and gender of insured persons, from the point of view of time period etc. These angles (points of view) are captured by the notion of dimensions that are used for qualification of facts (:ref:`image272`).

  .. _image272:
  .. figure:: /img / user_manual / image237.png
    :align: center

    `Facts and dimensions`

  A dimension is composed from points that represent specific values in the dimension for which we want to look at facts-for example *November* 2015 may be one point in the Time dimension. Points of a dimension may be organized in hierarchies. Higher levels of hierarchies represent more aggregate views. Going to the lower levels by so called *drill down* operation we can analyze facts in more detail-for example we may drill down from calendar years to quarters of corresponding calendar years and further to months. We can go in an opposite direction and look at facts from more aggregate points of view (*drill up*).For example from looking at the amount of collected contributions in calendar months we can look at the same indicator according to quarters of a year or according to calendar years.


  Facts with related meaning and the identical set of qualifying dimension are represented in the multidimensional model of the Data Warehouse as so called cubes. We can do other operations on cubes as for example *slicing* when we select one or several points in one dimension and look at the rest of cube or dicing when we select on or several points in two or more dimensions. All such operations allow analysis of data in the Data Warehouse in an easy and comprehensive way.
