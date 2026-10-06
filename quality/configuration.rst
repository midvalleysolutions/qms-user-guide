=============
Configuration
=============

This page explains how to install the **Quality** app and its add-ons, the order in which to set them up, and every
setting with its default value.

Install the app
===============

#. Go to the **Apps** app.
#. Search for *Quality Management System* and click :guilabel:`Activate` on *Quality Management System — Core*.

The **Quality** menu appears in the main menu. The app needs nothing but a standard Odoo Community database: no
Enterprise module and no connection to any outside service.

At installation:

- the administrator becomes a quality manager;
- ISO 9001 is enabled, and the four other standards are installed but disabled (see :doc:`clauses`);
- the settings take the default values listed below;
- the free source modules install themselves for the apps already present (Inventory, Manufacturing, Purchase,
  Repairs), and later for any of these apps you install afterwards. See :doc:`sources`.

.. note::
   The app is available in English, French, German, Spanish and Vietnamese. Add the language in the Settings app
   and choose it in the user's preferences.

Install QMS Advanced and the add-ons
------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 28 32 40

   * - Module
     - Needs
     - How it is installed
   * - **QMS Advanced**
     - The free core
     - Bought and installed from the Apps store.
   * - **Training & Competence** (free with QMS Advanced)
     - QMS Advanced and Employees
     - Installed separately, on purpose: search for it in **Apps**. Once installed, an audit whose lead auditor is not
       qualified cannot start: record the auditor qualifications first. See :doc:`competence`.
   * - **Supplier evaluation** (free with QMS Advanced)
     - QMS Advanced and Purchase
     - Installed separately, on purpose. From installation, every supplier is Unapproved: set the purchase confirmation
       control to Off while you build the approved supplier list. See :doc:`suppliers`.
   * - Supplier receipt measures
     - Supplier evaluation and Inventory
     - Installs itself when both are installed. See :doc:`suppliers`.
   * - Portal document readers
     - QMS Advanced and Portal
     - Installs itself when both are installed. See :ref:`documents-portal-readers`.

First-time setup
================

Follow this order the first time:

#. **Give people their roles.** Go to :menuselection:`Settings --> Users & Companies --> Users`, open each user and
   set their **Quality** role: :guilabel:`User` for people who raise and treat nonconformities,
   :guilabel:`Internal auditor` for people who must read every nonconformity, :guilabel:`Manager` for people who
   close, cancel, amend and configure. See :doc:`roles`.
#. **Enable your standards** in :menuselection:`Settings --> Quality`: add ISO 14001, 45001, 13485 or 22000 if your
   management system covers them. See :doc:`clauses`.
#. **Check the nonconformity settings**: days to treat, owner reminder, fallback owner and dashboard age buckets (see
   below).
#. **Decide on the password check** for signatures. Leave it on unless your users sign in through single sign-on.
#. **Declare the clauses that do not apply to you**, with their justification. See :ref:`clauses-not-applicable`.
#. **Record or raise your first nonconformity.** See :doc:`nonconformities`.

With **QMS Advanced**, continue with: the process register and the importance of each process (:doc:`audits`), the
top management and the quality policy (:doc:`documents`), the context and the signed scope (:doc:`context`), the risk
register (:doc:`risks`), the objectives (:doc:`objectives`), the equipment register (:doc:`calibration`) and the
retention periods (:ref:`documents-retention`). For ISO 14001 or ISO 45001, switch on the environment, health and safety
registers and set them up in the order of :doc:`ehs_setup`: legal requirements first, then emergency situations,
monitoring indicators, aspects or hazards.

Settings
========

Go to :menuselection:`Settings --> Quality`. The section is visible to quality managers only.

.. image:: ../_images/settings-quality.png
   :alt: The Standards block of the Quality settings with the enabled standards and the ISO 14001 and ISO 45001
         register boxes, and the start of the Environment, health and safety block.

.. important::
   Odoo opens the Settings app only to users with the *Administration: Settings* right. A quality manager without
   that right cannot change these settings: ask your administrator.

Every value is checked when you click :guilabel:`Save`; a wrong value is refused with a message, and nothing is
saved.

.. _config-setup-profile:

Setup profile
-------------

:guilabel:`Setup profile`
   Sets a group of settings in one go: :guilabel:`Lean (small team)`, :guilabel:`Standard (defaults)` or
   :guilabel:`Regulated`. It reads :guilabel:`Custom` when the settings differ from every profile. The values of each
   profile, and the settings that matter most for a small team, are on :doc:`small_company_setup`.

   - Default: Standard.

Standards
---------

.. _config-standards:

:guilabel:`Enabled standards`
   The standards whose clauses can be tagged on quality records.

   - Default: ISO 9001.
   - Allowed: any of the installed standards; at least one must stay enabled. Saving with none is refused with
     *At least one standard must be enabled.*
   - Disabling a standard hides its clauses from the pickers; records already tagged keep their tags.
   - Example: add *ISO 45001 — Occupational health and safety* to tag health and safety events with ISO 45001
     clauses.
   - A standard whose environment, health and safety registers are switched on cannot be disabled: *Turn off the ISO
     14001 environmental registers first.* See :doc:`ehs_setup`.

:guilabel:`ISO 14001 environmental registers` and :guilabel:`ISO 45001 health & safety registers`
   With **QMS Advanced**: show the environment, health and safety registers of that standard, and enable the standard.
   Switching a box off hides the registers; nothing is deleted.

   - Default: both off (on with demo data).
   - See :doc:`ehs_setup`.

Nonconformities
---------------

.. _config-days-to-treat:

:guilabel:`Days to treat`
   The due date proposed for a new nonconformity: its detection date plus this many days. It is used only when the
   due date is left empty; you can always change the due date on the record or in the :guilabel:`Accept` dialog.

   - Default: 30.
   - Allowed: 0 or more. 0 means the same day as detection.
   - Example: with 14, a nonconformity detected on 3 March is due on 17 March.

.. _config-owner-reminder:

:guilabel:`Owner reminder`
   When a nonconformity is accepted, its owner receives a *Nonconformity to treat* activity. This setting is how many
   days before the nonconformity's due date that activity falls due.

   - Default: 3.
   - Allowed: 0 or more. 0 makes the activity due on the due date itself.
   - Example: with 5, a nonconformity due on 20 March gives the owner an activity due on 15 March.

.. _config-fallback-owner:

:guilabel:`Fallback owner`
   The user who receives the overdue reminder of a nonconformity whose owner has been deactivated, for example
   someone who left the company.

   - Default: empty. The reminder then goes to the first active quality manager of the nonconformity's company.
   - Allowed: any internal user.
   - Example: set it to your quality coordinator so that orphaned nonconformities land on one desk.

.. _config-concession:

:guilabel:`Concessions need the customer's approval`
   When ticked, a repair or use-as-is disposition can be authorised only once the reference of the customer's written
   approval is recorded on its line, for example ``DEV-2026-114``. See :ref:`nc-disposition`.

   - Default: unticked.
   - Refusal when the reference is missing: *Record the customer's approval reference for this concession.*

.. _config-age-buckets:

:guilabel:`Dashboard age buckets`
   How the :guilabel:`Open nonconformities by age` tile of the :doc:`dashboard` splits open nonconformities by the
   number of days since detection. Enter the upper limit of each bucket, in days, separated by commas; a last bucket
   collects everything older.

   - Default: ``30,60,90``, which gives 0-30, 31-60, 61-90 and over 90 days.
   - Allowed: whole numbers above zero, each larger than the one before. ``30,30,90`` or ``90,60`` are refused with
     *Age buckets must be a strictly increasing list of positive day counts, e.g. 30,60,90.*
   - Example: ``7,14,30`` gives 0-7, 8-14, 15-30 and over 30 days.

Integrity
---------

.. _config-password:

:guilabel:`Ask the password before signing`
   When ticked, every signature — closing a nonconformity, amending a closed record and, with **QMS Advanced**, the other
   signed decisions — asks the signer for their own password first. See :doc:`trail`.

   - Default: ticked.
   - Untick it only on installations where users sign in through single sign-on and have no Odoo password.
   - Every change of this setting is recorded in the trail, with who changed it and when, and appears in the
     :menuselection:`Quality --> Evidence --> Trail export` of that period.

.. _config-trail-pdf-limit:

:guilabel:`Trail PDF row limit`
   The largest number of rows a trail PDF may contain. A larger export is refused as a PDF; use the CSV export,
   which has no limit, or a shorter period.

   - Default: 5000.
   - Allowed: 100 or more.
   - Example: raise it to 20000 if your auditor wants a whole year of trail on paper and your server copes with it.

Settings of QMS Advanced
------------------------

With **QMS Advanced** installed, the same page shows more blocks. A value outside its limits is refused when you click
:guilabel:`Save`, and nothing is saved.

.. list-table::
   :header-rows: 1
   :widths: 18 32 12 38

   * - Block
     - Setting
     - Default
     - What it does
   * - :guilabel:`Corrective actions`
     - :guilabel:`Effectiveness gap`, :guilabel:`Reminder interval`, :guilabel:`Recurrence window`,
       :guilabel:`Corrective action required for`
     - 30, 7, 180, ``major,critical``
     - See :doc:`corrective_actions`.
   * - :guilabel:`Documents`
     - :guilabel:`Review period`
     - 12
     - Months between periodic reviews, proposed for a new document type. See :doc:`documents`.
   * -
     - :guilabel:`Acknowledgement grace`
     - 14
     - Days a reader has to confirm a new version.
   * -
     - :guilabel:`External documents`
     - 12
     - Months between two checks for a new edition of an external document; 0 sends no reminder.
   * -
     - :guilabel:`Top management`
     - Empty
     - Who approves the quality policy of this company, with their password; they need no Quality role.
       :guilabel:`Top management history` lists the changes.
   * -
     - :guilabel:`Controlled-copy stamp`
     - CONTROLLED COPY
     - Stamped on every page of a printed version in force; cannot be empty.
   * - :guilabel:`Retention`
     - :guilabel:`Default retention`
     - 5
     - Years a record is kept once it stops being live when its type has no period of its own; 0 keeps it
       indefinitely. Nothing is deleted automatically. :guilabel:`Record retention` opens the periods per record
       type. See :ref:`documents-retention`.
   * - :guilabel:`Management review`
     - :guilabel:`Review interval`, :guilabel:`Review reminder`
     - 12, 30
     - See :doc:`management_reviews`.
   * - :guilabel:`Context`
     - :guilabel:`Issue review interval`
     - 12
     - Default months between two reviews of a new context issue, at least 1. See :doc:`context`.
   * -
     - :guilabel:`Review reminder`
     - 14
     - Days before a review date when the issue owner gets a to-do.
   * - :guilabel:`Risks`
     - :guilabel:`Level thresholds`: :guilabel:`Medium from score`, :guilabel:`High from score`, :guilabel:`Critical
       from score`
     - 5, 10, 15
     - Lowest score of each level, from 2 to 25, increasing. See :doc:`risks`.
   * -
     - :guilabel:`Review intervals`: a low, medium, high and critical risk every (months)
     - 12, 12, 6, 3
     - Months after the last assessment when a risk is due for review; 0: no periodic review.
   * -
     - :guilabel:`Risk review reminder`
     - 14
     - Days before a risk's review date when its owner gets a to-do.
   * - :guilabel:`Objectives`
     - :guilabel:`Measurement reminder`
     - 5
     - Days after a measurement was due when the owner gets a to-do. See :doc:`objectives`.
   * -
     - :guilabel:`Communication`
     - 14
     - Days after activation before an objective never communicated is listed as not communicated.
   * - :guilabel:`Changes`
     - :guilabel:`Effectiveness review`
     - 60
     - Days from the planned implementation date to the proposed effectiveness review date of a new change; at least
       1. Existing changes keep their date. See :doc:`change_register`.
   * - :guilabel:`Customer satisfaction`
     - :guilabel:`Deterioration threshold`
     - 5
     - Percentage points of drop since the previous result that expect an action; 0 flags every drop. See
       :doc:`satisfaction`.
   * - :guilabel:`Calibration`
     - :guilabel:`Due soon window`
     - 30
     - Days before its due date when an instrument shows Due soon and its responsible is reminded; 0: only on the due
       day. See :doc:`calibration`.
   * - :guilabel:`Audit programme proposal`
     - :guilabel:`Base interval by importance`: high, medium, low
     - 6, 12, 24
     - Months between two audits of a process before the factors apply. See :ref:`audits-importance`.
   * -
     - :guilabel:`Factors`: major finding, minor finding, change, nonconformity; nonconformities that shorten
     - 0.5, 0.75, 0.75, 0.75; 3
     - Each factor multiplies the base interval when its condition holds, above 0 and at most 1.
   * -
     - :guilabel:`Interval bounds`: shortest, longest interval
     - 3, 36
     - The proposed interval is kept between these months after rounding.
   * - :guilabel:`Audit pack`
     - :guilabel:`Longest period`, :guilabel:`Time cap`, :guilabel:`NC log rows per file`
     - 24, 600, 5000
     - See :doc:`audit_pack`.
   * - :guilabel:`Environment, health and safety` (shown while an ISO 14001 or ISO 45001 box is ticked)
     - :guilabel:`Legal requirements`, :guilabel:`Emergency preparedness`, :guilabel:`Monitoring`,
       :guilabel:`Incidents`, :guilabel:`Environmental aspects`, :guilabel:`Hazards (uses the risk thresholds)`,
       :guilabel:`Worker consultation`
     - See :doc:`ehs_setup`
     - Every key with its Lean, Standard and Regulated value is in the table of :doc:`ehs_setup`.

.. _config-context:
.. _config-risks:
.. _config-objectives:
.. _config-satisfaction:
.. _config-calibration:
.. _config-audit-proposal:

The labels above are those of the settings page. Each setting is explained with its feature on the page linked in the
table. Refusals you may meet when saving: *Thresholds must increase: medium < high < critical.*, *The audit proposal
factors must be above 0 and at most 1.*, *The base audit intervals must be above 0 months.*, *The shortest audit
interval must be at least 1 month and not above the longest.*, *The nonconformity threshold must be at least 1.*, *The
deterioration threshold cannot be negative.*, *The controlled-copy stamp cannot be empty.*, *Turn off the ISO 14001
environmental registers first.*, *Turn off the ISO 45001 health & safety registers first.*, and *<setting> must be at
least <n>.* or *<setting> must be at most <n>.* for a value out of its limits.

.. _config-training:

Settings of the Training & Competence add-on
--------------------------------------------

Block :guilabel:`Training & competence`:

.. list-table::
   :header-rows: 1
   :widths: 30 12 58

   * - Setting
     - Default
     - What it does
   * - :guilabel:`Training effectiveness`
     - 90
     - Days after a training when each attendee's manager evaluates it.
   * - :guilabel:`Expiry warning`
     - 60
     - Days before a required qualification expires when the manager is reminded; 0: none.
   * - :guilabel:`Internal auditor levels`: :guilabel:`Level to audit`, :guilabel:`Level to lead an audit`
     - 2, 3
     - Levels of the internal auditor qualification needed to audit as a co-auditor and to lead an audit, from 1 to 3;
       the level to lead is not below the level to audit.

See :doc:`competence`.

.. _config-supplier:

Settings of the supplier evaluation add-on
------------------------------------------

Block :guilabel:`Supplier evaluation`:

.. list-table::
   :header-rows: 1
   :widths: 30 14 56

   * - Setting
     - Default
     - What it does
   * - :guilabel:`Score weights`: on-time receipts, right quantities, nonconformities
     - 30, 20, 50
     - How each part weighs in the supplier score; at least one above 0.
   * - :guilabel:`Nonconformity points`: minor, major, critical
     - 1, 3, 5
     - Penalty points of a supplier nonconformity, per receipt of the period; they do not decrease with severity.
   * - :guilabel:`Receipt measures`: :guilabel:`Grace days`, :guilabel:`Quantity tolerance (%)`
     - 0, 0
     - Days after the deadline a receipt still counts as on time; how far the quantity received may differ from the
       quantity ordered. Receipt measures need Inventory.
   * - :guilabel:`Grades`: A, B and C from
     - 90, 75, 60
     - Lowest score of grades A, B and C; below C the grade is D.
   * - :guilabel:`Purchase confirmation control`
     - Warn
     - :guilabel:`Off`, :guilabel:`Warn` or :guilabel:`Block`: what happens when a purchase order is confirmed for an
       unapproved or blocked supplier. Set it to Off while you build the approved supplier list, then to Warn or Block.
   * - :guilabel:`Supplier delays`: :guilabel:`SCAR response (days)`, :guilabel:`Assessment reminder (days)`
     - 30, 30
     - Days the supplier has to answer a corrective action request (at least 1); lead time of the periodic assessment
       reminder.

See :doc:`suppliers`.

Other configuration menus
=========================

:menuselection:`Quality --> Configuration --> Standards`
   The standards and their clause libraries, with the sections that may be declared not applicable. Visible to quality
   managers only. See :doc:`clauses`.

:menuselection:`Quality --> Configuration --> Clause applicability`
   The clauses declared not applicable, per company, in force or withdrawn. See :ref:`clauses-not-applicable`.

With **QMS Advanced** and the add-ons, the :menuselection:`Configuration` menu also holds :guilabel:`Processes` and
:guilabel:`Audit templates` (:doc:`audits`), :guilabel:`Document types` (:doc:`documents`), :guilabel:`Review inputs`
(:doc:`management_reviews`), :guilabel:`Record retention` (:ref:`documents-retention`), :guilabel:`Competences` and
:guilabel:`Requirements` (:doc:`competence`), and :guilabel:`Assessment criteria` (:doc:`suppliers`).

Scheduled action
   Odoo runs *QMS: overdue nonconformities* once a day. It marks nonconformities that became overdue and sends their
   owners a reminder. See :doc:`nonconformities`. It is active from installation; there is nothing to set up.

Demo data
=========

When the app is installed on a database created with demo data, it adds a demonstration register:

- a quality manager called *DEMO Quality Manager* (login ``qms_demo_manager``), who owns every demo nonconformity;
- twelve nonconformities covering all six source types and the three severities; every accepted one is tagged with
  ISO 9001 clause 10.2:

  - four **closed** and signed, with a complete treatment;
  - six **open**, two of them **overdue**;
  - two **new**, waiting to be accepted.

One open nonconformity, *Wrong label on batch 0912*, has its treatment complete and its activity done: a manager can
close it straight away to see the signature at work.

The demo nonconformities fill the :doc:`dashboard` and the :doc:`clause view <clauses>` from the first minute. The
demo closures were signed without a password, since nobody could type one while the data was loaded.

.. seealso::
   - :doc:`roles`
   - :doc:`clauses`
   - :doc:`trail`
   - :doc:`dashboard`
