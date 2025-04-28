SCRIPTS_DIR := $(CURDIR)

all: build test run

build:
	@echo "Building the project..."
	@$(SCRIPTS_DIR)/utils/build/build.sh
	@echo "Project built."

test:
	@echo "Testing the project..."
	@pytest $(SCRIPTS_DIR)/utils/test/primesTest.py
	@echo "Project tested."

clean:
	@echo "Cleaning..."
	@$(SCRIPTS_DIR)/utils/clean/clean.sh
	@echo "Cleaned."

# Run doesn't work because the other running program on startup is using the file
# I could kill it but that's just mean
run: 
	@echo "Starting program..."
	@python3 $(SCRIPTS_DIR)/bin/currentCount
	@echo "Running."

build-deb:
	@echo "Building project..."
	@$(SCRIPTS_DIR)/utils/debBuild/debBuild.sh
	@echo "Complete."

lint-deb: build-deb
	@echo "Linting project..."
	@-lintian $(SCRIPTS_DIR)/counter-v2.0.0.deb
	@echo "project linted."