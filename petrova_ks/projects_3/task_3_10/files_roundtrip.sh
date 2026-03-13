#!/bin/bash

for i in {1..10}; do
	touch "test$i.txt"
	echo "Создан test${i}.txt"
done

n=10
while [ $n -ge 1 ]; do
	rm "test${n}.txt"
	echo "Удалён test${n}.txt"
	let "n -= 1"
done
