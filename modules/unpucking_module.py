from typing import NamedTuple

class CategoryRecord(NamedTuple):
  id: int
  categoryTitle: str
  worth: bool

class historyRecord(NamedTuple):
  id: int
  amount: int
  amountTitle: str
  typeOf: bool
  createdDate: str
  catId: int

class testRecord(NamedTuple):
  id: int
  name: str
  salary: int
  department: str
  position: str 
  hireDate: str

def unpucking_sqlite_answer(arr_with_tuples: list) -> list:
    arr_with_namedtuple = []
    for one_tuple in arr_with_tuples:
      if len(one_tuple) == 3:
        arr_with_namedtuple.append(CategoryRecord(one_tuple[0], one_tuple[1], one_tuple[2]))
      if len(one_tuple) == 6: 
        arr_with_namedtuple.append(historyRecord(one_tuple[0], one_tuple[1], one_tuple[2], one_tuple[3], one_tuple[4], one_tuple[5]))
      else: 
        arr_with_namedtuple.append(one_tuple[0], one_tuple[1], one_tuple[2], one_tuple[3], one_tuple[4], one_tuple[5])
    return arr_with_namedtuple
