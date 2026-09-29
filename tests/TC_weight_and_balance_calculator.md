# Test Case Document — Aircraft Weight & Balance Calculator

**Test Case ID:** FHD2026SEP27WBC
**Requirement Link:** `weight_and_balance_calculator.py`
**Tester:** Roberto Natera
**Date:** 2026-09-27
**Methodology:** Waterfall

---

## 1. Scope and Objectives

Validate the computational accuracy of `weight_and_balance_calculator.py`.
The script must convert fuel quantity from gallons to pounds and sum four
weight components into a total ramp weight.

Unlike the decision-logic programs in this repository, this script
contains no conditional branches. Testing therefore targets
**computational correctness, precision, and input handling** rather than
branch coverage.

## 2. Acceptance Criteria

The software passes validation when:

- Fuel converts from gallons to pounds at the correct density constant
- All four weight components are included in the total, none dropped
- Results match independently hand-calculated values
- Floating-point behavior is documented and within acceptable tolerance

## 3. Test Environment

| Item      | Value                                                   |
| --------- | ------------------------------------------------------- |
| Editor    | Visual Studio Code                                      |
| Runtime   | Python 3.x                                              |
| OS        | macOS (portable to Windows/Linux)                       |
| Execution | Manual, terminal                                        |
| Oracle    | Hand calculation, verified independently of source code |

## 4. Requirements Under Test

| Req ID | Rule                                                                                                                  |
| ------ | --------------------------------------------------------------------------------------------------------------------- |
| R1     | Accept four numeric inputs: aircraft empty weight (lb), fuel quantity (gal), passenger weight (lb), cargo weight (lb) |
| R2     | Convert fuel to pounds at 6.8 lb/gal (Jet-A)                                                                          |
| R3     | Total ramp weight = empty weight + fuel weight + passenger weight + cargo weight                                      |
| R4     | Display the total ramp weight in pounds                                                                               |

---

## 5. Test Suite — Computational Accuracy

All expected values hand-calculated independently of the source code.

| ID     | Objective                    | Empty   | Fuel (gal) | Pax    | Cargo   | Expected Fuel (lb) | Expected Ramp (lb) | Status   |
| :----- | :--------------------------- | :------ | :--------- | :----- | :------ | :----------------- | :----------------- | :------- |
| WBC-01 | Typical loadout              | 32000   | 1200       | 850    | 1000    | 8160.0             | 42010.0            | **Pass** |
| WBC-02 | Conversion constant isolated | 0       | 100        | 0      | 0       | 680.0              | 680.0              | **Pass** |
| WBC-03 | Single gallon                | 0       | 1          | 0      | 0       | 6.8                | 6.8                | **Pass** |
| WBC-04 | Zero fuel — dry weight only  | 32000   | 0          | 850    | 1000    | 0.0                | 33850.0            | **Pass** |
| WBC-05 | All components zero          | 0       | 0          | 0      | 0       | 0.0                | 0.0                | **Pass** |
| WBC-06 | Large values                 | 500000  | 50000      | 10000  | 25000   | 340000.0           | 875000.0           | **Pass** |
| WBC-07 | Decimal inputs throughout    | 32000.5 | 1200.25    | 850.75 | 1000.25 | 8161.7             | 42013.2            | **Pass** |

## 6. Test Suite — Component Isolation

Each run isolates one component to confirm no term is dropped from the sum.

| ID     | Component isolated | Empty | Fuel | Pax  | Cargo | Expected Ramp | Status   |
| :----- | :----------------- | :---- | :--- | :--- | :---- | :------------ | :------- |
| WBC-08 | Empty weight only  | 1000  | 0    | 0    | 0     | 1000.0        | **Pass** |
| WBC-09 | Fuel only          | 0     | 10   | 0    | 0     | 68.0          | **Pass** |
| WBC-10 | Passenger only     | 0     | 0    | 1000 | 0     | 1000.0        | **Pass** |
| WBC-11 | Cargo only         | 0     | 0    | 0    | 1000  | 1000.0        | **Pass** |

**Tester note:** a dropped term is invisible in WBC-01 if the missing
component happens to be small. Isolating each to 1000 lb against three
zeros makes an omission unmissable.

## 7. Test Suite — Floating-Point Precision

6.8 has no exact binary representation. These cases probe for artifacts.
All non-fuel fields set to 0 unless stated.

| ID      | Objective                 | Empty | Fuel (gal) | Pax | Cargo | Nominal Result | Actual Output | Artifact? | Status |
| :------ | :------------------------ | :---- | :--------- | :-- | :---- | :------------- | :------------ | :-------- | :----- |
| WBC-F01 | Small odd multiplier      | 0     | 3          | 0   | 0     | 20.4           |               |           |        |
| WBC-F02 | Fractional gallons        | 0     | 0.5        | 0   | 0     | 3.4            |               |           |        |
| WBC-F03 | Repeating-decimal input   | 0     | 0.1        | 0   | 0     | 0.68           |               |           |        |
| WBC-F04 | Accumulated sum precision | 0.1   | 0.1        | 0.1 | 0.1   | 0.98           |               |           |        |

**Actual Output must be recorded character for character.** A result of
`20.400000000000002` is expected IEEE 754 behavior, not an arithmetic
failure — but it is a presentation defect for a weight readout.

## 8. Test Suite — Negative / Invalid Input

| ID      | Objective                   | Input       | Expected Result                  | Actual Result                                                                                           | Status   |
| :------ | :-------------------------- | :---------- | :------------------------------- | :------------------------------------------------------------------------------------------------------ | :------- |
| WBC-N01 | Non-numeric weight          | `abc`       | Graceful error, reprompt         | Unhandled `ValueError`, program terminated with stack trace: `could not convert string to float: 'abc'` | **Fail** |
| WBC-N02 | Empty input (Enter only)    | ``          | Graceful error, reprompt         | Unhandled `ValueError`, program terminated: `could not convert string to float: ''`                     | **Fail** |
| WBC-N03 | Negative empty weight       | `-32000`    | Rejected as physically invalid   | Accepted. Output: `Total ramp weight: -32000.0 pounds`                                                  | **Fail** |
| WBC-N04 | Negative fuel quantity      | `-500`      | Rejected as physically invalid   | Accepted. Output: `Total ramp weight: -500.0 pounds`                                                    | **Fail** |
| WBC-N05 | Comma-separated thousands   | `32,000`    | Accepted or clear error          | Unhandled `ValueError`, program terminated: `could not convert string to float: '32,000'`               | **Fail** |
| WBC-N06 | Whitespace-padded numeric   | `    32000` | Accepted as 32000                | Accepted. Output: `Total ramp weight: 32000.0 pounds`                                                   | **Pass** |
| WBC-N07 | Scientific notation         | `1e6`       | Accepted as 1000000 or rejected  | Silently accepted. Output: `Total ramp weight: 1000000.0 pounds`                                        | **Fail** |
| WBC-N08 | Implausible aircraft weight | `99999999`  | Rejected or flagged out of range | Accepted. Output: `Total ramp weight: 99999999.0 pounds`                                                | **Fail** |

**Tester note:** WBC-N05 and WBC-N07 are the interesting pair. `float()`
rejects `32,000` with a `ValueError` but silently accepts `1e6` as one
million. A user typing a comma gets a crash; a user typing `1e6` gets a
number a thousand times larger than intended, with no warning either way.

## 9. Defect Log

| Defect ID | Related Test      | Severity   | Description                                                                                                                                                                                                              | Status |
| :-------- | :---------------- | :--------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----- |
| DEF-03    | WBC-N01, N02, N05 | **High**   | Non-numeric, empty, and comma-formatted input cause an unhandled `ValueError` and terminate the program with a stack trace. No validation and no reprompt — a typo on the fourth input discards the first three entries. | Open   |
| DEF-04    | WBC-N03, N04      | **High**   | Negative weights accepted without validation. A ramp weight of `-32000.0` lb is displayed as a valid result. Physically impossible values are neither rejected nor flagged.                                              | Open   |
| DEF-05    | WBC-N07           | **Medium** | Scientific notation silently accepted. `1e6` is interpreted as 1,000,000 lb with no confirmation. A mistyped entry returns a result three orders of magnitude off with no indication.                                    | Open   |
| DEF-06    | WBC-N08           | **Medium** | No upper bound on any input. 99,999,999 lb — roughly 100x the max takeoff weight of an An-225 — is accepted and reported as valid.                                                                                       | Open   |

**Severity rationale:** DEF-03 and DEF-04 are both High for opposite
reasons. DEF-03 fails loudly — the user knows something broke. DEF-04
fails silently and returns a confident wrong answer. For a preflight
tool, silent wrong output is the more dangerous of the two.

**Root cause:** all four defects share one cause — no input validation.
A single validation layer closes all of them.

**Remediation dependency:** graceful error handling requires `try`/`except`
(Angela Yu Day 30). Range and sign checks are implementable now with
`if` statements. Recommend implementing range checks immediately and
deferring exception handling to the Day 30 refactor.

## 10. Observations (Non-Defect / Requirements Gap)

| ID     | Description                                                                                                                                                                                                                                                                                                     |
| :----- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OBS-01 | **The program does not perform balance calculation.** Despite its name it computes total weight only — no arm, moment, or center of gravity. A true weight and balance computation requires station arms and a CG envelope check. Current scope is weight summation and the program name overstates it.         |
| OBS-02 | **No maximum gross weight check.** The program reports a ramp weight but never compares it against an aircraft limit. A result of 90,000 lb on a 66,000 lb airframe is displayed with no warning. For a preflight tool, the absence of a limit check is the difference between a calculator and a safety check. |
| OBS-03 | **Fuel density hardcoded at 6.8 lb/gal with no fuel type selection.** 6.8 is Jet-A; avgas is approximately 6.0 lb/gal. A piston aircraft loadout computed with this tool overstates fuel weight by roughly 13%. The constant is also unnamed in the source — a magic number with no comment.                    |
| OBS-04 | **No unit enforcement on input.** Nothing prevents a user entering fuel in pounds rather than gallons, which would inflate the result 6.8x with no indication.                                                                                                                                                  |

## 11. Summary

| Metric           | Count                |
| ---------------- | -------------------- |
| Total test cases | 23                   |
| Executed         | 19                   |
| Passed           | 12                   |
| Failed           | 7                    |
| Not yet executed | 4 (WBC-F01 – F04)    |
| Defects raised   | 4 (2 High, 2 Medium) |

**Assessment:** computational logic is correct across all accuracy and
isolation cases. Every failure is in input handling, not arithmetic. The
program calculates correctly and validates nothing.

---

_Manual test documentation. Automated unit tests (`pytest`) to follow
once the calculation is refactored into a function that accepts
parameters and returns a value rather than reading `input()` and
printing directly. This program is the strongest pytest candidate in the
repository — pure arithmetic with no I/O in the logic once refactored._
