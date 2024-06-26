import pickle
import streamlit as st
# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)
@st.cache_data()
# defining the function which will make the prediction using the data which the user inputs
def prediction(Gender, Married, Dependents, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Credit_History):  
   # Pre-processing user input    
   if Gender == "Male":
       Gender = 0
   else:
       Gender = 1
   if Married == "Unmarried":
       Married = 0
   else:
       Married = 1
   if Self_Employed == "No":
       Self_Employed =0
   else:
       Self_Employed = 1
   if Credit_History == "Unclear Debts":
       Credit_History = 0
   else:
       Credit_History = 1  
   LoanAmount = LoanAmount / 1000 

   # Making predictions
   prediction = classifier.predict(
       [[Gender, Married, Dependents, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Credit_History]])
   if prediction == 0:
       pred = 'Rejected'
   else:
       pred = 'Approved'
   return pred

# this is the main function in which we define our webpage  
def main():      
   # front end elements of the web page
   html_temp = """
<div style ="background-color:blue;padding:13px">
<h1 style ="color:white;text-align:center;">Loan Pre-screening Prediction ML Application</h1>
</div>
   """
   # display the front end aspect
   st.markdown(html_temp, unsafe_allow_html = True)
   # following lines create boxes in which user can enter data required to make prediction
   Gender = st.selectbox('Gender',("Male","Female"))
   Married = st.selectbox('Marital Status',("Unmarried","Married"))
   Dependents = st.number_input('Dependents')
   Self_Employed = st.selectbox('Self_Employed', ("Yes","No"))
   ApplicantIncome = st.number_input("Monthly Income")
   CoapplicantIncome = st.number_input('Other Income')
   LoanAmount = st.number_input("Total loan amount")
   Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
   result =""
   # when 'Predict' is clicked, make the prediction and store it
   if st.button("Predict"):
       result = prediction(Gender, Married, Dependents, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Credit_History)
       if result == 'Rejected':
           st.error('Your loan is {}'.format(result))
       else:
           st.success('Your loan is {}'.format(result))
       print(LoanAmount)
if __name__=='__main__':
   main()
