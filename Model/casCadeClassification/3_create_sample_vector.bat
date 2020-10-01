:: Identifying and control variable part
set /a width = 26	&:: Width (in pixels) of the output samples.
set /a height = 26	&:: Height (in pixels) of the output samples.
set /a numPosGen = 1000	&:: Number of positive samples to generate.

:: Command part
:: Delete old file .vec
DEL pos.vec
TIMEOUT 3
:: Create samples for HAAR cascade model
CMD/K _lib\opencv_createsamples.exe -info pos.txt -w %width% -h %height% -num %numPosGen% -vec pos.vec