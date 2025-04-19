# E-Commerce A/B Testing Dashboard

This project is an end-to-end A/B testing experiment built with Python and Streamlit to evaluate the impact of a new e-commerce webpage design on user conversion rates. It applies hypothesis testing, visual analytics, and is fully deployed using Streamlit Cloud.

---

## Live App

[Click here to launch the app](https://e-commerceabtestingapp-arugcovjnarauqqzh3v5wg.streamlit.app/)

---

## Project Structure

```
├── app.py                # Streamlit web app
├── ab_data.csv           # E-commerce A/B testing dataset
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
```

---

## Objective

To determine whether the new version of a website results in a statistically significant increase in conversion rates compared to the old version, using real data and hypothesis testing.

---

## Features

- Dataset Preview with filtering by group (control/treatment)
- Conversion Rate Visualization (Bar Chart & Pie Chart)
- Conversion Trends Over Time (Line Chart)
- Summary Metrics (Users, Conversions, Conversion Rate)
- Statistical Significance Test (Z-test)
- Deployed live using **Streamlit Cloud**

---

## Technologies Used

| Technology        | Purpose                                              |
|-------------------|------------------------------------------------------|
| Python            | Core programming language                           |
| Pandas, NumPy     | Data manipulation and preprocessing                 |
| Matplotlib, Seaborn | Data visualization                             |
| Statsmodels       | Z-test for proportions                             |
| Streamlit         | Frontend UI and web app hosting                    |

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ab-testing-dashboard.git
   cd ab-testing-dashboard
   ```
2. Create virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## Future Work

Here are a few ideas to enhance and extend the project in the future:

- Add Bayesian A/B testing for more flexible statistical insights
- Add date range filtering with interactive controls
- Compare multiple variants (A/B/n testing)
- Allow CSV upload for running custom A/B experiments
- Store results in a database for long-term tracking
- Email summaries or report generation

---

## Credits

This project is built for educational and demonstration purposes, simulating a real A/B testing scenario using open datasets.

---

## 📄 License

This project is licensed under the MIT License.
