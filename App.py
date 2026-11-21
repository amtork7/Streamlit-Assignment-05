import streamlit as st

# Title
st.title("🎓 Grade Calculator")
st.markdown("---")

# Markdown Section
st.markdown("""
## Student Grade Calculator

**Instructions:**
1. Enter your scores for the four subjects.
2. Click **Calculate Grade** to view your result.

### Subjects
- Mathematics
- Science
- English
- History
""")

# Widget 1: Text Input
student_name = st.text_input("Student Name")

# Widget 2-5: Number Inputs
mathematics = st.number_input("📘 Mathematics Score", min_value=0, max_value=100, value=50)
science = st.number_input("🔬 Science Score", min_value=0, max_value=100, value=50)
english = st.number_input("📖 English Score", min_value=0, max_value=100, value=50)
history = st.number_input("🏛️ History Score", min_value=0, max_value=100, value=50)

# Widget 6: Radio Button
grading_scale = st.radio(
    "Select Grading Scale",
    ["Standard Scale"]
)

# Widget 7: Checkbox
show_average = st.checkbox("Show Average Score")

# Information Message
st.info("Enter all scores and click the button to calculate your grade.")

# Widget 8: Button
if st.button("Calculate Grade"):

    average = (mathematics + science + english + history) / 4

    # Standard Scale
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    st.write(f"**Student:** {student_name}")

    if show_average:
        st.write(f"**Average Score:** {average:.2f}")

    # Coloured Message Boxes
    if grade == "A":
        st.success(f"Excellent! Your grade is {grade}")
    elif grade in ["B", "C"]:
        st.info(f"Good work! Your grade is {grade}")
    elif grade == "D":
        st.warning(f"You passed with grade {grade}. There is room for improvement.")
    else:
        st.error(f"Your grade is {grade}. Additional study is recommended.")
