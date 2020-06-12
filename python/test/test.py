# coding: utf-8
import sentencepiece as spm
sp = spm.SentencePieceProcessor()
text ='こんにちは世界'.encode('utf-8')
sp.Load("test_ja_model.model") 
print(sp.EncodeAsPieces(text.decode("shift_jis")))
print( "こんにちは世界",text.decode("shift_jis"))
