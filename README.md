# Python Projects 🐍

Applied Python — fundamentals, control flow, and object-oriented programming,
built through aviation and motorsport domain problems. U.S. Navy veteran with
15 years in aviation QA and critical systems.

## 📁 Projects

| Project                                  | What it does                                                                                                                                    |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `band_name_generator.py`                 | Generates a band name from your city and pet's name (input + f-strings)                                                                         |
| `tip_calculator.py`                      | Calculates each person's share of a bill, including tip, split among a group                                                                    |
| `treasure_island.py`                     | Branching text adventure built from a flowchart — every choice leads to a different ending                                                      |
| `rock_paper_scissors.py`                 | Classic game vs. the computer — random choice, ASCII art, and win/lose/tie logic                                                                |
| `password_generator.py`                  | Builds a strong, randomized password from user-chosen counts of letters, numbers, and symbols                                                   |
| `hangman.py`                             | Word-guessing game — pulls a random word, tracks guesses with a live blank display, counts lives with ASCII stages, and handles win/lose logic  |
| `pilot_callsign.py`                      | Creates a pilot callsign from your name and aircraft type (input + string concatenation)                                                        |
| `f1_race_name_generator.py`              | Generates an F1 driver nickname from your name, team, and nationality (input + f-strings)                                                       |
| `weight_and_balance_calculator.py`       | Computes aircraft ramp weight from empty weight, fuel (converted to pounds), passengers, and cargo                                              |
| `f1_pitstop_fuel_calculator.py`          | Calculates fuel needed to finish a race from laps remaining, burn rate, and current fuel                                                        |
| `weather_minimums_checker.py`            | Aviation go/no-go checker evaluating ceiling, visibility, and crosswind against flight minimums                                                 |
| `f1_tyre_strategy_advisor.py`            | Recommends an F1 pit/tyre strategy from track temp, laps remaining, and tyre age (if/elif/else + and/or logic)                                  |
| `tower_departure_clearance_generator.py` | Generates a randomized ATC departure clearance with runway, holding point, and four-digit squawk code                                           |
| `f1_grid_position_generator.py`          | Assigns a random team, tyre compound, and grid position to a named driver (lists + random module)                                               |
| `flight_log_analyzer.py`                 | Totals, longest flight, average, and count over 2 hours from a list of flight times (for loops + accumulators)                                  |
| `f1_race_pace_analyzer.py`               | Analyzes a 10-lap stint — total time, fastest lap, average pace, and laps under average (real 2026 Madrid GP data)                              |
| `radio_call_generator.py`                | Sequential ATC radio calls from startup through departure, each phase its own function (def + function calls)                                   |
| `oop_practice.py`                        | Object-oriented programming — classes, attributes, inheritance, multiple inheritance, special methods (`__len__`), `@property`, `@staticmethod` |

## 🧪 Testing

Manual test documentation lives in [`tests/`](tests/).

Applying 15 years of aviation quality assurance to software: each test
document covers functional coverage, boundary value analysis, evaluation
order, and negative input testing, with a defect log for findings.

| Document                                                                 | Covers                                                                                                           | Cases |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ----- |
| [`TC_weather_minimums_checker.md`](tests/TC_weather_minimums_checker.md) | Go/No-Go decision logic — all branches, threshold boundaries, invalid input                                      | 25    |
| [`TC_f1_tyre_strategy_advisor.md`](tests/TC_f1_tyre_strategy_advisor.md) | Tyre strategy decision logic — compound `and` truth table, threshold boundaries, evaluation order, invalid input | 29    |

Automated unit tests (`pytest`) to follow once program logic is refactored
into functions that return values rather than printing directly.

## 🛠️ How to run

Each file is standalone Python:

```bash
python3 filename.py
```

`hangman.py` requires the `random-word` package: `pip install random-word`

## 📚 Concepts covered

**Core** — variables, I/O, f-strings, data types and conversion, math operations
**Control flow** — `if`/`elif`/`else`, nested conditions, `and`/`or` for multi-case logic
**Collections** — lists, indexing, `.append()`, iteration
**Loops** — `for` with `range()`, `while` loops, accumulator and running-best patterns
**Functions** — definition and calls, `return`, the `if __name__ == "__main__":` entry-point guard
**OOP** — classes, inheritance, multiple inheritance, dunder methods, decorators
**Modules** — `random`, `string`, installing external packages with `pip`
**Strings** — `.strip()`, `.lower()`, `.join()` for cleaning and formatting
**Quality assurance** — manual test case design, boundary value analysis, negative testing, defect logging
**Practice** — translating flowcharts into code, consistent style, meaningful Git commits

---

_Aviation and motorsport domain problems — because the problems you care about are the ones you finish._
