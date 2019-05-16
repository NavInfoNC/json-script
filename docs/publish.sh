rm _build -rf
make html
mv _build/html _build/jsonscript
cp authorize.txt _build/jsonscript
scp -r _build/jsonscript simba@navicore.mapbar.com:/etc/navicore-site/docs
