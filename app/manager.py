from app.fetcher import Fetcher
from app.processor import Processor



class Manager:
    def __init__(self):
        self.fetcher = Fetcher()
        data = self.fetcher.get_all_data()
        self.processor = Processor(data)


    def run(self):
        print("analyzing process is starting...")
        self.processor.run_prepossessing()
        print("analyzing process is ended successfully...")
        return self.processor.get_df_as_dictionary()




    def get_result(self):
        return self.processor.get_df_as_dictionary()

