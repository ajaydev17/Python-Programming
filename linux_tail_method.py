# Efficiently reading the last few lines of a large file

def tail(file_path, lines_to_read=10):
    with open(file_path, 'rb') as file:
        # Move the file pointer to the end of the file
        file.seek(0, 2)

        buffer = bytearray()
        count = 0

        while count < lines_to_read:
            try:
                file.seek(-2, 1) # move backwards
                buffer.extend(file.read(1))

                if buffer.endswith(b'\n'):
                    count += 1
            except OSError:
                # If the file is too small, break the loop
                file.seek(0)
                break

        return buffer.decode()[::-1]