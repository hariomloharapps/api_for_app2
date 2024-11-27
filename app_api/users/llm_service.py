from groq import Groq
from datetime import datetime
import logging
from typing import Dict, List, Optional

class LLMService:
    def __init__(self):
        # if not api_key:
        #     raise ValueError("API key is required")
        
        try:
            self.client = Groq(api_key="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")
            self.model = "llama-3.2-90b-vision-preview"
            self.temperature = 0.85  # Slightly higher for more creative responses
            self._test_connection()
        except Exception as e:
            logging.error(f"Failed to initialize LLM service: {str(e)}")
            raise

    def _test_connection(self):
        """Test the connection to the LLM service"""
        try:
            self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "test"},
                    {"role": "user", "content": "test"}
                ],
                model=self.model,
                max_tokens=5
            )
        except Exception as e:
            raise ConnectionError(f"Failed to connect to LLM service: {str(e)}")

    def _format_chat_history(self, history: List[Dict], system_prompt: str) -> List[Dict]:
        """Format chat history into the required format for the API"""
        formatted_history = []
        # Always start with the system prompt
        formatted_history.append({
            "role": "system",
            "content": system_prompt
        })
        
        # Add conversation history
        for msg in history:
            if isinstance(msg, dict) and 'content' in msg and 'isUser' in msg:
                formatted_history.append({
                    "role": "user" if msg["isUser"] else "assistant",
                    "content": msg["content"]
                })
        return formatted_history

    def get_response(self, 
                    message: str, 
                    system_prompt: str,
                    chat_history: Optional[List[Dict]] = None) -> Dict:
        """
        Get response from LLM service
        
        Args:
            message (str): User's message
            system_prompt (str): System prompt to set the AI's behavior
            chat_history (Optional[List[Dict]]): Previous chat history
        """
        try:
            if not message.strip():
                return {
                    'error': 'Empty message',
                    'timestamp': datetime.now().strftime("%H:%M"),
                    'status': 'error'
                }

            # Prepare messages with provided system prompt
            messages = self._format_chat_history(chat_history or [], system_prompt)
            
            # Add current message
            messages.append({
                "role": "user",
                "content": message
            })

            # Get completion from API
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=self.temperature,
            )
            
            response = chat_completion.choices[0].message.content
            
            return {
                'response': response,
                'timestamp': datetime.now().strftime("%H:%M"),
                'status': 'success'
            }
            
        except Exception as e:
            logging.error(f"Error getting LLM response: {str(e)}")
            return {
                'error': str(e),
                'timestamp': datetime.now().strftime("%H:%M"),
                'status': 'error'
            }