#!/bin/sh

cd ..
cd ..

mvn test-compile gauge:execute -DspecsDir="specs" -Dtags="pre_requisites" -Denv="dev"
mvn test-compile gauge:execute -DspecsDir="specs" -Denv="dev"