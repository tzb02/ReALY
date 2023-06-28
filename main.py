import time
import streamlit as st
st.title("PropValAI")
st.write("Enter an address to get property and rental evaluations, along with neighborhood information.")

address = st.text_input("Address")
submit_button = st.button("Submit")
if address=='6307 Prestonshire Ln, Dallas, TX 75225':
# Function to get property and rental evaluation (replace with your own implementation)
    def get_property_rental_evaluation(address):
        property_evaluation = {
            'Estimated property value': '$2,705,800',
            'Price per square foot': '$502.75',
            'Comparable properties': 5,
            'Historical price trends': 'Upward'
    }
        rental_evaluation = {
            'Estimated monthly rent': '$15,625',
            'Rent per square foot': '$2.90',
            'Comparable rental properties': 4,
            'Historical rental trends': 'Upward'
    }
        return property_evaluation, rental_evaluation


# Function to get neighborhood information (replace with your own implementation)
    def get_neighborhood_information(address):
        neighborhood_info = {
            'Average home price': '$2,420,000',
            'Average rent price': '$2,380',
            'Crime rate': 'Low',
            'School ratings': 'Above average',
            'Walkability score': 13,
        
    }
        return neighborhood_info
elif address=='6314 Palo Pinto Ave, Dallas, TX 75214':
# Function to get property and rental evaluation (replace with your own implementation)
        def get_property_rental_evaluation(address):
            property_evaluation = {
                'Estimated property value': '$1,412,200',
                'Price per square foot': '$357.97',
                'Comparable properties': 5,
                'Historical price trends': 'Upward'
    }
            rental_evaluation = {
                'Estimated monthly rent': '$8,763',
                'Rent per square foot': '$2.22',
                'Comparable rental properties': 4,
                'Historical rental trends': 'Upward'
    }
            return property_evaluation, rental_evaluation

# Function to get neighborhood information (replace with your own implementation)
        def get_neighborhood_information(address):
            neighborhood_info = {
                'Average home price': '$980,000',
                'Average rent price': '$3,188',
                'Crime rate': 'Low',
                'School ratings': 'Average',
                'Walkability score': 51,
        
    }
            return neighborhood_info
elif address=='6314 Palo Pinto Ave, Dallas, TX 75214':
# Function to get property and rental evaluation (replace with your own implementation)
        def get_property_rental_evaluation(address):
            property_evaluation = {
                'Estimated property value': '$181,400',
                'Price per square foot': '$175.27',
                'Comparable properties': 5,
                'Historical price trends': 'Upward'
    }
            rental_evaluation = {
                'Estimated monthly rent': '$1,625',
                'Rent per square foot': '$1.57',
                'Comparable rental properties': 4,
                'Historical rental trends': 'Upward'
    }
            return property_evaluation, rental_evaluation

# Function to get neighborhood information (replace with your own implementation)
        def get_neighborhood_information(address):
            neighborhood_info = {
                'Average home price': '$226,000',
                'Average rent price': '$1,994',
                'Crime rate': 'Average',
                'School ratings': 'Below Average',
                'Walkability score': 74,
        
    }
            return neighborhood_info

# App layout


if submit_button:
    time.sleep(12)
    property_evaluation, rental_evaluation = get_property_rental_evaluation(address)
    neighborhood_info = get_neighborhood_information(address)

    st.header("Property & Rental Evaluation")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Property Evaluation")
        for key, value in property_evaluation.items():
            st.write(f"{key}: {value}")

    with col2:
        st.subheader("Rental Evaluation")
        for key, value in rental_evaluation.items():
            st.write(f"{key}: {value}")

    st.header("Neighborhood Information")
    for key, value in neighborhood_info.items():
        st.write(f"{key}: {value}")


