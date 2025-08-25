from app.fetcher import Fetcher
from app.processor import Processor



class Manager:
    """High level orchestrator for data retrieval and analysis."""

    def __init__(self):
        # Initialize the data fetcher and processor components.
        self.fetcher = Fetcher()
        data = self.fetcher.get_all_data()
        self.processor = Processor(data)


    def run(self):
        # Execute the full processing pipeline and return the results.
        print("analyzing process is starting...")
        self.processor.run_processing()
        print("analyzing process is ended successfully...")
        return self.processor.get_df_as_dictionary()




    def get_result(self):
        return self.processor.get_df_as_dictionary()

