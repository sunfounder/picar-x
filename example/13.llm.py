from picarx.llm import LLM

INSTRUCTIONS = "You are a funny rejector, who will reject any question or request with a funny reason."
WELCOME = "Ask me anything, maybe I can help. (or not)"

llm = LLM()

# ================= Set API Key =======================
# Set API Key with environment variable is recommended.
# export LLM_API_KEY=sk-xxxxxxxxxx
# or uncomment the following line
# llm.set_api_key("sk-xxxxxxxxxx")

# ================= Set LLM Server =======================
# Deepseek
llm.set_base_url("https://api.deepseek.com")
# Local
# llm.set_base_url("http://localhost:8000")
# OpenAI
# llm.set_base_url("https://api.openai.com")

# ================= Set LLM Model =======================
# Deepseek R1
llm.set_model("deepseek-reasoner")
# Local
# llm.set_model("local-model")

# Set OpenAI gpt4o
llm.set_model("gpt-4o")


# Set how many messages to keep
llm.set_max_messages(20)
# Set instructions
llm.set_instructions(INSTRUCTIONS)
# Set welcome message
llm.set_welcome(WELCOME)

print(WELCOME)

while True:
    input_text = input(">>> ")

    # Response without stream
    # response = llm.prompt(input_text)
    # print(f"response: {response}")

    # Response with stream
    response = llm.prompt(input_text, stream=True)
    llm.print_stream(response)

