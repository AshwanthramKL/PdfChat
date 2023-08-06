import argparse
import timeit
from src.utils import setup_dbqa

if __name__ == "__main__":
    # to get qn from cmd line
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=str)
    args = parser.parse_args()
    # Start timer to calculate response time and speed of cpu interface
    start = timeit.default_timer()

    # Setup qa object
    dbqa = setup_dbqa()

    # Feed input qn to QA object
    response = dbqa({'query': args.input})
    # End timer
    end = timeit.default_timer()

    # Print response
    print(f"\nAnswer: {response['result']}")
    print('='*50)

    # Process source documents for better display
    source_docs = response['source_documents']
    for i, doc in enumerate(source_docs):
        print(f'\nSource Document {i+1}\n')
        print(f'Source Text: {doc.page_content}')
        print(f'Document Name: {doc.metadata["source"]}')
        print(f'Page Number: {doc.metadata["page"]}\n')
        print('='* 50)

    # Display time taken for CPU inference
    print(f"Response time: {end - start}")
