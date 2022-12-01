class Singleton:
  __instance = None
  def __new__(cls, val= None):
    if Singleton.__instance is None:
        Singleton.__instance = object.__new__(cls)
    Singleton.__instance.val = val
    return Singleton.__instance

kurikulum_lama = Singleton()
kurikulum_lama.val = "Kurikulum 2017"
kurikulum_lama.val

kurikulum_baru = Singleton()
kurikulum_baru.val = "Kurikulum 2020"
kurikulum_baru.val 