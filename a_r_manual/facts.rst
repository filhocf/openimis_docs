Facts
^^^^^

Facts provided by AR-IMIS can be structured into the areas according to (:numref:`image273`). Within each area several facts packed into one or several cubes are provided. Facts are packed into the same cube if they have an associated meaning and are provided with the same set of dimension. The following articles lists available cubes according to the areas, for each cube indicates available facts with description of their meaning

.. figure:: /img / user_manual / image238.png
  :align: center
  :name: image273

  `Areas of facts`

underlying set of qualifying dimensions. If meaning of a dimension is not straightforward, its description is provided. It relates especially to the *Time* dimension where it is important which datum related with a fact is taken as the governing date for association with given point (period) in the *Time* dimension.

Facts on Enrolment and policies
"""""""""""""""""""""""""""""""

  This group of facts relates to acquisition of insures and development of coverage by health insurance schemes. Facts available are listed in :numref:`facts_enrolment_policies`

  .. list-table:: `Facts on Enrolment and policies`
      :widths: 2 2 4 2 4
      :header-rows: 1
      :stub-columns: 1
      :class: longtable
      :name: facts_enrolment_policies

      * - **Cube**
        - **Fact**
        - **Meaning**
        - **Dimension**
        - **Comment**

      * - Population
        - Population
        - Number of inhabitants
        - Gender
        -

      * -
        -
        -
        - Region
        -

      * -
        -
        -
        - Time
        -

      * - Number of families / groups
        - Number of families / groups
        - Number of households according to a census
        - Region
        -

      * -
        -
        -
        - Time
        -

      * - Current and new insurees
        - Current insurees
        - Insurees covered by at least one policy active at the end of a time period
        - Age
        - Age at the end of a time period

      * -
        -
        -
        - Gender
        -

      * -
        -
        -
        - Enrolment Officers
        - An enrolment officer responsible for corresponding policy

      * -
        - New acquired insurees
        - Insurees newly insured during a time period
        - Region
        - Place of living of a household

      * -
        -
        -
        - Products
        - An insurance product covering an insuree

      * -
        -
        -
        - Time
        - Period of enrolment of insurees for new insurees Period of effective day and later of their policies for current insurees

      * - All types of policies
        - Current policies
        - Number of active policies at the end of a time period
        - Age
        - Age of the head of a household at the end of a time period

      * -
        - Expired policies
        - Number of policies that expired during a time period
        - Gender
        - Gender of the head of a household

      * -
        - Renewed policies
        - Number of policies that were renewed during a time period
        - Enrolment Officers
        - An enrolment officer responsible for corresponding policy

      * -
        - Sold policies
        - Number of policies that were sold during a time period
        - Region
        - Place of living of a household

      * -
        -
        -
        - Products
        - An insurance product of a policy

      * -
        -
        -
        - Time
        - Period of enrolment date for sold policies Period of expiry date for expired policies Period of renewal date(when renewing was done)  for renewed policies Period of effective day and later for current policies

      * - Share of insured population
        - Share of insured population
        - Current insures /  Population at the end of a time period
        - Gender
        -

      * -
        -
        -
        - Region
        - Place of living of a household

      * -
        -
        -
        - Products
        - An insurance product covering an insuree

      * -
        -
        -
        - Time
        -

      * - Share of insured families / groups
        - Number of insured families / groups
        - Number of households that are covered by at least one active policy at the end of a time period
        - Region
        - Place of living of a household

      * -
        -
        -
        - Time
        -

      * -
        - Share of insured families / groups
        - =Number of insured households / Number of households at the end of a time period
        - Region
        - Place of living of a household

      * -
        -
        -
        - Time
        -


Facts on collected revenue
""""""""""""""""""""""""""

  This group of facts relates to revenue of health insurance schemes. Facts available are listed in :numref:`fact_contribution` .

  .. list-table:: `Facts on contributions`
    :name: fact_contribution
    :widths: 2 2 4 2 4
    :header-rows: 1
    :stub-columns: 1
    :class: longtable

    * - **Cube**
      - **Fact**
      - **Meaning**
      - **Dimension**
      - **Comment**

    * - Contribution collection
      - Contribution collected
      - contributions collected in given time period
      - Enrolment Officers
      - Collection of contributions from policies of an enrolment officer

    * -
      -
      -
      - Payers
      - Collection of contributions from an institution al payer or from families itself

    * -
      -
      -
      - Products
      - Collection of contributions within an insurance product

    * -
      -
      -
      - Time
      - Period of payment date of contributions

    * - Contribution allocation
      - Contribution allocated
      - Amount of collected contributions allocated proportionally for using in a time period
      - Products
      - Allocation of contributions within an insurance product

    * -
      -
      -
      - Time
      - Period of allocation of contributions


Facts on claims
"""""""""""""""

  This group of facts relates to claims forwarded by health care providers to administrators of health insurance schemes. Facts available are listed in :numref:`facts_claims`

  .. list-table:: `Facts on claims`
    :name: facts_claims
    :widths: 2 2 4 2 4
    :header-rows: 1
    :stub-columns: 1
    :class: longtable

    * - **Cube**
      - **Fact**
      - **Meaning**
      - **Dimension**
      - **Comment**

    * - Claim details
      - Amount claimed
      - Total amount in nominal prices that was submitted by health care providers for health care provided in given period
      - Providers
      - Providers that entered and or submitted claims

    * -
      - Amount rejected
      - Total amount that was on totally rejected claims
      - Time
      - Time period of provision of health care that was invoiced in claims

    * -
      - Entered claims
      - Number of claims entered
      -
      -

    * -
      - Submitted claims
      - Number of claims submitted
      -
      -

    * -
      - Rejected claims
      - Number of claims totally rejected
      -
      -

    * -
      - Average amount claimed
      - =Amount claimed / Submitted claims
      -
      -

    * -
      - Average amount rejected
      - =Amount rejected / Rejected claims
      -
      -

    * - Claim details products
      - Amount adjusted
      - Amount adjusted after processing in nominal prices
      - Providers
      - Providers that submitted claims

    * -
      - Amount paid
      - Amount actually to be paid to health facilities taking into account indexes of relative pricing
      - Products
      - Products by which health care claimed was covered

    * -
      - Processed claims
      - Number of claims sent for valuation
      - Time
      - Time period of provision of health care that was invoiced in claims

    * -
      - Paid claims
      - Number of claims actually valuated
      -
      -

    * -
      - Average amount adjusted
      - =Amount adjusted / Pr ocessed claims
      -
      -

    * -
      - Average amount paid
      - =Amount paid/ Valuated claims
      -
      -


Facts on utilization of health care
"""""""""""""""""""""""""""""""""""

  This group of facts relates to utilization of health care by insures according to submitted and not rejected claims. Facts available are listed in :numref:`facts-on-of-utilization-health-care`


.. list-table:: `Facts on of utilization health care`
    :name: facts-on-of-utilization-health-care
    :widths: 2 2 4 2 4
    :header-rows: 1
    :stub-columns: 1
    :class: longtable

    * - **Cube**
      - **Fact**
      - **Meaning**
      - **Dimension**
      - **Comment**

    * - Admissions and visits and hospital days
      - Number of hospital admissions
      - Number of hospital admissions
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      - Number of hospital days
      -
      - Care category
      -

    * -
      - Average length of stay
      - = Number of hospital days / Number of hospital admissions
      - Products
      - In case two or more insurance products covered a hospital admission / visit, it is accounted to each of them

    * -
      - Number of out-patient visits
      -
      - Providers
      - Providers which claimed health care

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - Utilization of services
      - Services utilized
      - | Number of utilized services according to submitted claims.
        | If a service was provided during one visit / hospital stay, the service is counted according to the number of its provision
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Care category
      -

    * -
      -
      -
      - Care type
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Providers
      - Providers which claimed health care

    * -
      -
      -
      - Services
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - Utilization of medical items
      - Items utilized
      - | Number of utilized medical items according to submitted claims
        | If a medical item was provided during one visit / hospital stay, the medical item is counted according to the number of its provision
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Care category
      -

    * -
      -
      -
      - Care type
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Providers
      - Providers which claimed health care

    * -
      -
      -
      - Items
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - Average utilization of services per insuree
      - Average utilization of services per insuree
      - = Services utilized / Current insurees
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Services
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - Average utilization of medical items per insuree
      - Average utilization of medical items per insuree
      - = Items utilized / Current insurees
      - Age
      -

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Items
      -

    * -
      -
      -
      - Time
      -

Facts on expenditures for health care
"""""""""""""""""""""""""""""""""""""

  This group of facts relates to expenditures for health care actually paid to health care providers. Facts available are listed in :numref:`facts_expenditures_health_care`

 .. list-table:: `Facts on expenditures for health care`
    :name: facts_expenditures_health_care
    :widths: 2 2 4 2 4
    :header-rows: 1
    :stub-columns: 1
    :class: longtable

    * - **Cube**
      - **Fact**
      - **Meaning**
      - **Dimension**
      - **Comment**

    * - expenditures for services
      - Service expenditures
      - Expenditures for services actually remunerated to health facilities
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Care category
      -

    * -
      -
      -
      - Care type
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Providers
      - Providers which claimed health care

    * -
      -
      -
      - Services
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - expenditures for medical items
      - Item expenditures
      - expenditures for medical items actually remunerated to health facilities
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Care category
      -

    * -
      -
      -
      - Care type
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Providers
      - Providers which claimed health care

    * -
      -
      -
      - Items
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - Average expenditures for services per insuree
      - Average expenditures for services per insuree
      - = Service expenditures/ Current insurees
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Services
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - Average expenditures for medical items per insuree
      - Average expenditures for medical items per insuree
      - = Item expenditures/ Number of inhabitants
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Items
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

    * - Average expenditures for health care per insuree
      - Average expenditures per insuree
      - = Average expenditures of services per insuree + Average expenditures for medical items per insuree
      - Age
      - Age at the time of provision health care

    * -
      -
      -
      - Gender
      -

    * -
      -
      -
      - Disease
      -

    * -
      -
      -
      - Products
      -

    * -
      -
      -
      - Time
      - Hospital admissions are associated with time periods according to dates of discharge. Time period of provision of health care

Facts on feedbacks
""""""""""""""""""

  This group of facts relates to evaluation of request for feedbacks on provided health care that are issued by medical officers during processing of claims. Facts available are listed in :numref:`fact_feedback`

  .. list-table:: `Facts on feedbacks`
    :name: fact_feedback
    :widths: 2 2 4 2 4
    :header-rows: 1
    :stub-columns: 1
    :class: longtable

    * - **Cube**
      - **Fact**
      - **Meaning**
      - **Dimension**
      - **Comment**

    * - Feedback details
      - Feedbacks sent
      - Number of requests for feedbacks sent in a time period
      - Products
      - Insurance products that covered claims initiating requests for feedbacks

    * -
      - Feedbacks responded
      - Number of feedbacks received in a time period
      - Providers
      - Providers that submitted claims initiating requests for feedbacks

    * -
      - Overall assessment
      - Sum of all assessment overall assessment marks in responded feedbacks
      - Time
      - Period of sending / rec eiving feedbacks

    * -
      - Feedback return share
      - = Feedbacks responded/ Feedbacks sent
      -
      -

    * -
      - Average overall assessment
      - = Overall assessment/ Feedbacks responded
      -
      -

    * - Feedback answers
      - Answers Yes
      - Count of all Yes answers
      - Products
      - Insurance products that covered claims initiating requests for feedbacks

    * -
      - Share of Answers Yes
      - = Answers Yes/ Feedbacks responded
      - Providers
      - Providers that submitted claims initiating requests for feedbacks

    * -
      -
      -
      - Questions
      -

    * -
      -
      -
      - Time
      - Period of sending / receiving feedbacks
