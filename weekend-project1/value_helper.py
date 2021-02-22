def format_value(value):
    '''
        Summary:
            The value is transformed -
                comma separated, limited to two decimal places, or unaltered
        Parameters:
            value (numerical): single value to format
        
        Returns:
            str: formatted value
    '''

    if isinstance(value, float):
        value = '{:.2f}%'.format(value*100)
    elif isinstance(value, int):
        value = '{:,}'.format(value)
    else:
        value = str(value)

    return value 