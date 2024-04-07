from drqa.tokenizers import CoreNLPTokenizer
tok = CoreNLPTokenizer()
tok.tokenize('hello world').words()  # Should complete immediately


import drqa.reader
# drqa.reader.set_default('model', '/path/to/model')
reader = drqa.reader.Predictor()  # Default model loaded for prediction