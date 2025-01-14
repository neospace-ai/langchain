

from langchain_neospace import ChatNeoSpace

# gets API Key from environment variable NEOSPACE_API_KEY, and NEOSPACE_BASE_URL
model = ChatNeoSpace(
    model="7b-mistral-balanced_loan_math_tools-loan_no_tools-rank32-scaling2-dropout01-lora_all",
    temperature=0,
    extra_body={"session_id": "fdaf"},
)

response = model.bind(extra_body={"session_id": "dfadaf"}).invoke(
    [{"role": "user", "content": "I want to calculate the monthly payment for a loan of $100,000 at 5% interest for 30 years."}]
)

print(response.content)

