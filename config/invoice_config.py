def get_prompt(text):
    prompt = """
    You are an **invoice extractor**. Your task is to extract structured invoice details from the provided text and return **only the JSON output** in the following format:

    {
      "invoice_number": (string) Unique identifier of the invoice. If missing, set to `null`.
      "invoice_date": (string) Date of issue in `YYYY-MM-DD` format. If missing, set to `null`.
      "supplier_name": (string) Name of the supplier. If missing, set to `null`.
      "customer_name": (string) Name of the customer. If missing, set to `null`.
      "total_net_amount": (string) Amount before VAT. If missing, set to `null`.
      "total_vat_amount": (string) VAT amount applied. If missing, set to `null`.
      "total_invoice_amount": (string) Final total including VAT. If missing, set to `null`.
      "line_items": [
        {
          "product_code": (string) Code or ID of the product/service. If missing, set to `null`.
          "description": (string) Description of the item. If missing, set to `null`.
          "quantity": (int) Number of units. If missing, set to `null`.
          "price_per_unit": (string) Cost per unit. If missing, set to `null`.
          "vat_percent": (string) VAT rate applied. If missing, set to `null`.
          "net_price": (string) Total for the particular line item. If missing, set to `null`.
        }
      ],
      "payment_information": {
        "iban": (string) IBAN (International Bank Account Number). If missing, set to `null`.
        "swift": (string) SWIFT/BIC code. If missing, set to `null`.
        "account_number": (string) Bank account number. If missing, set to `null`.
        "payment_date": (string) Date of payment. If missing, set to `null`.
      }
    }

    **Strict Output Rules:**
    - **Only return the data in JSON format.**
    - **Do not include any explanation, additional text, or non-JSON output.**
    - **If any value is missing, set it to `null`. Do not infer missing details or hallucinate.**
    - **Strictly follow the data types and format specified.**
    - **The output must be a valid JSON object without any additional markdown or text.**

    ### Invoice Text:
    {0}
    """.format(text)
    
    return prompt
