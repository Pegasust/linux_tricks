# - creates a script (build) that composes all tricks in scripts/ into a tricks.rc file
# - installs the tricks.rc file into ~/.linux_tricks/tricks.rc
# - appends into ~/.bashrc_aliases: alias enable_tricks="source ~/.linux_tricks/tricks.rc"
# - then calls `source ~/.bashrc_aliases`

ORIGIN_ALIASES=${HOME}/.bashrc_aliases
INSTALL_DIR=${HOME}/.linux_tricks/
ENABLE_TRICKS_CMD="alias enable_tricks=\"source ${INSTALL_DIR}/tricks.rc\""

all: build install

build: clean_build tricks.rc

install: clean_install build
	echo ${ORIGIN_ALIASES}
	cp tricks.rc ~/.linux_tricks/tricks.rc
	[ ! -f ${ORIGIN_ALIASES} ] && touch ${ORIGIN_ALIASES}
	! grep ${ORIGIN_ALIASES} "alias enable_tricks" && echo ${ENABLE_TRICKS_CMD}>>${ORIGIN_ALIASES}
	

tricks.rc: scripts/short_cwd_display.rc
	echo "LINUX_TRICKS_INSTALL_DIR=${INSTALL_DIR}">tricks.rc
	cat $^ >>tricks.rc

short_cwd_display_src: scripts/short_cwd_display
	mkdir -p ${INSTALL_DIR}
	cp -r $^ ${INSTALL_DIR}

scripts/short_cwd_display.rc: short_cwd_display_src
	touch $@

clean_build:
	if [ -f tricks.rc ]; then rm tricks.rc; fi

clean_install:
	rm -rf ~/.linux_tricks
	
clean: clean_build clean_install