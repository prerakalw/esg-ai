"""Custom LLM implementation using Google Generative AI directly."""
import google.generativeai as genai
from crewai.llms.base_llm import BaseLLM
from typing import Optional, Any, Dict, List

class GeminiLLM(BaseLLM):
    """Custom LLM implementation using Google Generative AI directly."""
    
    def __init__(self, model: genai.GenerativeModel):
        """Initialize with a Gemini model instance."""
        self.gemini_model = model
        super().__init__(model="gemini-1.5-pro")  # Pass the model name to the parent class

    def _format_prompt(self, prompt: Any) -> Dict[str, str]:
        """Helper method to format prompts consistently."""
        if isinstance(prompt, dict):
            if 'role' in prompt and 'content' in prompt:
                return {'text': prompt['content']}
            elif 'parts' in prompt:
                return prompt  # Already in Google Generative AI format
            else:
                return {'text': str(prompt)}
        elif isinstance(prompt, list):
            # If it's a list of messages, combine them
            text = "\n".join(
                msg['content'] if isinstance(msg, dict) and 'content' in msg 
                else str(msg) for msg in prompt
            )
            return {'text': text}
        elif isinstance(prompt, str):
            return {'text': prompt}
        else:
            return {'text': str(prompt)}

    def call(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        stream: Optional[bool] = False,
        stop: Optional[List[str]] = None,
        callbacks: Optional[Any] = None,  # Add support for callbacks
        **kwargs: Any  # Handle any additional arguments
    ) -> str:
        """Execute the LLM call with the given prompt."""
        try:
            if callbacks and hasattr(callbacks[0], 'on_llm_start'):
                callbacks[0].on_llm_start({"name": self.type})

            # Format the prompt
            formatted_prompt = self._format_prompt(prompt)

            # Configure generation parameters
            generation_config = {
                'temperature': temperature if temperature is not None else 0.7,
                'max_output_tokens': max_tokens if max_tokens is not None else 2048,
            }
            if stop:
                generation_config['stop_sequences'] = stop

            # Generate content with the processed prompt
            response = self.gemini_model.generate_content(
                formatted_prompt,
                generation_config=generation_config
            )
            
            if not response.text:
                error_msg = "Empty response from Gemini API"
                if callbacks and hasattr(callbacks[0], 'on_llm_error'):
                    callbacks[0].on_llm_error(error_msg)
                raise ValueError(error_msg)
            
            if callbacks:
                if hasattr(callbacks[0], 'on_llm_new_token'):
                    callbacks[0].on_llm_new_token(response.text)
                if hasattr(callbacks[0], 'on_llm_end'):
                    callbacks[0].on_llm_end()
                
            return response.text
            
        except Exception as e:
            error_msg = f"Error calling Gemini API: {str(e)}"
            if callbacks and hasattr(callbacks[0], 'on_llm_error'):
                callbacks[0].on_llm_error(error_msg)
            if isinstance(e, ValueError):
                raise e
            raise RuntimeError(error_msg)

    def stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        stop: Optional[List[str]] = None,
        callbacks: Optional[Any] = None,  # Add support for callbacks
        **kwargs: Any  # Handle any additional arguments
    ):
        """Stream response from the LLM."""
        try:
            if callbacks and hasattr(callbacks[0], 'on_llm_start'):
                callbacks[0].on_llm_start({"name": self.type})

            # Format the prompt
            formatted_prompt = self._format_prompt(prompt)

            # Configure generation parameters
            generation_config = {
                'temperature': temperature if temperature is not None else 0.7,
                'max_output_tokens': max_tokens if max_tokens is not None else 2048,
            }
            if stop:
                generation_config['stop_sequences'] = stop

            # Generate streaming content with the processed prompt
            response = self.gemini_model.generate_content(
                formatted_prompt,
                generation_config=generation_config,
                stream=True
            )
            
            for chunk in response:
                if chunk.text:
                    if callbacks:
                        if hasattr(callbacks[0], 'on_llm_new_token'):
                            callbacks[0].on_llm_new_token(chunk.text)
                    yield chunk.text
            
            if callbacks and hasattr(callbacks[0], 'on_llm_end'):
                callbacks[0].on_llm_end()
                    
        except Exception as e:
            error_msg = f"Error streaming from Gemini API: {str(e)}"
            if callbacks and hasattr(callbacks[0], 'on_llm_error'):
                callbacks[0].on_llm_error(error_msg)
            if isinstance(e, ValueError):
                raise e
            raise RuntimeError(error_msg)

    @property
    def type(self) -> str:
        """Return type of LLM."""
        return "gemini"
