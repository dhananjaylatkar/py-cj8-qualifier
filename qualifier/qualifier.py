from typing import Any, List, Optional


def get_len_of_longest_word(rows: List[List[Any]], labels: Optional[List[Any]] = None) -> List[int]:
    """Return List of len of largest word in each column.

    Args:
        rows (List[List[Any]]): table
        labels (Optional[List[Any]], optional): table header. Defaults to None.

    Returns:
        List[int]: List of len of largest word + 1 in each column.
    """
    res = [0] * len(rows[0])
    if labels:
        for i, itm in enumerate(labels):
            res[i] = len(str(itm))
    for row in rows:
        for i, itm in enumerate(row):
            itm_len = len(str(itm))
            res[i] = itm_len if res[i] < itm_len else res[i]
    return res


def create_header(labels: List[Any], len_of_clm: List[int], centered: bool = False) -> str:
    res = '│'
    res_top = '┌'
    res_bot = '├'

    # if labels are not provided return top of table. e.g. ┌────────────┬───────────┬─────────┐
    if not labels:
        res_top += ''.join([f"{'─' * (len_of_clm[i]+2)}{'┬' if i < len(len_of_clm)-1 else '┐'}" for i,
                           itm in enumerate(len_of_clm)])
        return res_top

    for i, itm in enumerate(labels):
        res_top += f"{'─' * (len_of_clm[i]+2)}{'┬' if i < len(labels)-1 else '┐'}"
        res_bot += f"{'─' * (len_of_clm[i]+2)}{'┼' if i < len(labels)-1 else '┤'}"
        if centered:
            res += f" {str(itm):^{len_of_clm[i]}} │"
        else:
            res += f" {str(itm):<{len_of_clm[i]}} │"

    return '\n'.join([res_top, res, res_bot])


def create_body(rows: List[List[Any]], len_of_clm: List[int], centered: bool = False) -> str:
    res = []
    for row in rows:
        res_tmp = '│'
        for i, itm in enumerate(row):
            if centered:
                res_tmp += f" {str(itm):^{len_of_clm[i]}} │"
            else:
                res_tmp += f" {str(itm):<{len_of_clm[i]}} │"
        res.append(res_tmp)
    res_bot = '└'
    res_bot += ''.join([f"{'─' * (itm+2)}{'┴' if i < len(len_of_clm)-1 else '┘'}" for i,
                       itm in enumerate(len_of_clm)])
    res.append(res_bot)
    return '\n'.join(res)


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    len_of_clm = get_len_of_longest_word(rows, labels)
    return '\n'.join([create_header(labels, len_of_clm, centered), create_body(rows, len_of_clm, centered)])
