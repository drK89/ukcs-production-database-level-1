# UKCS Monthly Hydrocarbon Production Database

## Level 1 — Foundational / المستوى الأول — تأسيسي

**Full professional title:** UKCS Monthly Hydrocarbon Production Database: Relational Design, Data Quality and SQL Analysis

**العنوان العربي:** تصميم قاعدة بيانات علائقية وتحليل جودة بيانات الإنتاج الشهري للهيدروكربونات في الجرف القاري البريطاني

## Author | صاحب المشروع

**Dr Khaldoun Shaker**  
Petroleum & Reservoir Engineer | Energy Data Analytics  
Edinburgh, United Kingdom  

This independent portfolio project combines my petroleum and reservoir
engineering background with Python, SQL and energy data analytics. I reviewed
the methodology, engineering assumptions, analytical results and limitations.

© 2026 Khaldoun Shaker. All rights reserved.
## Project question / سؤال المشروع

**English:** How can a relational database be designed and queried to organise monthly UKCS hydrocarbon production data, assess its quality, and support reliable analysis using SQL and Python?

**العربي:** كيف يمكن تصميم قاعدة بيانات علائقية وتنفيذ استعلامات عليها لتنظيم بيانات الإنتاج الشهري للهيدروكربونات في الجرف القاري البريطاني، وفحص جودتها، ودعم تحليل موثوق باستخدام SQL وPython؟

## Project level and boundaries / المستوى والحدود

This is a complete, independent **Level 1 foundational project**. It demonstrates data inspection, cleaning, relational design, SQLite, SQL queries, basic Python analysis, charts, tests and documentation. Level 2 and Level 3 will be designed later as explicit upgrades; they are not silently mixed into this version.

هذا مشروع مستقل ومتكامل بالمستوى الأول. يوضح فحص البيانات وتنظيفها، تصميم قاعدة علائقية، استخدام SQLite وSQL، تحليلًا أساسيًا ببايثون، الرسوم، الاختبارات والتوثيق. لن نخلط إضافات المستوى الثاني أو الثالث بهذه النسخة قبل مناقشتها بصورة مستقلة.

## Dataset / البيانات

The project uses the official NSTA UKCS PPRS field-production dataset for the five complete calendar years 2021-2025:

- 21,479 monthly records
- 60 calendar months
- 394 named fields in the source extract
- 399 distinct reporting-unit keys after combining field, location and unit type
- 38 reported operator names
- oil, associated gas, dry gas, condensate, injection, flaring, venting and water measures

The records represent fields/reporting units, not individual wells. See `DATA_SOURCE.md` and `docs/DATA_DICTIONARY.md`.

## Database structure / هيكل قاعدة البيانات

The database contains four normalised tables:

1. `fields` — field identity, region and onshore/offshore status.
2. `reporting_units` — reporting unit and unit type, linked to a field.
3. `operators` — operator names reported in the source.
4. `monthly_production` — the monthly measurements, linked to a reporting unit and operator.

Operator is linked to each monthly record rather than stored permanently on the field because reported operators can change over time.

## Folder structure / هيكل الملفات

```text
ukcs_production_database_level_1/
├── README.md
├── DATA_SOURCE.md
├── requirements.txt
├── run_project.py
├── data/
│   ├── raw/nsta_ukcs_production_2021_2025.csv
│   └── processed/production_clean.csv
├── database/ukcs_production_level_1.sqlite
├── docs/DATA_DICTIONARY.md
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
├── src/
│   ├── prepare_data.py
│   ├── build_database.py
│   └── analyse_data.py
├── tests/test_database.py
└── outputs/
    ├── data_quality_profile.json
    ├── tables/
    └── charts/
```

## How to run / طريقة التشغيل

From the project directory:

```bash
python3 -m pip install -r requirements.txt
python3 run_project.py
python3 -m unittest discover -s tests -v
```

The first command installs the required packages. The second prepares the data, rebuilds the SQLite database, executes the analysis and generates outputs. The third runs database-integrity tests.

## Data-quality decisions / قرارات جودة البيانات

- The original raw extract is not overwritten.
- Missing measures remain missing and become SQL `NULL`.
- A missing oil value in a dry-gas reporting unit is not automatically treated as an error or zero.
- Negative production volumes are rejected by validation and database constraints.
- One monthly record is allowed per reporting-unit key and month.
- Oil and gas are not added together because they use different physical units.
- 2026 is excluded because it is incomplete in the downloaded source version.

## Analyses included / التحليلات الموجودة

- annual reported oil production for 2021-2025;
- the ten fields with the highest reported oil volume;
- annual flaring and venting, kept as separate measures;
- annual records reported under BP Exploration as a clearly labelled subset;
- produced-water-to-oil ratio;
- missing oil values by reporting-unit type.

## Completion criteria / معايير الإكمال

The project is complete when another person can rebuild the clean dataset and database, run the SQL analyses, reproduce the output tables and charts, pass the tests, identify the data source and understand the scope and limitations without verbal assistance.

## Limitations / القيود

- The project does not contain individual-well data.
- Reported operator does not by itself establish ownership.
- Public reporting data may be revised after download.
- The analysis is descriptive and must not be represented as operational advice.
- Missing and zero values have different meanings and are preserved accordingly.

## Next-level discussion / مناقشة المستوى التالي

After Level 1 is accepted, Level 2 can be discussed as a separate upgrade. Possible subjects include automated validation, a stronger software architecture, more tests, an API or dashboard, and deeper comparative analysis. Level 3 can later add advanced engineering analytics, deployment, monitoring and explainability. These upgrades will be specified in full rather than referred back to by shorthand.

