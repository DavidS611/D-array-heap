# D-Array Max Heap Implementation

This Python script implements a D-Array Max Heap, a variant of a max heap where each node has 'd' children. The implementation includes basic operations such as insertion, extraction of the maximum value, heapifying up and down, printing the heap, increasing the key of an index, and deleting an element from the heap.

## Usage

1. Run the script using the command:

    ```bash
    python script_name.py file_name.txt
    ```

    Replace `script_name.py` with the name of the script file, and `file_name.txt` with the name of the file containing integers separated by whitespace or commas.

2. The script will prompt you to enter the value of 'd' for the D-Array Max Heap.

3. The script will read numbers from the specified file and insert them into the heap.

4. The heap will be printed, and various operations (extracting max value, increasing key, deleting key) will be performed.

## File Input Format

The file specified should contain integers separated by whitespaces or commas.

## D-Array Max Heap Class Methods

- `insert(value)`: Inserts a value into the heap.
- `extract_max()`: Extracts the maximum value from the heap.
- `increase_key(current_key, value)`: Increases the key of an index if the provided value is greater.
- `delete_key(current_key)`: Deletes an element from the heap.

## Helper Functions

- `read_numbers(heap_, filename)`: Reads integers from a file and inserts them into a heap.
- `get_d_array()`: Gets the 'd' value from the user.

## Example

```bash
python script_name.py input_numbers.txt

