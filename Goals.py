import streamlit as st


# Function to calculate Retirement Goal
def calculate_retirement(date_of_birth, retirement_age, savings_until_age, monthly_expense, inflation_rate):
    current_age = 2024 - date_of_birth  # Assuming the current year is 2024
    years_to_retirement = retirement_age - current_age
    if years_to_retirement < 0:
        return "You have already retired!"

    total_expense = monthly_expense * 12 * (savings_until_age - retirement_age) * (
                (1 + inflation_rate / 100) ** years_to_retirement)
    return total_expense


# Function to calculate Education Goal
def calculate_education(number_of_children, child_current_age, planned_college_age, education_cost):
    years_to_college = planned_college_age - child_current_age
    if years_to_college < 0:
        return "The child is already in college!"

    total_cost = number_of_children * education_cost
    return total_cost


# Function to calculate Vacation Goal
def calculate_vacation(family_size, vacation_type):
    if vacation_type == 'International':
        cost_per_person = 600000  # Upper limit for international vacation
    else:
        cost_per_person = 200000  # Upper limit for domestic vacation

    total_vacation_cost = family_size * cost_per_person
    return total_vacation_cost


# Streamlit App UI
st.title("Financial Goals Calculator")

# Retirement Goal
st.header("Retirement Goal Calculator")
dob = st.number_input("Enter your Date of Birth (YYYY format): (date_of_birth)", min_value=1900, max_value=2024, value=1984)
retirement_age = st.number_input("Enter Retirement Age: (retirement_age)", value=60)
savings_until_age = st.number_input("Enter Age Until Savings Should Last: (savings_until_age)", value=90)
monthly_expense = st.number_input("Enter Estimated Monthly Expense (in ₹): (monthly_expense)", value=50000)
inflation_rate = st.number_input("Enter Expected Inflation Rate (%): (expected_inflation_rate)", value=7)

if st.button("Calculate Retirement Goal"):
    retirement_total = calculate_retirement(dob, retirement_age, savings_until_age, monthly_expense, inflation_rate)
    st.success(f"Total Retirement Savings Required: ₹{retirement_total}")

# Education Goal
st.header("Education Goal Calculator")
number_of_children = st.number_input("Number of Children: (number_of_children)", value=1)
child_current_age = st.number_input("Current Age of Child: (child_current_age)", value=5)
planned_college_age = st.number_input("Planned Age for College Admission: (planned_age_for_college_admission)", value=17)
education_cost = st.selectbox("Select Education Cost: (total_education_cost)", options=[5000000, 20000000],
                                format_func=lambda x: "Domestic (₹50 Lakh)" if x == 5000000 else "International (₹2 Crore)")

if st.button("Calculate Education Goal"):
    education_total = calculate_education(number_of_children, child_current_age, planned_college_age, education_cost)
    st.success(f"Total Education Savings Required: ₹{education_total}")

# Vacation Goal
st.header("Vacation Goal Calculator")
family_size = st.number_input("Enter Family Size: (family_size)", value=2)
vacation_type = st.selectbox("Select Vacation Type: (vacation_type)", options=["International", "Domestic"])

if st.button("Calculate Vacation Goal"):
    vacation_total = calculate_vacation(family_size, vacation_type)
    st.success(f"Total Vacation Cost: ₹{vacation_total}")
