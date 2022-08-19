# التكليف 03

#     لديك ال String التالي كما في المثال والمطلوب جلب ال Matches كما في الصورة
#     قم بكتابة ال Regular Expression Code لعمل المطلوب

# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234
# 01006001234
# 0100 600 1234
# (0100) 600-1
# (0100) 600-12

# return
# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234
# ===================================================
#  (\+?\(\d{4}\) \d{2,4}-\d{4})
import re
text = """ 
+(0100) 600-1234
+(0100) 60-1234
(0100) 6000-1234
01006001234
0100 600 1234
(0100) 600-1
(0100) 600-12
"""
result = re.findall(r"(\+?\(\d{4}\) \d{2,4}-\d{4})", text )

print(result)