import streamlit as st


#pages
#each st.Page object will hold the sdcript information as written in each associated python file
#ordering of pages in st.navigation is given by number on script name
#pass all of these into st.navigation
homepage = st.Page("1homepage.py", title = "Homepage", icon = "🏠")
events = st.Page("4events.py", title = "Events", icon = "🥳")
contactus = st.Page("3contactus.py", title = "Contact Us", icon = "☎️")
whatis = st.Page("2whatis.py", title = "What Is Bioinformatics?", icon = "🧬")


#pass in a dictionary with header name and page object
pg = st.navigation(
    {
        "Home":[homepage, whatis, contactus, events]
    }
)
#to run the multipage, use .run() on st.navigation object
pg.run()

