# Task 3: Complaint Type Analysis

**Name:** Anastasios Lambrianos Stappas  
**Student ID:** 261009936  
**Course:** COMP 370 - Introduction to Data Science  
**Assignment:** Homework 5 - NYC 311 Data Analysis

---

## Objective

Identify the most abundant complaint type in the first two months of 2024 (January-February) and compare it to the same complaint type during June-July 2024.

---

## Methodology

### 1. Data Extraction

I used the `borough_complaints.py` CLI tool to extract complaint data for two time periods:

**Period 1: January-February 2024**
```bash
python3 borough_complaints.py -i 311_2024_records.csv -s 01/01/2024 -e 02/29/2024 -o jan_feb_2024.csv
```

**Period 2: June-July 2024**
```bash
python3 borough_complaints.py -i 311_2024_records.csv -s 06/01/2024 -e 07/31/2024 -o june_july_2024.csv
```

### 2. Analysis Approach

The CLI tool outputs complaint counts broken down by complaint type and borough. To find the overall most abundant complaint type, I:

1. Aggregated the counts across all boroughs for each complaint type
2. Sorted complaint types by total count in descending order
3. Identified the top complaint type in Jan-Feb 2024
4. Retrieved the count for the same complaint type in June-July 2024
5. Created a bar chart visualization comparing the two periods

---

## Results

### Most Abundant Complaint Type: **HEAT/HOT WATER**

| Time Period | Number of Complaints |
|-------------|---------------------|
| **Jan-Feb 2024** | 81,641 |
| **June-July 2024** | 6,890 |
| **Difference** | -74,751 (91.6% decrease) |

### Visualization

![Complaint Comparison](complaint_comparison.png)

The bar chart clearly shows the dramatic seasonal difference in HEAT/HOT WATER complaints between winter (Jan-Feb) and summer (June-July) months.

---

## Analysis & Interpretation

### Key Finding

**HEAT/HOT WATER** complaints were by far the most abundant complaint type in the first two months of 2024, with 81,641 total complaints across all NYC boroughs.

### Seasonal Pattern

The comparison between Jan-Feb and June-July 2024 reveals a **91.6% decrease** in heating-related complaints during the summer months. This makes intuitive sense:

- **Winter (Jan-Feb):** Residents depend on heating systems for basic comfort and survival. Heating failures during cold weather are urgent issues that prompt immediate 311 calls.

- **Summer (June-July):** Heating systems are not in use, so heating failures are non-urgent. The 6,890 complaints in summer likely represent water heater issues (hot water) rather than space heating.

### Context from Top 10 Complaints

Looking at the broader landscape of complaints:

1. **HEAT/HOT WATER:** 81,641 → 6,890 (91.6% decrease)
2. **Illegal Parking:** 79,916 → 86,240 (7.9% increase)
3. **Noise - Residential:** 43,602 → 58,197 (33.5% increase)

Interestingly, while heating complaints drop dramatically, other complaint types like "Noise - Residential" **increase** in summer months, likely due to:
- More open windows in warm weather (sound travels)
- More outdoor social activities
- Longer daylight hours encouraging evening activities

### Implications

This analysis demonstrates:

1. **Seasonal Resource Allocation:** NYC agencies should prepare for surges in heating-related complaints during winter months, with staffing and response capacity scaled accordingly.

2. **Predictable Patterns:** The stark seasonal difference suggests that heating complaint volumes are highly predictable and can inform proactive maintenance programs.

3. **Data-Driven Planning:** By analyzing historical patterns, city officials can better anticipate service demands and allocate resources efficiently throughout the year.

---

## Tools & Technologies Used

- **CLI Tool:** `borough_complaints.py` (Python with argparse)
- **Analysis:** Python (pandas, matplotlib)
- **Environment:** Jupyter Notebook for interactive analysis
- **Data Source:** NYC 311 Service Requests (2024 records, 3.4M+ entries)

---

## Conclusion

The analysis successfully identified **HEAT/HOT WATER** as the most abundant complaint type in early 2024 and demonstrated a clear seasonal pattern with a 91.6% reduction in summer months. This finding provides actionable insights for NYC's resource allocation and service planning.

The combination of the CLI tool for data extraction and Jupyter for analysis and visualization proved effective for exploring this large dataset and extracting meaningful patterns.

---

**Files Generated:**
- `jan_feb_2024.csv` - Complaint data for Jan-Feb 2024
- `june_july_2024.csv` - Complaint data for June-July 2024
- `complaint_comparison.png` - Bar chart visualization
- `task3_analysis.ipynb` - Jupyter notebook with full analysis

**Date Completed:** October 3, 2025

