# Test Case Document — Go / No-Go Weather Minimums Checker

**Test Case ID:** FHD2026SEP19WMC
**Requirement Link:** `weather_minimums_checker.py`
**Tester:** Roberto Natera
**Date:** 2026-09-19
**Methodology:** Waterfall

**Result: 25 executed · 21 passed · 4 failed · 84% pass rate**

---

## 1. Scope and Objectives

Validate the full functionality of `weather_minimums_checker.py`. The script
must accurately evaluate three flight weather parameters — ceiling (ft),
visibility (statute miles), and crosswind component (kt) — and output the
correct flight decision based on predefined aviation safety logic.

## 2. Acceptance Criteria

The software passes validation when:

- Every branch of the `if / elif / else` chain triggers its correct output
- All boundary values resolve to the correct side of their threshold
- Numeric inputs are correctly converted to float and evaluated in sequence

## 3. Test Environment

| Item | Value |
| --- | --- |
| Editor | Visual Studio Code |
| Runtime | Python 3.x |
| OS | macOS (portable to Windows/Linux) |
| Execution | Manual, terminal |
| Allocated time | < 30 minutes |

## 4. Requirements Under Test

| Req ID | Rule |
| --- | --- |
| R1 | Ceiling below 1000 ft → NO-GO |
| R2 | Visibility below 3 SM → NO-GO |
| R3 | Crosswind above 25 kt → NO-GO |
| R4 | Ceiling below 3000 ft (and R1–R3 not triggered) → CAUTION, IFR |
| R5 | All else → GO, VFR |
| R6 | Conditions evaluate in order R1/R2 → R3 → R4 → R5 |

---

## 5. Test Suite — Functional Coverage

| ID | Objective | Ceiling | Vis | Xwind | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WMC-01 | NO-GO on low ceiling | 900 | 5 | 10 | `Poor weather condition. Decision: NO-GO` | Poor weather condition. Decision: NO-GO | PASS |
| WMC-02 | NO-GO on low visibility | 5000 | 2 | 10 | `Poor weather condition. Decision: NO-GO` | Poor weather condition. Decision: NO-GO | PASS |
| WMC-03 | NO-GO on excessive crosswind | 5000 | 5 | 30 | `Crosswind winds too high; over the aircraft limitation. Decision: NO-GO` | Crosswind winds too high; over the aircraft limitation. Decision: NO-GO | PASS |
| WMC-04 | CAUTION on IFR ceiling | 2500 | 5 | 15 | `IFR pilot rating required. CAUTION - IFR CONDITIONS` | IFR pilot rating required. CAUTION - IFR CONDITIONS | PASS |
| WMC-05 | GO on VFR conditions | 3500 | 5 | 15 | `VFR CONDITIONS` | VFR CONDITIONS | PASS |

**5 of 5 passed.**

---

## 6. Test Suite — Boundary Value Analysis

Each threshold is tested at the value below, at, and above the limit.

### 6.1 Ceiling — 1000 ft NO-GO threshold (R1)

| ID | Ceiling | Vis | Xwind | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WMC-B01 | 999 | 5 | 5 | `Poor weather condition. Decision: NO-GO` | Poor weather condition. Decision: NO-GO | PASS |
| WMC-B02 | 1000 | 5 | 5 | `IFR pilot rating required. CAUTION - IFR CONDITIONS` | IFR pilot rating required. CAUTION - IFR CONDITIONS | PASS |
| WMC-B03 | 1001 | 5 | 5 | `IFR pilot rating required. CAUTION - IFR CONDITIONS` | IFR pilot rating required. CAUTION - IFR CONDITIONS | PASS |

### 6.2 Visibility — 3 SM NO-GO threshold (R2)

| ID | Ceiling | Vis | Xwind | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WMC-B04 | 5000 | 2.9 | 5 | `Poor weather condition. Decision: NO-GO` | Poor weather condition. Decision: NO-GO | PASS |
| WMC-B05 | 5000 | 3.0 | 5 | `VFR CONDITIONS` | VFR CONDITIONS | PASS |
| WMC-B06 | 5000 | 3.1 | 5 | `VFR CONDITIONS` | VFR CONDITIONS | PASS |

### 6.3 Crosswind — 25 kt NO-GO threshold (R3)

| ID | Ceiling | Vis | Xwind | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WMC-B07 | 5000 | 5 | 25 | `VFR CONDITIONS` | VFR CONDITIONS | PASS |
| WMC-B08 | 5000 | 5 | 25.1 | `Crosswind winds too high; over the aircraft limitation. Decision: NO-GO` | Crosswind winds too high; over the aircraft limitation. Decision: NO-GO | PASS |
| WMC-B09 | 5000 | 5 | 26 | `Crosswind winds too high; over the aircraft limitation. Decision: NO-GO` | Crosswind winds too high; over the aircraft limitation. Decision: NO-GO | PASS |

### 6.4 Ceiling — 3000 ft IFR threshold (R4)

| ID | Ceiling | Vis | Xwind | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WMC-B10 | 2999 | 5 | 5 | `IFR pilot rating required. CAUTION - IFR CONDITIONS` | IFR pilot rating required. CAUTION - IFR CONDITIONS | PASS |
| WMC-B11 | 3000 | 5 | 5 | `VFR CONDITIONS` | VFR CONDITIONS | PASS |
| WMC-B12 | 3001 | 5 | 5 | `VFR CONDITIONS` | VFR CONDITIONS | PASS |

**12 of 12 passed.** Every threshold resolves to the correct side of its limit.

---

## 7. Test Suite — Evaluation Order (R6)

| ID | Objective | Ceiling | Vis | Xwind | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| WMC-P01 | Ceiling takes precedence over crosswind | 500 | 5 | 30 | `Poor weather condition. Decision: NO-GO` | Poor weather condition. Decision: NO-GO | PASS |
| WMC-P02 | Visibility takes precedence over crosswind | 5000 | 1 | 30 | `Poor weather condition. Decision: NO-GO` | Poor weather condition. Decision: NO-GO | PASS |

**2 of 2 passed.**

**Tester note — not a defect.** Because the script evaluates
`ceiling < 1000 or visibility < 3` before it evaluates crosswind, a scenario
with both a 500 ft ceiling and a 30 kt crosswind reports "Poor weather
condition" rather than "Crosswind winds too high." Only the first failing
condition is reported.

This is expected behavior given the current `elif` structure, and the decision
returned is correct — NO-GO either way. But the output does not tell the pilot
that a second limit was also exceeded. The decision is right; the information
is incomplete.

---

## 8. Test Suite — Negative / Invalid Input

| ID | Objective | Input | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| WMC-N01 | Non-numeric ceiling | `abc` | Graceful error message, reprompt | `ValueError: could not convert string to float: 'abc'` — program terminates | **FAIL** |
| WMC-N02 | Empty input (Enter only) | `` | Graceful error message, reprompt | `ValueError: could not convert string to float: ''` — program terminates | **FAIL** |
| WMC-N03 | Negative ceiling | `-500` | Rejected as physically invalid | Accepted. Evaluated normally and returned `Poor weather condition. Decision: NO-GO` | **FAIL** |
| WMC-N04 | Negative crosswind | `-10` | Rejected as physically invalid | Accepted. Evaluated normally and passed through to a GO decision | **FAIL** |
| WMC-N05 | Whitespace-padded numeric | `  5000  ` | Accepted, treated as 5000 | Accepted and evaluated correctly | PASS |

**1 of 5 passed.** All four failures trace to the same root cause: the program
converts input directly to float and evaluates it without validating that the
value is well-formed or physically possible.

---

## 9. Defect Log

| Defect ID | Related Test | Severity | Description | Status |
| :--- | :--- | :--- | :--- | :--- |
| DEF-001 | WMC-N01, WMC-N02 | Major | Non-numeric and empty input raise an unhandled `ValueError` and terminate the program. Expected behavior is a caught exception, an error message, and a reprompt. A single typo ends the session and discards prior input. | Open |
| DEF-002 | WMC-N04 | Major | Negative crosswind accepted as valid. `-10` fails the `> 25` check and passes through toward a GO decision. A physically impossible value produces a permissive result. | Open |
| DEF-003 | WMC-N03 | Minor | Negative ceiling accepted as valid. `-500` satisfies `ceiling < 1000` and returns NO-GO — the safe answer, reached by coincidence rather than by validation. | Open |

### Note on DEF-002 vs DEF-003

Both defects accept a physically impossible value, but they fail in opposite
directions.

A negative ceiling satisfies the low-ceiling check and returns NO-GO — wrong
input, safe output. A negative crosswind fails the high-crosswind check and
passes through toward GO — wrong input, permissive output.

DEF-003 is masked by a conservative default. DEF-002 is not. Severity reflects
the direction of the failure, not just its presence.

### Recommended remediation

| Defect | Fix |
| :--- | :--- |
| DEF-001 | Wrap each input in `try` / `except ValueError` with a reprompt loop |
| DEF-002, DEF-003 | Add range validation before evaluation — reject negative values for all three parameters, and reject implausible upper bounds |

---

## 10. Summary

| Metric | Count |
| --- | --- |
| Total test cases | 25 |
| Executed | 25 |
| Passed | 21 |
| Failed | 4 |
| Blocked | 0 |
| **Pass rate** | **84%** |

### By suite

| Suite | Cases | Passed | Failed |
| :--- | :--- | :--- | :--- |
| Functional coverage | 5 | 5 | 0 |
| Boundary value analysis | 12 | 12 | 0 |
| Evaluation order | 2 | 2 | 0 |
| Negative / invalid input | 5 | 1 | 4 |

### Assessment

**The decision logic is sound.** Every functional branch triggers correctly,
every threshold resolves to the correct side of its boundary, and evaluation
order behaves as specified. Nineteen of nineteen positive-path cases passed.

**Input handling is not.** All four failures fall in the negative input suite,
and all four trace to a single root cause: the program converts input directly
to float and evaluates it without validating that the value is well-formed or
physically possible.

That distinction matters for how the work is prioritized. The logic does not
need rework — it needs a validation layer in front of it.

---

_Manual test documentation. Automated unit tests to follow once the program's
decision logic is refactored into testable functions that return values rather
than printing directly._
