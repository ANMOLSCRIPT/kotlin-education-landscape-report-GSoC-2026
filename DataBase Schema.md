# Database Schema: Kotlin Education Landscape

This schema is designed to support structured analysis of Kotlin adoption in education across multiple data sources, including universities, online platforms, and survey responses.

---

## 1. Core Table: Courses

| Field Name | Type | Description |
|-----------|------|-------------|
| course_id | STRING (PK) | Unique identifier for each course |
| course_name | STRING | Name of the course |
| institution_id | STRING (FK) | Linked institution |
| platform | STRING | Source platform (University, Coursera, Udemy, etc.) |
| country | STRING | Country of institution/platform |
| region | STRING | Region (Asia, Europe, etc.) |
| level | STRING | Beginner / Intermediate / Advanced |
| category | STRING | Android / Backend / General Kotlin / Software Engineering |
| delivery_mode | STRING | Online / Offline / Hybrid |
| language | STRING | Language of instruction |
| duration | STRING | Course duration (if available) |
| certification | BOOLEAN | Whether certification is offered |
| source_link | STRING | URL to course/syllabus |
| verified | BOOLEAN | Whether data is validated |
| data_source | STRING | Primary / Secondary |

---

## 2. Institutions Table

| Field Name | Type | Description |
|-----------|------|-------------|
| institution_id | STRING (PK) | Unique identifier |
| institution_name | STRING | Name of institution |
| institution_type | STRING | University / Platform / Bootcamp |
| country | STRING | Country |
| region | STRING | Region |
| ranking | STRING | Optional (QS/Other) |
| website | STRING | Official website |

---

## 3. Survey Responses Table

| Field Name | Type | Description |
|-----------|------|-------------|
| response_id | STRING (PK) | Unique response ID |
| user_type | STRING | Student / Professional / Educator |
| country | STRING | Respondent country |
| field_of_study | STRING | Academic/Work domain |
| kotlin_experience | BOOLEAN | Whether user has used Kotlin |
| proficiency_level | STRING | Beginner / Intermediate / Advanced |
| learning_source | STRING | Where Kotlin was learned |
| institution_name | STRING | Optional user institution |
| course_link | STRING | Optional syllabus/course link |

---

## 4. Perception Metrics Table

| Field Name | Type | Description |
|-----------|------|-------------|
| response_id | STRING (FK) | Linked to survey |
| resource_availability_score | INT | 1–5 rating |
| difficulty_score | INT | 1–5 rating |
| industry_relevance_score | INT | 1–5 rating |
| gap_score | INT | 1–5 rating |
| recommendation_score | INT | 1–5 rating |

---

## 5. Qualitative Insights Table

| Field Name | Type | Description |
|-----------|------|-------------|
| response_id | STRING (FK) | Linked to survey |
| challenges | TEXT | Learning challenges |
| suggestions | TEXT | Improvement suggestions |

---

## 6. Ecosystem Signals Table

| Field Name | Type | Description |
|-----------|------|-------------|
| record_id | STRING (PK) | Unique identifier |
| source | STRING | GitHub / StackOverflow / Reports |
| metric_type | STRING | Usage / Popularity / Mentions |
| value | FLOAT | Numeric value |
| timestamp | DATE | Time of record |
| region | STRING | Region |
| notes | TEXT | Additional context |

---

## 7. Data Quality & Metadata Table

| Field Name | Type | Description |
|-----------|------|-------------|
| record_id | STRING (PK) | Unique identifier |
| dataset_name | STRING | Dataset reference |
| completeness_score | FLOAT | % completeness |
| validation_status | STRING | Verified / Pending |
| last_updated | DATE | Timestamp |
| source_reliability | STRING | High / Medium / Low |

---

## Relationships

- Courses → Institutions (Many-to-One)
- Survey Responses → Perception Metrics (One-to-One)
- Survey Responses → Qualitative Insights (One-to-One)

---

## Notes

- The schema supports both **primary (survey)** and **secondary (web/API)** data.
- Designed for **scalability and normalization**.
- Enables **descriptive, trend, and gap analysis**.
- Can be implemented using relational databases (MySQL/PostgreSQL) or converted to CSV/JSON.

---
