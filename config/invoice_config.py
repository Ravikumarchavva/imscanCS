def get_gemini_prompt():
    PROMPT = (
        "Extract structured invoice details from this PDF. Return the fields exactly as they appear in the document. "
        "Separate the output into two parts: one for 'line_items' and another for the 'remaining details' in a flat format.\n\n"
        
        # Line items part (no nested structures)
        'Line Items:\n'
        '{\n'
        '    "line_items": [\n'
        "        {\n"
        '            "product_code": "string",\n'
        '            "description": "string",\n'
        '            "quantity": "string",\n'
        '            "price_per_unit": "string",\n'
        '            "vat_percent": "string",\n'
        '            "total_price": "string"\n'
        "        }\n"
        "    ]\n"
        
        "\nRemaining Details (Flattened):\n"
        '{\n'
        # Grouping related information (dates, amounts, and financial details)
        '    "invoice_number": "string",\n'
        '    "invoice_date": "YYYY-MM-DD",\n'
        '    "payment_date": "YYYY-MM-DD",\n'
        '    "due_date": "YYYY-MM-DD",\n'
        '    "total_items": "number",\n'  # Number of line items
        '    "total_tax": "string",\n'
        '    "tax_rate": "string",\n'  # Combined tax rate and amount into a flat string
        
        # Supplier and customer related details
        '    "supplier_name": "string",\n'
        '    "supplier_address": "string",\n'
        '    "supplier_vat_number": "string",\n'
        '    "customer_name": "string",\n'
        '    "customer_address": "string",\n'
        '    "customer_company_vat_number": "string",\n'
        
        # Financial details like account and banking information
        '    "iban": "string",\n'
        '    "swift": "string",\n'
        '    "bic": "string",\n'
        '    "account_number": "string",\n'
        
        # Miscellaneous details (reference numbers, locale, country, currency)
        '    "purchase_order": "string",\n'
        '    "reference_numbers": "string",\n'  # Flattened reference numbers (if multiple, they should be comma-separated)
        '    "country": "string",\n'
        '    "currency": "string"\n'
        "}\n\n"
        
        "Rules:\n"
        "- Retain the original number formatting exactly as it appears in the document, including decimal and thousand separators.\n"
        "- Ensure **all numbers match exactly** as in the document.\n"
        "- If any field is missing, return `null` rather than removing it.\n"
        "- DO NOT add extra details.\n"
        "- If items have any charges, also write them in line items—DO NOT skip.\n"
        "- Total items is the number of line items.\n"
        "- Strictly follow line items and remaining details as keys."
    )

    return PROMPT


def get_qwen_prompt():
    prompt = """
    Extract structured invoice details from the provided image. Return the fields exactly as they appear in the document.
    Separate the output into two parts: one for 'line_items' and another for 'remaining details' in a flat format.\n\n

    Line Items:
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
        ]
    }

    Remaining Details (Flattened):
    {
        "invoice_number": "string",
        "invoice_date": "YYYY-MM-DD",
        "payment_date": "YYYY-MM-DD",
        "due_date": "YYYY-MM-DD",
        "total_items": "number",
        "total_tax": "string",
        "tax_rate": "string",
        "supplier_name": "string",
        "supplier_address": "string",
        "supplier_vat_number": "string",
        "customer_name": "string",
        "customer_address": "string",
        "customer_company_vat_number": "string",
        "iban": "string",
        "swift": "string",
        "bic": "string",
        "account_number": "string",
        "purchase_order": "string",
        "reference_numbers": "string",  # Flattened reference numbers (if multiple, they should be comma-separated)
        "country": "string",
        "currency": "string"
    }

    Rules:
    - Retain the original number formatting exactly as it appears in the document, including decimal and thousand separators.
    - Ensure **all numbers match exactly** as in the document.
    - If any field is missing, return `null` rather than removing it.
    - DO NOT add extra details.
    - If items have any charges, also write them in line items—DO NOT skip.
    - Total items is the number of line items.
    - Strictly follow line items and remaining details as keys.
    - Calculate dates from terms like 'X days from invoice date' if needed.
    """

    return prompt
