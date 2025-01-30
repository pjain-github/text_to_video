from pydantic import BaseModel, Field
from typing import List


# Pydantic
# Define the Description model
class Description(BaseModel):
    """Description of an image."""
    image: str = Field(description="Image number")
    description: str = Field(description="Image Description")  # Fixed typo

# Define a wrapper model for handling a list of descriptions
class DescriptionList(BaseModel):
    """A list of image descriptions."""
    descriptions: List[Description]