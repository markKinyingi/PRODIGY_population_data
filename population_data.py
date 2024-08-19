import pandas as pd
import streamlit as st
import altair as alt

st.title("Population analysis by Country")

# Load the data from the World Bank API
url = "API_SP.POP.TOTL_DS2_en_csv_v2_3369961.csv"
data = pd.read_csv(url, sep=",", skiprows=[0,1,2,3])

# Data preview
st.subheader("Data preview")
st.write(data.head())

# Data summary
st.subheader("Data summary")
st.write(data.describe())

# Data visualization
st.subheader("Data Comparison")

def data_visualization(max_countries):
    country_numb = st.number_input(label=f"Select a maximum of {max_countries} countries to compare?", min_value=1, max_value=max_countries, value=1)

    selections = []

    for i in range(country_numb):
        choice = st.selectbox(
            f'Select country {i+1}',
            data.loc[:, 'Country Name'],
            key=f'selectbox_{i}'
        )
        selections.append(choice)
        # Getting the index of the country name
        val = data.loc[:, 'Country Name']
        val.tolist()
        for i in range(len(val)):
            if val[i] == choice:
                number = i
            else:
                continue

        var = data.loc[number, '1960':'2023']

        years = list(range(1960, 2024))
        values = var.tolist()

        # Create a DataFrame
        population = values
        df = pd.DataFrame({'Year': years, 'Population': population})

        # Create the Altair chart
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('Year:O', title='Year'),
            y=alt.Y('Population:Q', title='Population'),
            tooltip=['Year', 'Population']
        ).properties(
            title=f'Population of {data.loc[number, 'Country Name']} from 1960 to 2023'
        ).configure_mark(
            opacity=0.7,
            color='white'
        )

        st.altair_chart(chart, use_container_width=True)

# Calling the function
data_visualization(3)