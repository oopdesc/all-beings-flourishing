[Read the opening conclusions](00_conclusions.md#h-1) ｜ [Contents](../README.md#toc) ｜ [References](19_references.md#h-1) ｜ [Previous chapter](11_ai.md#h-1) ｜ [Next chapter](13_meaning.md#h-1)

<a id="h-1"></a>

# Chapter 12. Matching Evidence to the Size of a Conclusion

Something rare happens, and we wonder whether it has a special cause. That intuition can begin inquiry, but rarity alone does not identify the right cause. Probability helps bridge that gap.

This chapter follows three stages from observation to conclusion: how unusual a result is under one explanation, how to compare competing explanations, and how to control errors when drawing conclusions during an ongoing investigation.

<a id="h-2"></a>

## Out of a Million, How Many?

The following numbers are fictional teaching examples, not the performance of actual astronomical observations or detectors.

Suppose a signal occurs once in every thousand cases. A detector finds 99% of real signals but also classifies 1% of nonsignals as signals. Given a positive result, is the probability of a real signal 99%?

Consider a million cases. There are 1,000 real signals, of which 990 are detected. There are 999,000 nonsignals, and 1%—9,990—are falsely detected.

That makes 10,980 positive results, with 990 genuine signals.

**Fraction genuine = 990 ÷ 10,980 ≈ 9.02%**

Even a capable detector can produce many false positives when searching for something initially very rare. To evaluate the probability after detection, we used not only sensitivity but also initial frequency and false-positive rate.

Writing the same relationship as an equation gives Bayes’ theorem. With hypothesis H and data D,

**P(H｜D) = P(D｜H) P(H) ÷ P(D)**

The right side of the vertical bar states the given condition. The probability of this result given a genuine signal reverses the conditioning in the probability of a genuine signal given this result.

This calculation must not be directly substituted for a dark matter event or cosmological sigma value, where backgrounds, search ranges, and model freedoms differ. The point is simply that reversing a condition can radically change the answer.

<a id="h-3"></a>

## What a p-Value Answers

A p-value is the probability, assuming the null hypothesis and test setup, of a test statistic at least as extreme as the observed one. It is not the probability that the hypothesis is false. “Extreme,” one- versus two-sided testing, and what was searched all affect its meaning.

If we inspect results and then select only a convenient target, time interval, or analysis, the rarity of the chosen analysis differs from the rarity of the whole selection process. Trying many keys and displaying the one that opens the lock cannot be reported as trying only one.

Exploration is necessary for finding new possibilities. A later stage using unused data can connect discovery with confirmation. Preregistration is one way to make that distinction traceable.<a id="cite-33"></a>[[33]](19_references.md#ref-33) It does not remove error, but makes it easier to locate questions changed to fit results.

Ioannidis’s 2005 mathematical discussion examines how prior plausibility, statistical power, and multiplicity affect the reliability of positive findings.<a id="cite-34"></a>[[34]](19_references.md#ref-34) Its famous title should not be read as an empirical measurement that a fixed proportion of papers in a particular field is false. It helps ask which research arrangements produce more false positives.

<a id="h-4"></a>

## Fitting Well and Supporting a Whole Model

In Chapter 4, extra free parameters could improve cosmological fits. Additional freedom can be useful, but we may separately ask how much of a theory’s allowed range agrees with the data.

Suppose one measurement with Gaussian error of standard deviation 1 gives 3. H0 fixes the mean at zero. H1 gives the unknown mean a uniform prior from −a to a, with a greater than 3.

H1’s best-fitting mean is 3. At that point, its likelihood is about 90 times H0’s. The best point does not change whether a is 5, 50, or 500.

Averaging the likelihood over H1’s entire allowed range changes the answer. The Bayes factor, the ratio of H1’s marginal likelihood to H0’s, is about 22.1 for a = 5, 2.26 for 50, and 0.226 for 500. [Mathematical Note C](18_math_notes.md#note-c) gives the equations and calculations.

Widening H1 spreads weight over means less compatible with the observation 3. The best fit stays the same while the model’s average predictive performance changes. Priors should not be chosen opportunistically after seeing results. We need reasonable alternatives and checks of sensitivity to them.

This does not make the Bayes factor the only correct answer. It illustrates the need to align what numbers assess. Improved fit and model comparison under a prior can point differently without mathematical contradiction.

<a id="h-5"></a>

## Can We Control Error While Continuing to Look?

Checking after each new observation and stopping when a favorable result appears is tempting in research and everyday comparisons. If repeated looks are allowed, we should design guarantees suitable for them from the start.

Chugg, Ramdas, and Grünwald’s 2026 paper examines e-values and their sequential version, e-processes, as evidence measures. A nonnegative statistic E is constructed with expectation at most 1 under the hypothesis. Then the probability of E reaching at least 1/α at a fixed valid test is at most α. Stopping during a sequence requires additional sequential validity.<a id="cite-50"></a>[[50]](19_references.md#ref-50)

For a minimal example, assume a coin is equally likely to land heads or tails even conditional on the past. Starting from 1, multiply by 1.5 for heads and 0.5 for tails. The expected next multiplier is

**(1.5 + 0.5) ÷ 2 = 1**

If this holds at each step even after knowing the past, the record does not grow on average. Nonnegativity and this condition imply that its chance of ever reaching 20 is at most 5%. [Mathematical Note D](18_math_notes.md#note-d) derives this from finite sequences. This concerns sequential testing, not real-money betting.

“Each step” matters. Indicators individually valid at each time do not necessarily retain the same guarantee if we select their maximum. A small e-value also does not by itself support the null: an unresponsive indicator could always be chosen.[[50]](19_references.md#ref-50)

<a id="h-6"></a>

## Returning Beyond the Numbers

Statistics is not a way to delegate the entire interpretation of the world to numbers. We can read the numbers when we have records of what was measured, compared, and selected.

Being surprised by an observation matters. Afterward, we can retain alternative explanations and ask what next measurement would distinguish them. Probability then becomes a tool for developing surprise into a new question rather than extinguishing it.

---

[Read the opening conclusions](00_conclusions.md#h-1) ｜ [Contents](../README.md#toc) ｜ [References](19_references.md#h-1) ｜ [Previous chapter](11_ai.md#h-1) ｜ [Next chapter](13_meaning.md#h-1)
