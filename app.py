import streamlit as st
import pandas as pd
import preprocessor , helper
import plotly.express as px
import plotly.figure_factory as ff
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)
st.sidebar.title("Olympics Analysis")
st.sidebar.image("data:image/png;base64,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")
user_menu = st.sidebar.radio(
    'select an Option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athelete wise Analysis')
)

#st.dataframe(df)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years ,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_country = st.sidebar.selectbox("Select country" , country)

    medal_tally = helper.fetch_metal_tally(df, selected_year , selected_country)

    if selected_year == 'Overall' and selected_country =='Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country =='Overall':
        st.title("Medal Tally in "+ str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title((selected_country)+" Overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)
if user_menu =='Overall Analysis':
    editions = df['Year'].unique().shape[0] -1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    atheletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]


    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Edition')
        st.title(editions)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1 , col2 , col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athelets')
        st.title(atheletes)

    nation_over_time = helper.data_over_time(df, 'region')
    fig = px.line(nation_over_time , x = "Edition" , y = "region" )
    st.title("Participating Nations over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df , 'Event')
    fig = px.line(events_over_time , x = "Edition" , y = "Event")
    st.title("Events over the Years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df , 'Name')
    fig = px.line(athlete_over_time , x = "Edition" , y = "Name")
    st.title("Athletes over the Years")
    st.plotly_chart(fig)

    st.title("No of Events over time ( Every Sport) ")
    fig , ax = plt.subplots(figsize =(15,15))
    x = df.drop_duplicates([ 'Year' , 'Sport' , 'Event' ])
    ax = sns.heatmap(
     x.pivot_table(index = 'Sport' , columns = 'Year' , values = 'Event' , aggfunc = 'count').fillna(0).astype(
            'int') , annot = True)
    st.pyplot(fig)

    st.title("Most Successful Athelets")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x.reset_index())

if user_menu =='Country-wise Analysis':
    st.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country', country_list)

    country_df = helper.yearwise_medal_tally(df , selected_country)
    fig = px.line(country_df , x = "Year" , y = "Medal")
    st.title(selected_country +" Medal Tally over the Years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sport")
    pt =helper.country_event_heatmap(df ,selected_country)
    fig , ax = plt.subplots(figsize = (15 , 15))
    ax = sns.heatmap(pt , annot = True)
    st.pyplot(fig)

    st.title("Top 10 athletes of "+ selected_country)
    top10_df = helper.most_successful_countrywise(df ,selected_country)
    st.table(top10_df.head(10).reset_index())

if user_menu == 'Athelete wise Analysis':

    athlete_df = df.drop_duplicates(subset = [ 'Name' , 'region' ])

    x1 = athlete_df [ 'Age' ].dropna()
    x2 = athlete_df [ athlete_df [ 'Medal' ] == 'Gold' ] [ 'Age' ].dropna()
    x3 = athlete_df [ athlete_df [ 'Medal' ] == 'Silver' ] [ 'Age' ].dropna()
    x4 = athlete_df [ athlete_df [ 'Medal' ] == 'Bronze' ] [ 'Age' ].dropna()

    fig = ff.create_distplot([ x1 , x2 , x3 , x4 ] ,
                             [ 'Overall Age' , 'Gold Medalist' , 'Silver Medalist' , 'Bronze Medalist' ] ,
                             show_hist = False , show_rug = False)
    # fig.update_layout(autosize = False, width = 100 ,height = 600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    sport_list = df [ 'Sport' ].unique().tolist()
    sport_list.sort()
    sport_list.insert(0 , 'Overall')
    st.title("Height VS Weight")
    selected_sport = st.selectbox('Select a sport' , sport_list)
    temp_df = helper.weight_V_height(df,selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(temp_df['Weight'],temp_df['Height'],hue =temp_df['Medal'],style = temp_df['Sex'],s =60,)
    st.pyplot(fig)

    st.title("Men Vs Women Participation over the Year")

    final = helper.men_vs_women(df)
    fig = px.line(final , x = 'Year' , y = [ 'Male' , 'Female' ])
    st.plotly_chart(fig)