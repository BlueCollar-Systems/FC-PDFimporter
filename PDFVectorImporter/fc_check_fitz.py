import importlib.util; import sys; m=importlib.util.find_spec('fitz'); print('FITZ_SPEC', bool(m)); print('PY', sys.version)
