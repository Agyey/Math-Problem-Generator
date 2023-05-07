import streamlit as st
import requests
import json

# url = "https://api.berri.ai/create_template"

# data = {
#     "advanced": {
#         "intent": "qa_doc", 
#         "search": "default"
#         }, 
#     "prompt": "Provide students with question and answers that develop their learning", 
#     "output_length": "1024"
#     }

# response = requests.post(
#     url, 
#     data={"app_config": json.dumps(data)}
#     )

# print(response.text)

## Template ID aba27aca-1676-41aa-b24a-bc92252feb6e


# template_id = "aba27aca-1676-41aa-b24a-bc92252feb6e"

# url = "https://api.berri.ai/create_app"

# data = {
#     "template_id": template_id, 
#     "user_email": "agyey1997@gmail.com"
#     }

# files = {
#     'data_source': open('numerical.pdf', 'rb')
#     }

# response = requests.post(url, files=files, data=data)

# print(response.text)


## Instance ID 2bc76ae8-8a5f-4e0d-9868-f38d86de5ae5

# api_endpoint = "https://api.berri.ai/query?user_email=agyey1997@gmail.com&instance_id=2bc76ae8-8a5f-4e0d-9868-f38d86de5ae5"
# print(api_endpoint)

def generate_question():
    url = "https://api.berri.ai/query"

    querystring = {
    "user_email": "agyey1997@gmail.com",
    "instance_id": "2bc76ae8-8a5f-4e0d-9868-f38d86de5ae5",
    "query": "generate a math problem and if it requires an image, generate the svg code for the image, the answers should in MCQ format, also provide the solution to the problem. Put the question under the heading question, the solution under the heading solution, the answer under the heading answer and image under the heading image. if there is no image needed just mention that after the heading",
    "model": "gpt-3.5-turbo"
    }

    response = requests.get(url, params=querystring)
    print(response.json()['response'])
    question_solution_answer_image = response.json()['response']
    question_solution_answer, image = question_solution_answer_image.split("Image:")
    question_solution, answer = question_solution_answer.split("Answer:")
    question, solution = question_solution.split("Solution:")
    if "```" in image:
        image = image.split("```")[1].split('```')[0]
    else:
        image = None
    return question, solution, answer, image



st.title("Math Problem Generator")

generate =  st.button("Generate New Problem")
if 'generate' not in st.session_state:
    st.session_state['generate'] = False
if generate:
    st.session_state['generate'] = True
if st.session_state['generate']:
    question, solution, answer, image = generate_question()
    st.write(question)
    if image:
        st.image(image)
    st.text_input("Enter your answer: ")
    with st.expander("Show Solution"):
        st.write(solution)
        st.write("Therefore, the correct answer is", answer)
        st.session_state['generate'] = False

