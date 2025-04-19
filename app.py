import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest

# Set Streamlit page config
st.set_page_config(page_title="E-Commerce A/B Testing", layout="centered")

# Title
st.title("E-Commerce A/B Testing Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("ab_data.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date
    return df

df = load_data()

# Sidebar filter
group_filter = st.sidebar.selectbox("Select Group to Analyze", options=["all", "control", "treatment"])

if group_filter != "all":
    df = df[df['group'] == group_filter]

# Dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Summary metrics
total_users = len(df)
total_conversions = df['converted'].sum()
conversion_rate = total_conversions / total_users

st.subheader("Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", f"{total_users:,}")
col2.metric("Total Conversions", f"{total_conversions:,}")
col3.metric("Conversion Rate", f"{conversion_rate:.2%}")

# Conversion Rate by Group
st.subheader("Conversion Rate by Group")
group_summary = df.groupby('group')['converted'].agg(['count', 'sum'])
group_summary['conversion_rate'] = group_summary['sum'] / group_summary['count']

fig1, ax1 = plt.subplots()
sns.barplot(x=group_summary.index, y=group_summary['conversion_rate'], palette='viridis', ax=ax1)
ax1.set_title("Conversion Rate by Group")
ax1.set_ylabel("Conversion Rate")
ax1.set_ylim(0, 0.2)
st.pyplot(fig1)

# Overall Conversion Distribution
st.subheader("Overall Conversion Distribution")
conversion_counts = df['converted'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(conversion_counts, labels=['Not Converted', 'Converted'], autopct='%1.1f%%', startangle=140, explode=(0, 0.1))
ax2.axis('equal')
plt.tight_layout()
st.pyplot(fig2)

# Conversion Trend Over Time
st.subheader("Conversion Trend Over Time")
daily_conv = df.groupby(['date', 'group'])['converted'].mean().reset_index()
pivot_data = daily_conv.pivot(index='date', columns='group', values='converted')
st.line_chart(pivot_data)

# Z-Test for Statistical Significance
st.subheader("Statistical Significance Test (Z-Test)")

# Only run Z-test if both groups exist in current view
if 'control' in df['group'].unique() and 'treatment' in df['group'].unique():
    converted_counts = df.groupby('group')['converted'].sum()
    total_counts = df.groupby('group')['converted'].count()

    success = [converted_counts['control'], converted_counts['treatment']]
    nobs = [total_counts['control'], total_counts['treatment']]

    z_stat, p_val = proportions_ztest(success, nobs)

    st.write(f"Z-statistic: {z_stat:.4f}")
    st.write(f"P-value: {p_val:.4f}")

    if p_val < 0.05:
        st.success("Reject the Null Hypothesis — Statistically significant difference between groups.")
    else:
        st.warning("Fail to Reject the Null Hypothesis — No significant difference found.")
else:
    st.info("Z-test requires both control and treatment groups to be present.")
