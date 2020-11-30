# SparseArray.py
class SparseArray:
  def __init__(self, strings):
    self.strings = strings

  def matchingStrings(self,queries):
    Result = [self.strings.count(query) for query in queries]
    return dict(zip(queries, Result))