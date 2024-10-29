from datetime import datetime

def structure_survey_data(phone_number, responses, questions_list):
    """
    Structure the survey responses into a format suitable for MongoDB
    
    Args:
        phone_number (str): The phone number of the respondent
        responses (dict): Dictionary containing survey responses
        questions_list (list): List of survey questions in order
        
    Returns:
        dict: Structured survey data ready for MongoDB storage
    """
    # Extract location data
    location_raw = responses.get(questions_list[2], "")
    region, constituency = "", ""
    if "," in location_raw:
        region, constituency = [part.strip() for part in location_raw.split(",")]
    
    # Extract and process farming products
    farming_products_raw = responses.get(questions_list[3], "")
    farming_products = [product.strip() for product in farming_products_raw.split(",")]
    
    # Structure the data
    survey_data = {
        "phone_number": phone_number,
        "submission_date": datetime.utcnow(),
        "personal_info": {
            "name": responses.get(questions_list[0], ""),
            "date_of_birth": responses.get(questions_list[1], ""),
            "contact": phone_number
        },
        "location": {
            "region": region,
            "constituency": constituency,
            "raw_input": location_raw
        },
        "farming_details": {
            "products": farming_products,
            "harvest_frequency": responses.get(questions_list[4], ""),
            "government_assistance": responses.get(questions_list[5], ""),
            "nab_certified": responses.get(questions_list[6], "").lower() == "yes"
        },
        "challenges": responses.get(questions_list[7], ""),
        "raw_responses": responses  # Store original responses for reference
    }
    
    return survey_data