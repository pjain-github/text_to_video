tech_prompt= """
We aim to create a well-rounded review of the given software by analyzing its use case, pricing, benefits, competitors, and setup process. Using the provided 4–5 articles and images, follow the instructions below to synthesize the information, ensuring images and tables are integrated where relevant.  
Write the blog in way that you are a friend and advisor with technical knowledge, and you have personally used the product.

### Instructions  

#### **1. Introduction**  
- Describe the primary purpose of the software and the key problems it addresses.  
- Highlight specific industries or user groups that benefit the most from the software.  
- Use the images provided to visually support this section, such as showcasing workflows or diagrams explaining the software’s function.  

#### **2. Pricing Details**  
- Extract and summarize all available pricing plans (e.g., free, standard, premium).  
- Note if there are free trials, hidden fees, or subscription models.  
- Use a table to list and compare pricing plans along with key features included in each plan.  

**Example Table for Pricing:**  

| Plan          | Price          | Key Features                        | Free Trial  |  
|---------------|----------------|-------------------------------------|-------------|  
| Basic         | $10/month      | Feature A, Feature B                | Yes         |  
| Pro           | $25/month      | Feature A, Feature B, Feature C     | Yes         |  
| Enterprise    | Custom Pricing | Full feature set, custom support    | No          |  

#### **3. Key Benefits**  
- List and elaborate on the top features and benefits of the software.  
- Categorize features into functional groups like performance, user experience, scalability, or integrations.  
- Use bullet points for clarity, and integrate images showing key features where available.  
- After bullet points write some detailed text explaining some benefits to reader.

#### **4. Competitor Analysis**  
- Identify and briefly describe 2–3 competitors.  
- Create a comparison table highlighting the unique selling points (USPs), pricing differences, and feature gaps.  

**Example Table for Competitor Comparison:**  

| Feature         | Software A  | Software B  | Competitor 1  | Competitor 2  |  
|------------------|-------------|-------------|---------------|---------------|  
| Pricing          | $10/month   | $15/month   | $12/month     | $20/month     |  
| Key Feature 1    | Yes         | No          | Yes           | Yes           |  
| Integration      | 3rd Party   | Built-in    | Both          | Limited       |  

**Image Placement Suggestion:**  
- Use comparative charts or logos of competing brands to enhance this section.  

#### **5. Setup Process**  
- Provide a clear, step-by-step guide to setting up the software.  
- Emphasize ease of use, setup time, and prerequisites, if any.  
- Include screenshots or flowcharts to simplify explanations.  


### Final Deliverable:  
- Write the review using a mix of narrative text, bullet points, and tables to ensure readability.  

---  

If you don't find any information or topic, you can skip it.

This structure ensures a comprehensive, easy-to-digest review while effectively utilizing text and tables to present key information.

In the text you will find image urls as well, if these urls can help with better readability, use it as well.
Add images like <img src = url>
We are generating review for: {software}
"""


image_prompt = """
Task:

You are given a list of images with descriptions. Your task is to filter out any irrelevant images and provide descriptions for the relevant ones based on the context of a software blog. The images should directly relate to the software product or the subject matter discussed in the blog.

Instructions:

Remove Irrelevant Images:
    If an image is not directly related to the software product or the content of the blog, remove it from the list.
Provide Descriptions for Relevant Images:
    For each relevant image, write a clear and concise description based on the software context. The description should explain how the image is relevant to the software product or the topic being discussed in the blog.
Format:
    Return the descriptions in a list of JSON objects.
The format should be:
    description = [
      {"url": "www.example1.com", "description": "image description"}, 
      {"url": "www.example2.com", "description": "image description"}
    ]
Ensure Accuracy:
    Make sure that each image description aligns with the content of the software blog and helps the reader understand the context better.
"""


final_prompt = """
Task:

You are given a blog article that I have written, along with a list of images and their descriptions. Your task is to insert the most relevant images into the article at appropriate points where they enhance understanding and complement the text.

Instructions:
    Do not modify the text of the article. Keep the content exactly as it is.
    Use only relevant images. Choose images based on their descriptions to match the context of the surrounding text.
Placement of images:
    Insert images at natural breaks or where they provide additional clarity to the text.
    Avoid placing images too frequently—only where they add value.
Format:
    Use the <img> HTML tag to insert images.
    Example: <img src="image_link" alt="image description">
Do not include captions unless necessary. The image should seamlessly blend into the flow of the article.
Ensure that the final output maintains the readability and flow of the blog while effectively using images to enhance comprehension."""