def clear_list(dirty_list: list, mud: str = ' ') -> list:
  clean_list = []
  for piece in dirty_list:
    if piece != mud:
      clean_list.append(piece)
  return clean_list
