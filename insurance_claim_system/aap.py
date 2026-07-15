import streamlit as st
from graph_logic.workflow import app
 
tab1, tab2, tab3 = st.tabs(["Submission", "Dashboard", "Manual Review"])
 
with tab1:
    st.header("Claim Submission")
    with st.form("claim"):
        amount = st.number_input("Amount")
        if st.form_submit_button("Submit"):
            res = app.invoke(
                {"claim_amount": amount, "audit_log": []},
                config={"configurable": {"thread_id": "claim-session"}},
            )
            st.write("Recommendation:", res.get("recommendation"))
 
with tab2:
    st.header("Dashboard")
    st.write("Monitor agent status and graph path here.")
 
with tab3:
    st.header("Manual Review Queue")
    st.write("Claims flagged for manual intervention will appear here.")