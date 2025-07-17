import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Loop over each attendee
    for idx, person in enumerate(attendees, start=1):
        # Get values or use 'N/A'
        name = person.get("name", "N/A") or "N/A"
        title = person.get("event_title", "N/A") or "N/A"
        date = person.get("event_date", "N/A") or "N/A"
        location = person.get("event_location", "N/A") or "N/A"

        # Replace placeholders in template
        content = template.replace("{name}", name)
        content = content.replace("{event_title}", title)
        content = content.replace("{event_date}", date)
        content = content.replace("{event_location}", location)

        # Save to file
        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
            print(f"File created: {filename}")
        except Exception as e:
            print(f"Failed to write file {filename}: {e}")
