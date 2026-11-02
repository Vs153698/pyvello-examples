from typing import List, Optional
from pydantic import BaseModel, Field
import pyvello as ui

# 1. Define target Pydantic schema for structured output extraction
class LineItem(BaseModel):
    description: str = Field(description="Service or product description")
    quantity: int = Field(default=1, description="Number of units")
    unit_price: float = Field(description="Price per unit in USD")
    total: float = Field(description="Line item subtotal")

class FinancialInvoice(BaseModel):
    vendor_name: str = Field(description="Legal entity or vendor name")
    invoice_number: str = Field(description="Unique invoice reference identifier")
    billing_date: str = Field(description="ISO 8601 date of the transaction")
    line_items: List[LineItem] = Field(default_factory=list, description="Detailed itemized breakdown")
    subtotal: float = Field(description="Sum of all line items before tax")
    tax_amount: float = Field(default=0.0, description="Applicable tax amount")
    grand_total: float = Field(description="Final payable amount")
    payment_terms: str = Field(default="Net 30", description="Contract payment conditions")
    is_approved: bool = Field(default=True, description="Audit compliance validation flag")

# 2. Define Agent with Pydantic model and token limit ceiling
extractor_agent = ui.Agent(
    name="FinancialExtractor",
    system_prompt=(
        "You are an enterprise accounting auditor. Parse incoming invoice text or receipts "
        "and extract structured financial entities adhering strictly to the FinancialInvoice schema."
    ),
    model="openrouter/z-ai/glm-5.3-flash",  # Ultra low-cost ($0.05/M) or auto-prefixed 'z-ai/glm-5.3-flash'
    models=[
        "openrouter/z-ai/glm-5.3-flash",
        "openrouter/google/gemini-2.0-flash-001",
        "openrouter/deepseek/deepseek-chat",
        "openrouter/meta-llama/llama-3.3-70b-instruct",
        "openrouter/qwen/qwen3.7-flash",
    ],
    max_tokens=800,                       # Limit completion tokens strictly (accommodates reasoning models)
    structured_output=FinancialInvoice,   # Enforce Pydantic BaseModel schema validation
    temperature=0.0,                      # Zero temperature for deterministic extraction
)

# 3. Programmatic usage and typed property access
async def process_invoice(text: str):
    async for chunk in extractor_agent.run(text):
        print(chunk, end="")
    
    # Access strongly typed Pydantic instance directly:
    result: FinancialInvoice = extractor_agent.last_structured_output
    print(f"Vendor: {result.vendor_name}, Total: ${result.grand_total}")
    print(f"Line items extracted: {len(result.line_items)}")

# 4. Or launch as full interactive web application in single line:
if __name__ == "__main__":
    extractor_agent.to_app(
        title="Pyvello Financial Extraction & Structured Output",
        description="Extract itemized invoices into Pydantic models with token ceiling controls.",
    ).launch()