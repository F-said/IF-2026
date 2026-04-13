def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    TO_REMOVE_NEWLINE = '\n'
    TO_REMOVE_NODATA = 'NO DATA\n'

    clean_data  = []
    removed_data = []

    # clean each object by looping through the data
    for row in data:
        # if/else statement (aka conditional)
        # how do we check if "row" is a digit or not
        if row != TO_REMOVE_NEWLINE and row != TO_REMOVE_NODATA:
            new_row = int(row)
            # add one value to the end of the list
            clean_data.append(new_row)
        # TODO: introduce logic that states if above statemenet fails append to removed data
        else:
            # semantic error
            removed_data.append(row)

    # var: clean_data
    # value: list of integers that is the parameter type-casted and filtered
    # TODO: if no return statement maybe you're function isn't working (as it should)
    return clean_data, removed_data


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    pass


def median(data: list) -> float:
    """
    """
    pass


def range(data: list) -> float:
    """
    """
    pass


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    file_obj = open(file)

    # how do read data in? call the readlines method!
    file_data = file_obj.readlines()

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_data = clean_heartrate_data(file_data)

    print("cleaned list", cleaned_list)
    print("removed list", removed_data)

    # calculate the average, median, and range of this file using the functions you've wrote
    ...

    # print out your data quality measure to the console
    ...

    # print out your descriptive statistics to the console
    ...


run("data/phase0.txt")
#run("data/phase1.txt")
#run("data/phase2.txt")
#run("data/phase3.txt")
