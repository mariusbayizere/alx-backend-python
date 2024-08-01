from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing floats.

    Returns:
        float: The sum of the elements in the list as a float.
    """
    return float(sum(mxd_lst))
