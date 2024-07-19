import pytest 

# Initialization with valid name
def test_initialization_with_valid_name(self):
    agent = Agent(name="Chicken")
    assert agent.name == "Chicken"
    
    # Initialization with an empty string as name
    def test_initialization_with_empty_string_name(self):
        agent = Agent(name="")
        assert agent.name == ""
        
    
