for /l %%x in (1, 1, 5) do (
   echo %%x
   mvn gauge:execute -DspecsDir="specs\01. Get PI Token.spec"
)