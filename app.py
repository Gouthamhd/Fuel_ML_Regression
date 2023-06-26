
import pickle
import streamlit as st

from zipfile import ZipFile


# loading the temp.zip and creating a zip object
with ZipFile("regression_walmart_rf.pkl.zip", 'r') as zObject:
  
    # Extracting all the members of the zip 
    # into a specific location.
    zObject.extractall()

# loading the trained model
pickle_in = open('regression_walmart_rf.pkl', 'rb')
regressor = pickle.load(pickle_in)

@st.cache_data()

# defining the function which will make the prediction using the data which the user inputs
def prediction(Store, Holiday, Temperature, Fuel_Price, CPI, Unemployment, Day, Week,Month,Year):
  Holiday_Flag = 0  
  if Holiday == "Holiday":
      Holiday_Flag = 1
  else:
      Holiday_Flag = 0
    # Making predictions
  prediction = regressor.predict(
        [[Store, Holiday_Flag, Temperature, Fuel_Price, CPI, Unemployment, Day, Week,Month,Year]])

  return prediction


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:pink;padding:13px">
    <h1 style ="color:black;text-align:center;"> Goutham AI Walmart Sale Prediction ML App</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)
    st.image("""data:image/jpeg;base64,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""")
    st.image("""data:image/jpeg;base64,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""")
    # following lines create boxes in which user can enter data required to make prediction
    Store = st.number_input("EnterNumber of Store Number",min_value=1, max_value=50)
    Holiday = st.selectbox('Holiday Status',("Holiday","Not Holiday"))
    Temperature = st.number_input("Enter The Temperature value", min_value=1.0, max_value=75.0)
    Fuel_Price = st.number_input("Enter The Fuel_Price value", min_value=1.0, max_value=75.0)
    CPI = st.number_input("Enter The CPI value", min_value=100.0, max_value=250.0)
    Unemployment = st.number_input("Enter Unemployment Rate", min_value=1.0, max_value=20.0)
    Day = st.number_input("Enter The Day of Week",min_value=0, max_value=6)
    Week = st.number_input("Enter The Week of the Year",min_value=1, max_value=53)
    Month = st.number_input("Enter The Month of the Year",min_value=1, max_value=12)
    Year =  st.number_input('Enter The Year',min_value=2010, max_value=2023)
    result =""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(Store, Holiday, Temperature, Fuel_Price, CPI, Unemployment, Day, Week,Month,Year)
        st.success('Your Walmart Sale Prediction is {}'.format(result))
        print(result)

if __name__=='__main__':
    main()
