generate_requirements:
	@echo "Generating requirements.txt"
	@pipreqs --force --savepath requirements.txt .