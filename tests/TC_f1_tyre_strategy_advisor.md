# Test Case Document — F1 Tyre Strategy Advisor

**Test Case ID:** FHD2026SEP24TSA
**Requirement Link:** `f1_tyre_strategy_advisor.py`
**Tester:** Roberto Natera
**Date:** 2026-09-24
**Methodology:** Waterfall

---

## 1. Scope and Objectives

Validate the full functionality of `f1_tyre_strategy_advisor.py`. The
script must evaluate three race parameters — track temperature (°F),
laps remaining, and tyre age (laps) — and output the correct pit
strategy call based on predefined tyre degradation logic.

## 2. Acceptance Criteria

The software passes validation when:

- Every branch of the `if / elif / else` chain triggers its correct output
- All boundary values resolve to the correct side of their threshold
- The compound `and` condition in R2 fires only when both operands are true
- Rules evaluate in documented order, with the first matching rule winning

## 3. Test Environment

| Item           | Value                             |
| -------------- | --------------------------------- |
| Editor         | Visual Studio Code                |
| Runtime        | Python 3.x                        |
| OS             | macOS (portable to Windows/Linux) |
| Execution      | Manual, terminal                  |
| Allocated time | < 30 minutes                      |

## 4. Requirements Under Test

| Req ID | Rule                                                                                                       |
| ------ | ---------------------------------------------------------------------------------------------------------- |
| R1     | Tyre age above 25 laps → `BOX BOX BOX.`                                                                    |
| R2     | Track temp above 113°F **AND** tyre age above 18 laps → `Box now, new strategy; we are taking mediums.`    |
| R3     | Laps remaining strictly between 10 and 20 → `Consider a short stint on softs.`                             |
| R4     | All other conditions → `Stay out is Hammer Time!`                                                          |
| R5     | Rules evaluate in order R1 → R2 → R3 → R4; the first rule that matches wins and no later rule is evaluated |

**Note on units:** the 113°F threshold derives from a 45°C requirement
(45 × 9/5 + 32 = 113). See DEF-02.

---

## 5. Test Suite — R1: Critical Tyre Age

Other variables are set to values that would otherwise trigger lower
rules, proving R1 correctly overrides them.

| ID     | Objective                        | Temp | Age | Laps | Expected Result | Actual Result | Status |
| :----- | :------------------------------- | :--- | :-- | :--- | :-------------- | :------------ | :----- |
| TSA-01 | R1 fires and overrides R2 and R3 | 120  | 26  | 15   | `BOX BOX BOX.`  |               |        |

## 6. Test Suite — R2: Compound Condition Truth Table

`tyre_age` held at 25 or below so R1 does not interfere.
`laps_remaining` locked at 30 so any failure falls cleanly to R4.

| ID  | temp > 113 | age > 18 | Temp | Age | Laps | Expected Result | Actual Result | Status |
| :-- | :--------- | :------- | :--- | :-- | ---- | --------------- | ------------- | ------ |
