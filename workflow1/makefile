#include config.mk
.PHONY: default build test clean
default: build test clean
LANGS = py
MASTERS = $(foreach lang,$(LANGS),quantum-task-$(lang).exe)
WORKERS = $(foreach lang,$(LANGS),classical-task-$(lang).exe)
build: $(MASTERS) $(WORKERS)
MPIEXEC = mpiexec -n 1
test: build 
	@for i in $(LANGS); do \
		for j in $(LANGS); do \
			$(MPIEXEC) ./quantum-task-$$i.exe ./classical-task-$$j.exe; \
        done; \
    done  
clean:
	$(RM) -r $(MASTERS) $(WORKERS) __pycache__

# Python
quantum-task-py.exe: quantum-task.py
	echo '#!'`which python` > $@
	cat $< >> $@
	chmod +x $@
classical-task-py.exe: classical-task.py
	echo '#!'`which python` > $@
	cat $< >> $@
	chmod +x $@
