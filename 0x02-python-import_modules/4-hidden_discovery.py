#!/usr/bin/python3
if __name__ == "__main__":
    from glob import glob
    import importlib.util
    spec = importlib.util.spec_from_file_location("hidden_4", "./hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)
    for item in dir(hidden_4):
        if not item.startswith('__'):
            print(item)
