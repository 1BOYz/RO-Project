:: Identifying and control variable part
set /a width = 26	&:: Width (in pixels) of the output samples.
set /a height = 26	&:: Height (in pixels) of the output samples.
set /a nPos = 19	&:: Number of positive samples used in training for every classifier stage.
set /a nNeg = 31	&:: Number of negative samples used in training for every classifier stage.
set /a nStage = 12	&:: Number of cascade stages to be trained.

:: Command part
:: Delete old xml in cascade folder
DEL cascade\*.xml
TIMEOUT 3
:: Train cascade model
CMD/K _lib\opencv_traincascade.exe -data cascade\ -vec pos.vec -bg neg.txt -w %width% -h %height% -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos %nPos% -numNeg %nNeg% -numStages %nStage% -maxFalseAlarmRate 0.3 -minHitRate 0.999