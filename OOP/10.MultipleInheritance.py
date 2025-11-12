class Logger:
    def log(self, message):
        print(f'[LOG]: {message}')

class FileWriter:
    def write(self, text):
        print(f'Writing to file: {text}')

class LogFileWriter(Logger, FileWriter):
    def log(self, message):
        self.write(f"[LOG]: {message}")

log_file = LogFileWriter()
log_file.log("System started successfully.")
log_file.log("User logged in.")