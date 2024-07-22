{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "aa43d618-b667-4619-bf07-2485f3e9ee95",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\lenovo\\anaconda3\\Lib\\site-packages\\sklearn\\base.py:318: UserWarning: Trying to unpickle estimator LinearRegression from version 0.23.2 when using version 1.2.2. This might lead to breaking code or invalid results. Use at your own risk. For more info please refer to:\n",
      "https://scikit-learn.org/stable/model_persistence.html#security-maintainability-limitations\n",
      "  warnings.warn(\n",
      "2024-07-21 21:01:57.275 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\lenovo\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import numpy as np\n",
    "\n",
    "# Load the model\n",
    "with open(r'C:\\Users\\lenovo\\Documents\\hack\\model.pkl', 'rb') as file:\n",
    "    model = pickle.load(file)\n",
    "\n",
    "# Streamlit front-end\n",
    "st.title(\"Housing Price Prediction\")\n",
    "\n",
    "# Create input fields\n",
    "square_footage = st.number_input(\"Enter square footage:\")\n",
    "bedrooms = st.number_input(\"Enter number of bedrooms:\")\n",
    "bathrooms = st.number_input(\"Enter number of bathrooms:\")\n",
    "\n",
    "# Button to make prediction\n",
    "if st.button(\"Predict\"):\n",
    "    input_features = np.array([[square_footage, bedrooms, bathrooms]])\n",
    "    prediction = model.predict(input_features)\n",
    "    st.write(\"Predicted Price:\", prediction[0])\n",
    "\n",
    "# Additional features like charts, etc.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e18d9d3d-bb0a-42fc-b9a3-01596a0b12f4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
