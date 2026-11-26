
import streamlit as st

# Title of the app
st.title("Daily Health Checker")
st.write("Check your daily health and get some healthy tips!")

st.header("Enter Your Details")

# Taking information from the user
name = st.text_input("Enter your name")

age = st.number_input("Enter your age", min_value=1, max_value=100)

sleep = st.number_input("Hours of sleep", min_value=0, max_value=24)

water = st.number_input("Glasses of water you drank", min_value=0, max_value=30)

exercise = st.number_input("Exercise time (in minutes)", min_value=0, max_value=300)

screen = st.number_input("Screen time (in hours)", min_value=0, max_value=24)

mood = st.selectbox(
    "How is your mood?",
    ["Happy", "Sad", "Stressed", "Energetic"]
)

# Check health button
if st.button("Check My Health"):

    if name == "":
        st.warning("Please enter your name!")

    else:
        st.success("Hello " + name + "! Here is your health report.")

        st.header("Your Daily Health Summary")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Sleep:", sleep, "hours")
        st.write("Water:", water, "glasses")
        st.write("Exercise:", exercise, "minutes")
        st.write("Screen Time:", screen, "hours")
        st.write("Mood:", mood)

        st.header("Your Health Feedback")

        # Checking sleep
        if sleep >= 7:
            st.success("Good job! You are getting enough sleep.")
        else:
            st.warning("You should sleep more.")

        # Checking water
        if water >= 8:
            st.success("Great! You are drinking enough water.")
        else:
            st.warning("Try to drink more water.")

        # Checking exercise
        if exercise >= 30:
            st.success("You are exercising daily. Keep it up!")
        else:
            st.warning("Try to exercise for 30 minutes daily.")

        # Checking screen time
        if screen <= 4:
            st.success("Your screen time is good.")
        else:
            st.warning("Try to reduce your screen time.")

        # Checking mood
        if mood == "Happy":
            st.success("Keep smiling and stay happy!")
        elif mood == "Sad":
            st.info("Do something you enjoy and talk to someone you trust.")
        elif mood == "Stressed":
            st.info("Take some rest and try meditation.")
        else:
            st.success("Great! Keep your energy high.")

        # Calculating wellness score
        score = 0

        if sleep >= 7:
            score = score + 25
        else:
            score = score + 10

        if water >= 8:
            score = score + 20
        else:
            score = score + 10

        if exercise >= 30:
            score = score + 25
        else:
            score = score + 10

        if screen <= 4:
            score = score + 15
        else:
            score = score + 5

        if mood == "Happy" or mood == "Energetic":
            score = score + 15
        else:
            score = score + 5

        # Displaying wellness score
        st.header("Your Wellness Score")

        st.subheader(str(score) + " / 100")

        st.progress(score / 100)

        if score >= 80:
            st.success("Excellent! You have a healthy lifestyle.")
        elif score >= 60:
            st.info("Good! You can improve a little more.")
        else:
            st.warning("You need to take better care of your health.")

        # Healthy tips
        st.header("Healthy Tips For You")

        if sleep < 7:
            st.write("Sleep for 7 to 9 hours.")

        if water < 8:
            st.write("Drink more water.")

        if exercise < 30:
            st.write("Exercise for at least 30 minutes.")

        if screen > 4:
            st.write("Spend less time on mobile phones.")

        if mood == "Sad" or mood == "Stressed":
            st.write("Spend time with friends and family.")

        st.info("Stay healthy, stay happy!")

# Reset button
if st.button("Reset"):
    st.rerun()
