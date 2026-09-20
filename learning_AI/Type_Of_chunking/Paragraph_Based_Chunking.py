text = """
Spark ERP is billing software used by retail shops.

It manages invoices, products, and customers.

It also manages inventory and payments.

The system generates sales reports.
"""

paragraphs = text.strip().split("\n\n")

for index, paragraph in enumerate(paragraphs, 1):

    print(f"\nChunk {index}:")
    print(paragraph.strip())