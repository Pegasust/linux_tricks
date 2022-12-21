#!/usr/bin/env bash
# A simpe bash script that tells Linux to drop their unused (but allocated)
# memory to return shared memory back to host machine (Windows)
echo 1 >/proc/sys/vm/drop_caches

