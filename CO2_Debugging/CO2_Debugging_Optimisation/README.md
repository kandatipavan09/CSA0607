# CO2_Debugging_Optimisation — SentinelOps SOC Alert-Triage

## Repository contents
- `Pseudocode/`: pseudocode for sorting, blocklist lookup, signature matching, and closest pair.
- `Source_Code/original_buggy.py`: original faulty code as supplied.
- `Source_Code/corrected.py`: corrected algorithms preserving required output semantics.
- `Source_Code/optimized.py`: optimised code and assertions/test harness.
- `Report/CO2_Debugging_Optimisation_Report.docx`: full debugging, analysis and optimisation report.
- `Supporting_Files/`: raw execution logs, benchmark CSVs and graphs.
- `Screenshots/`: terminal-style execution screenshots.

## Run
Python 3.9+:
```bash
python Source_Code/original_buggy.py
python Source_Code/corrected.py
python Source_Code/optimized.py
```
The original file is intentionally buggy. Use `optimized.py` for the self-test harness; successful run prints `ALL OPTIMISED MODULE TESTS PASSED`.

## Key design decisions
- Stable insertion sort preserves equal-severity arrival order; production can use Python's stable Timsort for large/random batches.
- Convert blocklist to a set for repeated membership checks.
- KMP finds all signature occurrences in O(n+m).
- Closest-pair scan examines each unordered pair once and compares squared distances. It remains O(n²); no unsafe pruning is applied without spatial assumptions.

Before submitting, add your name/register number, rerun the tests, and upload this folder to your own GitHub repository.
