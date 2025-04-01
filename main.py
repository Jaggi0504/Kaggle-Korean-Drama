import streamlit as st
import pickle
import pandas as pd

drama_dict=pickle.load(open('drama_dict.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
dramas=pd.DataFrame(drama_dict)

def recommend(drama):
    drama_index=dramas[dramas["Title"]==drama].index[0]
    distances=similarity[drama_index]
    drama_list=sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_dramas=[]
    for i in drama_list:
        recommended_dramas.append(dramas.iloc[i[0]].Title)
        recommended_dramas.append(dramas.iloc[i[0]].Rating)
    return recommended_dramas

st.title("Korean Drama")

selected_drama_name=st.selectbox("Hello", dramas['Title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_drama_name)
    for i in recommendations:
        st.write(i)