
jpg_size=$(ls ..|grep [.]jpg|wc -l)
if [ $jpg_size -gt 0 ]
then
	rm ../*.jpg
fi

png_size=$(ls ..|grep [.]png|wc -l)
if [ $png_size -gt 0 ]
then
	rm ../*.png
fi
