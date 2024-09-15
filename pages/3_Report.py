import pandas as pd
import streamlit as st
import datetime
from Home import face_rec

# Function to retrieve logs from Redis


def retrieve_logs():
    try:
        logs_data = face_rec.retrieve_logs_from_redis()
        if isinstance(logs_data, pd.DataFrame):
            return logs_data
        else:
            return pd.DataFrame()  # Return an empty DataFrame if data is not in expected format
    except Exception as e:
        st.error(f"Error retrieving logs from Redis: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error


# Tabs setup
st.title("Attendance and Logs Report")
tab1, tab2, tab3 = st.columns(3)

# Tab 1: Registered Data
with tab1:
    st.subheader('Registered Data')
    if st.button('Refresh Data'):
        with st.spinner('Retrieving Data from Redis DB ...'):
            try:
                redis_face_db = face_rec.retrive_data(name='academy:register')
                if isinstance(redis_face_db, pd.DataFrame):
                    st.dataframe(redis_face_db[['Name', 'Role']])
                else:
                    st.error("Data format from Redis is not correct.")
            except Exception as e:
                st.error(f"Error retrieving data from Redis: {e}")

# Tab 2: Logs
with tab2:
    st.subheader('Logs')
    if st.button('Refresh Logs'):
        with st.spinner('Retrieving Logs from Redis DB ...'):
            logs_df = retrieve_logs()  # Fetch logs from Redis
            if not logs_df.empty:
                st.dataframe(logs_df)
            else:
                st.write("No logs available or error occurred.")

# Tab 3: Attendance Report
with tab3:
    st.subheader('Attendance Report')

    # Retrieve logs dynamically
    with st.spinner('Processing Logs for Report ...'):
        logs_df = retrieve_logs()

        if not logs_df.empty:
            # Processing logs into a report
            report_df = logs_df.groupby(['Name', 'Role']).agg(
                In_time=pd.NamedAgg(column='Timestamp', aggfunc='min'),
                Out_time=pd.NamedAgg(column='Timestamp', aggfunc='max')
            ).reset_index()

            report_df['Duration'] = report_df['Out_time'] - \
                report_df['In_time']
            report_df['Duration_hours'] = report_df['Duration'] / \
                pd.Timedelta(hours=1)

            # Displaying complete and filtered reports
            tab1, tab2 = st.columns(2)

            with tab1:
                st.subheader('Complete Report')
                st.dataframe(report_df)

            with tab2:
                st.subheader('Search Records')

                # Filter options
                date_in = st.date_input(
                    'Filter Date', datetime.datetime.now().date())
                name_list = report_df['Name'].unique().tolist()
                name_in = st.selectbox('Select Name', ['ALL'] + name_list)

                role_list = report_df['Role'].unique().tolist()
                role_in = st.selectbox('Select Role', ['ALL'] + role_list)

                duration_in = st.slider('Filter Duration in Hours', 0, 24, 6)

                status_list = [
                    'Present',
                    'Absent',
                    'Half Day (less than 4 hours)',
                    'Absent (Less than 1 hr)'
                ]
                status_in = st.multiselect(
                    'Select Status', status_list, default=status_list)

                if st.button('Apply Filters'):
                    filter_df = report_df.copy()
                    filter_df['Duration_hours'] = filter_df['Duration'] / \
                        pd.Timedelta(hours=1)

                    if name_in != 'ALL':
                        filter_df = filter_df[filter_df['Name'] == name_in]

                    if role_in != 'ALL':
                        filter_df = filter_df[filter_df['Role'] == role_in]

                    if duration_in > 0:
                        filter_df = filter_df[filter_df['Duration_hours']
                                              >= duration_in]

                    if 'Present' not in status_in:
                        filter_df = filter_df[~filter_df['Duration_hours'].isnull(
                        )]

                    st.dataframe(filter_df)
        else:
            st.write("No logs available for report generation.")
