#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

TYPE=$1
DEV=$2

usage() {
    echo "${0} [main|node] dev"
    exit 1
}

case ${TYPE} in
    main|node) ;;
    *)
        usage
        ;;
esac

if test -z ${TYPE} || test -z ${DEV}; then
    usage
fi

wget \
    http://micropython.org/resources/firmware/esp8266-20191220-v1.12.bin \
    -O ${DIR}/micropython.bin

esptool.py --port ${DEV} erase_flash
esptool.py --port ${DEV} --baud 460800 write_flash --flash_size=detect 0 ${DIR}/micropython.bin

sleep 1
mkdir -p target-${TYPE}
# deploy libs
for f in ${DIR}/src/libs/* ; do
    echo "deploy [${f}] to [$(basename ${f})]"
    ampy --port ${DEV} -b 115200 put ${f} /$(basename ${f})
    ampy --port ${DEV} -b 115200 get /$(basename ${f}) target-${TYPE}/$(basename ${f})
done

for f in ${DIR}/src/${TYPE}/* ; do
    echo "deploy [${f}] to [$(basename ${f})]"
    ampy --port ${DEV} -b 115200 put ${f} /$(basename ${f})
    ampy --port ${DEV} -b 115200 get /$(basename ${f}) target-${TYPE}/$(basename ${f})
done
