import os
import re
import streamlit as st
from PIL import Image
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader

# Define the Streamlit app
def app():
    st.title("Acupuncture Question Answering")
    question = st.text_input("Enter the question:", value="可否顯示曲差的照片? 請問可治療鼻塞和頭痛的穴位有哪些?")
    
    if st.button("Answer"):
        if not question:
            st.warning("Please enter a question.")
        else:
            response = index.query(question) #可否顯示曲差的照片? 請問可治療鼻塞和頭痛的穴位有哪些?
            image_path = re.findall('\w+.jpg', response.response)

            if image_path != []: 
                # Load the image
                image = Image.open('image/'+ image_path[0])
                #image = image.resize((300, 150))

                # Display the image
                st.image(image, caption=image_path[0]) #use_column_width=True

            st.success(response) #st.write(response)

if __name__ == '__main__':
    os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"]
    
    # Load the index from your saved index.json file
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    
    app()





