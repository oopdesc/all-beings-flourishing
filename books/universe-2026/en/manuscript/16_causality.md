# Chapter 16. Knowing Causes and Trusting Predictions

Predicting what happens and knowing what intervention would change it are similar but different tasks. Knowing more people go outside on sunny days does not mean sending people outside makes the sun shine. This matters both in explaining the universe and improving society.

Extending science’s scope need not mean immediately calling everything scientific. It means refining questions about prediction and causation and expanding the conditions under which they can be answered.

## What If We Changed Something—or Did Not?

Suppose people using a learning method achieve higher scores. Is that the method’s effect? More motivated people may have chosen it. Task difficulty and available time may differ too.

Causal reasoning distinguishes the same individual’s outcome using the method, Y(1), from the outcome without it, Y(0). We want their difference but cannot observe both for the same occasion. We therefore ask which assumptions and study designs permit comparing different individuals.[56]

Random assignment is a strong approach. Proper assignment controls bias from pre-intervention characteristics through its allocation mechanism. It does not ensure perfect balance of every characteristic in one realized study. Dropout, nonadherence, and missing outcomes still require treatment.

## Aggregation Can Reverse the Direction

These fictional numbers illustrate aggregation, not a real learning method’s evaluation. Suppose users and nonusers are unevenly distributed across easy and difficult tasks.

| Task | Success among users | Success among nonusers |
| --- | --- | --- |
| Easy | 8/10 people, 80% | 63/90 people, 70% |
| Difficult | 18/90 people, 20% | 1/10 people, 10% |
| Total | 26/100 people, 26% | 64/100 people, 64% |

Users outperform nonusers by 10 percentage points on both task types, yet by aggregation they perform 38 points worse. Most users faced difficult tasks.

If both comparison groups had equal shares of easy and difficult tasks, users would average 80% and 20%, giving 50%; nonusers would average 70% and 10%, giving 40%. Equalizing task composition yields a 10-point difference.

There is no numerical contradiction. Overall rates depend both on task-specific rates and on the allocation of people across tasks. We cannot choose the most attractive aggregation without defining the population we want to understand.

Adjusting this table alone does not prove causality. Conditions beyond task difficulty may still distort the comparison.

## Conditions for Moving from Observation to Cause

Estimating intervention effects from observations requires a clearly defined intervention corresponding to observed outcomes, expressed through consistency. We also need comparability of treatment selection and potential outcomes conditional on adjustment variables, and a possibility of receiving either treatment within the necessary strata. The latter is positivity.[56]

The terms are technical, but the questions are concrete. What counts as using the method? Are comparison groups too different, including in unobserved characteristics? If nobody under one condition uses one option, where does that comparison come from?

Large datasets do not automatically satisfy these conditions. Nor should we adjust indiscriminately for every post-intervention variable. That can change the pathway of interest or introduce bias. Subject knowledge and causal structure must come before statistical estimation.

If interventions on others also affect my outcome, Y(1) and Y(0) referring only to my own use are insufficient. We must redefine whose assignments and which arrangements are compared. Knowing the scope of a simple formula prepares us to study broader phenomena.

A 2026 review of externally controlled trials likewise organizes a framework beginning with the causal quantity of interest, then identification assumptions, then estimation and uncertainty.[57] Powerful computation cannot replace the question and its premises.

## Give Even Successful Predictions a Range

Separate from causation, mathematics can improve predictive reliability. A machine-learning surrogate may accelerate predictions of physical processes. We then want not only one number but some account of how far it might miss.

Conformal prediction constructs prediction intervals from error ranks using calibration data separate from the predictor’s training, among other setups. Suitable exchangeability conditions give coverage guarantees for new outcomes. Exchangeability means reordering the samples leaves their joint distribution unchanged.[51]

Take a minimal example. Fix the predictor first and measure absolute errors on nine calibration examples. Use their maximum as interval width. If the nine errors and the new example’s error are exchangeable and untied, the new error’s rank is uniform among ten positions.

It exceeds the calibration maximum only if it is the largest of all ten. Thus repeated use over the joint distribution gives 90% coverage. [Mathematical Note E](18_math_notes.xhtml#note-e) includes the premises. This does not promise that nine examples always yield narrow, practically useful intervals.

## Check What the Guarantee Refers To

Gopakumar and colleagues’ 2026 research applies the method to physical surrogate models. Its guarantee is marginal coverage at individual spacetime cells, not coverage for every specified input condition or simultaneous coverage of the entire field. It also relies on exchangeability between calibration and prediction.[51]

“90% overall” may permit more frequent misses under particular difficult conditions. Cutting a time series into equal-length windows does not prove their distributions match. Changed seasons, instruments, or operating conditions require rechecking assumptions and actual coverage.

Success outside a training distribution does not mean calibration and prediction distributions may differ arbitrarily. Reading exactly where matching conditions are required lets us use the method without overestimating or underestimating it.

## How Science’s Reach Expands

For causation, we specified intervention and comparison conditions. For prediction, we measured errors and defined the guarantee’s target. These do not solve the universe’s essence, but extract checkable parts from vague hopes.

Mathematics shows what follows under assumptions. Science investigates how those assumptions and measurements hold in reality. Philosophy reexamines what we want to know and what we call a cause or explanation. Moving among them can gradually enlarge understanding.
