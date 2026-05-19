import streamlit as st

def render_experiments(data):
    if not data:
        st.warning("No experiments found")
    for exp in data:

        exp_name = exp.get("name", "Experiment")
        exp_id = exp.get("id", "unknown")

        with st.expander(
            f"📋 {exp_name} ({exp_id})"
        ):

            questions = exp.get("questions", [])
            answers = exp.get("answers", [])
            metrics = exp.get("metrics", {})

            answers_map = {
                a["id"]: a for a in answers
            }

            for q in questions:

                st.markdown(
                    f"""
                    <div class="result-box">
                        <p style="color:#c084fc;">
                            ❓ <b>{q.get("id", "")}</b>
                        </p>

                        <p style="color:white;">
                            {q.get("text", "")}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if q.get("ground_true"):

                    st.success(
                        f"🎯 {q['ground_true']}"
                    )

                answer = answers_map.get(
                    q.get("id")
                )

                if answer and answer.get("text"):

                    st.info(
                        f"🤖 {answer['text']}"
                    )

                    metric_data = metrics.get(
                        answer["id"],
                        {}
                    )

                    st.json(metric_data)

                else:
                    st.warning(
                        "No answer yet"
                    )