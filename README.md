# sub-encoder
author: Ernest Feret

0. Requirements:
qnapi

1. Short description: 
Python script to fix qnapi encoding.

2. Motivation:
Somehow qnapi on my debian distribution isn't properly encoding downloaded files. 
To fix this, I wrote this little python script, that is calling qnapi as subprocess,
then decoding / encoding it from windows-1250 to UTF-8. 
To run this, add script to runable directory and call it with:
> sub-encoder.py <filename>
Where <filename> is a file where qnapi is executed on. 

3. TODO:
chardet validation of downloaded file
encodings as an optional argument
