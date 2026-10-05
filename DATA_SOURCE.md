# Data source and licence

## Dataset

North Sea Transition Authority (NSTA), **UKCS hydrocarbon field production reports PPRS points (WGS84)**.

- Catalogue page: https://www.data.gov.uk/dataset/e2c7af85-8b52-4ecc-ab8d-c4f0639d5459/ukcs-hydrocarbon-field-production-reports-pprs-points-wgs84
- Publisher: North Sea Transition Authority
- Accessed: 3 October 2026
- Project extract: January 2021 to December 2025
- Project extract size: 21,479 monthly records and 48 source columns
- Licence shown by the catalogue: Open Government Licence v3.0, except where otherwise stated

## Scope warning

The records describe UKCS fields and PPRS reporting units. They are not individual-well production records. The dataset includes many operators and must not be described as a BP-only dataset. Operator names are stored with the monthly records because operators may change over time.

## Reproducibility

The raw CSV is preserved without editing in `data/raw`. The cleaning program creates a separate processed file. Missing values are retained as missing unless there is a documented reason to interpret them as zero.

