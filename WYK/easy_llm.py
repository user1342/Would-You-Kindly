import re
from typing import List, Tuple

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


class EasyLLM:
    """
    A simple class for interacting with a pretrained language model for generating dialogue responses.
    """

    def __init__(
        self,
        max_new_tokens: int = 200,
        model_name: str = "unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
    ) -> None:
        """
        Initializes the EasyLLM class with a given model and token limit.

        Args:
            max_new_tokens: Maximum number of new tokens to generate in a response.
            model_name: Name of the pretrained language model.
        """
        self.max_new_tokens = max_new_tokens
        self.model_name = model_name

    def _load_model(
        self, model_name: str, device: str
    ) -> Tuple[AutoModelForCausalLM, AutoTokenizer]:
        """
        Load the pretrained language model and tokenizer.

        Args:
            model_name: Name of the pretrained model.
            device: Device to load the model onto (e.g., "cuda" or "cpu").

        Returns:
            Tuple[AutoModelForCausalLM, AutoTokenizer]: Loaded language model and tokenizer.
        """
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )
        model = AutoModelForCausalLM.from_pretrained(
            model_name, quantization_config=quantization_config
        )
        tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side="left")
        return model, tokenizer

    def _generate_dialogue_response(
        self,
        model: AutoModelForCausalLM,
        tokenizer: AutoTokenizer,
        device: str,
        messages: List[dict],
    ) -> str:
        """
        Generate a response from the language model given the input messages.

        Args:
            model: Loaded language model.
            tokenizer: Loaded tokenizer.
            device: Device to run the model on.
            messages: List of input messages.

        Returns:
            str: Generated response from the language model.
        """
        encodeds = tokenizer.apply_chat_template(messages, return_tensors="pt")
        model_inputs = encodeds.to(device)
        generated_ids = model.generate(
            model_inputs,
            max_new_tokens=self.max_new_tokens,
            do_sample=True,
            pad_token_id=50256,
        )
        decoded = tokenizer.batch_decode(generated_ids, skip_special_tokens=False)
        return decoded[0]

    def _remove_inst_tags(self, text: str) -> str:
        """
        Remove instruction tags and other unwanted tokens from the generated text.

        Args:
            text: Input text containing instruction tags.

        Returns:
            str: Cleaned text with instruction tags removed.
        """
        pattern = r"\[INST\].*?\[/INST\]"
        clean_text = re.sub(pattern, "", text, flags=re.DOTALL)
        return (
            clean_text.replace("<s>", "")
            .replace("</s>", "")
            .replace("Explanation:", "")
            .strip()
        )

    def ask_question(self, question: str) -> str:
        """
        Generate a response for the given question using the loaded model.

        Args:
            question: The question or prompt provided by the user.

        Returns:
            str: Generated response to the question.
        """
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model, tokenizer = self._load_model(self.model_name, device)
        result = self._generate_dialogue_response(
            model, tokenizer, device, [{"role": "user", "content": question}]
        )
        return self._remove_inst_tags(result)
