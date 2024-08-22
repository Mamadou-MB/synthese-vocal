import nltk
import streamlit as st
import speech_recognition as sr
from nltk.chat.util import Chat, reflections
import sounddevice as sd
import scipy.io.wavfile as wav
#==============================================================================================================================================================================

#  correspondances pour le chatbot
chats = [
    (r'bonjour|salut|coucou', ['Bonjour, comment puis-je vous aider ?']),
    (r'quel est ton nom ?', ['Je suis un chatbot vocal.']),
    (r'au revoir', ['Au revoir, à bientôt !']),
]

chatbot = Chat(chats, reflections)



def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Parlez maintenant...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='fr-FR')
        st.write(f"Vous avez dit : {text}")
        return text
    except sr.UnknownValueError:
        st.write("Désolé, je n'ai pas compris l'audio.")
        return None
    except sr.RequestError as e:
        st.write(f"Erreur de service de reconnaissance vocale : {e}")
        return None

    
def chatbot_response(input_text):
    response = chatbot.respond(input_text)
    return response

#==============================================================================================================================================================================


def main():
    st.title("Chatbot à Commande Vocale")
    
    input_mode = st.radio("Choisissez votre mode d'entrée", ('Texte', 'Vocal'))
    
    if input_mode == 'Texte':
        user_input = st.text_input("Entrez votre texte ici :")
        if st.button("Envoyer"):
            if user_input:
                response = chatbot_response(user_input)
                st.write(f"Chatbot : {response}")
    else:
        if st.button("Parler"):
            user_input = speech_to_text()
            if user_input:
                response = chatbot_response(user_input)
                st.write(f"Chatbot : {response}")

if __name__ == "__main__":
    main()
