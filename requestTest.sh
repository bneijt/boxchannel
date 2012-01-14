#!/bin/bash
set -e
. bin/activate
dd if=/dev/urandom count=100 of=/tmp/boxchannel.test
python boxc index /tmp/boxchannel.test
python boxc request boxchannel.test
python boxc request
python boxc stage
python boxc respond
python boxc stage
echo "Input was"
md5sum /tmp/boxchannel.test
echo "Output was"
md5sum ~/Downloads/boxchannel.test
