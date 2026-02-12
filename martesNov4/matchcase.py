method = "POST"
match method:
    case "GET":
         print("Fetching resource...")
    case "POST":
        print("Creating resource...")
    case "PUT":
        print("Updating resource...")
    case "DELETE":
        print("Deleting reosurce...")
    case _:
        print("Unsupported HTTP method")