import streamlit as st
# from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import tempfile

GOOGLE_API_KEY="AIzaSyCuPwAiKexa4yixaefiU7L7-M5S7_TAew8"

# Streamlit app
def main():
    st.title("AI Poetry Generator")

    # User inputs
    city = st.sidebar.text_input("Enter a city:")
    pollution_rate = st.sidebar.number_input("Enter the pollution rate (0-100):", min_value=0, max_value=100)
    length = st.sidebar.number_input("Enter the desired poem length (number of lines):", min_value=1)
    date = st.sidebar.date_input("Select a date:")

    # Generate poetry button
    if st.sidebar.button("Generate Poetry"):
        if city and 0 <= pollution_rate <= 100 and length > 0:
            prompt = f"""Craft a lyrical and evocative poem about {city}, a city with a pollution rate of {pollution_rate}% on {date.strftime('%B %d, %Y')} The poem should be {length} lines long, painting a vivid picture of the city's atmosphere, its people, and the impact of pollution on their lives. 
            Use powerful imagery and metaphors to convey the emotions and experiences of the city's beauty and culture, while maintaining a rhythmic and melodic flow throughout the poem. 
            The tone of the poem should be pleasing if the pollution rate is less than 40, medium if it's between 40 and 60, and more critical and rough if it's above 60. Don't generate negative poem. 
            Don't mention the word smog.
            In poetry mention the city history and culture.
            Take the reference of {city} city and pollution rate {pollution_rate}%.


            
            
            """
            
                       # llm = OpenAI(model_name="text-bison@001", temperature=0.7)
            llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
            poem = llm.invoke(prompt)
            st.subheader("Generated Poem:")
            st.write(poem)

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
                tmp.write(poem.encode("utf-8"))
                tmp.seek(0)
                st.download_button(
                    label="Download Poem",
                    data=tmp.read(),
                    file_name=f"{city}_{date.strftime('%Y%m%d')}.txt",
                    mime="text/plain",
                )
        else:
            st.warning("Please enter valid inputs for city, pollution rate, and poem length.")

if __name__ == "__main__":
    main()