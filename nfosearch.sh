#!/bin/bash

# Define the directory path to search for .nfo files
directory_path="/mnt/nas_mount/Movies/"

# Use 'find' command to search for .nfo files recursively
find "$directory_path" -type f -name "*.nfo" | while IFS= read -r file; do
    # Check if the file contains the <originaltitle> tag
    if grep -q '<originaltitle>' "$file"; then
        # Extract <originaltitle> tag content using grep and sed
        original_title=$(grep -oP '<originaltitle>\K[^<]*' "$file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

	# Extract <title> tag content using grep and sed
        title=$(grep -oP '<title>\K[^<]*' "$file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

        # Extract <poster> tag content using grep and sed
        poster=$(grep -oP '<poster>\K[^<]*' "$file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

	# Extract <plot> tag content using grep and sed
        plot=$(grep -oP '<plot>\K[^<]*' "$file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

	# Extract <year> tag content using grep and sed
        year=$(grep -oP '<year>\K[^<]*' "$file" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

        # Output the file name and its <originaltitle> content
        #echo "File: $file"
        echo "$original_title @ $poster@ $plot @ $year @ $title"
        #echo "-------------------------"
    fi
done
