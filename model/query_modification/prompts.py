query_modification_prompt = """
You have received a topic, question, query, or instruction from the user.

1. Carefully read and understand the user's input.
2. Identify the key information and main intent behind the user's input.
3. Formulate a precise and effective search query for Google that will help extract the necessary information to fulfill the user's task.

user_query: {user_query}

Generated search query:
"""

blog_prompt = """
You are tasked with researching a software product to write a detailed and insightful blog post. The goal is to gather comprehensive information about the product by crafting precise and relevant search queries for each aspect of the review.

Instructions:
Identify Key Information Areas: Focus on the following categories to gather a holistic understanding:

    Use Case: Understand what the software does, its purpose, and the problems it solves.
    Pricing: Find details about the software's pricing plans, free trials, or hidden costs.
    Benefits: Research the key advantages, features, and benefits the software offers.
    Competitors: Identify competitors, compare features, and determine where the software stands in the market.
    Setup: Look for a step-by-step setup guide or ease-of-use information.
    Generate Search Queries: For each category, create multiple queries to ensure comprehensive coverage. Use variations and keywords that target different aspects.

Example Search Queries:

Use Case
    "What is [Software Name] used for?"
    "Features and applications of [Software Name]"
    "What problems does [Software Name] solve?"
    "Top industries using [Software Name]"
Pricing
    "[Software Name] pricing plans"
    "Is [Software Name] free or paid?"
    "Comparison of [Software Name] pricing with competitors"
    "Are there any hidden costs in [Software Name]?"
Benefits
    "Benefits of using [Software Name]"
    "Top features of [Software Name]"
    "How [Software Name] improves productivity/effectiveness"
    "Customer reviews of [Software Name] benefits"
Competitors
    "Competitors of [Software Name]"
    "How does [Software Name] compare to [Competitor Name]?"
    "Top alternatives to [Software Name]"
    "Market position of [Software Name] vs competitors"
Setup
    "How to set up [Software Name] step by step"
    "Ease of use: [Software Name] setup guide"
    "Setup requirements for [Software Name]"
    "First-time user guide for [Software Name]"
Chain of Thought Process
    Break the product into critical aspects (use case, pricing, benefits, competitors, setup).
    Craft queries that address both general and specific details for each aspect.
    Use variations of keywords to ensure results cover multiple perspectives (e.g., features, user guides, comparisons).
    Ensure queries target both primary sources (official website, documentation) and user perspectives (reviews, forums, comparisons).
    By following this structure, you'll create a well-rounded list of search queries to gather detailed and relevant information for the software blog post.

    software_query: {query}
    software_description: {software_description}
"""