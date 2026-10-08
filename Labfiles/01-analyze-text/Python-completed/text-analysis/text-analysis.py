from dotenv import load_dotenv
import os

# Import namespaces
from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient



def main():
    try:
        # Clear the console
        os.system('cls' if os.name == 'nt' else 'clear')

        # Get Configuration Settings
        load_dotenv()
        foundry_endpoint = os.getenv('FOUNDRY_ENDPOINT')


        # Create client using endpoint
        # Create client using endpoint
        credential = DefaultAzureCredential()
        ai_client = TextAnalyticsClient(endpoint=foundry_endpoint, credential=credential)


        # Analyze each text file in the reviews folder
        reviews_folder = 'reviews'
        for file_name in os.listdir(reviews_folder):
            # Read the file contents
            print('\n-------------\n' + file_name)
            text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
            print('\n' + text)

            # Get language



            # Get entities



            # Get PII



    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()