from datetime import datetime


class Logger:

    @staticmethod
    def info(message):

        print(

            f"[{datetime.now():%H:%M:%S}] {message}"

        )