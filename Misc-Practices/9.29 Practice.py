#codes = {"a": ".-", "b": "-...", "c": "-.-."}
#print(codes["a"])
#print(codes.get("z", "?"))
#print(len(codes))
#print(codes["b"])

#codes = {"a": ".-", "b": "-..."}
#codes["c"]="-.-."
#codes["b"]="----"
#print("a" in codes)
#for letter, code in codes.items():
#    print(letter, code)

CODEBOOK = [('A', '.-'), ('B', '-...'), ('S', '...')]
ENCODE_MAP = {letter: pat for letter, pat in CODEBOOK}
DECODE_MAP = {pat: letter for letter, pat in ENCODE_MAP.items()}
print(ENCODE_MAP["S"])
print(DECODE_MAP["..."])

