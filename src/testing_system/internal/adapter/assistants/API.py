from dotenv import load_dotenv

from testing_system.internal.domain.value_objects import \
    AssistantRequest, AssistantResponse
from testing_system.internal.domain.interfaces import IAssistant
import requests
import time
import os, json, copy
from typing import Any, Optional
from pathlib import Path
from dataclasses import dataclass, field

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


class OpenAIAssistant(IAssistant):
    def __init__(self, 
                 model:str,
                 base_url:str,
                 temperature:Optional[float] = 0.9
                 ):
        try:
            load_dotenv(dotenv_path="/workspace/chat-prep-etl/.env")
            assert os.getenv("OPENAI_API_KEY") != None, "Need an API KEY to proceed with this adapter"
            self.model = ChatOpenAI(
                base_url=base_url,
                model=model,
                temperature=temperature
            )
        except Exception as e:
            raise Exception(f"Adapter init fell with error: {e}")
    def llm_chat(self, messages: list) -> AIMessage:
        """
        Sends the message history to the LLM and returns the model response.

        Parameters:
        messages — list of dialog messages. Each message is a LangChain object:
                    SystemMessage(content="...")   — instruction for the model (agent role)
                    HumanMessage(content="...")    — message from the user
                    AIMessage(...)                 — previous model response

        Returns AIMessage:
        msg.content    — text response (str)

        """
        return self.model.invoke(messages)
    def ask(self,r : AssistantRequest) -> AssistantResponse:
        """Asking API model"""
        start_time = time.time()
        documents = "\n".join([
            str(r.retrieved_context[i].id)+"."+r.retrieved_context[i].content \
                for i in range(len(r.retrieved_context))
            ])
        system_prompt = SystemMessage(content=f"{r.system_prompt}\nRetrieved documents:\n{documents}")
        user_prompt = HumanMessage(content = r.question)
        messages = [system_prompt, user_prompt]
        try:
            ai_message = self.llm_chat(messages=messages)
            messages.append(ai_message)
                
            prompt_tokens = ai_message.usage_metadata.get("input_tokens", 0)
            response_tokens = ai_message.usage_metadata.get("output_tokens", 0)
            total_tokens = prompt_tokens + response_tokens
            return AssistantResponse(
                answer = ai_message.content,
                token_count=total_tokens,
                latency_ms = (time.time() - start_time) * 1000,
                used_prompt=messages[:2],
                error = None,
                metadata=None
            )
        except Exception as e:
            return AssistantResponse(
                answer = "",
                token_count=0,
                latency_ms = (time.time() - start_time) * 1000,
                used_prompt=messages[:2],
                error = e,
                metadata=None
            )