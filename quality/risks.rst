=======================
Risks and opportunities
=======================

ISO 9001 clause 6.1 asks you to determine the risks and opportunities of your quality system, to plan actions on
them, and to check that those actions worked. With **QMS Advanced** installed, the **Quality** app keeps a risk register:
each risk or opportunity is scored likelihood × severity on a 5 × 5 matrix, given a treatment, followed through
treatment actions — the same actions as for nonconformities — and re-assessed, so that the score before and after
treatment shows whether the treatment worked.

.. list-table::
   :header-rows: 1
   :widths: 15 85

   * - State
     - Meaning
   * - **Draft**
     - Being described and scored. It has no number yet and is not evidence.
   * - **Open**
     - Opened with its treatment: it has a number, such as ``RSK/2026/001``, and a first assessment. It is reviewed at
       the interval of its level.
   * - **Closed**
     - Closed by a quality manager with a reason. It is locked.

.. image:: ../_images/risks-register.png
   :alt: The risk register: number, title, type, owner, score, a coloured level badge, treatment, next review and
         state, sorted by score.

Record a risk or an opportunity
===============================

#. Go to :menuselection:`Quality --> Planning --> Risks --> Risks and opportunities` and click :guilabel:`New`.
#. Write the risk or the opportunity in one line, for example *Single qualified supplier for anodising*.
#. Choose the :guilabel:`Type`: :guilabel:`Risk` (it may harm conformity or customer satisfaction) or
   :guilabel:`Opportunity` (it may improve them). The type is fixed once the risk is open.
#. Check the :guilabel:`Owner` (you by default) and :guilabel:`Identified on` (today; it cannot be in the future).
#. Score it: :guilabel:`Likelihood` and :guilabel:`Severity` — :guilabel:`Benefit` for an opportunity — from 1 to 5.
#. On the :guilabel:`Description` tab, describe it, its :guilabel:`Cause` and its :guilabel:`Consequence`. For an
   opportunity these read :guilabel:`What could bring it about` and :guilabel:`What we would gain`.
#. On the :guilabel:`Links` tab, add the :guilabel:`Processes` it concerns, the :guilabel:`Context issues` it stems
   from, the :guilabel:`Interested-party needs` it concerns (adopted needs of relevant parties only) and the
   :guilabel:`Nonconformities` where it materialised. Links stay within the risk's company.
#. Save.

Clause 6.1 of ISO 9001 is proposed in :guilabel:`Clauses`. The risk stays a **Draft** until it is opened.

.. _risks-2026-tags:

Clauses under the 2026 edition
------------------------------

The 2026 edition of ISO 9001 splits 6.1 into 6.1.1 (determining risks and opportunities), 6.1.2 (actions on risks)
and 6.1.3 (actions on opportunities). When the clause library follows 2026 (see :doc:`edition_switch`), the register
tags each record by its type, so the clause view answers *show me your 6.1.3 evidence* without anyone tagging by hand:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Type
     - Clauses proposed under 2026
   * - :guilabel:`Risk`
     - 6.1.1 and 6.1.2
   * - :guilabel:`Opportunity`
     - 6.1.1 and 6.1.3

.. image:: ../_images/risks-opportunity-2026-tags.png
   :alt: The open opportunity RSK/2026/007 tagged 9001 6.1, 6.1.1 and 6.1.3, with its likelihood, benefit and score.

- When you change the type of a draft, the sub-clause follows at once: 6.1.2 becomes 6.1.3, or the reverse. Your
  other clauses stay.
- At the switch to 2026, every draft or open risk and opportunity gains 6.1.1 and its type's sub-clause; its 6.1 and
  other clauses stay. A closed risk is not changed.
- A record that carries only clauses of other standards, such as an OH&S opportunity tagged with ISO 45001 6.1.2.3, is
  left alone.
- The clause view counts 6.1.1 to 6.1.3 under 6.1 too, so the 6.1 evidence does not drop.
- At a switch back to 2015, 6.1.1 to 6.1.3 are removed from every draft or open record, and 6.1 is added where it was
  missing. A risk closed under 2026 keeps its tags, and the library then stays on 2026.

Under 2015 nothing changes: risks and opportunities are tagged 6.1.

.. tip::
   From an open or closed nonconformity, click :guilabel:`Raise risk`: Odoo opens a new risk already linked to the
   nonconformity and its process. The nonconformity's :guilabel:`Risks` smart button lists the risks linked to it.

The scales
----------

.. list-table::
   :header-rows: 1
   :widths: 10 30 30 30

   * - Value
     - Likelihood
     - Severity (risk)
     - Benefit (opportunity)
   * - 1
     - Rare: less than once in 5 years
     - Negligible
     - Minimal
   * - 2
     - Unlikely: once in 2–5 years
     - Minor
     - Small
   * - 3
     - Possible: once a year
     - Moderate
     - Moderate
   * - 4
     - Likely: several times a year
     - Major
     - Large
   * - 5
     - Almost certain: monthly or more
     - Critical
     - Transformational

The :guilabel:`Score` is likelihood × severity, from 1 to 25, and the :guilabel:`Level` follows from the company's
:ref:`Level thresholds <config-risks>`. A score equal to a threshold takes the higher level. With the default
thresholds:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Level
     - Score
     - Periodic review, by default
   * - **Low**
     - 1 to 4
     - Every 12 months
   * - **Medium**
     - 5 to 9
     - Every 12 months
   * - **High**
     - 10 to 14
     - Every 6 months
   * - **Critical**
     - 15 to 25
     - Every 3 months

For example, a risk scored likelihood 4 × severity 4 has a score of 16: it is **Critical**. The form shows the 5 × 5
matrix, with the likelihood down the left side and the severity across the top, each cell in the colour of its level,
with the risk's cell outlined.

An opportunity reads the other way. Its matrix has the benefit across the top and one green that gets stronger as the
score rises, never red, and its level reads as a benefit: :guilabel:`Minor benefit`, :guilabel:`Moderate benefit`,
:guilabel:`High benefit` or :guilabel:`Major benefit`. In the register, the :guilabel:`Level` column and the colour of
the badge follow the same reading.

.. image:: ../_images/risks-form.png
   :alt: An open risk as a quality manager sees it, with Add treatment action, Re-assess and Close in the header:
         likelihood 4 and severity 4, score 16, level Critical, and the 5 × 5 matrix with the risk's cell outlined.

Decide the treatment
====================

On the :guilabel:`Treatment` tab, choose the :guilabel:`Treatment`. A risk offers :guilabel:`Reduce`,
:guilabel:`Avoid`, :guilabel:`Transfer` and :guilabel:`Accept`; an opportunity offers only :guilabel:`Pursue` and
:guilabel:`Decline`. What it needs before the risk or opportunity can be opened:

.. list-table::
   :header-rows: 1
   :widths: 25 20 55

   * - Treatment
     - For
     - Needs
   * - :guilabel:`Reduce`, :guilabel:`Avoid`, :guilabel:`Transfer`
     - Risks
     - At least one treatment action that is not cancelled.
   * - :guilabel:`Accept`
     - Risks
     - A :guilabel:`Treatment note` of at least ten characters, recorded with :guilabel:`Accept`. A **High** or
       **Critical** risk is accepted by a quality manager, with a signature.
   * - :guilabel:`Pursue`
     - Opportunities
     - At least one treatment action that is not cancelled.
   * - :guilabel:`Decline`
     - Opportunities
     - A :guilabel:`Treatment note` of at least ten characters.

Add treatment actions
---------------------

Click :guilabel:`Add treatment action` on a draft or open risk. Odoo opens a new **preventive** action linked to the
risk, tagged with clause 6.1 and owned by the risk's owner. Complete its title, due date and effectiveness date and
save. The action is then carried out, marked done and verified like any other action — see
:doc:`corrective_actions`. The :guilabel:`Actions` smart button and the :guilabel:`Treatment` tab list the risk's
actions, and :guilabel:`Treatment progress` says where they stand: :guilabel:`No treatment action`,
:guilabel:`Planned`, :guilabel:`In progress`, :guilabel:`Done` or :guilabel:`Re-assessed`. Cancelled actions do not
count.

When an open risk treated by actions has none left, the form shows *No treatment action: add one or choose another
treatment.* When a treatment action is judged ineffective, the owner gets a *Re-decide the treatment* to-do.

Accept a risk
-------------

#. Click :guilabel:`Accept` on the risk.
#. Write why the risk is accepted, at least ten characters.
#. Click :guilabel:`Accept risk`.

A **Low** or **Medium** risk is accepted by its owner or a quality manager. A **High** or **Critical** risk is accepted
by a quality manager only: Odoo asks for their password and records an electronic signature with the reason *Risk
acceptance*. :guilabel:`Accepted by` shows who accepted it.

Acceptance is recorded with the button, not by choosing :guilabel:`Accept` in the :guilabel:`Treatment` field. If you
pick it there, a window titled *Accepting a risk* says why, puts back only the treatment (your other changes are kept)
and, if you may accept this risk, offers :guilabel:`Accept now…`, which saves the form and opens the Accept dialog.
Otherwise it says who can — a quality manager for a high or critical risk, the owner or a quality manager otherwise —
and suggests Reduce, Avoid or Transfer instead. On a draft risk, the same window is titled *Opening a risk* and offers
:guilabel:`Accept and open…`.

On a risk you do not own, a line under the header says *Only the owner (…) or a quality manager can work on this
risk.*

If an accepted risk later becomes High or Critical after a re-assessment, its acceptance lapses: the form shows
*Acceptance lapsed: the risk became high or critical after it was accepted. Re-decide the treatment.*, and the owner
and the quality managers get a *Re-decide the treatment* to-do. The risk stays open.

Open the risk
-------------

When the risk is described, scored and its treatment decided, its owner or a quality manager clicks :guilabel:`Open`.
Odoo checks the title, type, owner, score, at least one clause and the treatment table above. If something is missing,
a window titled *Opening a risk* (*Opening an opportunity* for an opportunity) lists everything still needed at once and
says where to enter it, for example *Choose Pursue or Decline in the Treatment field on the Treatment tab, then press
Open again.* Click :guilabel:`Got it`, fill the fields it names and click :guilabel:`Open` again. When everything is
there, Odoo:

- gives the risk its number, ``RSK/<year identified>/<nnn>``, for example ``RSK/2026/001``;
- records the first row of the :guilabel:`Assessments` tab, phase :guilabel:`Initial`, with the date, who assessed,
  the scores and the level.

From then on the score changes only through a re-assessment. The level of each row is frozen with the thresholds of
that day, so a later change of the thresholds never rewrites the history.

Re-assess the risk
==================

When the last treatment action of an open risk is done or verified, its owner gets a *Re-assess the risk <risk>*
to-do. To record a re-assessment (the window is titled *Re-assess opportunity* on an opportunity, and asks for the
:guilabel:`Benefit` instead of the :guilabel:`Severity`):

#. Click :guilabel:`Re-assess` on the open risk.
#. Choose the :guilabel:`Phase`: :guilabel:`After treatment`, :guilabel:`Periodic review` or :guilabel:`Change`.
#. Enter the new :guilabel:`Likelihood` and :guilabel:`Severity` (or :guilabel:`Benefit`).
#. Write what changed and why. The note is required after treatment and on a change.
#. Click :guilabel:`Record assessment`.

A new row is added to the :guilabel:`Assessments` tab with the previous score and the change: a negative
:guilabel:`Delta` means the risk was reduced. When a treatment action is still open, the dialog warns that the
re-assessment records a partial treatment.

.. image:: ../_images/risks-assessments.png
   :alt: The Assessments tab of a risk with its initial assessment: date, phase Initial, likelihood 4, severity 4,
         score 16, level Critical and the assessor; each re-assessment adds a row with the previous score and the
         delta.

Review risks periodically
-------------------------

An open risk is due for review at its last assessment date plus the review interval of its level (see the table
above). :guilabel:`Next review` shows the date; a risk past it is marked with a red *Review overdue* ribbon and appears
under the :guilabel:`Overdue review` filter. Before the date — 14 days before by default — the owner gets a *Review the
risk <risk>* to-do. The review is recorded as a re-assessment of phase :guilabel:`Periodic review`, which moves the
next review date on. An interval of 0 in the settings means no periodic review for that level.

Close a risk
============

A quality manager closes an open risk that no longer needs treatment:

#. Click :guilabel:`Close`.
#. Write why, at least ten characters.
#. Click :guilabel:`Close risk`.

Odoo refuses while a treatment action is still in draft or in progress: *Finish or cancel the treatment actions
first.* The risk moves to **Closed**, the reason shows on its :guilabel:`Closing` tab, and it is locked. A closed risk
takes no new treatment action: record a new risk instead. Only a draft risk can be deleted.

Find risks and print the register
=================================

The register is sorted by score, highest first. A risk shows its score and level; for an opportunity the level reads
as a benefit, as above. Filters: :guilabel:`Risks`, :guilabel:`Opportunities`,
:guilabel:`High and critical`, :guilabel:`My risks`, :guilabel:`Overdue review`, :guilabel:`Draft`, :guilabel:`Open`
and :guilabel:`Closed`; group by :guilabel:`Level`, :guilabel:`Type` or :guilabel:`Owner`.

To print it, go to :menuselection:`Quality --> Planning --> Risks --> Print risk register`, choose the :guilabel:`As at` date and
click :guilabel:`Print`. The PDF lists every risk open on that date with its scores before and after treatment, its
treatment and its actions. The :doc:`audit pack <audit_pack>` includes it as ``11_risk_register.pdf``.

Evidence, review and dashboard
==============================

- **Evidence.** In the :doc:`clause view <clauses>`, an open or closed risk counts for its clauses in every period from
  its identification until it is closed. Drafts never count.
- **Management review.** Input *9.3.2 e — Effectiveness of actions on risks and opportunities* shows the risks and
  opportunities open by level, those identified, closed and treated in the period, how many were reduced, unchanged
  or increased, the high risks accepted, the treatment actions open and overdue, and the risks overdue for review.
  With nothing in the period it reads *No risk register entries for the period*. On a review created under the 2026
  edition, the risks and the opportunities have an input each, *Effectiveness of actions on risks* and *Effectiveness
  of actions on opportunities*, with the figures of their own type. See :doc:`management_reviews`.
- **Dashboard.** The :guilabel:`High and critical risks` tile counts the open risks of level High or Critical. It is
  red when one of them has no treatment action (and is not accepted) or is overdue for review, amber otherwise.
  Accepted high risks are counted but never turn it red.

Who can do what
===============

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Role
     - Risks and opportunities
   * - **User**
     - Records risks, edits and opens the risks they own, adds treatment actions, accepts their own Low or Medium
       risks, and re-assesses them.
   * - **Internal auditor**
     - Reads the whole register; does not change it.
   * - **Manager**
     - Everything: opens and re-assesses any risk, accepts any risk (High and Critical with a signature) and closes
       risks.

See :doc:`roles` for the full picture.

.. seealso::
   - :doc:`corrective_actions`
   - :doc:`context`
   - :doc:`management_reviews`
   - :doc:`audit_pack`
