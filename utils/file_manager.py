# file_manager.py

import os

class FileManager:
    def read_file(self, file_path):
        """Read and return the contents of a file."""
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    def write_file(self, file_path, content):
        """Write content to a file."""
        try:
            with open(file_path, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing to file {file_path}: {e}")

    def delete_file(self, file_path):
        """Delete the specified file."""
        try:
            os.remove(file_path)
        except FileNotFoundError:
            print(f"File {file_path} not found.")
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")

    def list_files(self, directory):
        """List all files in the specified directory."""
        try:
            return os.listdir(directory)
        except FileNotFoundError:
            print(f"Directory {directory} not found.")
        except Exception as e:
            print(f"Error listing files in directory {directory}: {e}")

    def create_directory(self, directory):
        """Create a new directory."""
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Directory {directory} created successfully.")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")