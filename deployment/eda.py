import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def app():
    # Set title
    st.title('Exploratory Data Analysis')

    # Load data
    df = pd.read_csv('text.csv')


# Membuat wordcloud
    text = df.text.values
    wordcloud= WordCloud(background_color='black',colormap='cool',collocations=False, width=2000,height=1000).generate(" ".join(text))
    plt.figure(figsize=(18,12))
    plt.axis('off')
    plt.title('All Word')
    plt.imshow(wordcloud)
    st.pyplot()

    # Visualisasi 2
    text_sad = df[df['label']==0].text.values
    wordcloud_sad= WordCloud(background_color='black',colormap='cool',collocations=False, width=2000,height=1000).generate(" ".join(text_sad))
    plt.figure(figsize=(18,12))
    plt.axis('off')
    plt.title("Wordcloud Sad")
    plt.imshow(wordcloud_sad)
    st.pyplot()

    # Visualisasi 3
    text_joy = df[df['label']==1].text.values
    wordcloud_joy= WordCloud(background_color='black',colormap='cool',collocations=False, width=2000,height=1000).generate(" ".join(text_joy))
    plt.figure(figsize=(18,12))
    plt.axis('off')
    plt.title("Wordcloud Joy")
    plt.imshow(wordcloud_joy)
    st.pyplot()

    # Visualisasi 4
    text_love = df[df['label']==2].text.values
    wordcloud_love= WordCloud(background_color='black',colormap='cool',collocations=False, width=2000,height=1000).generate(" ".join(text_love))
    plt.figure(figsize=(18,12))
    plt.axis('off')
    plt.title("Wordcloud Love")
    plt.imshow(wordcloud_love)
    st.pyplot()

    # Visualisasi 5
    text_anger = df[df['label']==3].text.values
    wordcloud_anger= WordCloud(background_color='black',colormap='cool',collocations=False, width=2000,height=1000).generate(" ".join(text_anger))
    plt.figure(figsize=(18,12))
    plt.axis('off')
    plt.title("Wordcloud Anger")
    plt.imshow(wordcloud_anger)
    st.pyplot()

    # Visualisasi 6
    text_fear = df[df['label']==4].text.values
    wordcloud_fear= WordCloud(background_color='black',colormap='cool',collocations=False, width=2000,height=1000).generate(" ".join(text_fear))
    plt.figure(figsize=(18,12))
    plt.axis('off')
    plt.title("Wordcloud Fear")
    plt.imshow(wordcloud_fear)
    st.pyplot()

    # Visualisasi 7 
    text_surprise = df[df['label']==5].text.values
    wordcloud_surprise= WordCloud(background_color='black',colormap='cool',collocations=False, width=2000,height=1000).generate(" ".join(text_surprise))
    plt.figure(figsize=(18,12))
    plt.axis('off')
    plt.title("Wordcloud Surprise")
    plt.imshow(wordcloud_surprise)
    st.pyplot()   

if __name__ == '__main__':
    app()
