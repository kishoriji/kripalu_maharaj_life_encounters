import json

# HTML structure with placeholders for stories
html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Highlighting various life encounters of Jagadguru Shri Kripalu Ji Maharaj, showcasing his divine wisdom and compassion.">
    <meta name="keywords" content="Jagadguru, Shri Kripalu Ji Maharaj, Life Encounters, Spirituality, Wisdom, Compassion">
    <meta name="author" content="kishoriji">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="Kripalu Maharaj: Life Encounters">
    <meta property="og:description" content="Discover various life encounters of Jagadguru Shri Kripalu Ji Maharaj that reveal his divine wisdom and compassion.">
    <meta property="og:image" content="thumb_cover_2.jpg">
    <meta property="og:url" content="https://kishoriji.github.io/kripalu_maharaj_life_encounters/">
    <meta property="og:type" content="website">
    
    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Kripalu Maharaj: Life Encounters">
    <meta name="twitter:description" content="Discover various life encounters of Jagadguru Shri Kripalu Ji Maharaj that reveal his divine wisdom and compassion.">
    <meta name="twitter:image" content="thumb_cover_2.jpg">

    <title>Jagadguru Kripalu Maharaj Life Encounters</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }}

        h1 {{
            text-align: center;
            margin: 20px 0;
        }}

        .story-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            grid-auto-rows: 1fr;
            gap: 20px;
            padding: 20px;
        }}

        .story {{
            border: 1px solid #ccc;
            padding: 15px;
            text-align: center;
            background-color: #fff;
            transition: transform 0.2s;
        }}

        .story img {{
            max-width: 100%;
            height: auto;
            margin-bottom: 10px;
            border-radius: 5px;
        }}

        .story:hover {{
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }}

        .read-more {{
            display: inline-block;
            padding: 8px 15px;
            background-color: #007bff;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }}

        .read-more:hover {{
            background-color: #0056b3;
        }}

        .source {{
            font-size: 0.9em;
            color: #666;
        }}
    </style>
</head>
<body>
    <h1>Kripalu Maharaj Life Encounters</h1>

    <div class="story-grid">
        {story_blocks}
    </div>
</body>
</html>
"""


def generate_story_block(story):
    return f"""
    <div class="story">
        <img src="thumbnails/{story['image_link']}" alt="{story['title']} Image">
        <h2>{story['title']}</h2>
        <p>{story['story'][:100]}....</p>
        <p class="source"><b>Source</b>: {story['source_name']} - {story['source_ref']}</p>
        <a href="{story['story_id']}.html" class="read-more">Read More</a>
    </div>
    """


def generate_story_page(story):
    # HTML template for the single story page
    story_page_html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Highlighting various life encounters of Jagadguru Shri Kripalu Ji Maharaj, showcasing his divine wisdom and compassion.">
    <meta name="keywords" content="Jagadguru, Shri Kripalu Ji Maharaj, Life Encounters, Spirituality, Wisdom, Compassion">
    <meta name="author" content="kishoriji">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="Kripalu Maharaj: Life Encounters">
    <meta property="og:description" content="Discover various life encounters of Jagadguru Shri Kripalu Ji Maharaj that reveal his divine wisdom and compassion.">
    <meta property="og:image" content="thumb_cover_2.jpg">
    <meta property="og:url" content="https://kishoriji.github.io/kripalu_maharaj_life_encounters/">
    <meta property="og:type" content="website">
    
    <!-- Twitter Card Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Kripalu Maharaj: Life Encounters">
    <meta name="twitter:description" content="Discover various life encounters of Jagadguru Shri Kripalu Ji Maharaj that reveal his divine wisdom and compassion.">
    <meta name="twitter:image" content="thumb_cover_2.jpg">

    <title>{story['title']}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
            background-color: #f4f4f4;
        }}

        .story-container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}

        h1 {{
            text-align: center;
            margin-bottom: 20px;
        }}

        .story-image {{
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
            border-radius: 8px;
        }}

        .story-content {{
            font-size: 1.1em;
            margin-bottom: 20px;
        }}

        .source {{
            font-size: 0.9em;
            color: #666;
        }}

        .back-link {{
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            color: #007bff;
            font-weight: bold;
        }}

        .back-link:hover {{
            color: #0056b3;
        }}
    </style>
</head>
<body>
    <div class="story-container">
        <h1>{story['title']}</h1>
        <img src="images/{story['image_link']}" alt="{story['title']}" class="story-image">
        <div class="story-content">
            <p>{story['story']}</p>
        </div>
        <p class="source"><b>Source</b>: {story['source_name']} - {story['source_ref']}</p>
        <a href="index.html" class="back-link">← Back to Homepage</a>
    </div>
</body>
</html>
"""

    # Generate a file name based on the story title
    file_name = f"public/{story['story_id']}.html"

    # Save the HTML content to a file
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(story_page_html_template)

    print(f"Story page generated successfully: {file_name}")


def generate_index_page(stories):
    # Generate the full HTML for all stories
    story_blocks = "\n".join(generate_story_block(story) for story in stories)

    # Complete the HTML content by filling in the story blocks
    full_html = html_template.format(story_blocks=story_blocks)

    # Write the HTML content to a file
    output_path = "public/index.html"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(full_html)
    print(f"homepage generated successfully: {output_path}")


def main():
    with open('life_stories.json') as f:
        stories = json.load(f)
    generate_index_page(stories)
    for story in stories:
        generate_story_page(story)


if __name__ == '__main__':
    main()
