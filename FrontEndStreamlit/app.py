import streamlit as st
import requests
#import imageio as io



background_color = '''
<style>
body {
    background-color: #f1f1f1;
}
</style>
'''

# Display the background color
st.markdown(background_color, unsafe_allow_html=True)



st.title("Story Spark: Empowering kids through an Interactive Story Generation Website")

st.markdown(" ## Introduction")
st.write("""We have developed an innovative story generation website for kids that takes prompts as input and generates engaging stories complete with images. 
 The website aims to foster creativity, imagination, and language skills in children while providing them with entertaining content. 
 This business plan outlines our vision, market analysis, marketing strategies, and financial projections.""")
st.markdown(" ## Generate your story")

input_text= st.text_input("Genre: ")
st.radio("Choose your story type: ",["long","radio"])
st.selectbox("Choose level of your child:",["toddler","adolescent"])
#st.button("Submit")

if st.button("Generate Response"):
    # Send the input_text to the FastAPI endpoint
    response = requests.get("http://localhost:8080/generate", params={"input": input_text})

    # Process the response from FastAPI
    if response.status_code == 200:
        print(response.json())
        output = response.json()["response"]
        st.text("Generated Response:")
        st.write(output)
    else:
        st.error("Error: Failed to generate response")


#st.image(image="sample.png",caption = "A few images")