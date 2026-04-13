def clean_heartrate_data(data):
    TO_REMOVE_NEWLINE = '\n'
    TO_REMOVE_NODATA = 'NO DATA\n'

    clean_data  = []

    # clean each object by looping through the data
    for row in data:
        # if/else statement (aka conditional)
        # how do we check if "row" is a digit or not
        if row != TO_REMOVE_NEWLINE and row != TO_REMOVE_NODATA:
            new_row = int(row)
            # add one value to the end of the list
            clean_data.append(new_row)
    
    return clean_data