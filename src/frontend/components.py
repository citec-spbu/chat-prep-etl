import streamlit as st

def render_experiments(data):
    if not data:
        st.warning("No experiments found")
        return
    
    for exp in data:
        exp_name = exp.get("name", "Experiment")
        exp_id = exp.get("id", "unknown")

        with st.expander(f" {exp_name} ({exp_id})"):
            questions = exp.get("questions", [])
            answers = exp.get("answers", [])
            metrics = exp.get("metrics", {})
            answers_map = {a["id"]: a for a in answers}

            for idx, q in enumerate(questions, start=1):
                q_id = q.get("id", "")
                q_text = q.get("text", "")
                ground_true = q.get("ground_true", "")
                metadata = q.get("metadata")

                with st.container(border=True):
                    st.markdown(f"""
                    <div class="result-box">
                        <p style="color:#c084fc; font-size: 20px; font-weight: bold;">
                             Вопрос {idx}: {q_id}
                        </p>
                        <p style="color:#e2e8f0; font-size: 16px; line-height: 1.5;">
                            {q_text}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    if ground_true:
                        with st.expander(" Правильный ответ (Ground Truth)", expanded=False):
                            st.markdown(f'<p style="color:#86efac;">{ground_true}</p>', unsafe_allow_html=True)
                    
                    if metadata:
                        with st.expander(" Метаданные (System Prompt)", expanded=True):
                            system_prompt = metadata.get("system_prompt", "")
                            if system_prompt:
                                st.markdown("** System Prompt:**")
                                st.code(system_prompt, language="text", line_numbers=False)
                    
                    answer = answers_map.get(q_id)
                    if answer and answer.get("text"):
                        with st.expander(" Ответ модели", expanded=True):
                            st.markdown(f'<p style="color:#fcd34d;">{answer["text"]}</p>', unsafe_allow_html=True)
                            
                            metric_data = metrics.get(answer["id"], {})
                            if metric_data:
                                st.markdown("** Метрики:**")
                                if isinstance(metric_data, dict):
                                    # Удаляем поле metadata, если оно есть и равно None
                                    if "metadata" in metric_data and metric_data["metadata"] == "NULL":
                                        del metric_data["metadata"]
                                    st.json(metric_data)
                                else:
                                    st.write(metric_data)
                    else:
                        st.warning(" Нет ответа от модели")
                    
                    st.divider()

def render_search_results(results, t):
    if not results:
        st.warning(t["nothing_found"])
    else:
        st.success(f"{t['results_found']}: {len(results)}")
        for i, result in enumerate(results, start=1):
            chat_id = result.get("chat_id", "")
            sender_id = result.get("sender_id", "")
            text = result.get("text", "")
            attached_files = result.get("attached_files", [])

            with st.container(border=True):
                st.subheader(f"{t['result']} {i}")
                st.write(f"**Sender:** {sender_id}")
                st.write("**Message:**")
                st.markdown(
                    f"<p style='font-size:30px;'>{text}</p>",
                    unsafe_allow_html=True
                )
                if attached_files:
                    st.write("**Files:**")
                    for file in attached_files:
                        st.write(f"- {file}")