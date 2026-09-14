# 📦 Return & Refund Pattern Analysis

## Overview
This project analyzes e-commerce return and refund patterns to uncover insights such as:
- Return rates by category, region, and customer segment
- Refund cycle times
- Top reasons for returns
- Predictive modeling to estimate probability of return
- Interactive dashboard for stakeholders

The goal is to help reduce return rates, improve customer satisfaction, and optimize operations.

📊Workflow

Phase 1: Data Pipeline

-Clean raw Kaggle dataset
-Normalize return reasons
-Add synthetic refund status
-Save processed dataset

Phase 2: Exploratory Data Analysis (EDA)
-Visualize return rates by category

-Analyze refund cycle times

-Identify top return reasons

Phase 3: Pattern Detection
-Segment returns by region, customer segment, and price band

-Detect root causes

Phase 4: Predictive Modeling
-Logistic regression to predict probability of return

-Evaluate with confusion matrix, ROC-AUC

Phase 5: Dashboard
-Interactive Streamlit dashboard

-KPIs, charts, segmentation filters

