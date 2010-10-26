tar -zxvf $1
cd ${1%*.*.*}
#echo "\n" | dh_make -c gpl -s -i -b -f ../$1
cp -R ../debian ./debian
cd debian/
debuild -us -uc
