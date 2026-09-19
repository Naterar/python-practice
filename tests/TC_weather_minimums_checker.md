# Test Case Document — Go / No-Go Weather Minimums Checker

**Test Case ID:** FHD2026SEP19WMC
**Requirement Link:** `weather_minimums_checker.py`
**Tester:** Roberto Natera
**Date:** 2026-09-19
**Methodology:** Waterfall

---

## 1. Scope and Objectives

Validate the full functionality of `weather_minimums_checker.py`. The
script must accurately evaluate three flight weather parameters —
ceiling (ft), visibility (statute miles), and crosswind component (kt) —
and output the correct flight decision based on predefined aviation
safety logic.

## 2. Acceptance Criteria

The software passes validation when:

- Every branch of the `if / elif / else` chain triggers its correct output
- All boundary values resolve to the correct side of their threshold
- Numeric inputs are correctly converted to float and evaluated in sequence

## 3. Test Environment

| Item           | Value                             |
| -------------- | --------------------------------- |
| Editor         | Visual Studio Code                |
| Runtime        | Python 3.x                        |
| OS             | macOS (portable to Windows/Linux) |
| Execution      | Manual, terminal                  |
| Allocated time | < 30 minutes                      |

## 4. Requirements Under Test

| Req ID | Rule                                                           |
| ------ | -------------------------------------------------------------- |
| R1     | Ceiling below 1000 ft → NO-GO                                  |
| R2     | Visibility below 3 SM → NO-GO                                  |
| R3     | Crosswind above 25 kt → NO-GO                                  |
| R4     | Ceiling below 3000 ft (and R1–R3 not triggered) → CAUTION, IFR |
| R5     | All else → GO, VFR                                             |
| R6     | Conditions evaluate in order R1/R2 → R3 → R4 → R5              |

---

## 5. Test Suite — Functional Coverage

| ID     | Objective                    | Ceiling | Vis | Xwind | Expected Result                                                           | Actual Result | Status |
| :----- | :--------------------------- | :------ | :-- | :---- | :------------------------------------------------------------------------ | :------------ | :----- |
| WMC-01 | NO-GO on low ceiling         | 900     | 5   | 10    | `Poor weather condition. Decision: NO-GO`                                 |               |        |
| WMC-02 | NO-GO on low visibility      | 5000    | 2   | 10    | `Poor weather condition. Decision: NO-GO`                                 |               |        |
| WMC-03 | NO-GO on excessive crosswind | 5000    | 5   | 30    | `Crosswind winds too high; over the aircraft limitation. Decision: NO-GO` |               |        |
| WMC-04 | CAUTION on IFR ceiling       | 2500    | 5   | 15    | `IFR pilot rating required. CAUTION - IFR CONDITIONS`                     |               |        |
| WMC-05 | GO on VFR conditions         | 3500    | 5   | 15    | `VFR CONDITIONS`                                                          |               |        |

## 6. Test Suite — Boundary Value Analysis

Each threshold is tested at the value below, at, and above the limit.

### 6.1 Ceiling — 1000 ft NO-GO threshold (R1)

| ID      | Ceiling | Vis | Xwind | Expected Result                                       | Actual Result | Status |
| :------ | :------ | :-- | :---- | :---------------------------------------------------- | :------------ | :----- |
| WMC-B01 | 999     | 5   | 5     | `Poor weather condition. Decision: NO-GO`             |               |        |
| WMC-B02 | 1000    | 5   | 5     | `IFR pilot rating required. CAUTION - IFR CONDITIONS` |               |        |
| WMC-B03 | 1001    | 5   | 5     | `IFR pilot rating required. CAUTION - IFR CONDITIONS` |               |        |

### 6.2 Visibility — 3 SM NO-GO threshold (R2)

| ID      | Ceiling | Vis | Xwind | Expected Result                           | Actual Result | Status |
| :------ | :------ | :-- | :---- | :---------------------------------------- | :------------ | :----- |
| WMC-B04 | 5000    | 2.9 | 5     | `Poor weather condition. Decision: NO-GO` |               |        |
| WMC-B05 | 5000    | 3.0 | 5     | `VFR CONDITIONS`                          |               |        |
| WMC-B06 | 5000    | 3.1 | 5     | `VFR CONDITIONS`                          |               |        |

### 6.3 Crosswind — 25 kt NO-GO threshold (R3)

| ID      | Ceiling | Vis | Xwind | Expected Result                                                           | Actual Result | Status |
| :------ | :------ | :-- | :---- | :------------------------------------------------------------------------ | :------------ | :----- |
| WMC-B07 | 5000    | 5   | 25    | `VFR CONDITIONS`                                                          |               |        |
| WMC-B08 | 5000    | 5   | 25.1  | `Crosswind winds too high; over the aircraft limitation. Decision: NO-GO` |               |        |
| WMC-B09 | 5000    | 5   | 26    | `Crosswind winds too high; over the aircraft limitation. Decision: NO-GO` |               |        |

### 6.4 Ceiling — 3000 ft IFR threshold (R4)

| ID      | Ceiling | Vis | Xwind | Expected Result                                       | Actual Result | Status |
| :------ | :------ | :-- | :---- | :---------------------------------------------------- | :------------ | :----- |
| WMC-B10 | 2999    | 5   | 5     | `IFR pilot rating required. CAUTION - IFR CONDITIONS` |               |        |
| WMC-B11 | 3000    | 5   | 5     | `VFR CONDITIONS`                                      |               |        |
| WMC-B12 | 3001    | 5   | 5     | `VFR CONDITIONS`                                      |               |        |

## 7. Test Suite — Evaluation Order (R6)

| ID      | Objective                                  | Ceiling | Vis | Xwind | Expected Result                           | Actual Result | Status |
| :------ | :----------------------------------------- | :------ | :-- | :---- | :---------------------------------------- | :------------ | :----- |
| WMC-P01 | Ceiling takes precedence over crosswind    | 500     | 5   | 30    | `Poor weather condition. Decision: NO-GO` |               |        |
| WMC-P02 | Visibility takes precedence over crosswind | 5000    | 1   | 30    | `Poor weather condition. Decision: NO-GO` |               |        |

**Tester note:** because the script evaluates `ceiling < 1000 or
visibility < 3` before it evaluates crosswind, a scenario with both a
500 ft ceiling and a 30 kt crosswind reports "Poor weather condition"
rather than "Crosswind winds too high." Only the first failing condition
is reported. This is expected behavior given the current `elif`
structure, not a defect — but it means the output does not tell the
pilot that a second limit was also exceeded.

## 8. Test Suite — Negative / Invalid Input

| ID      | Objective                 | Input      | Expected Result                  | Actual Result | Status |
| :------ | :------------------------ | :--------- | :------------------------------- | :------------ | :----- |
| WMC-N01 | Non-numeric ceiling       | `abc`      | Graceful error message, reprompt |               |        |
| WMC-N02 | Empty input (Enter only)  | ``         | Graceful error message, reprompt |               |        |
| WMC-N03 | Negative ceiling          | `-500`     | Rejected as physically invalid   |               |        |
| WMC-N04 | Negative crosswind        | `-10`      | Rejected as physically invalid   |               |        |
| WMC-N05 | Whitespace-padded numeric | `  5000  ` | Accepted, treated as 5000        |               |        |

## 9. Defect Log

| Defect ID | Related Test | Severity | Description | Status |
| :-------- | :----------- | :------- | :---------- | :----- |
|           |              |          |             |        |

## 10. Summary

| Metric           | Count |
| ---------------- | ----- |
| Total test cases | 25    |
| Executed         |       |
| Passed           |       |
| Failed           |       |
| Blocked          |       |

---

_Manual test documentation. Automated unit tests to follow once the
program's decision logic is refactored into testable functions that
return values rather than printing directly._
