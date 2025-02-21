def get_prompt():
    prompt = """
    You are an **invoice extractor**. Your task is to extract structured invoice details from the provided image and return **only the JSON output** in the following format:

    {
        "line_items": [
            {
                "product_code": "string",
                "description": "string",
                "quantity": "string",
                "price_per_unit": "string",
                "vat_percent": "string",
                "total_price": "string"
            }
        ],
        "total_amount": {
            "total_items": number,
            "total_tax": "string",
            "total_price": "string"
        },
        "due_date": "YYYY-MM-DD",
        "payment_date": "YYYY-MM-DD",
        "invoice_date": "YYYY-MM-DD",
        "invoice_number": "string",
        "purchase_order": "string",
        "reference_numbers": ["string"],
        "locale": "string",
        "country": "string",
        "currency": "string",
        "payment_details": {
            "iban": "string",
            "swift": "string",
            "bic": "string",
            "account_number": "string"
        },
        "vat_number": "string",
        "supplier_name": "string",
        "taxes_details": [
            {
                "rate": "string",
                "amount": "string"
            }
        ],
        "total_amount_including_taxes": "string",
        "total_net_amount_excluding_taxes": "string",
        "customer_address": "string",
        "shipping_address": "string",
        "billing_address": "string",
        "customer_company_registrations": {
            "vat_number": "string"
        },
        "customer_name": "string",
        "supplier_address": "string"
    }

    **Strict Output Rules:**
    - **Only return the data in JSON format.**
    - **Do not include any explanation, additional text, or non-JSON output.**
    - Precisely capture dates such as invoice date, due date, and payment date. You may find this in many ways like `payment terms`, `payment conditions` etc saying like `within X days`, `X days from date of INVOICE` or similar. If a due date is not directly provided but 'due in X days' is indicated, calculate it by adding X days to the invoice date.**
    - **If any value is missing, set it to `null`. Do not infer missing details or hallucinate.**
    - **Strictly follow the data types and format specified.**
    - **The output must be a valid JSON object without any additional markdown or text.**

    ### Invoice image:

    """
    return prompt