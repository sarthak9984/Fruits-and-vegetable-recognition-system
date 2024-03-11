import streamlit as st
import tensorflow as tf
import numpy as np

#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

# SLIDER BAR
st.sidebar.title("🌟 DASHBOARD 🌟")
app_mode = st.sidebar.selectbox(
    "Select Page",
    ["Home", "About Project", "Prediction"],
    key="sidebar_selectbox",  # Key to track changes in the selectbox
    help="Select a page from the menu", 
    )

# Add decorative elements to sidebar
st.sidebar.markdown("---")  # Horizontal line
st.sidebar.markdown("Explore the options below:")

# Add icons to the sidebar options
sidebar_icons = {
    "Home": "🏠",
    "About Project": "📋",
    "Prediction": "🔮",
}

# Render sidebar options with icons
for option in ["Home", "About Project", "Prediction"]:
    st.sidebar.markdown(f"{sidebar_icons.get(option, '')} {option}")

st.sidebar.markdown("---")  # Add a horizontal line
st.sidebar.markdown("---")  # Add a horizontal line
st.sidebar.markdown("**Created by:** Sarthak Singh & Ayushi Katiyar")

# MAIN PAGE 
if app_mode == "Home":
    st.title("🍏🍊🥕 FRUITS & VEGETABLES RECOGNITION SYSTEM 🥦🍇🍉")
    st.markdown("---")

    st.image("home_img.jpg", width=700)
    st.markdown(
        """
        Welcome to the Fruits & Vegetables Recognition System! 🌟

        This system allows you to easily identify various fruits and vegetables from images. 
        Whether you're a cooking enthusiast, a nutritionist, or just curious about what's in your 
        fridge, our system has got you covered! Simply upload an image, and let the magic happen. 📷✨
        """
    )

    # Add a call-to-action section with a button
    st.markdown("---")
    st.write("")  # Add some space
    st.info(
        """
        Ready to give it a try? Click the sliderbar below the Dashboard to recognizing fruits and vegetables!
        """
    )
    if st.button("Try it now from dashboard--> Prediction!"):
        app_mode = "Prediction"  # Redirect to the prediction page
#About Project
elif(app_mode=="About Project"):
    st.header("About Project")
    st.subheader("About Dataset")
    st.text("This dataset contains images of the following food items:")
    st.code("fruits- banana, apple, pear, grapes, orange, kiwi, watermelon, pomegranate, pineapple, mango.")
    st.code("vegetables- cucumber, carrot, capsicum, onion, potato, lemon, tomato, raddish, beetroot, cabbage, lettuce, spinach, soy bean, cauliflower, bell pepper, chilli pepper, turnip, corn, sweetcorn, sweet potato, paprika, jalepeño, ginger, garlic, peas, eggplant.")
    st.subheader("Content")
    st.text("This dataset contains three folders:")
    st.text("1. train (100 images each)")
    st.text("2. test (10 images each)")
    st.text("3. validation (10 images each)")

#Prediction Page
elif(app_mode=="Prediction"):
    st.header("Model Prediction")
    test_image = st.file_uploader("Choose an Image:")
    if(st.button("Show Image")):
        st.image(test_image,width=4,use_column_width=True)
    #Predict button
    if(st.button("Predict")):
        st.snow()
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        #Reading Labels
        with open("labels.txt") as f:
            content = f.readlines()
        label = []
        for i in content:
            label.append(i[:-1])
        st.success("Model is Predicting it's a {}".format(label[result_index]))
