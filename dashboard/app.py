import streamlit as st
import requests

st.set_page_config(
    page_title="ALIP v1.0 - QMS_TAT",
    page_icon="🧪",
    layout="wide",
)

st.title("ALIP v1.0 — QMS_TAT")
st.subheader("Laboratory TAT Foundation")

st.info("BUILD-17B-R3 — Domain Behaviour Verified")

api_url = st.text_input(
    "FastAPI Base URL",
    value="http://127.0.0.1:8000",
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### API Health")

    if st.button("Check Health"):
        try:
            response = requests.get(
                f"{api_url}/health",
                timeout=5,
            )

            st.write(f"HTTP {response.status_code}")
            st.json(response.json())

        except requests.RequestException as exc:
            st.error(f"API unavailable: {exc}")

with col2:
    st.markdown("### TAT Calculation")

    started_at = st.text_input(
        "Started At",
        value="2026-08-27T08:00:00+00:00",
    )

    completed_at = st.text_input(
        "Completed At",
        value="2026-08-27T08:30:00+00:00",
    )

    target_minutes = st.number_input(
        "Target Minutes",
        min_value=1,
        value=60,
        step=1,
    )

    if st.button("Calculate TAT"):
        try:
            response = requests.post(
                f"{api_url}/tat/calculate",
                json={
                    "started_at": started_at,
                    "completed_at": completed_at,
                    "target_minutes": target_minutes,
                },
                timeout=5,
            )

            st.write(f"HTTP {response.status_code}")

            if response.ok:
                st.success("TAT calculation successful")
                st.json(response.json())
            else:
                st.error(response.text)

        except requests.RequestException as exc:
            st.error(f"API unavailable: {exc}")

st.divider()

st.caption(
    "ALIP v1.0 | QMS_TAT | TAT Management Foundation"
)
