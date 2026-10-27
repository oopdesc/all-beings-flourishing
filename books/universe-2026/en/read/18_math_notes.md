[Read the opening conclusions](00_conclusions.md#h-1) ｜ [Contents](../README.md#toc) ｜ [References](19_references.md#h-1) ｜ [Previous chapter](17_synthesis.md#h-1) ｜ [Next chapter](19_references.md#h-1)

<a id="h-1"></a>

# Mathematical Notes: From Premises to Conclusions

These notes retain intermediate steps in the book’s calculations. All are examples constructed for this book, not reanalyses of research data or claims to new mathematical theorems. Small programs checked finite cases and numerical values alongside the hand derivations. No formal proof assistant was used.

If equations are unfamiliar, start with “What this shows” in each section. Links return to the main text.

<a id="note-a"></a>
<a id="h-2"></a>

## A. Different Explanations Through the Same Observations

**What this shows: agreement with finitely many observations need not determine a unique prediction beyond them.**

Let f(x) = x and g(x) = x + x(x−1)(x−2).

For x = 0, 1, or 2, one factor in the added product is zero, so f and g agree. At x = 3,

f(3) = 3

g(3) = 3 + 3×2×1 = 9

Agreement at three points therefore does not imply agreement for every x. Further observations or restrictions on permitted functions are needed.

This does not prove all physical theories equally valuable. Physics also compares consistency with other observations, symmetries, independent predictions, and applicability. The example is a counterexample to ending an argument at data fitting.

[Return to Chapter 1](01_truth.md)

<a id="note-b"></a>
<a id="h-3"></a>

## B. Do Not Reverse the Condition

**What this shows: 99% sensitivity does not ensure that 99% of positive results are genuine.**

For Chapter 12’s fictional detector, let H mean genuine and D a positive classification.

P(H) = 0.001

P(D｜H) = 0.99

P(D｜not H) = 0.01

The joint probability of genuine and positive is 0.001×0.99 = 0.00099. Nongenuine and positive is 0.999×0.01 = 0.00999. These cases are disjoint, giving P(D) = 0.01098.

Thus P(H｜D) = 0.00099/0.01098 = 11/122 ≈ 0.09016.

Changing the population frequency changes the answer. This is not an estimate about a real detector or disease.

[Return to Chapter 12](12_evidence.md)

<a id="note-c"></a>
<a id="h-4"></a>

## C. Separate Fit from the Bayes Factor

**What this shows: with the same best fit, the prior-allowed range can change comparison of whole models.**

Let observation x follow a normal distribution with mean μ and standard deviation 1, and observe x = 3. Write the standard normal density as φ and cumulative distribution as Φ.

Under H0, μ = 0, so the observed density is φ(3).

Under H1, μ has a uniform prior from −a to a; choose a > 3 before observing. Since the best mean is μ = 3, the maximum likelihood ratio is

φ(0)/φ(3) = exp(9/2) ≈ 90.017

H1’s marginal likelihood instead averages the density over μ:

m1(3) = {Φ(a−3) − Φ(−a−3)}/(2a)

The Bayes factor for H1 relative to H0 is B10 = m1(3)/φ(3).

| a | Maximum likelihood ratio | Bayes factor B10 |
| --- | --- | --- |
| 5 | About 90.017 | About 22.051 |
| 50 | About 90.017 | About 2.256 |
| 500 | About 90.017 | About 0.226 |

Weight allocated to poorly fitting parts of H1 changes the average. With prior probabilities on H1 and H0 themselves, the Bayes factor yields posterior model odds. The factor itself is not the probability that H1 is true.

This does not reproduce actual cosmological results. It isolates a mechanism for reading the differing comparison measures in Chapter 4.

[Return to Chapter 12](12_evidence.md) / [Return to Chapter 4](04_dark_energy.md)

<a id="note-d"></a>
<a id="h-5"></a>

## D. Conditions for Sequential Looks

**What this shows: a suitable nonnegative record can bound the chance of large values even when stopping during observation.**

Assume heads and tails each have probability 1/2 at every time conditional on the past. Let heads be X = 1 and tails X = 0. Before learning the outcome, choose λ between −1 and 1 and set the multiplier

B = 1 + λ(2X−1)

B is nonnegative. Its conditional average is

{(1+λ) + (1−λ)}/2 = 1

Start K0 = 1 and let Kt be the product of multipliers through t. Conditional on the past, Kt has expectation K(t−1): a nonnegative martingale. If conditional expected multipliers are at most 1, it is a nonnegative supermartingale.<a id="cite-50"></a>[[50]](19_references.md#ref-50)

Stop at the first value at least 20, or at N if that never occurs by N. The expected record at this bounded stopping time is at most 1. Paths reaching 20 stop at values at least 20; other paths remain nonnegative. Therefore

20 × P(reaching at least 20 by N) ≤ 1

Dividing by 20 gives at most 1/20, or 5%. Taking the limit of the increasing events as N grows preserves the same bound for ever reaching 20. This is the example’s time-uniform guarantee.

The computational check fixed λ = 1/2 and evaluated all 4,096 length-12 paths with exact fractions. It checked mean 1 at every time and probability at most 5% of reaching the threshold by 12. Finite enumeration does not replace the infinite-time argument; it checks agreement between derivation and implementation.

Real applications require checking the conditional hypothesis, selection of multipliers without future information, and inclusion of intermediate choices in the guarantee. Small values generally do not prove the hypothesis true.

[Return to Chapter 12](12_evidence.md)

<a id="note-e"></a>
<a id="h-6"></a>

## E. A 90% Prediction Interval from Ranks

**What this shows: under exchangeability, error ranks give coverage over the joint distribution.**

Fix a trained predictor f. For nine calibration cases and one new case, define absolute errors

Si = |Yi − f(Xi)|

Assume these ten errors are exchangeable and untied. The new case’s rank among ten is then uniform.

Let q be the largest of nine calibration errors and place an interval of width q on each side of the new prediction. It misses only if the new error is the largest of all ten, with probability 1/10. Coverage is therefore 9/10. With ties, this maximum-based rule gives coverage at least 9/10.

This is marginal coverage over the distribution including both calibration and new examples. It does not claim 90% at every input after fixing the particular nine calibration examples, nor guarantee narrow intervals.

Fitting f opportunistically on those same data to reduce calibration error may invalidate the symmetry assumed here. Follow the method’s premises, including training/calibration separation. Splitting a time series alone does not automatically establish exchangeability.<a id="cite-51"></a>[[51]](19_references.md#ref-51)

[Return to Chapter 16](16_causality.md)

<a id="note-f"></a>
<a id="h-7"></a>

## F. A Spring’s Period and Energy

**What this shows: the assumed equation of motion yields period and conservation step by step.**

Take positive constant m and k, no friction or external force, and spring force −kx. Twice differentiating x = A cos(ωt+φ) gives d²x/dt² = −ω²x. Substitution in m d²x/dt² = −kx requires ω² = k/m. A phase increase of 2π takes T = 2π/ω = 2π√(m/k).

The dimensions also agree. k has units newtons per meter, or kilograms per second squared. m/k has dimensions seconds squared, its square root seconds, and 2π is dimensionless.

For E = mv²/2+kx²/2, constant m and k give

dE/dt = mv dv/dt + kx dx/dt

= v(m d²x/dt² + kx)

= 0

With friction −cv, the last parentheses become −cv and dE/dt = −cv². For c ≥ 0, E decreases or stays constant.

This proves a relationship within the model. A real spring additionally requires checking changing m or k, friction, spring mass, nonlinear forces, and other neglected effects.

[Return to Chapter 15](15_laws.md)

<a id="note-g"></a>
<a id="h-8"></a>

## G. Checking an Aggregation Reversal

**What this shows: equalizing group composition reveals relations hidden in totals. Causal interpretation needs further assumptions.**

Chapter 16’s fictional users have 8+18 = 26 successes among 10+90 = 100 people. Nonusers have 63+1 = 64 among 90+10 = 100. The aggregate difference is 26%−64% = −38 percentage points.

Standardizing each task to half the population gives users 0.5×0.8+0.5×0.2 = 0.5 and nonusers 0.5×0.7+0.5×0.1 = 0.4, a +10-point difference.

Let Y(a) be a potential outcome, L pre-intervention task type, and A actual intervention. Under suitable identification conditions including consistency, conditional exchangeability given L, and positivity, standardization gives

E[Y(a)] = Σl E[Y｜A=a, L=l] P(L=l)

This connects a population’s average intervention outcome to observed quantities.<a id="cite-56"></a>[[56]](19_references.md#ref-56) The calculation alone cannot establish its conditions.

[Return to Chapter 16](16_causality.md)

<a id="note-h"></a>
<a id="h-9"></a>

## H. Comparing Four Correlations in a Quantum Question

**What this shows: models with local outcomes expressed using the same hidden variable face a correlation bound that quantum theory can exceed.**

At two sites, choose measurement settings 0 or 1 and record outcomes +1 or −1. Given a common hidden variable λ, assume each outcome depends only on its local setting, not the distant one. Write A0, A1, B0, B1 and begin with outcomes determined by λ.

For one λ,

Sλ = A0 B0 + A0 B1 + A1 B0 − A1 B1

= A0(B0+B1) + A1(B0−B1)

If B0 and B1 have equal signs, the second parentheses are zero and the first ±2. With opposite signs, the first are zero and the second ±2. Since A is also ±1, Sλ is always +2 or −2.

Assume the distribution of λ is independent of setting choices and average over that same distribution. With Eab = average[Aa Bb],

**|E00 + E01 + E10 − E11| ≤ 2**

This is one form of CHSH.<a id="cite-61"></a>[[61]](19_references.md#ref-61) Stochastic local models can likewise be represented by including local randomness. Local factorization and independence between settings and hidden variables are part of the argument’s conditions.

For a quantum spin singlet, the correlation for unit directions a and b is −a·b. With orthogonal unit vectors x and z, choose a0 = z, a1 = x, b0 = (z+x)/√2, b1 = (z−x)/√2. Three correlations are −1/√2 and E11 is +1/√2. The absolute combination becomes 2√2 ≈ 2.828.

This calculation is not an observation of quantum predictions. It identifies differing predictions so an experiment can be designed. Detection loopholes, site separation, setting choices, and finite-sample testing belong to the experiment.<a id="cite-12"></a>[[12]](19_references.md#ref-12) The example connects assumptions, mathematics, and observation while distinguishing them.

[Return to Chapter 6](06_quantum.md)

<a id="note-i"></a>
<a id="h-10"></a>

## I. One Bit and a Lower Bound on Heat

**What this shows: in the standard complete erasure of symmetric classical memory, memory entropy reduction connects to the heat bath’s balance.**

Assume initial probabilities 1/2 for zero and one, without correlations to other systems. Memory entropy is

Sinitial = −kB{(1/2)ln(1/2) + (1/2)ln(1/2)} = kB ln 2

After completely resetting to zero, logical-state uncertainty vanishes and this entropy contribution is zero. Its change is −kB ln 2.

For the standard isothermal model restoring symmetric memory structure and releasing heat Q to a bath at T, the bath’s entropy change is Q/T. Nondecreasing total entropy requires

−kB ln 2 + Q/T ≥ 0

Thus, on average, Q ≥ kB T ln 2. With kB = 1.380649×10⁻²³ joules per kelvin and T = 300 kelvin, the result is about 2.871×10⁻²¹ joules.<a id="cite-24"></a>[[24]](19_references.md#ref-24)<a id="cite-58"></a>[[58]](19_references.md#ref-58)<a id="cite-63"></a>[[63]](19_references.md#ref-63)

This single formula does not cover imperfect erasure, biased initial probabilities, using correlations with other systems, or quantum memories. Single-run fluctuations in small systems differ from repeated-run averages. Approaching the bound in a sufficiently slow limit also differs from achieving the same performance in finite time.<a id="cite-25"></a>[[25]](19_references.md#ref-25)[[63]](19_references.md#ref-63)

[Return to Chapter 8](08_information.md)

---

[Read the opening conclusions](00_conclusions.md#h-1) ｜ [Contents](../README.md#toc) ｜ [References](19_references.md#h-1) ｜ [Previous chapter](17_synthesis.md#h-1) ｜ [Next chapter](19_references.md#h-1)
