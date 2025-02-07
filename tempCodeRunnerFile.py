sql = "REPLACE INTO user (id, name, username, email, street, suite, city, zipcode, phone, website, company_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    # values = (row["id"], row["name"], row["username"], row["email"], row["street"],
    #             row["suite"], row["city"], row["zipcode"],
    #             row["phone"] , row["website"], row["company_name"])  
    # cursor.execute(sql, values)