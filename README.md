# kotlin-education-landscape-report-GSoC-2026

---

## Dataset Description

The dataset includes the following fields:

- institution: Name of the institution or platform
- country: Country of the institution
- course_name: Name of the course
- platform: Source of the course (University, Coursera, etc.)
- level: Difficulty level (Beginner, Intermediate, Advanced)
- category: Course category (Android, Kotlin, Software Engineering)

---

## Methodology

### Data Collection
- University course catalogs and curriculum pages
- Online platforms such as Coursera, Udemy, and MOOCs
- Public developer and educational resources

### Data Processing
- Cleaning and removing inconsistencies
- Standardizing formats across sources
- Structuring data into CSV format

### Data Analysis
- Descriptive analysis of adoption patterns
- Distribution analysis across regions and platforms
- Category-wise breakdown of courses

### Validation
- Manual verification of selected entries
- Cross-checking with multiple sources where possible

---

## Analysis and Visualizations

The project generates visual insights such as:

- Country-wise distribution of Kotlin courses
- Category distribution (Android, Kotlin, etc.)
- Platform-wise distribution

These visualizations help in understanding patterns of adoption and identifying trends.

---

## Report Structure

Kotlin_Education_Landscape_Report
```
├── 1_Abstract.md  
├── 2_Introduction.md  
│   ├── 2.1_Background.md  
│   ├── 2.2_Motivation.md  
│   └── 2.3_Problem_Statement.md  

├── 3_Objectives.md  

├── 4_Literature_Review.md  

├── 5_Methodology  
│   ├── 5.1_Data_Sources.md  
│   ├── 5.2_Data_Collection.md  
│   ├── 5.3_Data_Structuring.md  
│   └── 5.4_Data_Cleaning_Validation.md  

├── 6_Dataset_Description.md  

├── 7_Data_Analysis  
│   ├── 7.1_Descriptive_Analysis.md  
│   ├── 7.2_Trend_Analysis.md  
│   └── 7.3_Gap_Analysis.md  

├── 8_Visualization_and_Insights  
│   ├── 8.1_Charts.md  
│   ├── 8.2_Dashboards.md  
│   └── 8.3_Key_Insights.md  

├── 9_Discussion.md  

├── 10_Recommendations.md  

├── 11_Conclusion.md  

├── 12_Deliverables.md  

├── 13_Reproducibility  
│   ├── Dataset_Links.md  
│   ├── Scripts_and_Pipelines.md  
│   └── Resources.md  

├── 14_References.md  

└── 15_Appendix  
    ├── Additional_Charts.md  
    ├── Survey_Forms.md  
    └── Interview_Notes.md  
```
---
## Key Observations (Preliminary)

- Kotlin is primarily taught in the context of Android development
- Online platforms show higher adoption compared to universities
- Adoption varies significantly across regions

---

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- CSV

---

## Future Work

- Expanding the dataset to include more institutions and regions
- Continuous updates to track adoption trends over time
- Development of interactive dashboards for exploration

---

## Author

Anmol Garg  
GSoC 2026 Proposal – Kotlin Foundation
