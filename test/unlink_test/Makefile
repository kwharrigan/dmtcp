


test: test.c
	gcc -fPIC test.c -I$(HOME)/repos/dmtcp/include -o test

run: test
	dmtcp_launch --ckpt-open-files ./test

clean:
	echo $(HOME)
	rm -rf ckpt*
	rm -rf dmtcp_*
	rm -f tmpfile
	rm -f tmpfile
	rm -f test

