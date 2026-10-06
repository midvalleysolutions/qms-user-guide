=====================
Clauses and standards
=====================

Auditors read your quality system clause by clause: *show me your evidence for 10.2*. The **Quality** app ships the
clause lists of five ISO management-system standards. You tag each nonconformity with the clauses it is evidence
for, and the clause view shows, for any period, how many records are tagged to each clause — and which clauses have
none. Clauses that do not apply to your company can be declared not applicable, with a justification, so that the gap
list shows only the requirements you are subject to.

The standards
=============

.. list-table::
   :header-rows: 1
   :widths: 45 15 15 25

   * - Standard
     - Edition
     - Clauses
     - At installation
   * - ISO 9001 — Quality management systems
     - 2015 or 2026
     - 81 (83 on 2026)
     - Enabled
   * - ISO 14001 — Environmental management systems
     - 2015
     - 50
     - Disabled
   * - ISO 45001 — Occupational health and safety
     - 2018
     - 58
     - Disabled
   * - ISO 13485 — Medical devices
     - 2016
     - 89
     - Disabled
   * - ISO 22000 — Food safety management systems
     - 2018
     - 64
     - Disabled

ISO 9001 follows the 2015 edition until a quality manager switches it to 2026: see :doc:`edition_switch` and
:doc:`what_changed_in_2026`.

Each clause has its number as printed in the standard (for example ``10.2``), a short title, and one sentence saying
what the clause asks for. The titles are paraphrased: the official text of the standards is copyrighted and is not
included. Clauses are organised as a tree: ``10.2`` sits under ``10``.

In pickers and lists, a clause reads as the standard's code, its number and its title, for example
*9001 · 10.2 Nonconformity and corrective action*.

Enable a standard
=================

Only clauses of *enabled* standards can be tagged. To certify against ISO 14001 as well as ISO 9001, for example:

#. Go to :menuselection:`Settings --> Quality`.
#. In :guilabel:`Enabled standards`, add *ISO 14001 — Environmental management systems*.
#. Click :guilabel:`Save`.

Its clauses are now offered wherever clauses are tagged.

To disable a standard, remove it from :guilabel:`Enabled standards` and save. Its clauses are no longer offered, but
records already tagged with them keep their tags. At least one standard must stay enabled.

With **QMS Advanced**, ticking :guilabel:`ISO 14001 environmental registers` or :guilabel:`ISO 45001 health & safety
registers` enables the standard too, and a standard whose registers are on cannot be disabled until its box is
unticked. See :doc:`ehs_setup`.

.. important::
   Enable and disable standards in the settings. A standard switched on only from
   :menuselection:`Quality --> Configuration --> Standards` is switched off again the next time the settings are
   saved.

Tag records with clauses
========================

A nonconformity is tagged in its :guilabel:`Clauses` tab, or in the :guilabel:`Accept` dialog. At least one clause
is required before a nonconformity can be accepted, and it must still be there to close it. See
:doc:`nonconformities`.

- Tag the most precise clause that applies. A record tagged with ``10.2`` also counts as evidence for ``10``.
- Tag several clauses when one problem breaks several requirements, including clauses of different enabled
  standards: a chemical spill might be tagged with both an ISO 14001 and an ISO 45001 clause.
- The :guilabel:`Standards` field under the clauses fills itself with the standards of the tagged clauses.

With **QMS Advanced** installed, corrective actions, audits, audit findings, audit programmes, processes, documents,
management reviews, context issues, interested parties, scope versions, risks, objectives, satisfaction records,
instruments and calibrations are tagged the same way, and count as evidence too — and so do the records of the
Training & Competence and supplier evaluation add-ons when they are installed. Clause declarations of not applicable
count for clause 4.3.

The clause view
===============

#. Go to :menuselection:`Quality --> Evidence --> Clauses`.
#. In the dialog, choose the period with :guilabel:`Date From` and :guilabel:`Date To`. By default it covers the last
   twelve months, ending today.
#. Tick :guilabel:`Show Inactive` to also list the clauses of standards that are not enabled.
#. Click :guilabel:`Show evidence`.

.. image:: ../_images/clauses-period-dialog.png
   :alt: The clause view dialog with the period dates and the Show Inactive option.

The list, titled *Clauses — records tagged <start> to <end>*, shows one row per clause:

- :guilabel:`Standard`, :guilabel:`Number` and :guilabel:`Name` of the clause;
- :guilabel:`Records tagged`: how many records are tagged with this clause or one of its sub-clauses in the period;
- :guilabel:`Applicability`: *Not applicable*, as a grey badge, when the clause is declared not applicable (see `Declaring a clause not
  applicable`_); the optional :guilabel:`Why not applicable` column shows the justification;
- :guilabel:`Gap`: ticked when the clause has no record tagged in the period;
- a :guilabel:`Records tagged` button, shown when there is at least one record: click it to list them;
- for quality managers, a :guilabel:`Mark not applicable` button.

.. important::
   Records tagged to a clause show where to look. They are not proof of conformity: conformity is judged against the
   requirement. The same sentence is shown on each clause and printed under the clause matrix of the audit pack.

.. image:: ../_images/clauses.png
   :alt: The clause view: ISO 9001 clauses with their Records tagged count, the Not applicable badge on 8.3 and the gap
         mark for the chosen period.

How the evidence is counted
---------------------------

- A nonconformity counts in the period when its :guilabel:`Detected On` date falls in it. Records that happen on a day
  — an audit, an action, a calibration — count the same way, on their own date.
- Records that stay in force for a while — a document version in force, a process, a context issue, a risk, an
  objective, a scope version, a declaration of not applicable, an instrument in service — count in **every** period
  their time in force overlaps, whatever day they were created. A procedure approved in 2024 and still in force counts
  for 2026-Q3. This time in force is the record's *evidence span*; drafts never count.
- Cancelled nonconformities never count.
- A record tagged with both a clause and one of its sub-clauses counts once for the parent clause.
- Only the records you are allowed to see are counted. A quality user may see lower counts than a quality manager.

Find the gaps
-------------

A *gap* is a clause of an enabled standard with no record tagged in the period. Gaps are shown in amber. To list only
them, choose the :guilabel:`Gaps` filter. Clauses of disabled standards, shown with :guilabel:`Show Inactive`, are
never marked as gaps, and neither are clauses declared not applicable: use the :guilabel:`Not applicable` filter to
list those.

.. tip::
   Before a certification audit, open the clause view on the audit period and filter on :guilabel:`Gaps`. Each gap is a
   question the auditor may ask: either find the evidence and tag it, or plan an activity that produces it.

When clauses of more than one standard are listed, the list is grouped by :guilabel:`Standard`, every group folded:
click a standard to unfold its clauses. With a single standard, the clauses show directly. You can also group by :guilabel:`Standard` yourself, or search by
:guilabel:`Number` or :guilabel:`Name`.

Open the evidence of a clause
-----------------------------

Click the :guilabel:`Records tagged` button on a clause row. The records tagged with that clause or its sub-clauses
that count in the period open in a list titled *Records tagged to <clause>*; from there, open any of them.

.. image:: ../_images/clauses-evidence.png
   :alt: The nonconformities tagged with clause 10.2 in the chosen period, opened from the clause view.

.. _clauses-not-applicable:

Declaring a clause not applicable
=================================

ISO 9001 clause 4.3 lets a company state that a requirement cannot be applied to it — a build-to-print shop has no
product design (clause 8.3), for example — as long as it says why. A quality manager declares it once, for a company;
the clause and its sub-clauses then read *Not applicable* in the clause view, with the justification, and are no longer
counted as gaps.

#. Go to :menuselection:`Quality --> Evidence --> Clauses` and open the clause view.
#. On the clause's row, click :guilabel:`Mark not applicable`. The button shows only where a declaration is allowed: not
   on sections 4 and 5 or a section the standard's table leaves out, and not on a clause already declared (or under a
   declared clause).
#. Check the :guilabel:`Clause` and, with several companies, the :guilabel:`Company`.
#. Write the :guilabel:`Justification`: why this requirement cannot be applied, in at least 20 characters, for example
   *Build to print only: customers own the design.*
#. Click :guilabel:`Mark not applicable`.

.. image:: ../_images/clauses-not-applicable-dialog.png
   :alt: The Mark not applicable dialog for clause 9001 8.5.3 with a justification, and the warning that the scope in
         force will be out of date until it is revised.

The declaration is in force from today, in the name of the manager who made it. It is its own record, listed under
:menuselection:`Quality --> Configuration --> Clause applicability` with the :guilabel:`Standard`, the
:guilabel:`Clause`, :guilabel:`Not applicable since`, :guilabel:`Declared by` and its state. It is tagged with clause
4.3 of its standard (and of ISO 9001 when it is enabled) and counts as a 4.3 record for every period it is in force.

Which clauses can be declared
-----------------------------

- Clauses of sections **4** (context) and **5** (leadership) apply to every organization and can never be declared not
  applicable.
- Each standard lists the sections that may be declared not applicable in :guilabel:`Sections that may be declared not
  applicable` (see `Manage standards and clauses`_): sections 7 and 8 for ISO 9001, 14001, 45001 and 22000, and sections
  6, 7 and 8 for ISO 13485. A clause of any other section is refused with a message listing the sections that cannot
  be declared; for ISO 9001: *Clauses of sections 4, 5, 6, 9 and 10 apply to every organization.*
- The standard must be enabled: *Enable <standard> in the settings first.*
- A clause is declared once per company. A clause whose parent is already declared is covered by it: *8.3 already
  covers 8.3.2.* Declaring a parent withdraws the declarations of its sub-clauses, with the reason *Covered by the
  declaration of <parent>*.

With several companies selected in the company switcher, a clause reads *Not applicable* only when every company
selected declared it; when their justifications differ, each is shown with the company's name.

Make it applicable again
------------------------

When the requirement applies again — the company starts designing its own products — a quality manager withdraws the
declaration:

#. Go to :menuselection:`Quality --> Configuration --> Clause applicability` and open the declaration.
#. Click :guilabel:`Withdraw`, write why the clause applies again (at least ten characters) and click
   :guilabel:`Withdraw`.

The declaration moves to **Withdrawn** and is locked. :guilabel:`Applicable again from` is today and :guilabel:`Not
applicable until` is yesterday. A declaration is never deleted, and it never moves to another clause or company: withdraw
it and declare the other one.

The not-applicable map by date
------------------------------

The clause view reads the declarations as they stood on the **last day of the chosen period**. After a withdrawal, the
clause is a gap again from that day for any period ending after it, while the clause view of an earlier quarter still
reads *Not applicable*: the past stays as it was. The :guilabel:`In force` filter of
:menuselection:`Quality --> Configuration --> Clause applicability` shows the declarations in force today; remove it to
see the withdrawn ones.

.. note::
   With **QMS Advanced** installed, approving the scope copies the declarations in force for its standards into the
   signed scope. A declaration made or withdrawn later shows as a change on the scope in force, until the scope is
   revised. See :doc:`context`.

Manage standards and clauses
============================

Quality managers can review the libraries in :menuselection:`Quality --> Configuration --> Standards`. The list shows
every standard, enabled or not, with its :guilabel:`Code`, :guilabel:`Name`, :guilabel:`Edition`, number of clauses
and an :guilabel:`Active` switch. Drag the handle to change the order in which standards are listed.

.. image:: ../_images/standards-list.png
   :alt: The Standards list under Quality, Configuration, with the five ISO standards and their clause counts.

Open a standard to see its clauses in the :guilabel:`Clauses` tab. You can:

- add a clause with its :guilabel:`Number`, :guilabel:`Name`, :guilabel:`Intent` (one sentence) and
  :guilabel:`Parent` clause;
- create a new standard, for example an internal or customer-specific requirement set, with a :guilabel:`Name` and a
  unique :guilabel:`Code`. Then enable it in the settings;
- set :guilabel:`Sections that may be declared not applicable`: the section numbers separated by commas, for example
  ``7,8``. Left empty, any section except 4 and 5 may be declared not applicable.

A clause number must be unique within its standard. A clause that is already tagged on a record cannot be deleted:
disable its standard instead.

.. note::
   The clause titles and intents of the shipped standards are translated with the app (French, German, Spanish and
   Vietnamese). When the app is updated, the shipped titles and intents may be restored: to use your own wording,
   prefer adding your own clauses or your own standard.

.. seealso::
   - :doc:`nonconformities`
   - :doc:`configuration`
   - :doc:`audit_pack`
   - :doc:`edition_switch`
