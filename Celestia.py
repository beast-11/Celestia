import streamlit as st
from datetime import datetime

# Page Setup
st.set_page_config(
    page_title="Celestia - The Cosmic Messenger \U0001F320",
    page_icon="\U0001F30C",
    layout="wide"
)

# Celestia Header
st.title("🌌 Celestia - The Cosmic Messenger ✨")
st.write(
    "In the vast cosmos, some stars shine brighter than others. **Celestia** is here to remember those special stars and send wishes across the universe. "
    "No birthday is forgotten, and every moment is celebrated under the endless sky."
)
st.markdown("---")

# Predefined Birthdays
birthdays = {
    "Saketh": "04-02",  # Format: MM-DD
    "Fathima": "09-15",  
}

today = datetime.today().strftime("%m-%d")

date_input = st.date_input("Select a date to check for a special message:")
if date_input:
    selected_date_str = date_input.strftime("%m-%d")
    
    if selected_date_str == birthdays["Saketh"]:
        # Suspense Button before the reveal
        if st.button("What is there for you today, Griffin?"):
            st.subheader("🔥 The Legendary Tale of Leo and Griffin 🦁🦅")
            st.write(
                """
                There was a time when two forces met—uncertain of where they were going, but trusting in themselves, 
                they started their journey together. Their footsteps were small at first, but over time, these small prints 
                transformed into the mighty leg prints of **Leo** and **Griffin**. 
                Day and night, they struggled, and each struggle taught them new life lessons.

                The last year was the hardest phase of their lives. The world doubted them. They were tested by God in ways 
                they could never have imagined. At a time when others less talented and passionate were getting opportunities, 
                these two warriors were left behind, their confidence shattered.

                The world thought they were overhyped. But despite the odds, they trusted the journey and decided to pursue their master's dreams. 
                Their journey wasn’t just about work—it was about overcoming doubt and pushing forward when everything seemed impossible.
                They began with small projects, earning just enough to survive before college started. Their first earnings came from this simple work, but fate had other plans. Health issues prevented Leo from attending college for the first week, and Griffin, disheartened and disrespected by his love problems, came back without informing Leo.

                The weight of unspoken emotions, rejection, and heartbreak clouded Griffin's mind, causing him to retreat into himself, away from the very friend who trusted him.
                
                Imagine Leo’s pain. His heart sank, and no one could understand the sorrow he felt. He wished Griffin had told him before taking the decision.
                Leo believed in Griffin’s potential, but he feared his friend would settle for less than he deserved. The world didn’t know the strength Griffin had 
                deep inside, and Leo feared he might never realize his true potential.
                
                As time passed, Leo thought of his friend often, missing their shared moments. It wasn’t until they met again that the journey would take a turn. 
                The day came when these two forces reunited at a hackathon. The rest is history. Despite all the challenges they faced—tests of faith, trust, 
                and skill—they fought through them and are now standing strong as an unbreakable force. 

                What the world thought would be the end was just the beginning. Leo and Griffin didn’t come to compete with anyone—they came to rule.
                
                Now, standing side by side, Leo the Commander orders Griffin, and Griffin commands Leo. They listen only to each other. The world’s doubts 
                have been silenced. Together, they have made history.

                As they celebrated their 21st birthdays, they finally started their AI Community, which grew into the mighty AI Hub. They are now leading the juniors 
                in creating a strong empire, a place where innovation and creativity rule. For their hard work and persistence, they were recognized with an AI Innovation 
                award, and this birthday, Griffin’s birthday, became an epic milestone.

                But Leo has one wish for Griffin today: *"What may come, let’s keep pushing forward. We’ve overcome so much together, and we will continue to rise. 
                The world will see us shine."*

                And with that, Leo says, *"Hey Griffin, open your eyes and witness the sunrise we’ve created together. This is just the beginning. Let’s stay determined."*
                
                ### Now, with the first day of their journey written in the stars...
                """
            )
            # Adding transition image concept for 'Day One' with a '?' mark
            st.image("DayOne-OneDay.png", caption="Day One - One Day - What will we create today?")


            st.write(
                "We are the Dangerous Superheroes, the protectors of the digital realm, combating the misuse of AI and technology. "
                "Together, we rise to safeguard the future of this world. Our alter ego names are a secret... but one day, the world will know. "
                "For now, only we know who we truly are. Let’s make history!"
            )

            # Image or video with background score
            #st.image("path/to/hero_image.jpg", caption="Superheroes in Action!")
            st.video("Super Heroes.mp4")

            # Display the mission message
            st.write("Will you join hands with us to make the world a better place?")

            # Automatically assume "Yes" and proceed with the message
            st.write("Let’s do this! The world is about to witness the power of Leo and Griffin. Stay tuned.")

            st.markdown("---")
            st.write("### Happy Birthday, Griffin! 🎉🎂")

# Footer
st.markdown("<style>div.block-container{padding-bottom: 100px;}</style>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style="display: flex; align-items: center;">
        <div style="flex: 1;">
            <h3>🚀 Let's Connect!</h3>
            <p>This Application is Developed by Abdul Faheem (InnoUdayVoyager) with 💡 and 🥤. If you have any questions or just want to connect, feel free to reach out!</p>
            <p align="left">
              <a href="https://www.linkedin.com/in/abdulfaheem011/" target="_blank">
                <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" alt="LinkedIn" style="width:40px;"/>
              </a>
              <a href="https://github.com/abdulfaheemaf" target="_blank">
                <img src="https://img.icons8.com/fluent/48/000000/github.png" alt="GitHub" style="width:40px;"/>
              </a>
              <a href="mailto:abdulfaheemaf11@gmail.com">
                <img src="https://img.icons8.com/fluent/48/000000/mail.png" alt="Email" style="width:40px;"/>
              </a>
            </p>
            <p>Cheers,<br>-AF011</p>
        </div>
    </div>
""", unsafe_allow_html=True)
