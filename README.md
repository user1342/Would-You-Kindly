<p align="center">
    <img width=100% src="WYK.png">
  </a>
</p>
<p align="center"> 🤖 Testing LLM security with simulated attacks ⚔️ </p>


WouldYouKindly is a security testing tool designed to evaluate the effectiveness of large language models (LLMs) in protecting secrets and preventing security breaches. With customisable LLM options, the tool allows you to simulate attacks on LLMs using various techniques and observe their defence capabilities.

- 🔐 **Attack Simulation**: Use natural language prompts to simulate security attacks on LLMs. Test the resilience of LLMs against sophisticated attempts to retrieve hidden secrets.
- ⚔️ **Red and Blue Agent Setup**: Utilize both Red (attacking) and Blue (defending) agents to simulate realistic scenarios, ensuring thorough testing of the LLM’s security measures.
- 🤖 **Natural Language Input**: Formulate open-ended security challenges and attack strategies in plain text, powered by a built-in language model.
- 📊 **Automated Scoring**: Automatically evaluate the LLM's performance and security level based on the success of the attacks.

# ⚙️ Setup
## System Requirements
WouldYouKindly is built using the Mistral-7B-Instruct-v0.3 model, with optimizations for GPU offloading where possible. The recommended hardware setup includes:

- Minimum 16GB of RAM.
- Nvidia GPU with at least 4GB of VRAM for enhanced performance (though CPU execution is supported for lower-spec machines, with slower response times).

Tested on Windows 11. Should be compatible with other Unix-like systems as well.

### GPU and CUDA Setup
For enhanced performance, it is highly recommended to install Nvidia CUDA. Follow the steps below:

- Make sure your Nvidia drivers are up to date: Download here.
- Install PyTorch with GPU support: Follow the instructions here to set up CUDA on your machine.
- Validate CUDA installation:

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

You can install WouldYouKindly by running the following command:

```bash
python -m pip install .
```

# 🏃 Running the Tool
To perform a security test against a target LLM, follow the steps below:

## Example Execution
Initialize the Judge: The Judge class oversees the interaction between the Red (attacking) and Blue (defending) agents. Here is an example of running the tool:

```python
llm_name = "unsloth/mistral-7b-instruct-v0.3-bnb-4bit"
judge = Judge(llm_name, llm_name, llm_name, debug=True)
print(f"LLM '{llm_name}' scored {judge.asses()}")
```

Understanding Output: The Judge will return a score between 0 and 10, where:

- 0 indicates a complete failure to defend against attacks.
- 10 represents perfect defense and security against all known attack vectors.

# ⚔️ Attack Techniques
WouldYouKindly uses a range of sophisticated attack strategies, including:

- Token Smuggling: Encoding restricted content in various formats (e.g., Morse code, hexadecimal).
- Hypothetical Scenarios: Asking the LLM to consider an imaginary scenario where restricted actions are permissible.
- Few-shot and Many-shot Attacks: Providing multiple examples of compliance before asking the model to reveal the secret.
- Output Formatting Manipulation: Changing the format of the output (e.g., Base64, leetspeak) to bypass restrictions.

# 🙏 Contributions
Would You kindly is an open-source project and welcomes contributions from the community. If you would like to contribute to Monocle, please follow these guidelines:

- Fork the repository to your own GitHub account.
- Create a new branch with a descriptive name for your contribution.
- Make your changes and test them thoroughly.
- Submit a pull request to the main repository, including a detailed description of your changes and any relevant documentation.
- Wait for feedback from the maintainers and address any comments or suggestions (if any).
- Once your changes have been reviewed and approved, they will be merged into the main repository.

# ⚖️ Code of Conduct
Would You kindly follows the Contributor Covenant Code of Conduct. Please make sure to review and adhere to this code of conduct when contributing to Monocle.

# 🐛 Bug Reports and Feature Requests
If you encounter a bug or have a suggestion for a new feature, please open an issue in the GitHub repository. Please provide as much detail as possible, including steps to reproduce the issue or a clear description of the proposed feature. Your feedback is valuable and will help improve Monocle for everyone.

# 📜 License
GNU General Public License v3.0
