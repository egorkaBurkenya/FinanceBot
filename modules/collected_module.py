def collect_the_pieces(demounted: list) -> str:
  string = ''
  for piece in demounted:
    string += piece + ' '
  return string