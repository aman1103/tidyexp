## only for development

copy:
	@cp -r tidyexp /mnt/c/Users/ASUS/ExampleMLLog
	@cp setup.py /mnt/c/Users/ASUS/ExampleMLLog
	@cp README.md /mnt/c/Users/ASUS/ExampleMLLog
	@cp requirements.txt /mnt/c/Users/ASUS/ExampleMLLog

zip:
	@zip -rq tidyexp-share.zip tidyexp setup.py README.md requirements.txt

unzip:
	@unzip -q tidyexp-share.zip

sphinx:
	@sphinx-apidoc -o docs tidyexp
	@cd docs && make html

h5:
	@cp /mnt/c/Users/ASUS/ExampleMLLog/abcd/logs/log_1.hdf5 log.hdf5

todo:
	@cd tidyexp && grep -nr "# TODO"
